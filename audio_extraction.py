import moviepy.editor
import data

def audio_extractor(filename):
    
    video = moviepy.editor.VideoFileClip(filename)
    audio = video.audio
    audio.write_audiofile(filename+".wav")

    return filename+".wav"
