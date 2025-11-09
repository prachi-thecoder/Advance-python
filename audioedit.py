from moviepy.editor import AudioFileClip , concatenate_audioclips,CompositeAudioClip,afx
from moviepy.audio.fx.all import audio_fadein,audio_fadeout,volumex
from playsound import playsound

audio1= AudioFileClip("outaudio.mp3")


# print("audio1 duration:",audio.duration)
# playsound("extracted.mp3")

# looped_audio= audio1.fx(afx.audio_loop,duration =24)
# print("looped audio ",looped_audio.duration)
# looped_audio.write_audiofile("loopadudio.mp3")
# audio2 = AudioFileClip("loopeadudio.mp3")
# sub_audio=audio1.subclip(2,4)
# sub_audio.write_audiofile("subclip.mp3")
# effect to audio 
# faded=audio1.fx(audio_fadein,2).fx(audio_fadeout,2)
# lowere=faded.fx(volumex,0.3)
# lowere.write_audiofile("out_audio.mp3")
# adjust volume
# quieter=audio1.volumex(0.4)
# quieter.write_audiofile("quieter.mp3")
# concatenate audio clips
# concat_audio=concatenate_audioclips([audio1,audio1])
# concat_audio.write_audiofile("concatedaudio.mp3")
# overlay audio
audio2_start = audio1.set_start(2)
Composite_Audio = CompositeAudioClip([audio1,audio2_start])
Composite_Audio.write_audiofile("mixaudio.mp3",fps=44100)
