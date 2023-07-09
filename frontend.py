import tkinter as tk
from tkinter import filedialog
import Main as m
import time

def upload_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)

def execute_code():
    file_path = file_entry.get()
    tax_percentage = float(tax_entry.get())
    profit_percentage = float(profit_entry.get())

    loading_label.config(text="Loading...")
    root.update()

    m.execute_code(file_path, tax_percentage, profit_percentage)
    loading_label.config(text="Completed!")
    time.sleep(2.5)
    root.destroy()

#GUI code
root = tk.Tk()
root.title("File Upload")

file_label = tk.Label(root, text="Select File:")
file_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=10, pady=5)

browse_button = tk.Button(root, text="Browse", command=upload_file)
browse_button.grid(row=0, column=2, padx=10, pady=5)

tax_label = tk.Label(root, text="Tax Percentage:")
tax_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

tax_entry = tk.Entry(root, width=40)
tax_entry.grid(row=1, column=1, padx=10, pady=5)

profit_label = tk.Label(root, text="Profit Percentage:")
profit_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

profit_entry = tk.Entry(root, width=40)
profit_entry.grid(row=2, column=1, padx=10, pady=5)

execute_button = tk.Button(root, text="Execute", command=execute_code)
execute_button.grid(row=3, column=1, padx=10, pady=5)

loading_label = tk.Label(root, text="")
loading_label.grid(row=4, column=1, pady=5)

root.mainloop()