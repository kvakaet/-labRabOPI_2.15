#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

def find_files(directory, extension, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination, file)
                shutil.move(source_path, destination_path)
                print(f"Файл '{file}' перемещен в '{destination}'")

directory = 'C:/Users/FonK/Desktop/python/OPI/-labRabOPI_2.15'
extension = '.txt'
destination = 'C:/Users/FonK/Desktop/python/OPI/-labRabOPI_2.15/PyCharm'
find_files(directory, extension, destination)



