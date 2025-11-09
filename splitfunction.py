import re
text="this is split by regex"
parts=re.split(r'\s+',text,2)      
print(parts)
# 
# seprate by comma and semicolon
import re
text2="apple,banana;cherry,dates"
fruits=re.split(r'[;,]',text2)
print(fruits)
# seprate by special charcter
import re
user=input("enter a list:")
p=re.split(r'[,./&*$@#]',user)
print(p)
# replace string
import re
s="python programing"
p=re.sub(r'\s',"$",s)
print(p)
# 
import re
s="this is test123 program4"
p=re.sub(r"\d",' ',s,1)
print(p)
# write a program to take a mobile no from user and change first six digit with special symbol
import re
s=input("enter a no:")
p=re.sub(r"\d",'#',s,count=7)
print(p)
# 
import re
s="192.10.02.244"
p=re.sub(r"0"," ",s)
print(p)
# 
import re
p="""
<div class="product">
    <h2>Shirt</h2>
    <span class="price">$19.99</span>
</div>
<div class="product">
    <h2>Shoes</h2>
    <span class="price">$49.50</span>
</div>
<div class="product">
    <h2>Bag</h2>
    <span class="price">₹299</span>
</div>
<div class="product">
    <h2>Watch</h2>
    <span class="price">€75.25</span>
</div>
"""
s=r'[$\€\₹]\d+(?:\.\d{2})?'
l=re.findall(s,p)
print(l)
# 
import re
pattern=r".com"
text="examplecom"
match=re.findall(pattern,text)
print(match)
