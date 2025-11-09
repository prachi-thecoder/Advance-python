import re as r
import datetime as d
username=None
def f1(user):
    a=r.search(r"hi|hello|hey",user,r.I)
    if a:
        return f"{a.group()}!whats your name"
    # print(f"{a.group()},! what is ur name:")
    global username
    username=user
    if r.search(r"my name is \w+|\w+",user,r.I):
        return f"nice to meet uh {username}how can i assist uh today?"
print("chatpy is runing!(type 'exit' to quit)")
while True:
    user=input("you:")
    p=r.search(r"exit|quit",user,r.I)
    if(p):
        break
    else:
        print("bot:", f1(user))
        
