# user interface
# xây dựng 1 GUI
# Với python thì xây dựng GUI, bằng thư viện Tkinter

# import thư viện
import tkinter as tk

# Khởi tạo màn hình

screen = tk.Tk()
screen.title('My app')
# Thiết lập kích thước tối thiểu
screen.minsize(400, 200)

# Các layout có trong 1 màn hình Tk
# 3 loại
# PACK
# Các widget sẽ được hiển thị theo thứ tự hay cách sắp xếp từ trên xuống

# GRID
# Đặt các widget vào các vị trí trên lưới tương ứng -  có tính tùy biến cao hơn PACK

# Lưu ý: layout pack và layout grid KHÔNG được sử dụng ở trên cùng 1 màn hình

# PLACE - Đặt các widget vào vị trí bất kì được chỉ định ở trên màn hình (Vị trí tuyệt đối)


# Các widgets
# Label
label_1 = tk.Label(text='Nhập tên')
label_2 = tk.Label(text='Nhập tuổi', font=('Ariel', 24))
label_3 = tk.Label(text='Nhập địa chỉ')


# label_1.pack()
# label_2.pack(pady=50)
# label_3.pack()

label_1.grid(row=2, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=1, column=2)


# label_1.place(x=390, y=10)

# Button
button_1 = tk.Button(text='Đông ý')
button_2 = tk.Button(text='Nhập lai')


# button_1.pack(pady=10)
# button_2.pack(pady=10)

button_1.grid(row=3, column=2)
button_2.grid(row=1, column=4)

# Entry

entry_1 = tk.Entry()
entry_2 = tk.Entry()
entry_3 = tk.Entry()
entry_1.grid(row=2, column=1)
entry_2.grid(row=0, column=2)
entry_3.grid(row=1, column=3)


screen.mainloop()
