#! /usr/bin/env python
# coding: utf-8

from grandpybotapp.py_backend.textParser import TextParser
import nltk

class TestParser:

    def setup_class(self):
        self.parser = TextParser()
        self.text = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"

    def test_parse_the_text(self):
        response = self.parser.parse_text(self.text)
        assert response == "OpenClassrooms"
