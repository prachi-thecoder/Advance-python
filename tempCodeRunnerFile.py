c=''
i=Image.open("3.jpeg")
draw=ImageDraw.Draw(i)
font = ImageFont.load_default()
a=string.ascii_letters+string.digits
for j in range(4):
    c=c+random.choice(a) 
font = ImageFont.truetype("arial.ttf",30)
draw.text((400,200),a,fill="red",font=font)
i.show()
# 


