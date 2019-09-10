#! /usr/bin/env python
# coding: utf-8

from grandpybotapp.utils.textParser import TextParser
import pytest
import nltk



textList = ["Salut GrandPy ! Est-ce que tu connais OpenClassrooms ? ",
        "Que peux-tu me dire sur Kuala Lumpur ? ",
        "As-tu des informations sur le musé du Louvre ? ",
        "Je voudrais visiter le Mont saint Odile ",
        "Bonjour Papy ! As-tu connu les tours jumelles? ",
        "Je voudrais me rendre rue de la première armée à Strasbourg. "]

parsedTextList = ["OpenClassrooms Paris ",
            "Kuala Lumpur ",
            "informations musé Louvre ",
            "Mont saint Odile ",
            "tours jumelles ",
            "rue armée Strasbourg "]

def test_parse_the_text():
    for i, text in enumerate(textList):
        assert TextParser.parse_text(text) == parsedTextList[i]
