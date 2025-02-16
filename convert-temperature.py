import tkinter as tk
from tkinter import messagebox


def convert_from_c_to_f():
    # Lấy giá trị từ ô entry tương ứng
    entry_1_value = entry_1.get()

    # Kiểm tra value có tồn tại không
    if not entry_1_value:
        # Hiển thị hộp thoại báo lỗi
        messagebox.showerror('Lỗi', 'Vui lòng nhập vào dữ liệu!!')
    else:
        f_value = (float(entry_1_value) * 9 / 5) + 32
        # Xóa tất cả các thông tin có trong entry 2
        entry_2.delete(0, tk.END)
        # Thêm thông tin của giá trị độ F vào ô entry đó
        entry_2.insert(0, f_value)


def convert_from_f_to_c():
    # lấy giá trị độ F ở trong ô Entry 2
    entry_2_value = entry_2.get() # Giá trị độ F tỏng ô entry 2 

    if not entry_2_value:
        messagebox.showerror('Lỗi', 'Vui lòng nhập vào dữ liệu!!')
    else:
        print(entry_2_value)
        c_value = (float(entry_2_value) - 32) * 5  / 9
        entry_1.delete(0, tk.END)
        entry_1.insert(0, c_value)


screen = tk.Tk()
screen.title('temp convert')
screen.minsize(400, 200)

tk.Label(text='BỘ CHUYỂN ĐỔI NHIỆT ĐỘ',font=('Arial',24)).grid(row=0,column=0,columnspan=2)
tk.Label(text='Nhập độ C').grid(row=1, column=0)
tk.Label(text='Nhập độ F').grid(row=2, column=0)

entry_1 = tk.Entry()
entry_1.grid(row=1, column=1)

entry_2 = tk.Entry()
entry_2.grid(row=2, column=1)

tk.Button(text='Chuyển từ C->F',command=convert_from_c_to_f).grid(row=3, column=0, padx=10)
tk.Button(text='Chuyển từ F->C',command=convert_from_f_to_c).grid(row=3, column=1, padx=10)


screen.mainloop()

#version 1.0.0
#version 1.0.1
#version 1.0.2

# cập nhật thêm 1 chức năng mới mà mọi người sẽ thích thì tôi là ứng dụng bộ chuyển đổi 2.0.0