
from tkinter import *
import tkinter as tk
from tkinter import messagebox









win= tk.Tk()
win.title("MY PYTHON EXERCISE")
win.geometry("700x500")
win.configure(background='black')
win.resizable(False, False)

label=tk.Label(win,text="Hello Dear User",font="Arial",fg="white", bg="black")
label.pack(pady=70)
entry = tk.Entry(win, font=("Arial", 16))

def show_text():
    user_text = entry.get()  # get text from entry
    label.config(text=f"You typed: {user_text}")  # change label tex

win.mainloop()
