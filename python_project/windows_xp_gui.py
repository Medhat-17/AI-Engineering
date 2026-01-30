import tkinter as tk
from tkinter import ttk
import time
import winsound  
root = tk.Tk()
root.title("Windows XP Boot")
root.geometry("600x400")
root.configure(bg="#1A1A1A")  # Dark XP-style background
root.resizable(False, False)

# ---------------- XP Logo ---------------- #
# Replace with your image if you want later
logo_label = tk.Label(root, text="Windows XP", font=("Arial", 24, "bold"), fg="white", bg="#1A1A1A")
logo_label.pack(pady=80)

# ---------------- Progress Bar ---------------- #
style = ttk.Style()
style.theme_use('clam')
style.configure("TProgressbar", thickness=20, troughcolor="#333", background="#4CAF50")

progress = ttk.Progressbar(root, style="TProgressbar", orient="horizontal", length=400, mode="determinate")
progress.pack(pady=50)

# ---------------- Status Label ---------------- #
status = tk.Label(root, text="Starting Windows XP...", font=("Arial", 12), fg="white", bg="#1A1A1A")
status.pack()

# ---------------- XP Sound ---------------- #
def play_xp_sound():
    try:
        # Replace with the path to your XP startup sound if you have it
        winsound.PlaySound("C:\\Windows\\Media\\Windows XP Startup.wav", winsound.SND_FILENAME)
    except:
        print("Sound file not found or unsupported.")

# ---------------- Progress Simulation ---------------- #
def load():
    play_xp_sound()  # Play sound at the start
    for i in range(101):
        progress['value'] = i
        if i < 30:
            status.config(text="Checking hardware...")
        elif i < 60:
            status.config(text="Loading drivers...")
        elif i < 90:
            status.config(text="Starting services...")
        else:
            status.config(text="Almost done...")
        root.update()
        time.sleep(0.05)  # Speed of loading

    status.config(text="Welcome!")
    logo_label.config(text="Windows XP Ready")
    root.update()
    time.sleep(1)

load()
root.mainloop()
