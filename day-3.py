class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        """Tính điểm trung bình của sinh viên."""
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def add_score(self, score):
        """Thêm điểm vào danh sách điểm số."""
        self.scores.append(score)

    @classmethod
    def from_list(cls, student_data):
        """Tạo một sinh viên từ danh sách dữ liệu."""
        name, scores = student_data
        return cls(name, scores)

    @staticmethod
    def is_passing(average_score):
        """Kiểm tra sinh viên có đạt điểm qua môn không."""
        return average_score >= 5


# Ví dụ sử dụng
# Tạo sinh viên từ danh sách
student = Student.from_list(["Nguyen Van A", [8.5, 7.0, 9.0]])

# Tính điểm trung bình
average = student.calculate_average()
print(f"Điểm trung bình: {average}")

# Thêm điểm và tính lại điểm trung bình
student.add_score(6.5)
average = student.calculate_average()
print(f"Điểm trung bình sau khi thêm điểm: {average}")

# Kiểm tra sinh viên có qua môn hay không
is_passing = Student.is_passing(average)
print(f"Sinh viên có qua môn không? {'Có' if is_passing else 'Không'}")
