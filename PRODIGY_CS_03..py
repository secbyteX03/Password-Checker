import tkinter as tk
from tkinter import messagebox
import re
import math

# Function to check if password is weak based on a known list of weak passwords
def is_common_password(password):
    common_passwords = [
        "password", "1234", "qwerty", "abc123", "password1", "letmein", "welcome",
        "12345", "123456", "monkey", "qwertyuiop", "123321", "admin", "123123",
        "iloveyou", "1q2w3e4r", "sunshine", "princess", "123qwe", "qwerty123",
        "password123", "trustno1", "dragon", "123", "football", "123abc"
    ]
    return password.lower() in common_passwords

# Function to check for sequential or simple patterns
def has_sequential_pattern(password):
    patterns = [
        r"1234", r"abcd", r"qwerty", r"asdf", r"zxcvbnm",
        r"0123456789", r"9876543210", r"qwertyuiop", r"asdfghjkl", r"qwerty123",
        r"1111", r"2222", r"3333", r"abcd1234", r"123abc", r"password1", r"qwerty12"
    ]
    for pattern in patterns:
        if re.search(pattern, password.lower()):
            return True
    return False

# Function to calculate entropy
def calculate_entropy(password):
    lowercase = 26
    uppercase = 26
    digits = 10
    special_chars = 32
    character_set_size = 0
    if any(char.islower() for char in password):
        character_set_size += lowercase
    if any(char.isupper() for char in password):
        character_set_size += uppercase
    if any(char.isdigit() for char in password):
        character_set_size += digits
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        character_set_size += special_chars
    if character_set_size > 0:
        entropy = math.log2(character_set_size ** len(password))
        return entropy
    return 0

# Function to calculate cracking time
def calculate_crack_time(password, guesses_per_second=1_000_000_000):
    character_set_size = 94
    possible_combinations = character_set_size ** len(password)
    time_seconds = possible_combinations / guesses_per_second
    if time_seconds < 60:
        return f"{time_seconds:.2f} seconds"
    elif time_seconds < 3600:
        return f"{time_seconds / 60:.2f} minutes"
    elif time_seconds < 86400:
        return f"{time_seconds / 3600:.2f} hours"
    elif time_seconds < 31536000:
        return f"{time_seconds / 86400:.2f} days"
    else:
        return f"{time_seconds / 31536000:.2f} years"

# Function to check password strength
def check_password_strength(password):
    feedback = []
    strength = "Strong"
    if is_common_password(password):
        feedback.append("Password is too common and easily guessable.")
        strength = "Weak"
    if has_sequential_pattern(password):
        feedback.append("Password contains a simple sequential pattern.")
        strength = "Weak"
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")
        strength = "Weak"
    if not any(char.isupper() for char in password):
        feedback.append("Password must contain at least one uppercase letter.")
        strength = "Weak"
    if not any(char.islower() for char in password):
        feedback.append("Password must contain at least one lowercase letter.")
        strength = "Weak"
    if not any(char.isdigit() for char in password):
        feedback.append("Password must contain at least one number.")
        strength = "Weak"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Password must contain at least one special character.")
        strength = "Weak"
    entropy = calculate_entropy(password)
    feedback.append(f"Password entropy: {entropy:.2f}")
    if entropy < 40:
        feedback.append("Password entropy is too low.")
        strength = "Weak"
    cracking_time = calculate_crack_time(password)
    return feedback, strength, cracking_time

# GUI Implementation
def evaluate_password():
    password = entry.get()
    feedback, strength, cracking_time = check_password_strength(password)
    feedback_text = "\n".join(feedback)
    result_label.config(text=f"Feedback:\n{feedback_text}\n\nStrength: {strength}\nCracking Time: {cracking_time}")

def toggle_password_visibility():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_btn.config(text="Hide Password")
    else:
        entry.config(show='*')
        toggle_btn.config(text="Show Password")

def copy_to_clipboard():
    password = entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main Application
root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=40)
entry.pack(pady=5)

toggle_btn = tk.Button(root, text="Show Password", command=toggle_password_visibility)
toggle_btn.pack(pady=5)

tk.Button(root, text="Check Strength", command=evaluate_password).pack(pady=5)
tk.Button(root, text="Copy Password", command=copy_to_clipboard).pack(pady=5)

result_label = tk.Label(root, text="", justify="left", wraplength=400)
result_label.pack(pady=10)

root.geometry("500x400")
root.mainloop()
