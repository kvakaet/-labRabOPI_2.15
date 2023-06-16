#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open("file1.txt", 'a') as fileptr:
        fileptr.write("\nThis text fragment was added here.")
