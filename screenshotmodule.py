import pyscreenshot as Imagegrab
# img=Imagegrab.grab()
# img.save("screenshot.png")
# print("saved screenshot.png")
# img.show()
# capture spacific region
bbox=(100,100,400,300)
img=Imagegrab.grab(bbox=bbox)
img.save("regionscreenshot.png")
print("saved regionscreenshot.png")
img.show()