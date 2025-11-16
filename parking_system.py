import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime

# ---------- Database Connection ----------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="vanir35^#k",   # change to your MySQL password
        database="park"
    )

# ---------- Gradient Drawer ----------
def draw_gradient(canvas, color1, color2, width, height):
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f"#{nr//256:02x}{ng//256:02x}{nb//256:02x}"
        canvas.create_line(0, i, width, i, fill=color)

# ---------- Start Page ----------
def start_page():
    win = tk.Tk()
    win.title("Smart Parking System")
    win.state("zoomed")

    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()

    # Light Blue Gradient Background
    canvas = tk.Canvas(win, width=width, height=height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    draw_gradient(canvas, "#87CEFA", "#E6F2FF", width, height)

    # Title
    canvas.create_text(width//2, 150, text="SMART PARKING SYSTEM",
                       font=("Helvetica", 42, "bold"), fill="#003366")

    # Login button
    login_btn = tk.Button(win, text="LOGIN", font=("Arial", 22, "bold"),
                          bg="#28a745", fg="white", width=18, height=2,
                          command=lambda: [win.destroy(), login_page()])
    canvas.create_window(width//2, height//2, window=login_btn, anchor="center")

    win.mainloop()

# ---------- Login Page ----------
def login_page():
    win = tk.Tk()
    win.title("Login")
    win.state("zoomed")

    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()

    # Light Blue Gradient
    canvas = tk.Canvas(win, width=width, height=height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    draw_gradient(canvas, "#87CEFA", "#E6F2FF", width, height)

    # Center frame
    login_frame = tk.Frame(canvas, bg="#e6f2ff", bd=8, relief="ridge")
    canvas.create_window(width//2, height//2, window=login_frame, anchor="center")

    # Title
    tk.Label(login_frame, text="User Login",
             font=("Helvetica", 24, "bold"),
             bg="#e6f2ff", fg="#003366").grid(row=0, column=0, columnspan=2, pady=20)

    # Username
    tk.Label(login_frame, text="Username", font=("Helvetica", 18),
             bg="#e6f2ff", fg="#003366").grid(row=1, column=0, pady=10, padx=10)
    username_entry = tk.Entry(login_frame, font=("Helvetica", 18))
    username_entry.grid(row=1, column=1, pady=10, padx=10)

    # Password
    tk.Label(login_frame, text="Password", font=("Helvetica", 18),
             bg="#e6f2ff", fg="#003366").grid(row=2, column=0, pady=10, padx=10)
    password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 18))
    password_entry.grid(row=2, column=1, pady=10, padx=10)

    # Login function
    def check_login():
        user = username_entry.get()
        pwd = password_entry.get()

        conn = connect_db()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM Users WHERE User_Name=%s AND Password=%s", (user, pwd))
        row = cur.fetchone()
        conn.close()

        if row:
            messagebox.showinfo("Success", "Login Successful")
            win.destroy()
            booking_page(row["ID"])
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    # Login button
    login_btn = tk.Button(login_frame, text="Login",
                          font=("Helvetica", 18, "bold"),
                          bg="#28a745", fg="white", width=15,
                          command=check_login)
    login_btn.grid(row=3, column=0, columnspan=2, pady=20)

    win.mainloop()

# ---------- Booking Page ----------
def booking_page(user_id):
    win = tk.Tk()
    win.title("Smart Parking - Booking")
    win.state("zoomed")

    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()

    # Light Blue Gradient
    canvas = tk.Canvas(win, width=width, height=height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    draw_gradient(canvas, "#87CEFA", "#E6F2FF", width, height)

    # Title
    canvas.create_text(width//2, 80, text="SMART PARKING SYSTEM",
                       font=("Helvetica", 34, "bold"), fill="#003366")

    # Main frame
    main_frame = tk.Frame(canvas, bg="#e6f2ff")
    canvas.create_window(width//2, height//2, window=main_frame, anchor="center")

    left_frame = tk.Frame(main_frame, bg="#e6f2ff", padx=30, pady=20)
    left_frame.grid(row=0, column=0, sticky="n")

    right_frame = tk.Frame(main_frame, bg="#e6f2ff", padx=30, pady=20)
    right_frame.grid(row=0, column=1, sticky="n")

    # Area selector
    tk.Label(left_frame, text="Select Parking Area",
             font=("Helvetica", 18, "bold"), bg="#e6f2ff", fg="#003366").pack(pady=10)

    conn = connect_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Areas")
    areas = cur.fetchall()
    conn.close()

    area_var = tk.StringVar()
    area_dropdown = ttk.Combobox(left_frame, textvariable=area_var,
                                 font=("Helvetica", 14),
                                 values=[a["Area_Name"] for a in areas],
                                 state="readonly")
    area_dropdown.pack(pady=10)
    area_dropdown.current(0)

    # Vehicle selector
    tk.Label(left_frame, text="Select Vehicle Type",
             font=("Helvetica", 18, "bold"), bg="#e6f2ff", fg="#003366").pack(pady=10)

    vehicle_var = tk.StringVar()
    vehicle_dropdown = ttk.Combobox(left_frame, textvariable=vehicle_var,
                                    font=("Helvetica", 14),
                                    values=["Car", "Bike", "EV", "Auto", "Cycle"],
                                    state="readonly")
    vehicle_dropdown.pack(pady=10)
    vehicle_dropdown.current(0)

    # Slots frame
    slots_frame = tk.Frame(right_frame, bg="#e6f2ff")
    slots_frame.pack()

    def on_hover(e): e.widget.config(bg="#00cc66")
    def on_leave(e, c): e.widget.config(bg=c)

    def load_slots():
        for widget in slots_frame.winfo_children():
            widget.destroy()

        selected_area = area_var.get()
        selected_vehicle = vehicle_var.get()

        conn = connect_db()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT ID FROM Areas WHERE Area_Name=%s", (selected_area,))
        area_id = cur.fetchone()["ID"]

        cur.execute("SELECT * FROM Slots WHERE Area_ID=%s AND Vehicle_Type=%s",
                    (area_id, selected_vehicle))
        slots = cur.fetchall()
        conn.close()

        tk.Label(slots_frame, text=f"Slots in {selected_area} ({selected_vehicle})",
                 font=("Helvetica", 18, "bold"), bg="#e6f2ff", fg="#003366").grid(row=0, column=0, columnspan=3, pady=10)

        row, col = 1, 0
        for slot in slots:
            color = "#28A745" if slot["Status"] == "Available" else "#DC3545"
            state = tk.NORMAL if slot["Status"] == "Available" else tk.DISABLED

            btn = tk.Button(slots_frame,
                            text=f"{slot['Slot_Number']}\n{slot['Status']}",
                            font=("Helvetica", 12, "bold"),
                            bg=color, fg="white", width=12, height=4,
                            relief="flat", state=state,
                            command=lambda s=slot, a=selected_area: booking_details_page(s, user_id, a))
            btn.grid(row=row, column=col, padx=12, pady=12)

            if state == tk.NORMAL:
                btn.bind("<Enter>", on_hover)
                btn.bind("<Leave>", lambda e, c=color: on_leave(e, c))

            col += 1
            if col > 2:
                col = 0
                row += 1

        win.after(5000, load_slots)

    tk.Button(left_frame, text="Show Slots",
              font=("Helvetica", 14, "bold"),
              bg="#0066ff", fg="white", width=15, height=2,
              relief="flat", command=load_slots).pack(pady=20)

    win.mainloop()

# ---------- Booking Details with Popup ----------
def booking_details_page(slot, user_id, area_name):
    popup = tk.Toplevel()
    popup.title("Confirm Booking")
    popup.geometry("400x300")
    popup.configure(bg="#e6f2ff")

    tk.Label(popup, text="Enter Your Details", font=("Helvetica", 18, "bold"),
             bg="#e6f2ff", fg="#003366").pack(pady=10)

    tk.Label(popup, text="Username", font=("Helvetica", 14),
             bg="#e6f2ff").pack(pady=5)
    name_entry = tk.Entry(popup, font=("Helvetica", 14))
    name_entry.pack(pady=5)

    tk.Label(popup, text="Phone Number", font=("Helvetica", 14),
             bg="#e6f2ff").pack(pady=5)
    phone_entry = tk.Entry(popup, font=("Helvetica", 14))
    phone_entry.pack(pady=5)

    def confirm_booking():
        username = name_entry.get()
        phone = phone_entry.get()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        popup.destroy()
        messagebox.showinfo("Booking Confirmed",
                            f"Name: {username}\n"
                            f"Phone: {phone}\n"
                            f"Area: {area_name}\n"
                            f"Slot No: {slot['Slot_Number']}\n"
                            f"Token: {slot['ID']}\n"
                            f"Date & Time: {now}")

    tk.Button(popup, text="Book Slot", font=("Helvetica", 14, "bold"),
              bg="#28a745", fg="white", width=15,
              command=confirm_booking).pack(pady=20)

# ---------- Run ----------
if __name__ == "__main__":
    start_page()
