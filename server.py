from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import yt_dlp
import os
import uuid
from auto_clip import auto_generate_clips
from gemini_helper import extract_best_moments_from_transcript

app = Flask(__name__)
CORS(app)

@app.route('/process-video', methods=['POST'])
def process_video():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL tidak ditemukan'}), 400

    video_id = str(uuid.uuid4())
    download_path = f"downloads/{video_id}.mp4"
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        'outtmpl': download_path,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'writeautomaticsub': True,
        'subtitleslangs': ['en', 'id'],
        'subtitlesformat': 'vtt'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Video Tanpa Judul')
            transcript = title  # Simulasi karena transkrip asli tidak dijamin muncul

        best_moments = extract_best_moments_from_transcript(transcript)
        scenes = [(moment['start'], moment['end']) for moment in best_moments]

        clips = auto_generate_clips(download_path, scenes)

        return jsonify({
            'original_title': title,
            'clips': clips
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/clips/<path:filename>')
def serve_clip(filename):
    return send_from_directory('static/clips', filename)