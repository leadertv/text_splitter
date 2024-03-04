# Список файлов
file_names = ['1.txt', '2.txt', '3.txt']

# Запись в итоговый супер-файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for i, file_name in enumerate(file_names):
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Запись служебной информации
            result_file.write(file_name + '\n')
            result_file.write(str(len(lines)) + '\n')
            # Запись содержимого файла
            result_file.writelines(lines)
            # Добавление пустой строки для разделения файлов для красоты.
            if i < len(file_names) - 1:
                result_file.write('\n')

# Подсчёт количества строк в итоговом файле
with open('result.txt', 'r', encoding='utf-8') as result_file:
    total_lines = sum(1 for line in result_file)

print('\U0001F680 \033[36m' + 'Файл содержит \033[31m' + str(total_lines) + ' строк! ' +
      '\033[36mОбъединение (или обновление) файлов завершено!')
print('\n\033[92mЖду 5-ку в дневник 😄!')
