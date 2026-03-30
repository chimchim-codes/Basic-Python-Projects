import tkinter as tk

def add_item():
    item = entry.get()
    if item != "":
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
