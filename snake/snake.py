from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
import random
print("Welcome to snake water gun game")
i=1
pu=0
cp=0
while(i<=5):
  lst=["snake","water","gun"]
  comp=random.choice(lst)
  user=input(print("Enter your choice\n snake\n water\n gun\n"))
  if user=="snake" or user=="water" or user=="gun":
   if user=="snake" and comp=="water":
     pu=pu+1
     sa=f"you win computer choice was water your points are {pu} and computer points are {cp}"
     print(sa)
     i=i+1
   elif user=="snake" and comp=="gun":
      cp=cp+1
      sa=f"you loose your points are {pu} and computer points are {cp} and computer choice was gun"
      print(sa)
      i=i+1
   elif user=="snake" and comp=="snake":
    
      sa=f"Tie your points are {pu} and computer points are {cp} computer choice was also snake"
      print(sa)
      i=i+1
   elif user=="water" and comp=="snake":
     cp=cp+1
     sa=f"you loose your points are {pu} and computer points are {cp} computer choice was snake"
     print(sa)
     i=i+1
   elif user=="water" and comp=="water":
    
    sa=f"Tie your points are {pu} and computer points are {cp} computer choice was also water"
    print(sa)
    i=i+1
   elif user=="water" and comp=="gun":
    pu=pu+1
    sa=f"you win your points are {pu} and computer points are {cp} computer choice was gun"
    print(sa)
    i=i+1
   elif user=="gun" and comp=="snake":
     pu=pu+1
     sa=f"you win your points are {pu} and computer points are {cp} computer choice was snake"
     print(sa)
     i=i+1
   elif user=="gun" and comp=="water":
    cp=cp+1
    sa=f"you loose your points are {pu} and computer points are {cp} computer choice was water"
    print(sa)
    i=i+1
   elif user=="gun" and comp=="gun":
    
    sa=f"Tie your points are {pu} and computer points are {cp} computer choice was also gun"
    print(sa)
    i=i+1
  else :
    print("Wrong input")
    i=i+1
if pu>cp: 
   print(" you win your total score ",pu)
elif pu==cp:
    print("tie")
else:
    print("computer win",cp)
    
  
