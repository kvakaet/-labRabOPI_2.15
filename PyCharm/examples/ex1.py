#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    with open("file1.txt", 'w') as fileptr:
        fileptr.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vitae fermentum lectus.\n"
            "Cras et nulla elit. Curabitur rhoncus ipsum nisl, in rutrum ante mattis ac."
        )
