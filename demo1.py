# Nhập vào 2 số nguyên
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

# Tính toán
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b if b != 0 else "Không thể chia cho 0"

# In kết quả
print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Thương:", thuong)