import turtle
import time

# ----------------- ตั้งค่าหน้าจอ -----------------
screen = turtle.Screen()
screen.title("I Love You")
screen.bgcolor("white")
screen.setup(width=900, height=500)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)

# ----------------- หน้า Loading -----------------
def loading_screen():
    pen.clear()
    pen.penup()
    pen.goto(0, 40)
    pen.write("Loading...", align="center", font=("Arial", 24, "bold"))

    # กรอบแถบโหลด
    pen.goto(-200, 0)
    pen.pendown()
    pen.forward(400)
    pen.penup()

    # แถบโหลดขยับ
    bar = turtle.Turtle()
    bar.hideturtle()
    bar.speed(0)
    bar.pensize(8)
    bar.color("black")

    bar.penup()
    bar.goto(-200, 0)
    bar.pendown()
    for i in range(40):
        bar.forward(10)
        time.sleep(0.05)

    bar.clear()
    pen.clear()

# ----------------- วาดตัวอักษรแบบมือ -----------------
def draw_line(x, y, heading, length):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(heading)
    pen.pendown()
    pen.forward(length)

def draw_love_you():
    pen.color("black")

    # L
    draw_line(-200, -50, 270, 100)
    draw_line(-200, -150, 0, 50)

    # O
    pen.penup()
    pen.goto(-120, -100)
    pen.pendown()
    pen.circle(40)

    # V
    draw_line(-40, -50, 300, 100)
    draw_line(-40, -50, 240, 100)

    # E
    draw_line(60, -50, 270, 100)
    draw_line(60, -50, 0, 50)
    draw_line(60, -100, 0, 40)
    draw_line(60, -150, 0, 50)

    # YOU
    draw_line(160, -50, 300, 60)
    draw_line(160, -50, 240, 60)

    pen.penup()
    pen.goto(230, -100)
    pen.pendown()
    pen.circle(35)

    draw_line(300, -50, 270, 100)

# ----------------- วาดตัว I ด้วยเมาส์ -----------------
drawer = turtle.Turtle()
drawer.speed(0)
drawer.pensize(5)
drawer.color("black")
drawer.hideturtle()

drawing = False

def start_draw(x, y):
    global drawing
    drawing = True
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

def draw(x, y):
    if drawing:
        drawer.goto(x, y)

def stop_draw(x, y):
    global drawing
    drawing = False
    drawer.penup()

# ----------------- เริ่มโปรแกรม -----------------
loading_screen()

# ข้อความแนะนำ
pen.penup()
pen.goto(0, 200)
pen.write("Use mouse to draw letter I", align="center",
          font=("Arial", 18, "bold"))

# เปิดให้ลากเมาส์
screen.onscreenclick(start_draw)
screen.onmousemove(draw)
screen.onscreenclick(stop_draw, btn=3)

# วาด LOVE YOU
draw_love_you()

screen.mainloop()