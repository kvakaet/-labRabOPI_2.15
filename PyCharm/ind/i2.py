#!/user/bin/env python3
# -*- coding: utf-8 -*-


#вариант 17
"""Продолжая тему предыдущего упражнения, в тех же операционных системах на базе Unix
обычно есть и утилита с названием tail, которая отображает последние десять строк
содержимого файла, имя которого передается в качестве аргумента командной строки.
Реализуйте программу, которая будет делать то же самое. В случае отсутствия файла,
указанного пользователем, или аргумента командной строки вам нужно вывести
соответствующее сообщение."""
def tail(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            last_lines = lines[-10:]

            for line in last_lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except IsADirectoryError:
        print(f"'{filename}' является директорией, а не файлом.")


filename = 'individual2.txt'
tail(filename)
