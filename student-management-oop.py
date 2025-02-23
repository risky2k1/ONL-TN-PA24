import tkinter as tk
from tkinter import messagebox, simpledialog


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def update_score(self, subject, score):
        self.scores[subject] = score

    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def __str__(self):
        return f"{self.name} - Scores: {self.scores} - Average: {self.get_average():.2f}"


class StudentManager:
    def __init__(self, root):
        self.students = {}
        self.root = root
        self.root.title("Quản lý Điểm Học Sinh")

        self.label = tk.Label(root, text="Chọn một chức năng:")
        self.label.pack()

        self.add_btn = tk.Button(root, text="Thêm học sinh", command=self.add_student)
        self.add_btn.pack()

        self.update_btn = tk.Button(root, text="Cập nhật điểm", command=self.update_score)
        self.update_btn.pack()

        self.show_btn = tk.Button(root, text="Hiển thị danh sách học sinh", command=self.show_students)
        self.show_btn.pack()

        self.avg_btn = tk.Button(root, text="Xem điểm trung bình", command=self.get_average)
        self.avg_btn.pack()

        self.quit_btn = tk.Button(root, text="Thoát", command=root.quit)
        self.quit_btn.pack()

    def add_student(self):
        name = simpledialog.askstring("Thêm học sinh", "Nhập tên học sinh:")
        if name:
            if name in self.students:
                messagebox.showerror("Lỗi", "Học sinh đã tồn tại!")
            else:
                self.students[name] = Student(name)
                messagebox.showinfo("Thành công", "Đã thêm học sinh.")

    def update_score(self):
        name = simpledialog.askstring("Cập nhật điểm", "Nhập tên học sinh:")
        if name in self.students:
            subject = simpledialog.askstring("Cập nhật điểm", "Nhập môn học:")
            score = simpledialog.askfloat("Cập nhật điểm", "Nhập điểm:")
            if subject and score is not None:
                self.students[name].update_score(subject, score)
                messagebox.showinfo("Thành công", "Cập nhật điểm thành công.")
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy học sinh!")

    def show_students(self):
        if not self.students:
            messagebox.showinfo("Danh sách học sinh", "Danh sách trống!")
        else:
            student_list = "\n".join(str(student) for student in self.students.values())
            messagebox.showinfo("Danh sách học sinh", student_list)

    def get_average(self):
        name = simpledialog.askstring("Xem điểm trung bình", "Nhập tên học sinh:")
        if name in self.students:
            avg = self.students[name].get_average()
            messagebox.showinfo("Điểm trung bình", f"Điểm trung bình của {name}: {avg:.2f}")
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy học sinh!")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManager(root)
    root.mainloop()
