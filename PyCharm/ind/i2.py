#!/user/bin/env python3
# -*- coding: utf-8 -*-


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
