#!/user/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    with open("file2.txt", 'x') as fileptr:
        print(fileptr)

        if fileptr:
            print("File created successfully!")
