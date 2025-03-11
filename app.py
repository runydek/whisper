from flask import Flask, request, jsonify
import os
import whisper

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

if __name__ == '__main__':
    app.run(debug=True)
