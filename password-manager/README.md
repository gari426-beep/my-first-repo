# Password Manager

## Description
A simple Python-based Password Manager that allows users to save and view passwords. This project demonstrates file handling, functions, loops, and user input in Python.

## Features
- Save website credentials
- View saved passwords
- Menu-driven interface
- Stores data in a text file

## Technologies Used
- Python 3

## Project Structure

```
password-manager/
│── password_manager.py
│── passwords.txt
└── README.md
```

## How to Run

1. Open the project folder.
2. Run the program:

```bash
py password_manager.py
```

3. Choose an option from the menu:
   - 1 → Save Password
   - 2 → View Passwords
   - 3 → Exit

## Example

```
=== Password Manager ===

1. Save Password
2. View Passwords
3. Exit

Enter your choice: 1

Enter website: gmail.com
Enter username: demo@gmail.com
Enter password: Password123

Password saved successfully!
```

## Learning Outcomes
- Functions
- File Handling
- Loops
- Conditional Statements
- User Input
- Basic Password Management

## Note
This project is for educational purposes only. Passwords are stored in plain text inside `passwords.txt`, which is **not secure** for real-world use. A production password manager should encrypt stored passwords and protect them with a master password.

## Author

Gauri