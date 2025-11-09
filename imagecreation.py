from moviepy.editor import ImageClip
clip = ImageClip("pil.png")
clip = clip.set_duration(4)
clip.write_videofile("imagevideo.mkv",fps=24,codec="libx264")
