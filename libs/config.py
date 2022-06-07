# -*- coding: utf-8 -*-
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname

load_dotenv(join(dirname(__file__), '.env'))

SERVER_PATH = environ.get('SERVER_PATH')
TMP_PATH    = environ.get('TMP_PATH')
STATIC_PATH = environ.get('STATIC_PATH')