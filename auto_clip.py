import os
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
from moviepy.video.io.VideoFileClip import VideoFileClip
from utils import add_subtitle

def auto_generate_clips(video_path, scenes, output_dir="static/clips"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    clip_paths = []
    for i, (start, end) in enumerate(scenes):
        clip = VideoFileClip(video_path).subclip(start, end)
        clip_title = f"clip_{i+1}.mp4"
        clip_path = os.path.join(output_dir, clip_title)

        # Tambah subtitle otomatis
        clip = add_subtitle(clip, start_time=start)

        clip.write_videofile(clip_path, codec="libx264", audio_codec="aac")
        clip_paths.append({"filename": clip_title, "title": f"Momen Terbaik #{i+1}"})

    return clip_paths