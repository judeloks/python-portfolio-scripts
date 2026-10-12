import string
import secrets


def generate_password(length=12):
    # Набор символов для генерации
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Генерация надежного пароля с помощью модуля secrets
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return password


def main():
    print("--- Генератор надежных паролей ---")

    try:
        length_input = input("Введите длину пароля (по умолчанию 12): ").strip()
        length = int(length_input) if length_input else 12

        if length < 4:
            print("Пароль слишком короткий! Рекомендуемая длина — от 8 символов.")
            return

        password = generate_password(length)
        print(f"\nСгенерированный пароль: {password}")

        save = input("Сохранить пароль в файл 'password.txt'? (y/n): ").strip().lower()
        if save == "y":
            with open("password.txt", "w", encoding="utf-8") as f:
                f.write(password)
            print("Пароль успешно сохранен в файл 'password.txt'!")

    except ValueError:
        print("Пожалуйста, введите корректное число!")


if __name__ == "__main__":
    main()
