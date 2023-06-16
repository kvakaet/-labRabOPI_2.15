#!/user/bin/env python3
# -*- coding: utf-8 -*-


def rever(filename):
    with open(filename, 'r') as file:
        text = file.read()
        sentences = text.split('.')

        reversed_sentences = reversed(sentences)
        for sentence in reversed_sentences:
            print(sentence.strip())


filename = 'individual1.txt'

rever(filename)
