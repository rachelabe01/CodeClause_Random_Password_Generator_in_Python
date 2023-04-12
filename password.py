import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Random Password Generator")
        
        self.uppercase = tk.IntVar()
        self.lowercase = tk.IntVar()
        self.digits = tk.IntVar()
        self.punctuation = tk.IntVar()
        self.length = tk.IntVar()
        
        self.uppercase_checkbox = tk.Checkbutton(master, text="Uppercase", variable=self.uppercase)
        self.uppercase_checkbox.pack()
        
        self.lowercase_checkbox = tk.Checkbutton(master, text="Lowercase", variable=self.lowercase)
        self.lowercase_checkbox.pack()
        
        self.digits_checkbox = tk.Checkbutton(master, text="Digits", variable=self.digits)
        self.digits_checkbox.pack()
        
        self.punctuation_checkbox = tk.Checkbutton(master, text="Punctuation", variable=self.punctuation)
        self.punctuation_checkbox.pack()
        
        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.pack()
        
        self.length_entry = tk.Entry(master, textvariable=self.length)
        self.length_entry.pack()
        
        self.generate_button = tk.Button(master, text="Generate", command=self.generate_password)
        self.generate_button.pack()
        
        self.password_label = tk.Label(master, text="")
        self.password_label.pack()
        
    def generate_password(self):
        if self.uppercase.get() == 0 and self.lowercase.get() == 0 and self.digits.get() == 0 and self.punctuation.get() == 0:
            messagebox.showwarning("Warning", "Please select at least one character type.")
            return
        
        length = self.length.get()
        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4 characters.")
            return
        
        characters = []
        if self.uppercase.get():
            characters.extend(string.ascii_uppercase)
        if self.lowercase.get():
            characters.extend(string.ascii_lowercase)
        if self.digits.get():
            characters.extend(string.digits)
        if self.punctuation.get():
            characters.extend(string.punctuation)
        
        password = ''.join(random.choice(characters) for i in range(length))
        self.password_label.config(text=password)

root = tk.Tk()
password_generator = PasswordGenerator(root)
root.mainloop()
