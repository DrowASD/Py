def normalize_spaces(input_string):
    # Разбиваем строку на слова, удаляя лишние пробелы
    words = input_string.split()
    # Объединяем слова, добавляя один пробел между ними
    result = ' '.join(words)
    return result

# Пример использования
input_string = "Это    пример строки с   несколькими     пробелами."
print(normalize_spaces(input_string))

