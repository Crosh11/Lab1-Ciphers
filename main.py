UKR = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
ENG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar(text, key, decrypt=False):
    if decrypt:
        key = -key

    result = ""

    for char in text:
        upper = char.upper()

        if upper in UKR:
            alphabet = UKR
        elif upper in ENG:
            alphabet = ENG
        else:
            result += char
            continue

        index = alphabet.index(upper)
        new_index = (index + key) % len(alphabet)
        new_char = alphabet[new_index]

        if char.islower():
            new_char = new_char.lower()

        result += new_char

    return result


def get_order(key):
    # Нумеруємо стовпці за алфавітним порядком ключа
    return sorted(
        range(len(key)),
        key=lambda i: (key[i].upper(), i)
    )


def permutation_encrypt(text, key):
    columns = len(key)
    order = get_order(key)

    table = [
        text[i:i + columns]
        for i in range(0, len(text), columns)
    ]

    result = ""

    for col in order:
        for row in table:
            if col < len(row):
                result += row[col]

    return result


def permutation_decrypt(text, key):
    columns = len(key)
    rows = (len(text) + columns - 1) // columns
    order = get_order(key)

    table = [[""] * columns for _ in range(rows)]

    index = 0

    for col in order:
        for row in range(rows):
            if row * columns + col < len(text):
                table[row][col] = text[index]
                index += 1

    result = ""

    for row in table:
        result += "".join(row)

    return result


def main():
    while True:
        print("\n===== ЛАБОРАТОРНА РОБОТА №1 =====")
        print("1. Шифр Цезаря")
        print("2. Шифр перестановки")
        print("0. Вихід")

        choice = input("Оберіть алгоритм: ")

        if choice == "0":
            print("Завершення програми.")
            break

        if choice not in ("1", "2"):
            print("Неправильний вибір!")
            continue

        text = input("Введіть текст: ")

        if choice == "1":
            try:
                key = int(input("Введіть числовий ключ: "))
            except ValueError:
                print("Ключ повинен бути числом!")
                continue

            encrypted = caesar(text, key)
            decrypted = caesar(encrypted, key, True)

            print("\n--- Шифр Цезаря ---")

        else:
            key = input("Введіть ключове слово: ")

            if not key or not key.isalpha():
                print("Ключ повинен містити лише літери!")
                continue

            encrypted = permutation_encrypt(text, key)
            decrypted = permutation_decrypt(encrypted, key)

            print("\n--- Шифр перестановки ---")

        print("Початковий текст:", text)
        print("Ключ:", key)
        print("Зашифрований текст:", encrypted)
        print("Розшифрований текст:", decrypted)


if __name__ == "__main__":
    main()
