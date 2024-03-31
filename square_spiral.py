import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral")

t = turtle.Turtle()
t.speed(0)
t.width(2)

iterations = 400

# Draw !!!!
for i in range(iterations):
    hue = i / iterations
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.color(color)
    t.forward(i * 2)
    t.left(89)

# Get ready boisss
t.hideturtle()
turtle.done()
