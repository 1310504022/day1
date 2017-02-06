import turtle

def draw_square(t,size):
        for i in range(4):
                t.forward(size)
                t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
           
john = turtle.Turtle()
john.color("hotpink")

for i in range(5):
    john.pendown()     
    draw_square(john,50)
    john.penup()
    john.forward(70)

window.exitonclick()
