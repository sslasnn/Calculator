import tkinter as tk
from tkinter import messagebox
import math

# --- Functions ---
def add_to_expression(value):
    """Add number, operator, or function to the display."""
    entry_display.insert(tk.END, str(value))

def calculate_expression():
    """Evaluate the mathematical expression safely."""
    try:
        expression = entry_display.get()
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        result = eval(expression, {"__builtins__": None}, allowed_names)
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        entry_display.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Error", "Invalid expression!")
        entry_display.delete(0, tk.END)

def clear_display():
    entry_display.delete(0, tk.END)

def backspace():
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current_text[:-1])

# --- Hover Effect ---
def on_enter(e):
    e.widget['bg'] = "#ffffff"
    e.widget['fg'] = "#2c3e50"

def on_leave(e, color, fg="#fff"):
    e.widget['bg'] = color
    e.widget['fg'] = fg

# --- Main Window ---
root = tk.Tk()
root.title("🌌 2025 Advanced Scientific Calculator")
root.configure(bg="#1c1c1c")
root.geometry("500x650")
root.minsize(450, 600)

# --- Display ---
entry_display = tk.Entry(root, font=("Fira Code", 24, "bold"), justify="right", bd=10, relief=tk.FLAT, bg="#2c3e50", fg="#ecf0f1", insertbackground='white')
entry_display.pack(fill='x', padx=15, pady=15)

# --- Frame Buttons ---
frame_buttons = tk.Frame(root, bg="#1c1c1c")
frame_buttons.pack(fill='both', expand=True, padx=15, pady=10)

# --- Buttons Layout ---
buttons = [
    ['7', '8', '9', '/', 'sqrt'],
    ['4', '5', '6', '*', 'pow'],
    ['1', '2', '3', '-', 'log'],
    ['0', '.', '=', '+', 'exp'],
    ['(', ')', 'sin', 'cos', 'tan'],
]

colors = {
    '+': "#27ae60", '-': "#c0392b", '*': "#2980b9", '/': "#8e44ad",
    '=': "#f39c12", 'sqrt': "#16a085", 'pow': "#8e44ad", 'log': "#f39c12",
    'exp': "#d35400", 'sin': "#2980b9", 'cos': "#2980b9", 'tan': "#2980b9"
}

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        bg_color = colors.get(char, "#34495e")
        fg_color = "white"
        if char == '=':
            btn = tk.Button(frame_buttons, text=char, font=("Fira Code", 18, "bold"),
                            bg=bg_color, fg=fg_color, bd=0, relief=tk.FLAT,
                            command=calculate_expression)
        elif char in '+-*/':
            btn = tk.Button(frame_buttons, text=char, font=("Fira Code", 18, "bold"),
                            bg=bg_color, fg=fg_color, bd=0, relief=tk.FLAT,
                            command=lambda x=char: add_to_expression(x))
        else:
            btn = tk.Button(frame_buttons, text=char, font=("Fira Code", 18, "bold"),
                            bg=bg_color, fg=fg_color, bd=0, relief=tk.FLAT,
                            command=lambda x=char: add_to_expression(x + '(' if x in ['sin','cos','tan','log','sqrt','pow','exp'] else x))
        btn.grid(row=r, column=c, sticky='nsew', padx=6, pady=6)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", lambda e, color=bg_color, fg=fg_color: on_leave(e, color, fg))

# Make buttons responsive
for i in range(len(buttons)):
    frame_buttons.rowconfigure(i, weight=1)
for i in range(len(buttons[0])):
    frame_buttons.columnconfigure(i, weight=1)

# --- Extra Controls ---
btn_clear = tk.Button(root, text="C", font=("Fira Code", 18, "bold"), bg="#e74c3c", fg="white", bd=0, relief=tk.FLAT, command=clear_display)
btn_clear.pack(fill='x', padx=15, pady=5)
btn_clear.bind("<Enter>", on_enter)
btn_clear.bind("<Leave>", lambda e: on_leave(e, "#e74c3c"))

btn_back = tk.Button(root, text="⌫", font=("Fira Code", 18, "bold"), bg="#95a5a6", fg="white", bd=0, relief=tk.FLAT, command=backspace)
btn_back.pack(fill='x', padx=15, pady=5)
btn_back.bind("<Enter>", on_enter)
btn_back.bind("<Leave>", lambda e: on_leave(e, "#95a5a6"))

# --- Keyboard Support ---
def key_press(event):
    allowed_keys = "0123456789+-*/()."
    if event.char in allowed_keys:
        add_to_expression(event.char)
    elif event.keysym == "Return":
        calculate_expression()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym.lower() == "c":
        clear_display()

root.bind("<Key>", key_press)

# --- Start App ---
root.mainloop()
