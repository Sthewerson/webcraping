from flask import Flask
from web_scraping import scrap
import json


'''
Api utilizando flask para disponibilizar os dados gerados no webscraping
'''
app = Flask(__name__)


@app.route("/")
def get_notebooks():
    notebooks = scrap()
    return  json.dumps(notebooks)