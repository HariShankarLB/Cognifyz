# Task 3: Password Strength Checker - Create a Python function that evaluates the strength of a password entered by the user. Implement checks for factors such as length, presence of uppercase and lowercase letters, digits, and special characters.

import re

strenght = 0

word=input("enter the password to check strenght: ")

criteria = {
            "lenght":len(word)>=8,
            "Uppercase": bool(re.search(r"[A-Z]",word)),
            "Lowercase": bool(re.search(r"[a-z]",word)),
            "Digits": bool(re.search(r"[0-9]",word)),
            "Special Characters": bool(re.search(r"[!@#$%^&*(){}]",word)),
            }

strenght = sum(criteria.values())

if strenght==5:
    x="Very Strong"
elif strenght==4:
    x="Strong"
elif strenght==3:
    x="Moderate"
else:
    x="Weak"

print(f"The strength of password is {x}")