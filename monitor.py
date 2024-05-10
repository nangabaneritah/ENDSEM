import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
import time



def add_record():
    name = names_entry.get()
    goods = goods_entry.get()
    price = f"Ugx {price_entry.get()}"
    payment_status = payment_status_combobox.get()
    #date = datetime.datetime.now().strftime("%Y-%m-%d")
    expected_payment_date = expected_payment_date_entry.get()
    borrowing_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    contact = contact_entry.get() if payment_status == "Borrowed" and borrow_checkbox_var.get() else ""

    if goods and price and payment_status:
        record = (name,goods, price, payment_status, expected_payment_date, borrowing_time, contact)
        tree.insert("", tk.END, values=record)
    else:
        messagebox.showwarning("Warning", "Please fill all the requered fields.")

def delete_record():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Warning", "Please select a record to delete.")

def mark_as_paid():
    selected_item = tree.selection()
    if selected_item:
        tree.item(selected_item, values=(*tree.item(selected_item, 'values')[:3], "Paid", *tree.item(selected_item, 'values')[4:]))
    else:
        messagebox.showwarning("Warning", "Please select a record to mark as paid.")

def update_borrowing_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d   %H:%M:%S")
    tree.item("", values=("Borrowed", "Current Time:", current_time))
    tree.after(1000, update_borrowing_time)  # Update every 1000 milliseconds (1 second)

def toggle_contact_entry():
    if payment_status_combobox.get() == "Borrowed" and borrow_checkbox_var.get():
        contact_entry.config(state="normal")
    else:
        contact_entry.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("Goods Record System")
root.resizable = (1,1)

#root.geometry("1000x800")
tk.Label(root, text="Business Management System", font=("arial bold",23), bg='Blue',fg='white').pack(side="top", fill="x")
# Create a frame for adding records
frame_add_record = tk.Frame(root)
frame_add_record.pack(pady=10)


# names entry widget
tk.Label(frame_add_record,fg="white",bg='gray',font=("bold arial",13), text="Name:").grid(row=1, column=0, padx=5, pady=5)
names_entry = tk.Entry(frame_add_record,fg='blue',font=("bold arial",13), width=30)
names_entry.grid(row=1, column=1, padx=5, pady=5)

# Goods entry widget
tk.Label(frame_add_record,fg="white",bg='gray',font=("bold arial",13), text="Goods:").grid(row=2, column=0, padx=5, pady=5)
goods_entry = tk.Entry(frame_add_record,fg='blue',font=("bold arial",13), width=30)
goods_entry.grid(row=2, column=1, padx=5, pady=5)

# Price entry widget
tk.Label(frame_add_record,fg="white",bg='gray',font=("bold arial",13), text="Price:").grid(row=3, column=0, padx=5, pady=5)
price_entry = tk.Entry(frame_add_record, width=30,fg="blue",font=("bold arial",13))
price_entry.grid(row=3, column=1, padx=5, pady=5)

# Payment status combobox
tk.Label(frame_add_record,fg="white",bg='gray',font=("bold arial",13), text="Payment Status:").grid(row=4, column=0, padx=5, pady=5)
payment_status_combobox = ttk.Combobox(frame_add_record, width=27,font=("bold arial",13), values=["","Paid", "Borrowed"])
payment_status_combobox.grid(row=4, column=1, padx=5, pady=5)
payment_status_combobox.current(0)

# Expected payment date entry widget
tk.Label(frame_add_record,fg="white",bg='gray',font=("bold arial",13), text="Expected Payment Date:").grid(row=5, column=0, padx=5, pady=5)
expected_payment_date_entry = tk.Entry(frame_add_record, width=30,fg="blue",font=("bold arial",13))
expected_payment_date_entry.grid(row=5, column=1, padx=5, pady=5)

# Contact entry widget
tk.Label(frame_add_record,fg="white",bg='gray',font=("bold arial",13), text="Contact:").grid(row=6, column=0, padx=5, pady=5)
contact_entry = tk.Entry(frame_add_record,fg="blue",font=("bold arial",13), width=30, state="disabled")
contact_entry.grid(row=6, column=1, padx=5, pady=5)

# Borrow checkbox
borrow_checkbox_var = tk.BooleanVar()
borrow_checkbox = tk.Checkbutton(frame_add_record,fg="white",bg='gray',font=("bold arial",13), text="Borrow", variable=borrow_checkbox_var, command=toggle_contact_entry)
borrow_checkbox.grid(row=7, columnspan=2)

# Add record button
add_record_button = tk.Button(root, text="Add Record", width=15,fg="white",bg='green',font=("bold arial",13), command=add_record)
add_record_button.pack(pady=5)

# Create Treeview widget
tree = ttk.Treeview(root,columns=("Names","Goods", "Price", "Payment Status", "Expected Payment Date", "Borrowing Time", "Contact"), show="headings")
tree.heading("Names", text="Names")
tree.heading("Goods", text="Goods")
tree.heading("Price", text="Price")
tree.heading("Payment Status", text="Payment Status")
#tree.heading("Date", text="Date")
tree.heading("Expected Payment Date", text="Expected Payment Date")
tree.heading("Borrowing Time", text="Borrowing Time")
tree.heading("Contact", text="Contact")
tree.pack(pady=10)

# Create buttons for delete and mark as paid
button_frame = tk.Frame(root)
button_frame.pack(pady=5)
delete_button = tk.Button(button_frame, text="Delete Record", width=15, fg="white",bg='red',font=("bold arial",13), command=delete_record)
delete_button.grid(row=0, column=0, padx=5)
mark_paid_button = tk.Button(button_frame, text="Mark as Paid", width=15,fg="white",bg='blue',font=("bold arial",13), command=mark_as_paid)
mark_paid_button.grid(row=0, column=1, padx=5)

# Update borrowing time
update_borrowing_time()

# Run the application
root.mainloop()