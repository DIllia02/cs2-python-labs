import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from shared.student import STUDENT_NAME, GROUP_NAME, VARIANT_NUMBER

def main():
    print(f"Студент: {STUDENT_NAME} | Група: {GROUP_NAME} | Варіант: {VARIANT_NUMBER}\n")

    print("*Завдання 1*")

    passwords = [
        "Digital@F0r3nsics",
        "plain",
        "Encrypt10n@Key",
        "member",
        "Security@Audit2023",
        "regular",
        "Hack3r@D3fense",
        "ordinary",
        "Threat@Intel",
        "usual",
    ]

    criteria = {
        "min_length": 8,
        "require_digits": True,
        "require_upper": True,
        "require_special": True,
    }

    forbidden_passwords = {"plain", "member", "regular", "ordinary", "usual", "user"}

    random_passwords = random.sample(passwords, 3)
    all_passwords = random_passwords + passwords

    for password in all_passwords:
        passed_checks = [
            len(password) >= criteria["min_length"],
            (
                any(char.isdigit() for char in password)
                if criteria["require_digits"]
                else True
            ),
            (
                any(char.isupper() for char in password)
                if criteria["require_upper"]
                else True
            ),
            (
                any(char in "!@#$%^&*()_+-=[]{}|;:,.<>/?`~" for char in password)
                if criteria["require_special"]
                else True
            ),
        ]

        total_passed = sum(passed_checks)
        total_criteria = len(passed_checks)

        if password in forbidden_passwords or len(password) < criteria["min_length"]:
            print(
                f'[!] Пароль "{password}" не відповідає вимогам (заборонений або закороткий)'
            )
        elif total_passed == 1:
            print(f'[-] Пароль "{password}" слабкий')
        elif 1 < total_passed < total_criteria:
            print(f'[~] Пароль "{password}" сильний ')
        elif all(passed_checks):
            print(f'[+] Пароль "{password}" дуже сильний ')

    print()

if __name__ == "__main__":
    main()
    