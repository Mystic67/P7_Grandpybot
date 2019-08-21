#! /usr/bin/env python
# coding: utf-8

import requests
import json
#from settings import config as constants
import config

class Geocode:

    def __init__(self):
        self.api_key = config.GOOGLE_API_KEY#app.config['GOOGLE_API_KEY']
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.geocode_params = {
                            "address" : "",
                            "key" : self.api_key,
                            }

    def search_place(self, place):
        placeInfos={}
        self.geocode_params["address"] = place
        req = requests.get(self.url, self.geocode_params)
        geocode_json_data = req.json()
        placeInfos["status"] = geocode_json_data["status"]
        if placeInfos["status"].lower() == "ok":
            placeInfos["adress"] = geocode_json_data["results"][0]["formatted_address"]
            placeInfos["location"] = geocode_json_data["results"][0]["geometry"]["location"]
            placeInfos["place_id"] = geocode_json_data["results"][0]["place_id"]
        else:
            try:
                placeInfos['error_message'] = geocode_json_data["error_message"]
            except KeyError:
                placeInfos['error_message'] = "Unknown error"

        return placeInfos
