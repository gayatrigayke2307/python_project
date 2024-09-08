import tkinter as tk
from tkinter import ttk, messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book ")
        self.root.geometry("800x600")
        self.root.configure(bg='#f7f7f7')

        self.contacts = {}  
        self.main_frame = tk.Frame(self.root, bg='#f7f7f7')
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.details_frame = tk.Frame(self.main_frame, bg='#ffffff')
        self.details_frame.pack(fill=tk.X, padx=10, pady=10)

        self.list_frame = tk.Frame(self.main_frame, bg='#e0e0e0')
        self.list_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        tk.Label(self.details_frame, text="Name", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.entry_name = tk.Entry(self.details_frame, width=40, font=('Arial', 12))
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.details_frame, text="Phone Number", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.entry_phone = tk.Entry(self.details_frame, width=40, font=('Arial', 12))
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.details_frame, text="Email Address", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.entry_email = tk.Entry(self.details_frame, width=40, font=('Arial', 12))
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.button_frame = tk.Frame(self.details_frame, bg='#ffffff')
        self.button_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')

        self.button_add = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact, bg='#4CAF50', fg='white', font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5)
        self.button_add.grid(row=0, column=0, padx=5)

        self.button_view = tk.Button(self.button_frame, text="View Contact", command=self.view_contact, bg='#2196F3', fg='white', font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5)
        self.button_view.grid(row=0, column=1, padx=5)

        self.button_search = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact, bg='#FFC107', fg='black', font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5)
        self.button_search.grid(row=0, column=2, padx=5)

        self.button_update = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact, bg='#FF5722', fg='white', font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5)
        self.button_update.grid(row=0, column=3, padx=5)

        self.button_delete = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, bg='#F44336', fg='white', font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5)
        self.button_delete.grid(row=0, column=4, padx=5)

        self.tree = ttk.Treeview(self.list_frame, columns=("Name", "Phone", "Email"), show='headings', height=15)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone Number")
        self.tree.heading("Email", text="Email Address")
        self.tree.column("Name", width=150)
        self.tree.column("Phone", width=150)
        self.tree.column("Email", width=200)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.list_frame, orient="vertical", command=self.tree.yview)
        self.tree_scroll.pack(side=tk.RIGHT, fill="y")
        self.tree.configure(yscrollcommand=self.tree_scroll.set)

        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()

        if name and phone and email:
            if name in self.contacts:
                messagebox.showwarning("Duplicate Contact", "Contact already exists.")
            else:
                self.contacts[name] = (phone, email)
                self.tree.insert("", "end", iid=name, values=(name, phone, email))
                self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def view_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            name = selected_item[0]
            phone, email = self.contacts[name]
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, name)
            self.entry_phone.delete(0, tk.END)
            self.entry_phone.insert(0, phone)
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, email)
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to view.")

    def search_contact(self):
        name = self.entry_name.get()
        if name in self.contacts:
            phone, email = self.contacts[name]
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {phone}\nEmail: {email}")
        else:
            messagebox.showwarning("Search Error", "Contact not found.")

    def update_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            old_name = selected_item[0]
            new_name = self.entry_name.get()
            phone = self.entry_phone.get()
            email = self.entry_email.get()

            if new_name and phone and email:
                if old_name != new_name and new_name in self.contacts:
                    messagebox.showwarning("Duplicate Contact", "Contact with this name already exists.")
                else:
                    del self.contacts[old_name]
                    self.contacts[new_name] = (phone, email)
                    self.tree.item(old_name, iid=new_name, values=(new_name, phone, email))
                    self.tree.delete(old_name)
                    self.clear_entries()
            else:
                messagebox.showwarning("Input Error", "Please fill in all fields.")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            name = selected_item[0]
            del self.contacts[name]
            self.tree.delete(name)
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            name = selected_item[0]
            phone, email = self.contacts[name]
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, name)
            self.entry_phone.delete(0, tk.END)
            self.entry_phone.insert(0, phone)
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, email)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
