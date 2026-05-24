import re
import random
import string

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letters.")

    # Numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add numbers.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add special characters.")

    return strength, remarks

def suggest_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

password = input("Enter your password: ")

strength, remarks = check_password_strength(password)

print("\nPassword Strength Score:", strength, "/ 5")

if strength == 5:
    print("Strong Password ✅")
elif strength >= 3:
    print("Medium Password ⚠️")
else:
    print("Weak Password ❌")

if remarks:
    print("\nSuggestions:")
    for remark in remarks:
        print("-", remark)

print("\nSuggested Strong Password:", suggest_password())
