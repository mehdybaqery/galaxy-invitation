"""
Galaxy Date Invitation App
A fun interactive dating invitation with cosmic theme
Author: MehdyBaqery
Date: 2025-09-28
Version: 1.0
GitHub: https://github.com/MehdyBaqery
"""

import tkinter as tk
import random
import os
import sys
from datetime import datetime

# Configuration
CORRECT_CODE = "xxxx"  # Change this to your desired code
PHONE_NUMBER = "xxxxxxxxxxx"  # Change this to your phone number

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Functions
def show_code_section():
    """
    Show code entry section and hide main buttons
    """
    yes_btn.place_forget()
    no_btn.place_forget()
    signature_label.place_forget()  # Hide signature when entering code
    code_frame.place(x=CODE_FRAME_X, y=CODE_FRAME_Y, anchor="center")
    message_label.config(text="", bg=CARD_BG)
    code_entry.focus_set()

    # Show Back button in code entry section
    back_btn.place(x=160, y=320, width=100, height=30)

def verify_code():
    """
    Verify the entered code and show appropriate message
    """
    code = code_entry.get().strip()
    if code == CORRECT_CODE:
        code_frame.place_forget()
        back_btn.place_forget()  # Hide Back button on success
        signature_label.place_forget()  # Hide signature on success
        message_label.config(text=f"❤️ Nice shot! Call me: {PHONE_NUMBER}",
                             bg=SUCCESS, fg=TEXT_COLOR)
    else:
        message_label.config(text="❌ Please enter the correct verification code",
                             bg=ERROR, fg=TEXT_COLOR)
        shake_effect()
        code_entry.delete(0, tk.END)
        code_entry.focus_set()

def shake_effect():
    """
    Create shake animation for wrong code entry
    """
    original_x = CODE_FRAME_X
    original_y = CODE_FRAME_Y

    movements = [
        (original_x + 8, original_y),
        (original_x - 8, original_y),
        (original_x + 6, original_y),
        (original_x - 6, original_y),
        (original_x + 4, original_y),
        (original_x - 4, original_y),
        (original_x + 2, original_y),
        (original_x - 2, original_y)
    ]

    for x, y in movements:
        code_frame.place(x=x, y=y, anchor="center")
        root.update()
        root.after(40)

    code_frame.place(x=original_x, y=original_y, anchor="center")

def reset_app():
    """
    Reset application to initial state
    """
    code_frame.place_forget()
    back_btn.place_forget()  # Hide Back button in main screen
    message_label.config(text="", bg=CARD_BG)
    yes_btn.place(x=80, y=150, width=button_w, height=button_h)
    no_btn.place(x=230, y=150, width=button_w, height=button_h)
    signature_label.place(relx=0.5, rely=0.85, anchor="center")  # Show signature again

def escape_no(event):
    """
    Move No button randomly when hovered (escape effect)
    """
    c_w, c_h = 420, 520
    new_x = random.randint(20, c_w - button_w - 20)
    new_y = random.randint(100, c_h - button_h - 20)
    no_btn.place(x=new_x, y=new_y, width=button_w, height=button_h)

def on_enter_key(event):
    """
    Handle Enter key press for code verification
    """
    verify_code()

def show_about():
    """
    Show about information
    """
    about_text = f"""🚀 Galaxy Date Invitation

✨ Created by: Mehdy Baqery
📅 Version: 1.0
🎯 Date: {datetime.now().strftime('%Y-%m-%d')}
🌌 Made with cosmic energy

A fun interactive dating invitation
with a touch of magic!"""

    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("300x250")
    about_window.configure(bg=CARD_BG)
    about_window.resizable(False, False)

    # Center the about window
    about_window.transient(root)
    about_window.grab_set()

    tk.Label(about_window, text="About", font=("Arial", 16, "bold"),
             bg=CARD_BG, fg=PRIMARY).pack(pady=10)

    tk.Label(about_window, text=about_text, font=("Arial", 10),
             bg=CARD_BG, fg=TEXT_COLOR, justify="center").pack(pady=10)

    tk.Button(about_window, text="Close", bg=PRIMARY, fg="white",
              font=("Arial", 10, "bold"), command=about_window.destroy).pack(pady=10)

# Initialize main window
root = tk.Tk()
root.title("Galaxy Date Invitation 🌌")

# Set application icon
try:
    icon_path = resource_path("galaxy_icon.ico")
    root.iconbitmap(icon_path)
except:
    pass  # Continue without icon if not found

root.geometry("500x600")
root.configure(bg="#0f0c29")
root.resizable(False, False)

