#! /usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, url_for, request, json

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
        searchText = request.args.get('search')
    return render_template('index.html', text=searchText)
