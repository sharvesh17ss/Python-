import turtle as t

screen = t.Screen()
screen.title("Drawing SHARVESH")
screen.bgcolor("#52D3D8")

pen = t.Turtle()
pen.shape("turtle")
pen.speed(1)
pen.pensize(7)
pen.color("#D75550")

def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

#----S---
move(-350, 0)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(30)

#----H---
move(-280, 0)
pen.left(90)
pen.forward(60)
pen.backward(30)
pen.right(90)
pen.forward(40)
pen.left(90)
pen.forward(30)
pen.backward(60)

#----A---
move(-210, 0)
pen.forward(60)
pen.right(90)
pen.forward(45)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(45)
pen.right(180)
pen.forward(45)
pen.right(90)
pen.forward(30)

#----R---
move(-130,0)
pen.backward(60)
pen.left(90)
pen.forward(50)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(50)
pen.left(180)
pen.right(30)
pen.forward(60)

#----V---
move(-55, 60)
pen.left(35)
pen.right(60)
pen.forward(80)
pen.left(120)
pen.forward(70)

#----E--
move(40, 60)
pen.right(150)
pen.left(85)
pen.forward(50)
pen.backward(50)
pen.right(90)
pen.forward(30)
pen.left(90)
pen.forward(50)
pen.backward(50)
pen.right(90)
pen.forward(30)
pen.left(90)
pen.forward(50)
##pen.right(90)
##pen.forward(40)

#----S---
move(130,0)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(30)

#----H---
move(200, 0)
pen.right(180)
pen.right(90)
pen.forward(60)
pen.backward(30)
pen.right(90)
pen.forward(40)
pen.left(90)
pen.forward(30)
pen.backward(60)


pen.hideturtle()

turtle.done()







