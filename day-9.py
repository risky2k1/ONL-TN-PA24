# Cách đã được học ở bài trước:
# with open('toy-store.csv', 'r') as file:
#     toys = file.readlines()
#     print(toys)

# Cách 2 là sử dụng thư viện csv để đọc file csv:
# import csv
# with open('toy-store.csv', 'r') as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row[0])

# Sử dụng thư viện pandas:
import pandas as pd

data = pd.read_csv('toy-store.csv')

print(data)
# Dữ liệu được hiển thị dưới dạng DataFrame

# Lấy dữ liệu của cột: data['tên cột'] or data.TÊN_CỘT
# print(data['Stock'])
# print(data['Price'])
# print(data['Toy Name'])
# print(data.Stock)
# print(data.Price)

# Cột đó mà chứa toàn dữ liệu số nguyên (int) -> sử dụng .sum() để tính tổng
# print(data.Stock.sum())
# print(data.Price.sum())
# Tính giá trị trung bình của cột mean()
# print(data.Stock.mean())

# Tính max or min
# print(data.Price.max())
# print(data.Price.min())
max_price = data.Price.max()
min_price = data.Price.min()

# Tìm trong cột Price hàng nào có giá trị = max_price or min_price
max_price_row = data[data.Price == max_price]
min_price_row = data[data.Price == min_price]
# print(max_price_row)
# In ra tên của sản phẩm có giá tiền lớn nhất or nhỏ nhất
print(max_price_row['Toy Name'])
print(min_price_row['Toy Name'])


# Lấy ra Tên đồ chơi có số lượng ít nhất
min_stock = data.Stock.min()
min_stock_row = data[data.Stock == min_stock]
print(min_stock_row['Toy Name'])