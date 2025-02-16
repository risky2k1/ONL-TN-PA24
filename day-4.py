import turtle

# Mình vạch sẵn đường đi cho con rùa

man_hinh = turtle.Screen()
man_hinh.bgcolor('yellow')
man_hinh.setup(width=500, height=500)

rua_1 = turtle.Turtle()
rua_1.shape('turtle')
rua_1.color('red')

rua_2 = turtle.Turtle()
rua_2.shape('square')
rua_2.color('green')


def turn_left():
    rua_1.left(90)


def move_forward():
    rua_1.forward(25)


def turn_right():
    rua_1.right(90)


def turn_behind():
    rua_1.right(180)


man_hinh.onkey(turn_left, 'a')
man_hinh.onkey(turn_behind, 's')
man_hinh.onkey(turn_right, 'd')
man_hinh.onkey(move_forward, 'w')

man_hinh.listen()

man_hinh.exitonclick()

#  Theo mn ra 1 và rùa 2 có cùng trạng thái không?

# Higher order function


# def tinh_tong(a, b):
#     return a+b

# def tinh_hieu(a, b):
#     return a-b

# def tinh_tich(a, b):
#     return a*b


# def tinh_tong_ba_so(c, callback):
#     return c + callback(4, 5)


# print(tinh_tong_ba_so(3, tinh_hieu))
# print(tinh_tong_ba_so(3, tinh_tong))
# print(tinh_tong_ba_so(3, tinh_tich))

