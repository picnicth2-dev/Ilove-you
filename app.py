import turtle
import time

screen = turtle.Screen()
screen.title("I Love You")
screen.bgcolor("white")
screen.setup(900, 500)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)

def loading_screen():
    pen.clear()
    pen.penup()
    pen.goto(0, 40)
    pen.write("Loading...", align="center", font=("Arial", 24, "bold"))
    pen.goto(-200, 0)
    pen.pendown()
    pen.forward(400)
    pen.penup()
    bar = turtle.Turtle()
    bar.hideturtle()
    bar.speed(0)
    bar.pensize(8)
    bar.penup()
    bar.goto(-200, 0)
    bar.pendown()
    for _ in range(40):
        bar.forward(10)
        screen.update()
        time.sleep(0.05)
    bar.clear()
    pen.clear()

def draw_line(x, y, heading, length):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(heading)
    pen.pendown()
    pen.forward(length)

def draw_love_you():
    draw_line(-200, -50, 270, 100)
    draw_line(-200, -150, 0, 50)
    pen.penup()
    pen.goto(-120, -100)
    pen.pendown()
    pen.circle(40)
    draw_line(-40, -50, 300, 100)
    draw_line(-40, -50, 240, 100)
    draw_line(60, -50, 270, 100)
    draw_line(60, -50, 0, 50)
    draw_line(60, -100, 0, 40)
    draw_line(60, -150, 0, 50)
    draw_line(160, -50, 300, 60)
    draw_line(160, -50, 240, 60)
    pen.penup()
    pen.goto(230, -100)
    pen.pendown()
    pen.circle(35)
    draw_line(300, -50, 270, 100)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.pensize(5)
drawer.penup()

def start_draw(x, y):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    screen.ondrag(draw)

def draw(x, y):
    drawer.goto(x, y)
    screen.update()

def stop_draw(x, y):
    screen.ondrag(None)
    drawer.penup()

loading_screen()

pen.penup()
pen.goto(0, 200)
pen.write("Click and drag mouse to draw letter I",
          align="center", font=("Arial", 16, "bold"))

draw_love_you()
screen.update()

screen.onscreenclick(start_draw)
screen.onscreenclick(stop_draw, add=True)

screen.mainloop()