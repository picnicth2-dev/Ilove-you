import turtle
import time

# ตั้งค่าหน้าจอ
screen = turtle.Screen()
screen.title("I Love You - Special Message")
screen.bgcolor("white")  # ปรับเป็นสีขาวตามคำขอครับคุณปิคนิค
screen.setup(900, 500)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)

def loading_screen():
    pen.clear()
    pen.penup()
    pen.color("#555") # สีเทาสำหรับตัวหนังสือ Loading
    pen.goto(0, 40)
    pen.write("Loading Sweetness...", align="center", font=("Arial", 20, "bold"))
    
    # วาดแถบโหลด
    pen.goto(-200, -10)
    pen.pendown()
    for _ in range(2):
        pen.forward(400)
        pen.right(90)
        pen.forward(20)
        pen.right(90)
    pen.penup()

    bar = turtle.Turtle()
    bar.hideturtle()
    bar.speed(0)
    bar.color("#ff3385") # สีชมพูโหลด
    bar.penup()
    bar.goto(-200, -20)
    
    for _ in range(40):
        bar.begin_fill()
        for _ in range(2):
            bar.forward(10)
            bar.left(90)
            bar.forward(20)
            bar.left(90)
        bar.end_fill()
        bar.forward(10)
        screen.update()
        time.sleep(0.04)
    
    bar.clear()
    pen.clear()

def show_final_message():
    # เขียนคำว่า I LOVE YOU ตัวใหญ่กลางจอ
    pen.penup()
    pen.goto(0, 20)
    pen.color("#ff1a75") # สีชมพูเข้มเด่นบนพื้นขาว
    pen.write("I LOVE YOU", align="center", font=("Verdana", 70, "bold"))
    
    pen.goto(0, -60)
    pen.color("#333")
    pen.write("วาดรูปหัวใจคืนให้เค้าหน่อยสิ ❤️", align="center", font=("Tahoma", 18, "normal"))

# ตั้งค่าปากกาสำหรับให้แฟนคุณวาด
drawer = turtle.Turtle()
drawer.shape("circle")
drawer.shapesize(0.5)
drawer.color("#e6005c")
drawer.pensize(6)
drawer.penup()

def start_draw(x, y):
    drawer.goto(x, y)
    drawer.pendown()

def draw(x, y):
    drawer.goto(x, y)
    screen.update()

def release_draw(x, y):
    drawer.penup()

# เริ่มทำงาน
loading_screen()
show_final_message()
screen.update()

# ระบบ Interactive
screen.listen()
screen.onscreenclick(start_draw, 1) # คลิกซ้ายเริ่มวาด
drawer.ondrag(draw)                # ลากเมาส์เพื่อเขียน
screen.onclick(release_draw, 3)      # คลิกขวาเพื่อยกปากกา

screen.mainloop()
