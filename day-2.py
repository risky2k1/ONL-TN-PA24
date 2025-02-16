# Class person chứa thong tin để có thể tạo nên 1 người hoàn chỉnh ,
# cùng với những hành động(Phương thức)của đối tuowjgn đó

# camelCase, underscore(snake-case) hay PascalCase
# myNameIsTuan
# my_name_is_Tuan
# MyNameIsTuan

# Tạo ra 1 class:


class Car:
    # Khai báo thuộc tính, chúng ta sử dụng hàm khởi tạo __init__ để khai báo các thuộc tính cho class đó
    # self khi sử dụng trong class sẽ tượng trưng cho chính class đó(self là ánh xạ Class)
    def __init__(self, name, color, number_of_seats, max_speed, engine):
        self.name = name
        self.color = color
        self.number_of_seats = number_of_seats
        self.max_speed = max_speed
        self.engine = engine

    def drift(self):
        print(f'Xe {self.name} có thể drift')

    def turn_wheel(self):
        print(f'Xe {self.name} có thể đánh lái')

    def brake(self):
        print(f'Xe {self.name} có phanh')


# Khởi tạo 1 đối tượng từ Class
car_1 = Car('Honda', 'red', 4, '100km/h', 'V6')

# Truy cập các thuộc tính - ten_object.ten_thuoc_tinh

# print(car_1.color)
# print(car_1.number_of_seats)
# print(car_1.max_speed)
# print(car_1.engine)

# Truy cập các Phương thức - ten_object.ten_phương_thức()
# print(car_1.drift())

car_2 = Car('Mitsubishi', 'yellow', 2, '80km/h', 'V4')

# print(car_2.color)
# print(car_2.number_of_seats)
# print(car_2.max_speed)
# print(car_2.engine)
