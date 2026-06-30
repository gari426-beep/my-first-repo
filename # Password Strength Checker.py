# Password Strength Checker

password = input("Enter your password:")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters ="!@#$%^&*()<>?/:;'{}[]|\_-+="

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True
print("\nPassword Check Results:")

if len(password) < 8:
    print("- Password should be at least 8 characters long")
if not has_upper:
    print("- Password should contain at least one uppercase letter")
if not has_lower:
    print("- Password should contain at least one lowercase letter")
if not has_digit:
    print("- Password should contain at least one digit")
if not has_special:
    print("- Password should contain at least one special character")
if (len(password) >=8 and has_upper and has_lower and has_digit and has_special):
    print("✅ Your password is strong.")
else:
    print("❌ Your password is weak. Please consider improving it.")