import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)

t = turtle.Turtle()
t.speed(0)  
t.width(2)

def draw_spiral(length):
    radius = 1
    angle = 90
    color = [255, 0, 255]
    for _ in range(length):
        t.color(color)
        t.circle(radius, angle)
        t.left(10)  
        radius += 3
        color[0] -= 255//length
        color[1] += 255//length 
        color[2] -= 255//length

t.penup()
t.setpos(0, 0)
t.pendown()

draw_spiral(length=250)

t.hideturtle()
screen.mainloop()
