#! /usr/bin/env python
# coding: utf-8

import requests
#from settings import config
import config

class Geocode:
    """ This class search the geolocation informations of a place """
    def __init__(self, place=""):
        self.api_key = config.GOOGLE_API_KEY
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.geocode_params = {
                            "address" : place,
                            "key" : self.api_key,
                            }
        self.get_place_infos()

    def get_place_infos(self):
        req = requests.get(url = self.url, params = self.geocode_params)
        data = req.json()
        self.placeInfos={}
        self.placeInfos["status"] = data["status"]
        if self.placeInfos["status"] == "OK":
            self.placeInfos["adress"] = data["results"][0]["formatted_address"]
            self.placeInfos["location"] = data["results"][0]["geometry"]["location"]
            self.placeInfos["place_id"] = data["results"][0]["place_id"]
        elif self.placeInfos['status'] == "ZERO_RESULTS":
            pass
        else:
            try:
                self.placeInfos['error_message'] = data["error_message"]
            except KeyError:
                pass
        return self.placeInfos

    @property
    def infos(self):
        return self.placeInfos

    @property
    def status(self):
        return self.placeInfos["status"]

    @property
    def adress(self):
        try:
            if self.placeInfos["adress"]:
                return self.placeInfos["adress"]
        except KeyError:
            return "'adress' not found for this request"

    @property
    def location(self):
        try:
            if self.placeInfos["location"]:
                return self.placeInfos["location"]
        except KeyError:
            return "'location' not found for this request"

    @property
    def place_id(self):
        try:
            if self.placeInfos["place_id"]:
                return self.placeInfos["place_id"]
        except KeyError:
            return "'place_id' not found for this request"

    @property
    def message_error(self):
        try:
            if self.placeInfos["error_message"]:
                return self.placeInfos["error_message"]
        except KeyError:
            return "No message Error"

# if __name__=="__main__":
#     geo = Geocode("OpenClassrooms Paris")
#     print(geo.status)
#     print(geo.adress)
#     print(geo.location)
#     print(geo.location['lat'])
#     print(geo.location['lng'])
#     print(geo.place_id)
#     print(geo.message_error)
