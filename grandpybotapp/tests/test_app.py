#! /usr/bin/env python
# coding: utf-8

from grandpybotapp.utils.textParser import TextParser
from grandpybotapp.utils.googleGeocode import Geocode
import nltk

class TestParser:

    def setup_class(self):
        self.parser = TextParser()
        self.text = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"

    def test_parse_the_text(self):
        response = self.parser.parse_text(self.text)
        assert response == "OpenClassrooms"

class TestGeocode:
    def setup_class(self):
        self.geocode = Geocode()

    def test_geocode_search_place(self):
        response = self.geocode.search_place("OpenClassrooms Paris")
        print(response['status'])
        assert response == {'status': 'OK', 'adress': '7 Cité Paradis, 75010 Paris, France', 'location': {'lat': 48.8748465, 'lng': 2.3504873}, 'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}
