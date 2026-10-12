# 🧑‍💻 Interactive Personal Detail Collector

A simple Python project that collects personal details from the user and displays the information along with its data types. It also calculates the user's approximate birth year using their age and the current year.

## 📌 Project Overview

The **Interactive Personal Detail Collector** is a beginner-friendly Python program designed to practice basic programming concepts such as user input, variables, data types, type conversion, and formatted output.

## ✨ Features

- 👤 Collects the user's name
- 🎂 Collects the user's age
- 📏 Collects the user's height in centimeters
- 🔢 Collects the user's favorite number
- 📅 Calculates the approximate birth year
- 🧠 Displays the data type of each collected value
- 💬 Displays a personalized welcome and goodbye message

## 🛠️ Technologies Used

- **Python 3**
- Python `input()` function
- Variables and data types
- Type conversion using `int()`
- Formatted strings (f-strings)
- `print()` function

## 💻 Source Code

```python
print("Welcome to the interactive personal detail collector!")

name = input("Please enter your name: ")
age = input("Please enter your age: ")
height = input("Please enter your height in cm: ")
favorite_number = input("Please enter your favorite number: ")

current_year = 2026

birth_year = current_year - int(age)

print("Thank you! Here is the information we collected:")

print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Favorite number: {favorite_number} (Type: {type(favorite_number)})")

print(f"Birth year: {birth_year}")

print("Thank you for using Personal Data Collector. Goodbye!")
```

## ▶️ How to Run the Project

1. Install Python 3 on your computer.
2. Create a file named `main.py`.
3. Copy the Python source code into `main.py`.
4. Open a terminal in the project folder.
5. Run the following command:

```bash
python main.py
```

## 📷 Example Output

```text
Welcome to the interactive personal detail collector!
Please enter your name: Jay
Please enter your age: 20
Please enter your height in cm: 175
Please enter your favorite number: 7

Thank you! Here is the information we collected:
Name: Jay (Type: <class 'str'>)
Age: 20 (Type: <class 'str'>)
Height: 175 (Type: <class 'str'>)
Favorite number: 7 (Type: <class 'str'>)
Birth year: 2006

Thank you for using Personal Data Collector. Goodbye!
```

## 📚 What I Learned

- How to collect user input using `input()`.
- How to store information in variables.
- How to check data types using `type()`.
- How to convert a string to an integer using `int()`.
- How to perform basic mathematical calculations.
- How to display information using f-strings.

## 🚀 Future Improvements

- Add input validation for age and height.
- Calculate birth year more accurately using the user's birthday.
- Convert age and height into numeric data types.
- Add an option to collect information from multiple users.

## 👨‍💻 Author

Created as a beginner Python programming project.

---

⭐ If you like this project, consider giving the repository a star!

**Thank you for visiting my project!**
