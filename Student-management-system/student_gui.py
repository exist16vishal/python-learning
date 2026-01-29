import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
FILE = "students.csv"

def load_data():
    try:
        return pd.read_csv(FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Roll", "Marks", "Grade"])

def save_data(df):
    df.to_csv(FILE, index=False)
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")
root.config(bg="#f2f2f2")

df = load_data()
tk.Label(root, text="Name:", bg="#f2f2f2").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Roll:", bg="#f2f2f2").pack()
roll_entry = tk.Entry(root, width=40)
roll_entry.pack()

tk.Label(root, text="Marks:", bg="#f2f2f2").pack()
marks_entry = tk.Entry(root, width=40)
marks_entry.pack()
columns = ("Name", "Roll", "Marks", "Grade")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(pady=10)
def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    marks = marks_entry.get()

    if not (name and roll and marks):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        marks = float(marks)
    except ValueError:
        messagebox.showerror("Error", "Marks must be numeric!")
        return

    global df
    new_row = pd.DataFrame([{
        "Name": name,
        "Roll": int(roll),
        "Marks": marks,
        "Grade": grade(marks)
    }])
    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)
    update_table()
    messagebox.showinfo("Success", f"Student {name} added successfully!")

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)
def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    marks = marks_entry.get()

    if not (name and roll and marks):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        marks = float(marks)
    except ValueError:
        messagebox.showerror("Error", "Marks must be numeric!")
        return

    global df
    new_row = pd.DataFrame([{
        "Name": name,
        "Roll": int(roll),
        "Marks": marks,
        "Grade": grade(marks)
    }])
    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)
    update_table()
    messagebox.showinfo("Success", f"Student {name} added successfully!")

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)
def update_table():
    for row in tree.get_children():
        tree.delete(row)
    for _, row in df.iterrows():
        tree.insert("", tk.END, values=(row["Name"], row["Roll"], row["Marks"], row["Grade"]))
tk.Button(root, text="Add Student", command=add_student, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="View Data", command=update_table, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, bg="#f44336", fg="white").pack(pady=5)
update_table()
root.mainloop()