# Color scheme
CARD_BG = "#1a1f29"
TEXT_COLOR = "#f8f9fa"
PRIMARY = "#8a2be2"
SUCCESS = "#4caf50"
ERROR = "#f44336"
ACCENT = "#ff6b6b"

# Main card container
card = tk.Frame(root, bg=CARD_BG, bd=0, relief="flat")
card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=520)

# Title section
title = tk.Label(card, text="🌌 Galaxy Date Invitation", font=("Arial", 20, "bold"),
                 bg=CARD_BG, fg=PRIMARY)
title.pack(pady=20)

question = tk.Label(card, text="Would you like to go on a galaxy date with me?",
                    font=("Arial", 14, "bold"), bg=CARD_BG, fg=TEXT_COLOR, wraplength=380)
question.pack(pady=10)

# Main buttons
button_w, button_h = 100, 40
yes_btn = tk.Button(card, text="✅ Yes", bg=SUCCESS, fg="white",
                    font=("Arial", 12, "bold"), relief="flat", cursor="hand2")
no_btn = tk.Button(card, text="❌ No", bg=ERROR, fg="white",
                   font=("Arial", 12, "bold"), relief="flat", cursor="hand2")

# Position main buttons
yes_btn.place(x=80, y=150, width=button_w, height=button_h)
no_btn.place(x=230, y=150, width=button_w, height=button_h)

# Back button (initially hidden, shown only in code entry section)
back_btn = tk.Button(card, text="🔙 Back", bg="#666", fg="white",
                     font=("Arial", 10, "bold"), command=reset_app, cursor="hand2")

# Code entry section
code_frame = tk.Frame(card, bg=CARD_BG)
code_title = tk.Label(code_frame, text="Enter the galaxy code 🌠",
                      font=("Arial", 12, "bold"), bg=CARD_BG, fg=TEXT_COLOR)
code_title.pack(pady=(10, 5))

# Code entry field
code_entry = tk.Entry(code_frame,
                      font=("Arial", 14),
                      justify="center",
                      bg="#2a2f39",
                      fg=TEXT_COLOR,
                      insertbackground=TEXT_COLOR,
                      relief="flat",
                      bd=2,
                      highlightbackground=PRIMARY,
                      highlightcolor=PRIMARY,
                      highlightthickness=1)
code_entry.pack(pady=5, ipady=5)

# Verify button
verify_btn = tk.Button(code_frame, text="🔒 Verify Code",
                       bg=PRIMARY, fg="white", font=("Arial", 12, "bold"), cursor="hand2")
verify_btn.pack(pady=10, fill="x")

# Message display area
message_frame = tk.Frame(card, bg=CARD_BG)
message_frame.place(relx=0.5, rely=0.75, anchor="center", width=400, height=50)

message_label = tk.Label(message_frame, text="", font=("Arial", 12, "bold"),
                         padx=10, pady=5, wraplength=380)
message_label.pack(fill="both", expand=True)

# Developer signature (elegant and professional)
signature_label = tk.Label(card,
                          text="✨ Crafted with ❤️ by MehdyBaqery ✨",
                          font=("Arial", 9, "italic"),
                          bg=CARD_BG,
                          fg=ACCENT,
                          cursor="hand2")
signature_label.place(relx=0.5, rely=0.85, anchor="center")

# Make signature clickable for about info
signature_label.bind("<Button-1>", lambda e: show_about())

# Fixed positions
CODE_FRAME_X = 210  # 420 / 2 = 210 (half of card width)
CODE_FRAME_Y = 208  # 520 * 0.4 = 208 (40% of card height)

# Configure button commands
yes_btn.config(command=show_code_section)
verify_btn.config(command=verify_code)

# Bind events
no_btn.bind("<Enter>", escape_no)
code_entry.bind("<Return>", on_enter_key)

# Footer
footer = tk.Label(card, text="Made with ❤️ across the galaxy • 2025",
                  font=("Arial", 8), bg=CARD_BG, fg="#666")
footer.place(relx=0.5, rely=0.95, anchor="center")

# Info button (top right) - با رنگ زمینه کارت
info_btn = tk.Button(card, text="ℹ️", bg=CARD_BG, fg=PRIMARY,
                    font=("Arial", 10, "bold"), command=show_about,
                    relief="flat", bd=0, cursor="hand2")
info_btn.place(x=390, y=10, width=20, height=20)

# Hide code frame and back button initially
code_frame.place_forget()
back_btn.place_forget()

# Start application
root.mainloop()