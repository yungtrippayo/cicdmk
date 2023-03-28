# ключове слово
keyword = input("Введіть ключове слово: ")

# вихідний файл для запису
with open("filtered.txt", "w") as output_file:

    # вхідний файл для читання
    with open("input.txt", "r") as input_file:

        # перебір
        for line in input_file:

            # додяння рядків до вихідного файлу
            if keyword in line:
                output_file.write(line)