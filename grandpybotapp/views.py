#! /usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request, jsonify
from .utils.textParser import TextParser
from .utils.googleGeocode import Geocode
from .utils.mediawiki import MediaWiki
from .utils.settings import texts_config as constants
import random
from collections import deque

app = Flask(__name__)

# To get one variable from config, tape app.config['MY_VARIABLE']
app.config.from_object('config')

fifoBotGeoResponse = deque([], maxlen=2)
fifoBotWikiResponse = deque([], maxlen=2)


@app.route('/')
@app.route('/index/')
def index():
    Google_API_Key = app.config['GOOGLE_API_KEY']
    return render_template('index.html', API_Key=Google_API_Key)


@app.route('/search', methods=['POST'])
def search():

    if request.method == 'POST':
        # Get JSON data from POST
        data = request.get_json()
        userMessage = data[0]['userMessage']
        # parse the user message
        parsedUserMessage = TextParser().parse_text(userMessage)
        # instance geocode with parsed user message
        geocode = Geocode(parsedUserMessage)
        # instance mediawiki with parsed user message
        wiki = MediaWiki(parsedUserMessage)
        # choice bot message in list for geocode result
        # use fifo to not have same response
        if geocode.status == "OK":
            while 1:
                maps_bot_message = random.choice(constants.GOOGLEFOUND)
                if maps_bot_message not in fifoBotGeoResponse:
                    fifoBotGeoResponse.append(maps_bot_message)
                    break
        else:
            while 1:
                maps_bot_message = random.choice(constants.GOOGLENOTFOUND)
                if maps_bot_message not in fifoBotGeoResponse:
                    fifoBotGeoResponse.append(maps_bot_message)
                    break
        # choice bot message in list for wiki result
        # use fifo to not have same response
        if wiki.status == "OK":
            while 1:
                wiki_bot_message = random.choice(constants.WIKIFOUND)
                if wiki_bot_message not in fifoBotWikiResponse:
                    fifoBotWikiResponse.append(wiki_bot_message)
                    break
        else:
            while 1:
                wiki_bot_message = random.choice(constants.WIKINOTFOUND)
                if wiki_bot_message not in fifoBotWikiResponse:
                    fifoBotWikiResponse.append(wiki_bot_message)
                    break

        return jsonify(
            maps_bot_message=maps_bot_message,
            maps_infos=geocode.infos,
            wiki_bot_message=wiki_bot_message,
            wikiInfos=wiki.infos
        )


# if __name__ == "__main__":
#    app.run()
