oviepy.editor import TextClip, CompositeVideoClip

def add_subtitle(clip, start_time=0):
    subtitle = TextClip("Subtitle otomatis...", fontsize=24, color='white', bg_color='black')
    subtitle = subtitle.set_position(('center', 'bottom')).set_duration(clip.duration)
    return CompositeVideoClip([clip, subtitle])
