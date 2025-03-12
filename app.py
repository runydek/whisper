from flask import Flask, request, jsonify
import os
import whisper
import yt_dlp

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = whisper.load_model("base")

@app.route('/upload-video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video file part"}), 400
    
    file = request.files['video']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    transcript = model.transcribe(filepath)
    text = transcript["text"]
    
    txt_filename = os.path.splitext(file.filename)[0] + ".txt"
    txt_filepath = os.path.join(UPLOAD_FOLDER, txt_filename)
    with open(txt_filepath, "w") as f:
        f.write(text)
    
    return jsonify({"message": "Video uploaded and transcribed", "transcript_file": txt_filepath})

@app.route('/upload-youtube', methods=['POST'])
def upload_youtube():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "No YouTube URL provided"}), 400
    
    url = data['url']
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(UPLOAD_FOLDER, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")
    
    transcript = model.transcribe(filename)
    text = transcript["text"]
    
    txt_filename = os.path.splitext(os.path.basename(filename))[0] + ".txt"
    txt_filepath = os.path.join(UPLOAD_FOLDER, txt_filename)
    with open(txt_filepath, "w") as f:
        f.write(text)
    
    return jsonify({"message": "YouTube video downloaded and transcribed", "transcript_file": txt_filepath})

if __name__ == '__main__':
    app.run(debug=True)
