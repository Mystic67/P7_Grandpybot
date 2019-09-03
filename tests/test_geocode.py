#! /usr/bin/env python
# coding: utf-8

from grandpybotapp.utils import googleGeocode
import requests
import json
import pytest

json_requests_response = {
                           "results" : [
                              {
                                 "formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                                 "geometry" : {
                                    "location" : {
                                       "lat" : 48.8748465,
                                       "lng" : 2.3504873
                                    }
                                 },
                                 "place_id" : "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8"
                              }
                           ],
                           "status" : "OK"
                        }

result = {
            'status': 'OK',
            'adress': '7 Cité Paradis, 75010 Paris, France',
            'location': {'lat': 48.8748465, 'lng': 2.3504873},
            'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
        }

class MockResponse:
    @staticmethod
    def json():
        return json_requests_response

def test_get_geocode_place_infos_is_ok(monkeypatch):
    # custom class to be the mock return value
    # will override the requests.Response returned from requests.get
    def mock_get(*url, **params):
        #mockResponse = MockResponse.json()
        return MockResponse()

    #patch method "get_place_infos" with "mock_get_place_infos"
    monkeypatch.setattr(requests,'get', mock_get)

    # instance geocode
    geocode_instance = googleGeocode.Geocode('Fake_place')

    # "get_place_infos", uses the monkeypatch
    assert geocode_instance.get_place_infos() == result

    #print(geocode_instance.get_place_infos())
