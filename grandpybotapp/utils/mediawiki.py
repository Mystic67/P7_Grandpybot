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
                                "exlimit" : "1",
                                "pageids" : ""
                                }
        self.wiki_page_id = ""

    def get_id(self):
        req = requests.get(self.url, self.found_id_params)
        if req.status_code == 200:
            wikiData = req.json()
            try:
                wiki_page_id = wikiData["query"]["search"][0]["pageid"]
                return wiki_page_id
            except:
                return ""
        else:
            return ""

    def get_infos(self):
        wikiInfos={}
        self.found_extract_params["pageids"] = self.get_id()
        req = requests.get(self.url, self.found_extract_params)
        if req.status_code == 200:
            wikiData = req.json();
            wiki_page_id =[]
            wikiInfos["status"] = "OK"
            try:
                for key in wikiData["query"]["pages"]:
                    wiki_page_id.append(key)
                wikiInfos["text"]= wikiData["query"]["pages"][wiki_page_id[0]]["extract"]
                return wikiInfos
            except KeyError:
                wikiInfos["status"] = "NOT FOUND"
                return wikiInfos
            except IndexError:
                wikiInfos["status"] = "NOT FOUND"
                return wikiInfos
        else:
            wikiInfos["status"] = "error 404"
            return wikiInfos

    @property
    def infos(self):
        infos = self.get_infos()
        return infos

    @property
    def status(self):
        infos = self.get_infos()
        return infos['status']
