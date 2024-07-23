import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime
from collections import defaultdict

# File to store expenses
FILE_NAME = 'expenses.csv'

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        self.create_widgets()
        self.create_file()

    def create_widgets(self):
        # Labels
        self.amount_label = ttk.Label(self.root, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=5, sticky='W')
        
        self.description_label = ttk.Label(self.root, text="Description:")
        self.description_label.grid(row=1, column=0, padx=10, pady=5, sticky='W')

        self.category_label = ttk.Label(self.root, text="Category:")
        self.category_label.grid(row=2, column=0, padx=10, pady=5, sticky='W')

        # Entry fields
        self.amount_entry = ttk.Entry(self.root, width=20)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=5)

        self.description_entry = ttk.Entry(self.root, width=20)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)

        # Category dropdown
        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(self.root, textvariable=self.category_var)
        self.category_combobox['values'] = ('Food', 'Transportation', 'Entertainment', 'Others')
        self.category_combobox.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = ttk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.summary_button = ttk.Button(self.root, text="View Summary", command=self.view_summary)
        self.summary_button.grid(row=4, column=0, columnspan=2, pady=10)

    def create_file(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Amount', 'Description', 'Category'])

    def add_expense(self):
        amount = self.amount_entry.get()
        description = self.description_entry.get()
        category = self.category_var.get()

        if not amount or not description or not category:
            messagebox.showerror("Input Error", "All fields are required")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number")
            return

        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d"), amount, description, category])

        messagebox.showinfo("Success", "Expense added successfully")
        self.clear_entries()

    def clear_entries(self):
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.category_combobox.set('')

    def view_summary(self):
        expenses = defaultdict(float)
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row['Category']
                amount = float(row['Amount'])
                expenses[category] += amount

        summary_message = "Expense Summary:\n"
        for category, total in expenses.items():
            summary_message += f"{category}: ${total:.2f}\n"

        messagebox.showinfo("Expense Summary", summary_message)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
