#!/user/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    with open("file1.txt") as fileptr:
        print("The filepointer is at byte: ", fileptr.tell())

        fileptr.seek(10)

        print("After reading, the filepointer is at: ", fileptr.tell())
