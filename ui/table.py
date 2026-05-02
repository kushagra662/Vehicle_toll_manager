import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def get_frame(parent):
    frame = tk.Frame(parent, bg="black")

    def load_data():
        conn = sqlite3.connect("toll.db")
        cursor = conn.cursor()

        for row in tree.get_children():
            tree.delete(row)

        cursor.execute("SELECT * FROM vehicles ORDER BY id DESC")

        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

        conn.close()

    def delete_record():
        selected = tree.focus()

        if not selected:
            messagebox.showerror("Error", "Select a record")
            return

        record_id = tree.item(selected)['values'][0]

        conn = sqlite3.connect("toll.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM vehicles WHERE id=?", (record_id,))
        conn.commit()
        conn.close()

        load_data()

    tk.Label(frame, text="Records",
             font=("Arial", 60, "bold"),
             bg="black", fg="cyan").pack(pady=10)

    columns = ("ID", "Vehicle", "Type", "Time", "Amount")

    tree = ttk.Treeview(frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)

    tree.pack(fill="both", expand=True, pady=10)

    tk.Button(frame, text="Delete Selected",
              command=delete_record,
              bg="red", fg="blue").pack(pady=10)

    frame.load_data = load_data  # IMPORTANT

    load_data()

    return frame