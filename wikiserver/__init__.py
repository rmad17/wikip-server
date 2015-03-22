from flask import Flask
wikiserver = Flask(__name__)
wikiserver.config.from_object('config')
from wikiserver import views
