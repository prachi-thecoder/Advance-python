from PIL import Image , ImageFont, ImageDraw
import random
import re
import string
# i=Image.open("3.jpeg")
# draw=ImageDraw.Draw(i)
# font = ImageFont.load_default()
# u=input("enter a string:")
# font = ImageFont.truetype("arial.ttf",30)
# draw.text((400,200),u,fill="red",font=font)
# i.show()
#
# c=''
# i=Image.open("3.jpeg")
# draw=ImageDraw.Draw(i)
# font = ImageFont.load_default()
# a=string.ascii_letters+string.digits
# for j in range(4):
#     c=c+random.choice(a) 
# font = ImageFont.truetype("arial.ttf",30)
# draw.text((400,200),a,fill="red",font=font)
# i.show()
# 
# landscape
# i=Image.open("pil.png").convert('RGBA')
# img=Image.new("RGBA",i.size,(220,230,220,0))
# font = ImageFont.truetype("arial.ttf",80)
# draw=ImageDraw.Draw(img)
# draw.text((i.width-400,i.height-200),"ukkk",fill="white",font=font)
# prev=Image.alpha_composite(i,img)
# prev.show()
# 
# portrait image
i=Image.open("3.jpeg").convert('RGBA')
img=Image.new("RGBA",i.size,(220,230,220,0))
font = ImageFont.truetype("arial.ttf",40)
draw=ImageDraw.Draw(img)
draw.text((i.width-100,i.height-100),"ukkk",fill="white",font=font)
prev=Image.alpha_composite(i,img)
prev.show()

 


