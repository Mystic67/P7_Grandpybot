#! /usr/bin/env python
# coding: utf-8

from .settings import texts_config as constants
import nltk

class TextParser:
    ''' This module parse the text from userMessage'''
    @classmethod
    def parse_text(cls, text):
        stopwords = constants.STOPWORDS + constants.CUSTOM_STOPWORDS
        parsedListText =[]
        tokenizer = nltk.RegexpTokenizer(r'\w+')
        tokenized_text = tokenizer.tokenize(text)
        for word in tokenized_text:
            if word.lower() not in stopwords:
                parsedListText.append(word)
            if "openclassrooms" in word.lower():
                parsedListText.append("Paris")
        parsedWords = " ".join(parsedListText)
        print(parsedWords)
        return parsedWords
