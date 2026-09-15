import csv
import hashlib
import json
import os
import sys
from datetime import datetime
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
from shared.student import  VARIANT_NUMBER

sys.path.append(PROJECT_ROOT)


def main():
    print()
    print("*Завдання 3*\n")

    class ValidationError(Exception):
        """Виняток для паролів, що не відповідають мінімальній довжині."""

        pass

    MIN_LENGTH = 13

    SALT = str(VARIANT_NUMBER).zfill(5)

    DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(DATA_DIR, exist_ok=True)

    USERS_CSV_PATH = os.path.join(DATA_DIR, "users.csv")
    LOG_JSON_PATH = os.path.join(DATA_DIR, "log.json")

    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    def generate_hash(password: str, salt: str = SALT) -> str:
        if not password or not salt:
            raise ValueError("Пароль або сіль не можуть бути порожніми.")
        if len(password) < MIN_LENGTH:
            raise ValidationError(
                f"Пароль занадто короткий ({len(password)} с.). Мін. довжина: {MIN_LENGTH}"
            )

        # Хешування конкатенації пароля та солі
        salted_password = (password + salt).encode("utf-8")
        return hashlib.sha224(salted_password).hexdigest()

    # 3. Реєстрація користувачів
    def create_user(username: str, password: str):
        if not username or not password:
            raise ValueError("Ім'я користувача або пароль порожні.")
        hash_value = generate_hash(password, SALT)
        return (username, hash_value)

    def create_users(users_list):
        try:
            with open(USERS_CSV_PATH, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["login", "password_hash"])
                for username, password in users_list:
                    try:
                        user_data = create_user(username, password)
                        writer.writerow(user_data)
                    except (ValueError, ValidationError) as e:
                        print(f"{RED}[ERROR] Не вдалося створити користувача {username}: {e}{RESET}")
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(f"{RED}[ERROR] Помилка запису файлу бази даних: {e}{RESET}\n")

    def log_event(func):
        def wrapper(username, password, *args, **kwargs):
            try:
                result = func(username, password, *args, **kwargs)
            except Exception as e:
                result = False
                raise e
            finally:
                log_entry = {
                    "event": "login",
                    "user": username,
                    "result": "success" if result else "failure",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "args": [username, password],
                    "kwargs": kwargs,
                }
                try:
                    with open(LOG_JSON_PATH, "a", encoding="utf-8") as log_file:
                        json.dump(log_entry, log_file, ensure_ascii=False)
                        log_file.write("\n")
                except (FileNotFoundError, PermissionError, IOError) as e:
                    print(f"{RED}[ERROR] Помилка запису логу: {e}{RESET}")

            return result

        return wrapper

    @log_event
    def login(username: str, password: str) -> bool:
        if not username or not password:
            raise ValueError("Логін чи пароль не можуть бути порожніми.")

        try:
            user_hash = generate_hash(password, SALT)
        except (ValidationError, ValueError):
            return False

        for user in users_db:
            if user.get("login") == username and user.get("password_hash") == user_hash:
                return True

        return False

    users_to_register = (
        ("student", "1234567890123"),
        ("user", "jungle879_pass_long"),
        ("kraken", "sonta867"),
        ("ford3398", "palin1098_secret"),
        ("justin0987", "horse9845_secure"),
        ("iman35", "ironman000_hero"),
        ("oleg", "olegthebest7_pass"),
        ("operator", "N1cE_operator_key"),
        ("COMANDER", "fork867_commander"),
        ("ill1as", ""),
    )

    print()

    create_users(users_to_register)

    print()

    users_db = []
    try:
        with open(USERS_CSV_PATH, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            users_db = [row for row in reader]

        print(f"{'Логін':<15} | {'Хеш пароля (SHA-224 + Salt)'}")
        print("-" * 70)
        for row in users_db:
            print(f"{row['login']:<15} | {row['password_hash']}")
    except (FileNotFoundError, PermissionError, IOError) as e:
        print(f"[ERROR] Не вдалося прочитати CSV: {e}")

    test_credentials = list(users_to_register) 

    print()

    for u, p in test_credentials:
        try:
            status = login(u, p)
            res = f"{GREEN}success{RESET}" if status else f"{RED}failure{RESET}"
            print(f"Авторизація [{u}]: {res}\n")
        except (ValueError, ValidationError) as e:
            print(f"[!] Помилка для [{u}]: {e}")


if __name__ == "__main__":
    main()
