#!/usr/bin/env python3

import ipdb


class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) is not str:
            print("The value must be a string.")
        else:
            self._value = value

    def is_sentence(self):
        if self.value[-1] == ".":
            return True
        else:
            return False

    def is_question(self):
        if self.value[-1] == "?":
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value[-1] == "!":
            return True
        else:
            return False

    def count_sentences(self):
        sentences = [
            string.strip()
            for string in self.value.replace("?", ".").replace("!", ".").split(".")
            if string.strip() != ""
        ]
        return len(sentences)
