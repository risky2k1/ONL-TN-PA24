import turtle

# Khởi tạo màn hình vẽ
man_hinh = turtle.Screen()
man_hinh.bgcolor('yellow')
man_hinh.setup(width=1000,height=500)

# Khởi tạo ra rùa để vẽ
rua_1 = turtle.Turtle()
rua_1.shape('classic')
rua_1.color('red')
rua_1.speed(1)

rua_2 = turtle.Turtle()
rua_2.shape('square')
rua_2.color('green')
rua_2.speed(1)

# rua_1.forward(100)
# rua_1.left(90)

# rua_1.forward(100)
# rua_1.left(90)

# rua_1.forward(100)
# rua_1.left(90)

# rua_1.forward(100)
# rua_1.left(90)

for i in range(0,5):
    rua_1.forward(100)
    rua_1.left(90)

for i in range(0,5):
    rua_2.forward(200)
    rua_2.left(90)

man_hinh.exitonclick()
