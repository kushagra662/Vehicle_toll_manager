import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

def get_frame(parent):
    frame = tk.Frame(parent, bg="black")

    def calculate_toll(v_type):
        return {"Car": 50, "Bike": 20, "Truck": 100}.get(v_type, 0)

    def add_entry():
        v_no = entry_number.get()
        v_type = vehicle_type.get()

        if not v_no or not v_type:
            messagebox.showerror("Error", "All fields required")
            return

        toll = calculate_toll(v_type)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("toll.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO vehicles (vehicle_number, vehicle_type, entry_time, toll_amount)
        VALUES (?, ?, ?, ?)
        """, (v_no, v_type, time, toll))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Toll Generated: ₹{toll}")

        entry_number.delete(0, tk.END)
        vehicle_type.set("")

    tk.Label(frame, text="🚗 Entry Form",
             font=("Arial", 60, "bold"),
             bg="black", fg="lime").pack(pady=10)

    entry_number = tk.Entry(frame)
    entry_number.pack(pady=10)

    vehicle_type = ttk.Combobox(frame, values=["Car", "Bike", "Truck"])
    vehicle_type.pack(pady=10)

    tk.Button(frame, text="Generate Toll",
              command=add_entry,
              bg="green", fg="blue").pack(pady=10)

    return frame