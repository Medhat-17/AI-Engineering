import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    """Generates a random secure password"""
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols
    password = ''.join(random.choice(all_chars) for _ in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                          f"Username: {username}\nPassword: {password}\nSave?")
    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {username} | {password}\n")
        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        messagebox.showinfo(title="Success", message="Password saved successfully!")


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
tk.Label(window, text="Website:").grid(row=0, column=0)
tk.Label(window, text="Username/Email:").grid(row=1, column=0)
tk.Label(window, text="Password:").grid(row=2, column=0)
website_entry = tk.Entry(window, width=35)
website_entry.grid(row=0, column=1, columnspan=2)
website_entry.focus()

username_entry = tk.Entry(window, width=35)
username_entry.grid(row=1, column=1, columnspan=2)
username_entry.insert(0, "your_email@example.com")  # default email
password_entry = tk.Entry(window, width=21)
password_entry.grid(row=2, column=1)
tk.Button(window, text="Generate Password", command=generate_password).grid(row=2, column=2)
tk.Button(window, text="Add", width=36, command=save_password).grid(row=3, column=1, columnspan=2)

window.mainloop()
