#! /usr/bin/env python
# coding: utf-8

import requests
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
        self.placeInfos={}
        req = requests.get(self.url, self.geocode_params)
        if req.status_code >=200 and req.status_code <=400:
            data = req.json()
            self.placeInfos["status"] = data["status"]
            if self.placeInfos["status"] == "OK":
                self.placeInfos["address"] = data["results"][0]["formatted_address"]
                self.placeInfos["location"] = data["results"][0]["geometry"]["location"]
                self.placeInfos["place_id"] = data["results"][0]["place_id"]
            else:
                try:
                    self.placeInfos['error_message'] = data["error_message"]
                except KeyError:
                    pass
            return self.placeInfos
        else:
            self.placeInfos['status'] = "Erreur 404"
            self.placeInfos['error_message'] = "Page not found or error in URL"
            return self.placeInfos

    @property
    def infos(self):
        return self.placeInfos

    @property
    def status(self):
        return self.placeInfos["status"]

    @property
    def address(self):
        try:
            if self.placeInfos["address"]:
                return self.placeInfos["address"]
        except:
            return "'address' not found for this request"

    @property
    def location(self):
        try:
            if self.placeInfos["location"]:
                return self.placeInfos["location"]
        except:
            return "'location' not found for this request"

    @property
    def place_id(self):
        try:
            if self.placeInfos["place_id"]:
                return self.placeInfos["place_id"]
        except:
            return "'place_id' not found for this request"

    @property
    def message_error(self):
        try:
            if self.placeInfos["error_message"]:
                return self.placeInfos["error_message"]
        except:
            return "No message Error"

# if __name__=="__main__":
#     geo = Geocode("OpenClassrooms Paris")
#     print(geo.status)
#     print(geo.address)
#     print(geo.location)
#     print(geo.location['lat'])
#     print(geo.location['lng'])
#     print(geo.place_id)
#     print(geo.message_error)
