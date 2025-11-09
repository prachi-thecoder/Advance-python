user=input("enter a no:")
if(len(user)==10 and not user.startswith("0")):
    # print("valid")
    if( user.isdigit() or user.startswith("+91")):
        # print("valid")
            print("valid")
else:
 
 print("invalid")
#  \
# ^
# q=[^ abc]
'''[a-z]'''
'''c=[1-9]'''
# meta character
a="abc\\tpqr"
print(a)
# quantifier
# a+= 1 or more
# a*= 0 or more
# a?=  0 or 1
# a{2}=len a is exactly 2
# a{2,}=len a is minimum 2 and etc
# a{,3}
# a{2,3}
# write a pattern in which 1st four character are digit between 1 to 4 follwed by 2 uppercase char
# 2 lower case char
# r='''^[0-4]{4}[A-z]{2}[a-z]{2}$''' 
# # create a pattern first 3 char are from surname follwed by date of birth follwed by 3 char from
# #  1st name and follwed by age
# k='''^[a-zA-z]{3}[0-9]{8}[a-zA-Z]{3}[1-9]{2,3}$'''
# # pincode
# p='''^[4]{1}[0-4]{1}[0-9]{4}$'''
# m='''^[+91]?[7-9]{1}[0-9]{9}$'''
# e='''^[a-zA-Z0-9]+[@][a-zA-Z]{2,8}[.][a-zA-Z]{2,3}$'''
import re
# p=r"a|z"
# s='python'
# r=re.search(p,s)
# print(r)
# print(type(r))
p=r"a|z"
s=input("enter a string:")
k=re.search(p,s,re.I)
if(re.search(p,s)):
    print("found:",k.group(),k.end(),k.start())
else:
    print("not found")
#re.match 
import re
p=r'[0-9]{2}'
s=input("enter a string:")
k=re.match(p,s)
if(k):
    print("found:",k.group(),k.start(),k.end())
else:
    print("not ")
# 
# to validate first name of a user which contain only alphanumeric charwith length min2 and max10
import re
user=input("enter a username:")
p=r'^[a-zA-Z0-9]{2,10}$'
t=re.search(p,user)
if(t):
    print("found")
else:
    print("enter valid")
# 
import re
user=input("enter pincode:")
p=r'''^[4]{1}[1-4]{1}[0-9]{4}$'''
t=re.search(p,user)
if(t):
    print("found")
else:
    print("not")
# 
import re
user=input("enter a no:")
p='''^[+91]{3}?[7-9]{1}[0-9]{9}$'''
m=re.search(p,user)
if(m):
    print("yes")
else:
    print("no")  
# findall method
import re
p="(ab)"
s=input("enter a string:")
l=re.findall(p,s)
print(l)
# 
import re
p="^\w+$"
s=input("enter a string:")
l=re.findall(p,s)
print(l)
# 
import re
p="[0-9]{2}[a-z]{1}[A-Z]{1}"
s=input("enter a string:")
l=re.findall(p,s)
print(l)
# 
import re
p="[0-9]{2}[a-z]{1}[A-Z]{1}"
s=input("enter a string:")
l=re.finditer(p,s)
for i in l:
    print(i.group(),i.start(),i.end())
# 

import re
p="[0-9]"
s=input("enter a string:")
l=re.finditer(p,s)
for i in l:
    print("span",i.span(),"starting",i.start(),"ending",i.end(),"group",i.group())
# 
import re
# p='^[1-9]{4}[-/.]{1}[0-9]{1,2}[-/.]{1}[0-3]{1}[1-9]{1,2}$'
p=r"\d{4}[-\/\.]\d{1,2}[-\/\.][0-3]{1}\d{1}$"
s=input("enter a date:")
l=re.findall(p,s)
print(l)

# 
# cradit card
import re
p=r"\d{4}-\d{4}-\d{4}-\d{4}$"
s=input("enter a cradit card no:")
l=re.findall(p,s)
print(l) 
# 
# Url
import re
p=r"^https?://\w+[.-]\w+"
s=input("enter a url:")
l=re.findall(p,s)
print(l)
# 
# capturing group
import re
p=r"(\d{4})-(\d{4})-(\d{4})-(\d{4})$"
s=input("enter a cradit card no:")
l=re.search(p,s)
print(l.group(),l.group(1),l.group(2),l.group(3),l.group(4)) 
#non-capturing
#?:\d{4}
import re
p=r"(?:\d{4})-(\d{4})-(\d{4})-(\d{4})$"
s=input("enter a cradit card no:")
l=re.search(p,s) 
print(l.group())
print(l.group(),l.group(1),l.group(2),l.group(3)) 
#
import re
p=r"</?\w+>" 
s="<h1>python</h1><i>prachi</i>"
l=re.findall(p,s)
print(l)
# 
import re
p=r"</?\w+>" 
s=input("enter a string:")
l=re.findall(p,s)
print(l)
# 
import re
p=r"(</?\w+>)(?:\w+)?\1"
s=input("enter a string:")
l=re.findall(p,s)
print(l)
# 
import re
p=r"(\w+)\1" 
s=input("enter a string:")
l=re.findall(p,s)
print(l)
# 
import re
p=r"\b(\w)(\w)(\1)\b"
s=input("enter a name:")
l=re.findall(p,s)
print(l) 
# 
import re
p=r"\b(\w+)\s+\1\b"
s=input("enter a :")
l=re.findall(p,s)
print(l)
# 
import re
p=r"\b(\w+)\s+\1\b"
s=input("enter a :")
l=re.findall(p,s)
print(l)
# 
import re
p=r"\b\w*(\w)\1\w*\b"
s=input("enter a :")
l=re.search(p,s)
print(l.group())
# 
import re
p=r"(?=.{8,})(?=\w+)"
s=input("enter a pass:")
l=re.search(p,s)
# print(l)
if(l):
    print("valid")
else:
    print("wrong")

# 
import re   
p=r"(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*\d)"
s=input("enter a pass:")
l=re.search(p,s)
# print(l)
if(l):
    print("valid")
else:
    print("wrong")

