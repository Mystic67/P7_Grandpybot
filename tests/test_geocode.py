#! /usr/bin/env python
# coding: utf-8

from grandpybotapp.utils.googleGeocode import Geocode
import requests
import pytest

# -----------------------Mock request result with status OK -------------------
# Response from requests.get json if address was found
json_requests_response_ok = {
    "results": [
        {
            "formatted_address": "7 Cité Paradis, 75010 Paris, France",
            "geometry": {
                "location": {
                    "lat": 48.8748465,
                    "lng": 2.3504873
                }
            },
            "place_id": "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8"
        }
    ],
    "status": "OK"

}
# Result after parsing the response from requests.get json
result_ok = {
    'status': 'OK',
    'address': '7 Cité Paradis, 75010 Paris, France',
    'location': {'lat': 48.8748465, 'lng': 2.3504873},
    'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
}

# ---------------Mock request result with status ZERO_RESULTS -----------------
# Response from requests.get json if address was found
json_requests_response_zero_results = {
    "results": [],
    "status": "ZERO_RESULTS"
}

# ---------- Mock request result with status INVALID_REQUEST ------------------
# Response from requests.get json if address was found
json_requests_response_invalid_request = {
    "error_message": "Invalid request. Missing the 'address', 'components', 'latlng' or 'place_id' parameter.",
    "results": [],
    "status": "INVALID_REQUEST"}


# will mock the requests.get methode
# custom class to be the mock return value
class MockRequestsGet:
    '''This class will mock the requests.get method'''

    def __init__(self, status_code, response):
        self.status_code = status_code
        self.response = response

    def json(self):
        return self.response


def test_get_geocode_place_infos_parsing_with_status_ok(monkeypatch):
    ''' This function test if get_geocode_place_infos parsing response is ok if requests response has result'''
    # instance mock requests.get class with params
    mockRequestsGet = MockRequestsGet(200, json_requests_response_ok)

    def mock_response(*url, **params):
        return mockRequestsGet
    # patch method get with mock_response
    monkeypatch.setattr(requests, 'get', mock_response)
    # Test the responses
    assert Geocode('').get_place_infos() == result_ok
    assert Geocode('Fake_request').infos == result_ok
    assert Geocode('Fake_request').status == "OK"
    assert Geocode(
        'Fake_request').address == '7 Cité Paradis, 75010 Paris, France'
    assert Geocode('Fake_request').location == {
        'lat': 48.8748465, 'lng': 2.3504873}
    assert Geocode('Fake_request').place_id == 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
    assert Geocode('Fake_request').message_error == "No message Error"


def test_get_geocode_place_infos_parsing_with_status_zero_result(monkeypatch):
    ''' This function test if get_geocode_place_infos parsing response is ok if requests response has no result'''
    # instance mock requests.get class with params
    mockRequestsGet = MockRequestsGet(200, json_requests_response_zero_results)

    def mock_response(*url, **params):
        return mockRequestsGet
    # patch method get with mock_response
    monkeypatch.setattr(requests, 'get', mock_response)
    # Test the responses
    assert Geocode('Fake_request').get_place_infos() == {
        'status': 'ZERO_RESULTS'}
    assert Geocode('Fake_request').infos == {'status': 'ZERO_RESULTS'}
    assert Geocode('Fake_request').status == 'ZERO_RESULTS'
    assert Geocode(
        'Fake_request').address == "'address' not found for this request"
    assert Geocode(
        'Fake_request').location == "'location' not found for this request"
    assert Geocode(
        'Fake_request').place_id == "'place_id' not found for this request"
    assert Geocode('Fake_request').message_error == "No message Error"


def test_get_geocode_place_infos_parsing_with_status_invalid_request(
        monkeypatch):
    ''' This function test if get_geocode_place_infos parsing response is ok if error in request params '''
    # custom class to be the mock return value
    # will mock the requests.get methode
    mockRequestsGet = MockRequestsGet(
        200, json_requests_response_invalid_request)

    def mock_response(*url, **params):
        return mockRequestsGet
    # patch method "get_place_infos" with "mock_get_place_infos"
    monkeypatch.setattr(requests, 'get', mock_response)
    # Test the responses
    assert Geocode('Fake_request').get_place_infos() == {
        'status': 'INVALID_REQUEST',
        'error_message': "Invalid request. Missing the 'address', 'components', 'latlng' or 'place_id' parameter."}
    assert Geocode('Fake_request').infos == {
        'status': 'INVALID_REQUEST',
        'error_message': "Invalid request. Missing the 'address', 'components', 'latlng' or 'place_id' parameter."}
    assert Geocode('Fake_request').status == "INVALID_REQUEST"
    assert Geocode(
        'Fake_request').address == "'address' not found for this request"
    assert Geocode(
        'Fake_request').location == "'location' not found for this request"
    assert Geocode(
        'Fake_request').place_id == "'place_id' not found for this request"
    assert Geocode(
        'Fake_request').message_error == "Invalid request. Missing the 'address', 'components', 'latlng' or 'place_id' parameter."


def test_get_geocode_place_infos_parsing_with_error_404(monkeypatch):
    ''' This function test if get_geocode_place_infos parsing response is ok if server return page not found '''
    # will mock the requests.get methode
    mockRequestsGet = MockRequestsGet(404, 'no_response')

    def mock_response(*url, **params):
        return mockRequestsGet
    # patch method "get_place_infos" with "mock_get_place_infos"
    monkeypatch.setattr(requests, 'get', mock_response)
    # test responses
    assert Geocode('Fake_request').get_place_infos() == {
        'status': 'Erreur 404', 'error_message': 'Page not found or error in URL'}
    assert Geocode('Fake_request').infos == {
        'status': 'Erreur 404',
        'error_message': 'Page not found or error in URL'}
    assert Geocode('Fake_request').status == "Erreur 404"
    assert Geocode(
        'Fake_request').address == "'address' not found for this request"
    assert Geocode(
        'Fake_request').location == "'location' not found for this request"
    assert Geocode(
        'Fake_request').place_id == "'place_id' not found for this request"
    assert Geocode(
        'Fake_request').message_error == "Page not found or error in URL"
