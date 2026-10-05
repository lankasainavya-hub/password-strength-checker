import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Add at least one number.")

    # Special character check
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character (@$!%*?&).")

    # Strength rating
    if strength == 5:
        return "Very Strong Password ✅"
    elif strength == 4:
        return "Strong Password 👍"
    elif strength == 3:
        return "Moderate Password ⚠️"
    else:
        return "Weak Password ❌\n" + "\n".join(remarks)

# User Input
password = input("Enter your password: ")
result = check_password_strength(password)
print("\nPassword Strength:", result)
