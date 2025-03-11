Flask Video Transcription API

📌 Deskripsi

Proyek ini adalah API berbasis Flask yang memungkinkan pengguna mengunggah video, kemudian menggunakan OpenAI Whisper untuk mengubah audio dalam video menjadi teks transkripsi. Transkrip akan disimpan dalam file .txt di folder /tmp/.

🚀 Teknologi yang Digunakan

Python 3

Flask

OpenAI Whisper

FFmpeg

📦 Instalasi

1️⃣ Clone Repository

git clone https://github.com/username/repo-name.git
cd repo-name

2️⃣ Buat Virtual Environment

python3 -m venv venv
source venv/bin/activate  # Linux & macOS
venv\Scripts\activate  # Windows

3️⃣ Instal Dependensi

pip install -r requirements.txt

4️⃣ Instal FFmpeg

Linux (Ubuntu/Debian)

sudo apt update && sudo apt install ffmpeg -y

macOS (Homebrew)

brew install ffmpeg

Windows

Download FFmpeg dari situs resmi.

Tambahkan ffmpeg.exe ke PATH environment variable.

🔥 Menjalankan Aplikasi

python app.py

Server akan berjalan di http://127.0.0.1:5000.

📤 API Endpoint

1️⃣ Upload Video & Transkripsi

Endpoint: /upload-video

Metode: POST

Form Data:

video (file) → Video yang akan diunggah

Contoh cURL:

curl -X POST http://127.0.0.1:5000/upload-video \
     -F "video=@/path/to/your/video.mp4"

Contoh Respons:

{
    "message": "Video uploaded and transcribed",
    "transcript_file": "/tmp/video.txt"
}

📜 Lisensi

MIT License. Silakan gunakan dan kontribusi!

🙌 Kontribusi

Pull request dipersilakan! Untuk perubahan besar, harap buka issue terlebih dahulu untuk mendiskusikan perubahan yang akan dilakukan.

