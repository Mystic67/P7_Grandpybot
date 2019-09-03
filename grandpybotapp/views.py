#! /usr/bin/env python
# coding: utf-8
import os
from flask import Flask, render_template, url_for, request, jsonify
from .utils.textParser import TextParser
from .utils.googleGeocode import Geocode
from .utils.mediawiki import MediaWiki
from .utils.settings import texts_config as constants
import random

app = Flask(__name__)

# To get one variable from config, tape app.config['MY_VARIABLE']
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    Google_API_Key = app.config['GOOGLE_API_KEY']
    return render_template('index.html', API_Key = Google_API_Key)

@app.route('/search', methods=['POST'])
def search():

    if request.method == 'POST':
        #init sended user message
        #userMessage = request.form.get('userMessage')
        # Get JSON data from POST
        data = request.get_json()
        userMessage = data[0]['userMessage']
        # parse the user message
        parsedUserMessage = TextParser().parse_text(userMessage)
        # instance geocode with parsed user message
        geocode = Geocode(parsedUserMessage)
        # instance mediawiki with parsed user message
        wiki = MediaWiki(parsedUserMessage)
        if geocode.status == "OK":
            #mapsLocation = geocode.location
            maps_bot_message = random.choice(constants.GOOGLEFOUND)
        else:
            maps_bot_message = random.choice(constants.GOOGLENOTFOUND)

        if wiki.status == "OK":
            wiki_bot_message = random.choice(constants.WIKIFOUND)
        else:
            wiki_bot_message = random.choice(constants.WIKINOTFOUND)

        return jsonify(
                    maps_bot_message = maps_bot_message,
                    maps_infos = geocode.infos,
                    wiki_bot_message = wiki_bot_message,
                    wikiInfos = wiki.infos
                    )


#if __name__ == "__main__":
#    app.run()
