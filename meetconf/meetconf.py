import turtle
from turtle import *
turtle.speed(100)

#def draw_circle(x,y,size):
 #   turtle.penup()
  #  turtle.goto(x,y)
#def fun(x,y):
    #turtle.pendown()
    #t>>> turtle.fillcolor("violet")
#turtle.fillcolor()
#'violet'
#col = turtle.pencolor()
#col(50.0, 193.0, 143.0)
 #turtle.fillcolor(col)
 #turtle.fillcolor()
#(50.0, 193.0, 143.0)
 #turtle.fillcolor('#ffffff')
 #turtle.fillcolor()
#(255.0, 255.0, 255.0)urtle.goto(x,y)

    
#turtle.onclick(fun(10,10),btn=2,add = True)f
#turtle.onscreenclick(fun,btn=  1,add = True)
#turtle.ondrag(fun,btn =1 ,add = True)
#turtle.onclick(fun(10,10),btn=1,add = True)
color = 'red'
shape = 'circle'
def square(x,y):
    global color
    turtle.penup()
    turtle.goto(0+x,0+y)
    turtle.pendown()
    begin_fill()
    fillcolor(color)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    
    turtle.forward(50)
    end_fill()
    turtle.right(90)
def circle (x,y):
    global color
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    begin_fill()
    fillcolor(color)
    turtle.circle(10)
    end_fill()
#turtle.onscreenclick(square,btn = 1 ,add = True)
#turtle.ondrag(square,btn=1,add= True)
#flag = 1
#def flagg():
   #  flag = 2
        
#turtle.getscreen().onkeypress(flagg,"c")
#turtle.getscreen().listen()
#if flag == 2 :
 #   turtle.onscreenclick(square,btn =1 ,add = True)
#def draw ():
 #    turtle.forward(50)

#turtle.getscreen().onkeypress(draw,"c")
     
#turtle.getscreen.listen()
#color = ["red","blue","black"]
#r=0
#def count(n):
 #   global r++
#def color_list(r):
 #   color[r]

#color_list(0)

#count(r)
#color_list(r)
def draw(x,y):
    if shape == 'circle':
        circle(x,y)
    elif shape == 'square':
        square(x,y)
     

def choose_circle():
     global shape
     shape = 'circle'
def choose_square():
    global shape
    shape = 'square'
turtle.getscreen().onkeypress(choose_circle,"c")
turtle.getscreen().onkeypress(choose_square,"s")
turtle.onscreenclick(draw)





def change_blue():
    global color
    color = 'blue'
def change_red():
    global color
    color = 'red'
turtle.getscreen().onkeypress(change_red,"r")
turtle.getscreen().onkeypress(change_blue,"b")







listen()
turtle.mainloop()
