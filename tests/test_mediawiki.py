#! /usr/bin/env python
# coding: utf-8

from grandpybotapp.utils.mediawiki import MediaWiki
import requests
import json
import pytest

#requests query result look like
mediaWikiIdRequestsResult = {'query': {'search': [{'pageid': '4338589'}] } }

idResult = "4338589"

#requests query result look like
mediawikiTextRequestsResult = {"query" :
                                {"pages" :
                                    {"4338589":
                                        {"extract" : "OpenClassrooms est une école ..."
                                        }
                                    }
                                }
                            }

infosResult = {'status': 'OK',
                'text': 'OpenClassrooms est une école ...'
            }

# will mock the requests.get methode
# custom class to be the mock return value
class MockRequestsGet:
    '''This class will mock the requests.get method'''
    def __init__(self, status_code, response):
        self.status_code = status_code
        self.response = response
    def json(self):
        return self.response

def test_get_id_parsing_with_results(monkeypatch):
    ''' This function test if get_id parsing response is ok when requests result is ok '''
    # instance mock requests.get class with params
    mockRequestsGet = MockRequestsGet(200, mediaWikiIdRequestsResult)
    def mock_response(*url, **params):
        return mockRequestsGet

    #print(mock_response().json())
    #patch method get with mock_response
    monkeypatch.setattr(requests,'get', mock_response)
    # "get_id", uses the monkeypatch
    assert MediaWiki('fake_place').get_id() == idResult

def test_get_infos_parsing_with_result(monkeypatch):
    ''' This function test if get_infos parsing response is ok when requests response has result'''
    # instance mock requests.get class with params
    mockRequestsGet = MockRequestsGet(200, mediawikiTextRequestsResult)
    def mock_response(*url, **params):
        return mockRequestsGet

    print(mock_response().json())
    #patch method get with mock_response
    monkeypatch.setattr(requests,'get', mock_response)
    # Test responses
    print(MediaWiki('OpenClassrooms Paris').get_infos())
    assert MediaWiki('OpenClassrooms Paris').get_infos() == infosResult
    assert MediaWiki('fake_place').infos == infosResult

def test_get_id_parsing_with_no_results(monkeypatch):
    ''' This function test if get_id parsing response is ok when requests result has no result '''
    # instance mock requests.get class with params
    mockRequestsGet = MockRequestsGet(200, {"query":{"search":[]}})
    def mock_response(url, params= None):
        return mockRequestsGet
    #patch method get with mock_response
    monkeypatch.setattr(requests,'get', mock_response)
    # Test responses
    assert MediaWiki('fake_place').get_id() == ""

def test_get_infos_parsing_with_no_result(monkeypatch):
    ''' This function test if get_infos parsing response is ok when requests response has no result'''
    # instance mock requests.get class with params
    mockRequestsGet = MockRequestsGet(200, {"query":{"search":[]}})
    def mock_response(url, params= None):
        return mockRequestsGet
    #patch method get with mock_response
    monkeypatch.setattr(requests,'get', mock_response)
    # Test responses
    assert MediaWiki('fake_place').get_infos() == {'status': 'NOT FOUND'}
    assert MediaWiki('fake_place').infos == {'status': 'NOT FOUND'}

def test_get_id_parsing_with_error_404(monkeypatch):
    ''' This function test if get_id parsing response if url is not correct or service not accessible  '''
    # instance mock requests.get class with params
    mockRequestsGet = MockRequestsGet(404, {"query":{"search":[]}})
    def mock_response(url, params= None):
        return mockRequestsGet
    #patch method get with mock_response
    monkeypatch.setattr(requests,'get', mock_response)
    # Test responses
    assert MediaWiki('fake_place').get_id() == ""

def test_get_infos_parsing_with_error_404(monkeypatch):
    ''' This function test get_infos parsing response if url is not correct or service not accessible'''
    # instance mock requests.get class with params
    mockRequestsGet = MockRequestsGet(404, {"query":{"search":[]}})
    def mock_response(url, params= None):
        return mockRequestsGet
    #patch method get with mock_response
    monkeypatch.setattr(requests,'get', mock_response)
    # Test responses
    assert MediaWiki('fake_place').get_infos() == {'status': 'error 404'}
    assert MediaWiki('fake_place').infos == {'status': 'error 404'}
