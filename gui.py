import tkinter as tk
import os
import pathlib
from pathlib import Path

win = tk.Tk()
win.geometry("340x440")
win.title("Authentication_Parser")
win.configure(bg="black")

frame = tk.Frame(win, bg="black")

def info_text():
    line = Path(str(search_entry.get()))
    output = "Parsing " + (str(line)) + "..."
    info_sec = tk.Text(frame, width=100, height=75, bg='#333333', fg='green')
    info_sec.grid(row=3, column=1, columnspan=2, pady=10)
    info_sec.insert(1.0, str(output))
    info_sec.insert(2.0, str("\n"))
    if line.is_file():
        with open(line) as pass_file:
            for L in pass_file:
                info_sec.insert(3.0, str(L)),
    elif line.is_dir():
        list_dir = os.listdir(line)
        info_sec.insert(tk.END, str(list_dir) + "\n"),
    info_sec.configure(state="disabled")


#Creating Widget
title_label = tk.Label(frame, text="Auth_Parse", bg="black", fg="#FFFFFF", font=("Courier", 10))
parse_button = tk.Button(frame, text="Parce", font=("Courier", 10), command=info_text)
search_entry = tk.Entry(frame)

#Placing Widgets
title_label.grid(row=0, column=1, columnspan=2, stick="news", pady=10)
parse_button.grid(row=2, column=1, columnspan=2)
search_entry.grid(row=1, column=1, columnspan=2, pady=10)
frame.pack()

rows = 4
columns = 2
for i in range(rows):
    win.grid_rowconfigure(i, weight=1)
for i in range(columns):
    win.grid_columnconfigure(i, weight=1)

win.mainloop()