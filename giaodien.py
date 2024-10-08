import tkinter as tk

# Hàm xử lý khi nút được nhấn
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Hàm để tính toán kết quả
def btn_equal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

# Hàm xóa màn hình
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

expression = ""

# Khung để hiển thị biểu thức và kết quả
input_text = tk.StringVar()

# Tạo một Entry widget để hiển thị input
input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Tạo khung để chứa các nút
btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# Hàng đầu tiên
clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3)
divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3)

# Hàng thứ hai
seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0)
eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1)
nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2)
multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3)

# Hàng thứ ba
four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0)
five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1)
six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2)
minus = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3)

# Hàng thứ tư
one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0)
two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1)
three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2)
plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3)

# Hàng thứ năm
zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2)
point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2)
equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_equal()).grid(row=4, column=3)

# Bắt đầu vòng lặp chính của chương trình
root.mainloop()
