# Список имён файлов (3.txt тоже есть, скачал все три файла и запихал в список)
file_names = ['1.txt', '2.txt', '3.txt']
file_contents = []

# Чтение содержимое и считаем чё там...
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents.append((file_name, len(lines), lines))

# Сортировка - калибровка
file_contents.sort(key=lambda x: x[1])

# Запись в итоговый супер-файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count, lines in file_contents:
        # Запись служебной информации
        result_file.write(file_name + '\n')
        result_file.write(str(line_count) + '\n')
        # Запись содержимого файла
        result_file.writelines(lines)
        # Добавление пустой строки для разделения файлов (чисто на всякий случай, чтобы спать спокойно)
        result_file.write('\n')

print('\033[36mОбъединение (или обновление) файлов завершено!')
print('\n\033[92mЖду 5-ку в дневник 😄!' + '\033[0m')
