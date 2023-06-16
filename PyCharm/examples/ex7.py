#!/user/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    with open("file3.txt", 'r') as fileptr:
        sentences = fileptr.readlines()

    for sentence in sentences:
        if ',' in sentence:
            print(sentence)
