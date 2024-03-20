import turtle
import random
renkler=["red","blue","magenta","yellow","pink"]
for a in range (4):
    # print(renkler[a])
    # turtle.color(renkler[a])
    turtle.color(random.choice(renkler))
    turtle.forward(100)
    turtle.right(60)
    
input()
