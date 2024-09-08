import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_button_click():
    try:
        length = int(length_combobox.get())
        if length < 1:
            raise ValueError("Password length must be at least 1")
        
        password = generate_password(length)
        password_text.delete(1.0, tk.END)  
        password_text.insert(tk.END, password)
        color_password(password)
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_text.get(1.0, tk.END).strip())
    root.update()  
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")  
root.configure(bg="white smoke")  

main_frame = tk.Frame(root, padx=20, pady=20, bg="sky blue", borderwidth=2, relief="raised")
main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

header_label = tk.Label(main_frame, text="Password Generator", bg="sky blue", fg="white", font=("Arial", 16, "bold"))
header_label.pack(pady=(0, 20))

length_frame = tk.Frame(main_frame, bg="sky blue")
length_frame.pack(pady=(0, 10))

length_label = tk.Label(length_frame, text="Password Length:", bg="sky blue", fg="white", font=("Arial", 12))
length_label.pack(side=tk.LEFT, padx=(0, 10))

length_options = [8, 10, 11, 12, 15 ,16, 20]
length_combobox = ttk.Combobox(length_frame, values=length_options, state="readonly", width=10, font=("Arial", 12))
length_combobox.set(length_options[0])  
length_combobox.pack(side=tk.LEFT)

generate_button = tk.Button(main_frame, text="Generate Password", command=on_generate_button_click, bg="green", fg="white", font=("Arial", 12, "bold"), relief="flat")
generate_button.pack(pady=(10, 10))

copy_button = tk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard, bg="blue", fg="white", font=("Arial", 12, "bold"), relief="flat")
copy_button.pack(pady=(0, 20))

password_frame = tk.Frame(main_frame, bg="black")
password_frame.pack()

password_label = tk.Label(password_frame, text="Generated Password:", bg="black", fg="white", font=("Arial", 12))
password_label.pack(side=tk.LEFT, padx=(0, 10))

password_text = tk.Text(password_frame, width=50, height=2, font=("Arial", 12), borderwidth=2, relief="sunken", wrap=tk.NONE)
password_text.pack(side=tk.LEFT)

root.mainloop()
