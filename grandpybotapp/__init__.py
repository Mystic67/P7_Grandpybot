#! /usr/bin/env python
# coding: utf-8

import os
from flask import Flask

from .views import app
app.config.from_object('config')
