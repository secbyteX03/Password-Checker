# 🔐 Password Strength Checker  
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Contributions-Welcome-orange" alt="Contributions">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
</p>

A **Python-based GUI application** that evaluates password strength by checking against common vulnerabilities, patterns, and calculating entropy and estimated cracking time.  

---

## ✨ Features
- **Common Password Detection:** Checks against a list of known weak passwords  
- **Pattern Recognition:** Identifies sequential and simple keyboard patterns  
- **Entropy Calculation:** Measures password complexity in bits  
- **Cracking Time Estimation:** Provides realistic time estimates for brute-force attacks  
- **Interactive GUI:** User-friendly interface with visual feedback  
- **Copy to Clipboard:** Convenient password copying functionality  
- **Password Visibility Toggle:** Option to show/hide the entered password  

---

## 📦 Requirements
- Python **3.x**  
- Tkinter (usually included with the Python standard library)  

---

## ⚙️ Installation
1. Clone or download the repository  
2. Ensure Python 3 is installed on your system  
3. No additional dependencies are required  

---

## 🚀 Usage
Run the script:

```bash
python password_strength_checker.py
````

1. Enter a password in the text field
2. Click **"Check Strength"** to evaluate your password
3. View feedback, strength rating, and estimated cracking time
4. Use **"Show Password"** to reveal your entry or **"Copy Password"** to copy it to the clipboard

---

## 🧩 Password Evaluation Criteria

The tool checks for the following:

* Minimum **8 characters** in length
* At least **one uppercase letter**
* At least **one lowercase letter**
* At least **one digit**
* At least **one special character** (`!@#$%^&*(),.?":{}|<>`)
* Not in the list of **common passwords**
* No sequential or simple patterns (e.g., `1234`, `qwerty`)
* Minimum entropy of **40 bits**

---

## ⚙️ Technical Details

### 🔢 Entropy Calculation

Entropy is calculated as:

```
Entropy = log2(CharacterSetSize ^ PasswordLength)
```

Where the character set size depends on included character types:

* Lowercase letters: 26
* Uppercase letters: 26
* Digits: 10
* Special characters: 32

---

### ⏳ Cracking Time Estimation

* Assumes attack speed of **1,000,000,000 guesses/sec**
* Full **94-character keyboard set** used for calculation
* Time displayed in **seconds → years** depending on scale

---

## 🖥️ Example Output

### ✅ Strong Password

```
Feedback:
Password entropy: 95.60
Strength: Strong
Cracking Time: 1.95e+27 years
```

### ❌ Weak Password

```
Feedback:
Password is too common and easily guessable.
Password contains a simple sequential pattern.
Password must contain at least one uppercase letter.
Password must contain at least one special character.
Password entropy: 11.30
Password entropy is too low.
Strength: Weak
Cracking Time: 0.00 seconds
```

---

## ⚠️ Limitations

* Common password list is **not exhaustive**
* Pattern recognition uses a **predefined set** of patterns
* Cracking time estimates are **theoretical** and based on fixed assumptions
* Entropy calculation assumes **optimal character distribution**

---

## 🔒 Security Notes

* Runs **locally** on your machine
* No passwords are transmitted over the network
* Common password list is embedded in the application
* For highly sensitive applications, consider **additional security measures**

---

## 🤝 Contributing

Contributions are welcome! You can help by:

* Expanding the common passwords list
* Adding more pattern recognition rules
* Improving the GUI interface
* Enhancing the entropy calculation algorithm

---

## 📄 License

This project is open-source and available under the **MIT License**.
---
