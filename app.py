import turtle
import time

# ---------- Screen ----------
screen = turtle.Screen()
screen.title("I Love You ❤️")
screen.bgcolor("white")
screen.setup(900, 500)
screen.tracer(0)

# ---------- Pen สำหรับวาดข้อความ ----------
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)
pen.color("black")

# ---------- Loading Screen ----------
def loading_screen():
    pen.clear()
    pen.penup()
    pen.goto(0, 40)
    pen.write("Loading...", align="center",
              font=("Arial", 24, "bold"))

    bar = turtle.Turtle()
    bar.hideturtle()
    bar.speed(0)
    bar.pensize(10)
    bar.color("pink")

    bar.penup()
    bar.goto(-200, 0)
    bar.pendown()

    for _ in range(40):
        bar.forward(10)
        screen.update()
        time.sleep(0.04)

    bar.clear()
    pen.clear()

# ---------- ฟังก์ชันวาดเส้น ----------
def draw_line(x, y, heading, length):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(heading)
    pen.pendown()
    pen.forward(length)

# ---------- วาด I LOVE YOU ----------
def draw_love_you():
    # I
    draw_line(-350, -50, 270, 100)

    # L
    draw_line(-300, -50, 270, 100)
    draw_line(-300, -150, 0, 50)

    # O
    pen.penup()
    pen.goto(-200, -150)
    pen.pendown()
    pen.circle(40)

    # V
    draw_line(-100, -50, 300, 100)
    draw_line(-100, -50, 240, 100)

    # E
    draw_line(0, -50, 270, 100)
    draw_line(0, -50, 0, 50)
    draw_line(0, -100, 0, 40)
    draw_line(0, -150, 0, 50)

    # Y
    draw_line(120, -50, 300, 60)
    draw_line(120, -50, 240, 60)
    draw_line(120, -100, 270, 60)

    # O
    pen.penup()
    pen.goto(200, -150)
    pen.pendown()
    pen.circle(35)

    # U
    draw_line(260, -50, 270, 100)
    draw_line(260, -150, 0, 50)
    draw_line(310, -50, 270, 100)

# ---------- Turtle สำหรับวาดด้วยเมาส์ ----------
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.pensize(4)
drawer.color("red")

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

# ---------- RUN ----------
loading_screen()

pen.penup()
pen.goto(0, 200)
pen.write("Click & drag mouse to draw ❤️",
          align="center", font=("Arial", 16, "bold"))

draw_love_you()
screen.update()

screen.onmousedown(start_draw)
screen.onmouseup(stop_draw)

screen.mainloop()