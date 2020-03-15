#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template
import os
from flask_pymongo import PyMongo

# to import a .py file from another location
import sys
sys.path.append('/Users/priyankasenapati/Desktop/Classwork/Mission-to-Mars/app')

import scraping

app = Flask(__name__)

app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    print("Rendering index.html")
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    print("Scraping Successful!")
    return "Scraping Successful!"

if __name__ == "__main__":
    app.run(host=os.getenv('IP', 'localhost'), 
            port=int(os.getenv('PORT', 4444)))
