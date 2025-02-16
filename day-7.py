# Thao tác với file sử dụng Python
# r -> read Chỉ có quyền đọc
# w -> write Có quyền đọc và ghi
# a -> append Chỉ thêm nội dung vào cuối file - Ko sửa được nội dung cũ

# Cách 1: sử dụng open và close
# file = open('./file_test.txt', 'r')

# Đọc nội dung file -> trả về chuỗi:
# file_content = file.read()
# Đọc dòng đầu tiên của file
# first_line = file.readline()
# Đọc nội dung file -> trả về các dòng dưới dạng 1 list:
# lines = file.readlines()


# Khi đã mở file bằng open thì cần close file để giải phóng bộ nhớ
# file.close()

# Cách 2: 
# + Ko đóng mở thủ công
# + Tự tạo file nếu ko tìm thấy
with open('new_file.txt', 'a') as file:
    # content = file.read()
    file.write('\na new line')
    # print(content)
