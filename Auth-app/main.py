# Phan mem xac thuc nguoi dung
# Authentication app

# Social login (oauth)

# Chương trình -> có mục tiêu là xây dựng 2 form Đăng Nhập - Đăng Ký
# Đăng nhập:
# - Tiêu đề chính của Form
# - Tiêu đề của ô nhập username + ô entry của username
# - Tiêu đề ô password + ô entry nhập password
# - Nút "Đăng nhập" -> được ấn thì hệ thống kiểm tra là username và pass có tồn tại không -> có thì đăng nhập thành công
#   Không thì Đăng nhập thất bại
# - Nút "Đăng ký" -> Hiển thị form đăng ký nếu người dùng chưa có tài khoản

# Đăng ký:
# - Tiêu đề chính của Form
# - Tiêu đề của ô nhập username + ô entry của username
# - Tiêu đề ô password + ô entry nhập password
# - Tiêu đề ô re-enter password + ô entry nhập re-enter password
# - Nút "Đăng ký"
# - Nút "Đăng nhập" -> Hiển thị form đăng nhập nếu người dùng đã có tài khoản

# Sau khi đăng nhập or đăng ký thành công => Hiển thị danh sách các tài khoản
# có trong hệ thống

#  chuyển về sử dụng OOP

import tkinter as tk
from tkinter import messagebox


def show_login_form():
    # Xóa các widgets đang có trên root hiện tại
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, font=("Arial", 24, "bold"), text='Đăng nhập').pack()

    tk.Label(root, text='Username').pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text='Password').pack()
    password_entry = tk.Entry(root)
    password_entry.pack()

    def handle_login():
        # Lấy giá trị username và passs mà người dùng nhập vào
        username_value = username_entry.get()
        password_value = password_entry.get()

        # Kiểm tra username hay password có bị trống hay không
        # nếu không có username_value hoặc không có password_value
        if not username_value or not password_value:
            messagebox.showwarning(
                'Lỗi', 'Tài khoản hoặc mật khẩu không được để trống!')
        else:
            # Đọc dữ liệu từ file accounts
            with open('accounts.txt', 'r') as file:
                # Lấy ra các tài khoản dưới dạng từng dòng
                accounts = file.readlines()
                found = False

                for account in accounts:
                    removed_blank_account = account.strip()
                    # tai_khoan_da_duoc_bo_khoang_trong = account.strip()

                    # cắt chuỗi bởi dấu '-'
                    splited_account = removed_blank_account.split('-')
                    # Tài khoản : splited_account[0]
                    # Mật khẩu : splited_account[1]
                    if username_value == splited_account[0] and password_value == splited_account[1]:
                        found = True
                        break

                if found:
                    messagebox.showinfo('Yes', 'Đăng nhập thành công')
                else:
                    messagebox.showerror('Oppps', 'Đăng nhập không thành công')

    tk.Button(root, text='Đăng nhập', command=handle_login).pack(pady=10)
    tk.Button(root, text='Bạn chưa có tài khoản? Ấn vào đây!',
              command=show_register_form).pack(pady=10)


def show_register_form():
    # Xóa các widgets đang có trên root hiện tại
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, font=("Arial", 24, "bold"), text='Đăng ký').pack()

    tk.Label(root, text='Username').pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text='Password').pack()
    password_entry = tk.Entry(root)
    password_entry.pack()

    tk.Label(root, text='Re-enter Password').pack()
    re_enter_password_entry = tk.Entry(root)
    re_enter_password_entry.pack()

    def handle_register():
        # Khi đến đây, chúng ta đã có username_entry, password_entry, re_enter_password_entry
        # tên người dùng đăng ký, mật khaau đăng ký
        username_register_value = username_entry.get()
        password_register_value = password_entry.get()
        re_enter_password_register_value = re_enter_password_entry.get()

        danh_sach_ten_tai_khoan = []

        with open('accounts.txt', 'r') as f:
            list_accounts = f.readlines()
            danh_sach_ten_tai_khoan = [
                ((account.strip()).split('-'))[0] for account in list_accounts]

           # Kiểm tra 1 trong 3 có bị trống hay không?
        if not username_register_value or not password_register_value or not re_enter_password_register_value:
            messagebox.showwarning(
                'Warning!', 'Vui lòng nhập dầy đủ thông tin')
            # Kiểm tra password có giống với re-enter password hay không?
        elif password_register_value != re_enter_password_register_value:
            messagebox.showwarning(
                'Warning!', 'Mật khẩu và mật khẩu nhập lại không khớp!')
            # Kiểm tra username có tồn tại trong file accounts.txt hay không?
        elif username_register_value in danh_sach_ten_tai_khoan:
            messagebox.showwarning('Lỗi', 'Tài khoản đã tồn tại!')
            # else: Ghi thêm username-password vào file accounts.txt
        else:
            with open('accounts.txt', 'a') as f:
                f.write("\n" + username_register_value + '-' +password_register_value)
                messagebox.showinfo('Thành công!', 'Tài khoản đã được tạo!')

    tk.Button(root, text='Đăng ký', command=handle_register).pack(pady=10)
    tk.Button(root, text='Bạn đã có tài khoản? Ấn vào đây!',command=show_login_form).pack(pady=10)


if __name__ == '__main__':
    # khởi tạo màn hình
    root = tk.Tk()
    root.title('Authentication app')
    root.minsize(400, 200)

    show_login_form()

    root.mainloop()
