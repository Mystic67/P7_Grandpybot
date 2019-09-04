#! /usr/bin/env python
# coding: utf-8

from grandpybotapp.utils import mediawiki
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

# instance mediawiki
mediawiki_instance = mediawiki.MediaWiki('OpenClassrooms Paris')

class MockResponseId:
    @staticmethod
    def json():
        return mediaWikiIdRequestsResult

class MockResponseInfos:
    @staticmethod
    def json():
        return mediawikiTextRequestsResult

def test_get_id_is_ok(monkeypatch):
    # custom class to be the mock return value
    # will override the requests.Response returned from requests.get
    def mock_get_id_get(*url, **params):
        return MockResponseId
    #patch method "get_place_infos" with "mock_get_id"
    monkeypatch.setattr(requests,'get', mock_get_id_get)
    # "get_id", uses the monkeypatch
    assert mediawiki_instance.get_id() == idResult

def test_get_infos_is_ok(monkeypatch):
    # custom class to be the mock return value
    # will override the requests.Response returned from requests.get
    def mock_get_infos_get(*url, **params):
        return MockResponseInfos

    #patch method "get_place_infos" with "mock_get_id"
    monkeypatch.setattr(requests,'get', mock_get_infos_get)

    # "get_infos", uses the monkeypatch
    assert mediawiki_instance.get_infos() == infosResult
