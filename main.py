import tkinter as tk
import sqlite3

# import UI modules
from ui import form, table, dashboard


# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("toll.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_number TEXT,
    vehicle_type TEXT,
    entry_time TEXT,
    toll_amount INTEGER
)
""")

conn.commit()
conn.close()


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("🚗 Toll Management System")
root.geometry("900x550")
root.configure(bg="black")


# ---------------- CONTAINER ----------------
container = tk.Frame(root, bg="black")
container.pack(fill="both", expand=True)


# ---------------- FRAMES ----------------
frames = {}

frames["form"] = form.get_frame(container)
frames["table"] = table.get_frame(container)
frames["dashboard"] = dashboard.get_frame(container)

for frame in frames.values():
    frame.grid(row=0, column=0, sticky="nsew")


# ---------------- NAVIGATION FUNCTION ----------------

def show_frame(name):
    frame = frames[name]

    # Safe calls (prevents crash if missing)
    if hasattr(frame, "load_data"):
        frame.load_data()

    if hasattr(frame, "load_stats"):
        frame.load_stats()

    frame.tkraise()


# ---------------- TOP MENU ----------------
menu = tk.Frame(root, bg="gray")
menu.pack(fill="x")

tk.Button(menu, text="🚗 Entry Form",
          command=lambda: show_frame("form")).pack(side="left", padx=10, pady=5)

tk.Button(menu, text="📊 Records",
          command=lambda: show_frame("table")).pack(side="left", padx=10, pady=5)

tk.Button(menu, text="📈 Dashboard",
          command=lambda: show_frame("dashboard")).pack(side="left", padx=10, pady=5)


# ---------------- DEFAULT SCREEN ----------------
show_frame("form")
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)


# ---------------- RUN APP ----------------
root.mainloop()