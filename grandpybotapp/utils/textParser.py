#! /usr/bin/env python
# coding: utf-8

from .settings import config as constants
import nltk

class TextParser:

    def __init__(self):
        self.stopwords = constants.STOPWORDS + constants.CUSTOM_STOPWORDS

    def parse_text(self, text):
        parsedListText =[]
        tokenizer = nltk.RegexpTokenizer(r'\w+')
        tokenized_text = tokenizer.tokenize(text)
        for word in tokenized_text:
            if word.lower() not in self.stopwords:
                parsedListText.append(word)
        parsedWords = " ".join(parsedListText)
        return parsedWords
