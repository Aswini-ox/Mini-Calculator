import tkinter as tk
import math

# Button click function
def click(button_text):
    current = entry.get()
    try:
        if button_text == "=":
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button_text == "C":
            entry.delete(0, tk.END)
        elif button_text == "√":
            result = str(math.sqrt(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button_text == "π":
            entry.insert(tk.END, str(math.pi))
        elif button_text == "sin":
            result = str(math.sin(math.radians(float(current))))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button_text == "cos":
            result = str(math.cos(math.radians(float(current))))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button_text == "tan":
            result = str(math.tan(math.radians(float(current))))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button_text == "log":
            result = str(math.log10(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        else:
            entry.insert(tk.END, button_text)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x550")
root.config(bg="#2b2b2b")

# Entry field
entry = tk.Entry(root, font=("Arial", 20), bd=8, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=15, padx=10, ipady=8)

# Button style
btn_style = {
    "font": ("Arial", 14, "bold"),
    "bd": 4,
    "relief": "raised",
    "width": 5,
    "height": 2
}

# Buttons layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3), ("C",1,4),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3), ("√",2,4),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3), ("π",3,4),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3), ("log",4,4),
    ("sin",5,0), ("cos",5,1), ("tan",5,2)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, **btn_style,
                    command=lambda t=text: click(t),
                    bg="#444", fg="white", activebackground="#666")
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
