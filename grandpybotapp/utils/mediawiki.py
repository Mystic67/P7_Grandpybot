import requests
import json

class MediaWiki:
    """This class search from wikimedia, the placeId with place name and with placeId search and return the place intro text (extract)."""
    def __init__(self, place):
        self.url = "https://fr.wikipedia.org/w/api.php?"
        self.found_id_params = {
                                "action":"query",
                                "list" : "search",
                                "format" : "json",
                                "utf8" : "",
                                "srlimit" : "1",
                                "srsearch" : place
                                }

        self.found_extract_params = {
                                "action":"query",
                                "format" : "json",
                                "prop" : "extracts",
                                "explaintext" : "",
                                "pageterms" : "histoire",
                                "exintro" : "",
                                "utf8" : "",
                                "exlimit" : "1"
                                }
        self.wiki_page_id = ""

    def get_id(self):
        req = requests.get(self.url, self.found_id_params)
        wikiData = req.json()
        try:
            self.wiki_page_id = wikiData["query"]["search"][0]["pageid"]
            return self.wiki_page_id
        except KeyError:
            return ""
        except IndexError:
            return ""

    def get_infos(self):
        wikiInfos={}
        self.found_extract_params["pageids"] = self.get_id()
        if self.found_extract_params["pageids"] != "":
            req = requests.get(self.url, self.found_extract_params)
            wikiData = req.json();
            wikiInfos["status"] = "OK"
            wikiInfos["text"]= wikiData["query"]["pages"][str(self.wiki_page_id)]["extract"]
        else:
            wikiInfos["status"] = "NOT FOUND"
        return wikiInfos

    @property
    def infos(self):
        infos = self.get_infos()
        return infos

    @property
    def status(self):
        infos = self.get_infos()
        return infos['status']
