import tkinter as tk
from tkinter import Entry, Label, Button, messagebox
import numpy as np

def solve_equations():
    try:
        # Lấy dữ liệu từ các ô nhập liệu
        coefficients = []
        for i in range(n):
            row = []
            for j in range(n + 1):
                entry = entries[i][j]
                value = float(entry.get())
                row.append(value)
            coefficients.append(row)
        
        A = np.array(coefficients[:, :-1])  # Ma trận hệ số
        b = np.array(coefficients[:, -1])   # Vector vế phải
        
        # Giải hệ phương trình
        x = np.linalg.solve(A, b)
        
        # Hiển thị kết quả
        result_label.config(text="Nghiệm của hệ phương trình là:\n" + format_solution(x))
    except Exception as e:
        messagebox.showerror("Lỗi", "Đã xảy ra lỗi: " + str(e))

def format_solution(x):
    # Định dạng nghiệm thành chuỗi
    solution_str = ""
    for i, value in enumerate(x):
        solution_str += f"x{i+1} = {value}\n"
    return solution_str

def confirm_dimensions():
    global n
    n = int(n_entry.get())
    
    # Xóa các ô nhập liệu cũ (nếu có)
    for row_entries in entries:
        for entry in row_entries:
            entry.destroy()
    
    entries.clear()
    
    # Tạo lại các ô nhập liệu cho hệ phương trình mới
    for i in range(n):
        row_entries = []
        for j in range(n + 1):
            entry = Entry(window)
            entry.grid(row=i + 3, column=j + 1)
            row_entries.append(entry)
        entries.append(row_entries)

    # Tạo nút để giải hệ phương trình
    solve_button = Button(window, text="Giải", command=solve_equations)
    solve_button.grid(row=n + 4, column=1, columnspan=n + 1)

# Tạo cửa sổ giao diện người dùng
window = tk.Tk()
window.title("Giải hệ phương trình")

# Nhập số phương trình và số ẩn
n_label = Label(window, text="Nhập số phương trình và số ẩn:")
n_label.grid(row=1, column=1)
n_entry = Entry(window)
n_entry.grid(row=1, column=2)

# Tạo nút để xác nhận số phương trình và số ẩn
confirm_button = Button(window, text="Xác nhận", command=confirm_dimensions)
confirm_button.grid(row=1, column=3)

# Label để hiển thị kết quả
result_label = Label(window, text="")
result_label.grid(row=2, column=1, columnspan=3)

entries = []
n = 0  # Số phương trình và số ẩn

# Bắt đầu vòng lặp chạy chương trình GUI
window.mainloop()
