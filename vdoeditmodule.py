from moviepy.editor import*
c=VideoFileClip("video2.mp4")
# c.preview()
# sc=c.subclip(0,4)
# sc.preview()
# sc.write_videofile("output.mp4")
# d=c.write_gif("gif.gif")
# editing
# k=c.rotate(90)
# k.preview()
# from PIL import Image
# if not hasattr(Image, 'ANTIALIAS'):
#     Image.ANTIALIAS = Image.Resampling.LANCZOS
#     small=c.resize(width=200)
#     small.preview()
# l=c.cutout(0,4)
# l.preview()
# m=c.margin(20,color=(244,0,0))
# m.preview()
# 
# c.fx(vfx.speedx,2)
# c.preview()
# c.fx(vfx.fadein,2)
# c.preview()
# k=c.fx(vfx.fadein,4).fx(vfx.fadeout,4)
# k.preview()
# p=c.fx(vfx.blackwhite)
# p.preview()
# n2=c.fx(vfx.loop,n=2)
# o=n2.write_videofile("kkkkkp.mp4")
# # n=c.without_audio()
# n.preview()
# set1=c.set_duration(4)
# set1.preview()
# c=VideoFileClip("video.mp4").subclip(0,7)
c1=VideoFileClip("video2.mp4").subclip(0,7)
# c2=VideoFileClip("video.mp4").subclip(0,7)
# c3=VideoFileClip("video2.mp4").subclip(0,7)
# ou=clips_array([[c,c1],[c2,c3]])
# ou.preview()
# l=ou.write_videofile("kkkkk.mp4")
# l.preview()
# v=concatenate_videoclips([c,c1])
# pp=v.write_videofile("vuushdu.mp4")
# 
# from moviepy.config import change_settings
# change_settings({
#     "IMAGEMAGICK_BINARY":"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\\magick.exe"
# })
# txt=TextClip("hiiiiiiiiiii",fontsize=40,color="white")
# txt=txt.set_position("center").set_duration(4)
# b=CompositeVideoClip([c,txt])
# q=b.write_videofile("txt.mp4")
# save screenshots
# c.save_frame("test.jpeg")
# c.save_frame("test.jpg",t=3)
# 

#extraction a audio from video
c.audio.write_audiofile("outaudio.mp3")
# 
without=c1.without_audio()
without.write_videofile("without.mp4")
# 
d=VideoFileClip("without.mp4")
audio=AudioFileClip("outaudio.mp3")
clips_with_audio=d.set_audio(audio)
clips_with_audio.write_videofile("withsong.mp4")

# clips_with_audio=clip1.set_audio(audio)
# clips_with_audio.write_videofile("withsong.mp4")
