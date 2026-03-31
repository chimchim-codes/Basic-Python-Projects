import customtkinter as tk
import tkinter as tko
def add_item():
    item = entry.get()
    if item != "":
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

def delete_item():
    selected= listbox.curselection()
    if selected:
        listbox.delete(selected)

root= tk.CTk()
root.title("To Do List")
root.geometry("420x400")

entry=tk.CTkEntry(root, width=375)
entry.grid(row=1, column=0,columnspan=4, padx=10, pady=10)

btn1=tk.CTkButton(root, text="Add your item", command= add_item)
btn1.grid(row=2, column=0, padx=10)

btn2=tk.CTkButton(root, text="Delete your item", command= delete_item)
btn2.grid(row=2, column=3, padx=10)

listbox=tko.Listbox(root, width=47, height=200)
listbox.grid(row=3, column=0, columnspan=4)

root.mainloop()
