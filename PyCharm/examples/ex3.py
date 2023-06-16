#!/user/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    with open("file1.txt", 'r') as fileptr:
        content1 = fileptr.readline()
        content2 = fileptr.readline()

        print(content1)
        print(content2)
