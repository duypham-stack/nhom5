import tkinter as tk
from tkinter import Entry, Label, Button, Text
import numpy as np

# Hàm để giải hệ phương trình
def solve_equations():
    equations = []
    results = []
    
    # Lấy giá trị từ các ô nhập liệu và tách chúng thành các phương trình
    for i in range(num_equations):
        equation = []
        for j in range(num_variables):
            entry = entry_matrix[i][j].get()
            equation.append(float(entry))
        result = float(result_entries[i].get())
        
        equations.append(equation)
        results.append(result)
    
    # Giải hệ phương trình bằng NumPy
    try:
        solutions = np.linalg.solve(equations, results)
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Kết quả:\n")
        for i in range(num_variables):
            result_text.insert(tk.END, f"x{i+1} = {solutions[i]}\n")
        result_text.config(state=tk.DISABLED)
    except np.linalg.LinAlgError:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Hệ phương trình không có nghiệm hoặc có vô số nghiệm.")
        result_text.config(state=tk.DISABLED)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Giải hệ phương trình")

# Nhập số lượng phương trình và biến
num_equations_label = Label(root, text="Số lượng phương trình:")
num_equations_label.pack()
num_equations_entry = Entry(root)
num_equations_entry.pack()

num_variables_label = Label(root, text="Số lượng biến:")
num_variables_label.pack()
num_variables_entry = Entry(root)
num_variables_entry.pack()

# Hàm xử lý khi nhấn nút "Xác nhận"
def confirm_dimensions():
    global num_equations
    global num_variables
    num_equations = int(num_equations_entry.get())
    num_variables = int(num_variables_entry.get())

    # Tạo các ô nhập liệu cho hệ phương trình và kết quả
    global entry_matrix
    global result_entries
    entry_matrix = []
    result_entries = []

    for i in range(num_equations):
        equation_frame = tk.Frame(root)
        equation_frame.pack()

        equation_entries = []
        for j in range(num_variables):
            entry = Entry(equation_frame)
            entry.grid(row=0, column=j)
            equation_entries.append(entry)
        result_entry = Entry(equation_frame)
        result_entry.grid(row=0, column=num_variables)
        equation_entries.append(result_entry)

        entry_matrix.append(equation_entries)
        result_entries.append(result_entry)

    # Thêm nút giải phương trình
    solve_button = Button(root, text="Giải", command=solve_equations)
    solve_button.pack()

# Thêm nút "Xác nhận"
confirm_button = Button(root, text="Xác nhận", command=confirm_dimensions)
confirm_button.pack()

# Kết quả
result_text = Text(root, state=tk.DISABLED, height=10, width=30)
result_text.pack()

root.mainloop()
