# Advanced Scientific Calculator - Python 2025

This repository contains an **advanced scientific calculator** built with Python and Tkinter. Users can perform basic arithmetic as well as scientific operations including trigonometric, logarithmic, exponential, and power functions. Input can be entered via the keyboard or through the GUI buttons.

---
## Features

- Basic operations: addition (+), subtraction (-), multiplication (*), division (/)
- Scientific functions: square root (`sqrt`), power (`pow`), logarithm (`log`), exponential (`exp`)
- Trigonometric functions: sin, cos, tan
- Keyboard and on-screen input support
- Backspace (`⌫`) and clear (`C`) functionality
- Modern, visually appealing user interface

---

## Installation and Usage

1. Ensure Python 3.x is installed (tkinter module included)
2. Run the calculator script:

```bash
python AdvancedCalculator.py
```
## Code
```bash
import tkinter as tk
from tkinter import messagebox
import math
```
# --- Functions ---
```bash
def add_to_expression(value):
    """Add number, operator, or function to the display."""
    entry_display.insert(tk.END, str(value))

def calculate_expression():
    """Evaluate the mathematical expression."""
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
```
# --- Main Window ---
```bash
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.configure(bg="#2c3e50")
root.geometry("450x600")
root.minsize(400, 550)
```
# --- Display ---
```bash
entry_display = tk.Entry(root, font=("Helvetica", 20), justify="right", bd=5, relief=tk.RIDGE)
entry_display.pack(fill='x', padx=10, pady=10)
```
# --- Button Frame ---
```bash
frame_buttons = tk.Frame(root, bg="#2c3e50")
frame_buttons.pack(fill='both', expand=True, padx=10, pady=10)
```
# --- Buttons Layout ---
```bash
buttons = [
    ['7', '8', '9', '/', 'sqrt'],
    ['4', '5', '6', '*', 'pow'],
    ['1', '2', '3', '-', 'log'],
    ['0', '.', '=', '+', 'exp'],
    ['(', ')', 'sin', 'cos', 'tan'],
]

operation_colors = {'+': "#27ae60", '-': "#c0392b", '*': "#2980b9", '/': "#8e44ad",
                    '=': "#f39c12", 'sqrt': "#16a085", 'pow': "#8e44ad", 'log': "#f39c12",
                    'exp': "#d35400", 'sin': "#2980b9", 'cos': "#2980b9", 'tan': "#2980b9"}

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char == '=':
            btn = tk.Button(frame_buttons, text=char, font=("Helvetica", 14, "bold"),
                            bg=operation_colors[char], fg="white", command=calculate_expression)
        elif char in '+-*/':
            btn = tk.Button(frame_buttons, text=char, font=("Helvetica", 14, "bold"),
                            bg=operation_colors[char], fg="white", command=lambda x=char: add_to_expression(x))
        else:
            btn = tk.Button(frame_buttons, text=char, font=("Helvetica", 14, "bold"),
                            bg=operation_colors.get(char, "#34495e"), fg="white",
                            command=lambda x=char: add_to_expression(x+'(' if x in ['sin','cos','tan','log','sqrt','pow','exp'] else x))
        btn.grid(row=r, column=c, sticky='nsew', padx=5, pady=5)

for i in range(len(buttons)):
    frame_buttons.rowconfigure(i, weight=1)
for i in range(len(buttons[0])):
    frame_buttons.columnconfigure(i, weight=1)
```
# --- Extra Controls ---
```bash
btn_clear = tk.Button(root, text="C", font=("Helvetica", 14, "bold"), bg="#e74c3c", fg="white",
                      command=clear_display)
btn_clear.pack(fill='x', padx=10, pady=5)

btn_back = tk.Button(root, text="⌫", font=("Helvetica", 14, "bold"), bg="#95a5a6", fg="white",
                     command=backspace)
btn_back.pack(fill='x', padx=10, pady=5)
```
# --- Keyboard Support ---
```bash
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
```
# --- Start App ---
```bash
root.mainloop()
```