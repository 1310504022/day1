import turtle

def draw_multicolor_square(t, sz):
        for i in ["red", "purple", "hotpink", "blue"]:
                t.color(i)
                t.forward(sz)
                t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

john = turtle.Turtle()
john.pensize(3)

size = 20
for i in range(15):
        draw_multicolor_square(john, size)
        size = size + 10
        john.forward(10)
        john.right(18)

window.exitonclick()
