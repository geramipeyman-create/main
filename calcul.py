import tkinter as tk

root = tk.Tk()
root.title("PEYMAN")
root.geometry("320x480")
root.configure(bg="#1e1e1e")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = tk.StringVar()

# 🔥 عنوان ساده و تمیز
title = tk.Label(root, text="PEYMAN",
                 font=("Arial", 20, "bold"),
                 fg="#00e6ac", bg="#1e1e1e")
title.grid(row=0, column=0, columnspan=4, pady=10)

# 📺 نمایشگر
entry = tk.Entry(root, textvariable=equation,
                 font=("Arial", 20),
                 bd=5, relief="flat",
                 justify="right",
                 bg="#2b2b2b", fg="white")
entry.grid(row=1, column=0, columnspan=4,
           padx=10, pady=10, ipady=10, sticky="nsew")

# 📱 تنظیم ریسپانسیو (خیلی مهم برای بیرون نزدن)
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# دکمه‌ها
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

def create_btn(text, row, col):
    if text == "=":
        color = "#00cc66"
        cmd = equalpress
    elif text in ['+', '-', '*', '/']:
        color = "#404040"
        cmd = lambda x=text: press(x)
    else:
        color = "#333333"
        cmd = lambda x=text: press(x)

    tk.Button(root, text=text,
              font=("Arial", 14, "bold"),
              bg=color, fg="white",
              relief="flat",
              command=cmd
              ).grid(row=row, column=col,
                     padx=5, pady=5,
                     sticky="nsew")

for (t, r, c) in buttons:
    create_btn(t, r, c)

# 🔴 دکمه C
tk.Button(root, text="C",
          font=("Arial", 14, "bold"),
          bg="#cc3333", fg="white",
          relief="flat",
          command=clear
          ).grid(row=6, column=0, columnspan=4,
                 sticky="nsew",
                 padx=10, pady=10)

root.mainloop()