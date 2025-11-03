def main():
    max_sections = 20

    # Запитуємо кількість розділів
    while True:
        try:
            num_sections = int(input(f"Введіть кількість розділів (максимум {max_sections}): "))
            if 1 <= num_sections <= max_sections:
                break
            else:
                print(f"Число повинно бути в межах від 1 до {max_sections}.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    # Запитуємо метод сортування
    while True:
        print("\n1. Алфавітний порядок (за зростанням)")
        print("2. Алфавітний порядок (за спаданням)")
        print("3. Довжина назв (за зростанням)")
        try:
            method = int(input("Виберіть метод сортування (1, 2 або 3): "))
            if method in [1, 2, 3]:
                break
            else:
                print("Будь ласка, виберіть 1, 2 або 3.")
        except ValueError:
            print("Помилка! Введіть число 1, 2 або 3.")

    # Вводимо назви розділів
    sections = []
    for i in range(num_sections):
        section_name = input(f"Введіть назву для розділу {i + 1}: ")
        sections.append(section_name)

    # Видаляємо дублікати та сортуємо
    sections = list(set(sections))  # Видалення дублікатів

    if method == 1:
        sections.sort()  # Алфавітний порядок за зростанням
    elif method == 2:
        sections.sort(reverse=True)  # Алфавітний порядок за спаданням
    elif method == 3:
        sections.sort(key=len)  # За довжиною рядків

    # Виводимо результат
    print("\nРозділи після сортування:")
    for section in sections:
        print(section)


if __name__ == "__main__":
    main()
