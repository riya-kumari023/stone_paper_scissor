import random
print("..................ROCK PAPER AND SCISSOR..............................")


def game(comp,you):
    if (comp==you):
       print("match tie")
    elif comp =='r':
       if you == "s":
          print("you loss")
       elif you =='p':
          print("you win")
    elif comp=='p':
       if you =='r':
          print("you loss")
       elif you =='s':
         print("you win")
    elif comp=='s':
        if you =='p':
         print("you loss")
        elif you =='r':
            print("you win")
    
print("comp turn : rock (r) scissor (s) and p (paper)")
randno=random.randint(1,3)
if randno==1:
    comp="r"
elif randno==2:
    comp="p"
elif randno==3:
    comp="s"
a= input("your  turn : rock (r) scissor (s) and p (paper)")

print("comp choose: ")
print(comp)
print("you chose:")
print(a)
game(comp,a)