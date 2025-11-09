from PIL import Image ,ImageFilter , ImageEnhance , ImageDraw,ImageFont,ImageOps
# i=Image.open("3.jpeg")
# i.show()
# i.save("pil.png")
# # image properties
# print(i.format)
# print("filename",i.filename)
k=Image.open("D:\\advance python\\pil.png")
print("size of image",k.size)
# print("mode of file :",i.mode)
# # create a new image
# img = Image.new("RGB",(100,100),"green")
# # img.show()
# rotated=i.rotate(47,expand=True,fillcolor='pink')
# # rotated.show()
# resize = i.resize((200,200))
# # resize.show
# # crop
# crop=i.crop((40,40,200,200))
# # crop.show()
# # convert the image to rgba mode
# rgba = i.convert("L")
# # rgba.show()
# # 
# rgba = i.convert("RGBA")
# # rgba.show()
# # image filter effects
# blurred = i.filter(ImageFilter.BLUR)
# # blurred.show()
# # 
# sharp=i.filter(ImageFilter.SHARPEN)
# # sharp.show()

# edge=i.filter(ImageFilter.FIND_EDGES)
# # edge.show()
# # 
# # brightness
# enha = ImageEnhance.Brightness(i)
# bright = enha.enhance(1.7)
# # bright.show()
# # 
# # contrast
# con=ImageEnhance.Contrast(i).enhance(1.8)
# # con.show()
# # sharpness
# sharp = ImageEnhance.Sharpness(i).enhance(3.0)    
# # sharp.show()
# # colour
# color = ImageEnhance.Color(i).enhance(2.0)
# color.show()
# drawing on image

draw=ImageDraw.Draw(k)
# rectangle
# draw.rectangle([40,40,80,80],fill="yellow",outline="white",width=3)
# i.show()
# text
# font = ImageFont.load_default()
# font = ImageFont.truetype("arial.ttf",30)
# draw.text((400,200),"hello pill",fill="red",font=font)
# i.show()
# flip the mirror
# flipped = ImageOps.flip(i)      #vertical flip
# flipped.show()
# mirrored = ImageOps.mirror(i)   #horizontal flip
# mirrored.show()
# paste one image onto another
# create new blank canvas

canvas = Image.new("RGBA",(k.width,k.height),"pink")
canvas.show()
# # 
# font = ImageFont.load_default()
# u=input("enter a string:")
# font = ImageFont.truetype("arial.ttf",30)
# draw.text((400,200),u,fill="red",font=font)
# i.show()

# u.show()
i2=Image.open("3.jpeg")
# canvas.paste(i,(200,200))
# canvas.show()
# a=Image.alpha_composite(i,canvas)
# a.show()

#





