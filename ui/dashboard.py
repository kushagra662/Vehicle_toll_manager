import tkinter as tk
import sqlite3

def get_frame(parent):
    frame = tk.Frame(parent, bg="black")

    def load_stats():
        conn = sqlite3.connect("toll.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM vehicles")
        total = cursor.fetchone()[0]

        cursor.execute("SELECT SUM(toll_amount) FROM vehicles")
        amount = cursor.fetchone()[0] or 0

        total_label.config(text=f"🚗 Total Vehicles: {total}")
        amount_label.config(text=f"💰 Total Collection: ₹{amount}")

        conn.close()

    tk.Label(frame, text="Dashboard",
             font=("Arial", 60, "bold"),
             bg="black", fg="yellow").pack(pady=10)

    total_label = tk.Label(frame, text="", bg="black", fg="white")
    total_label.pack(pady=5)

    amount_label = tk.Label(frame, text="", bg="black", fg="white")
    amount_label.pack(pady=5)

    tk.Button(frame, text="Refresh",
              command=load_stats,
              bg="green", fg="blue").pack(pady=10)

    frame.load_stats = load_stats  # IMPORTANT

    load_stats()

    return frame