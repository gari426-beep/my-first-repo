import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "passwords.txt")


def save_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(FILE_PATH, "a") as file:
        file.write(f"{website} | {username} | {password}\n")

    print("\nPassword saved successfully!")


def view_passwords():
    try:
        with open(FILE_PATH, "r") as file:
            print("\nSaved Passwords:")
            print("-" * 40)
            print(file.read())
    except FileNotFoundError:
        print("No passwords found.")


while True:
    print("\n=== Password Manager ===")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        save_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")