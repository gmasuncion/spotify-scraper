from flask import Flask, render_template, redirect, url_for, request
from flask.helpers import send_file
from services import Scraper
from services import Settings
from services import GraphService
import matplotlib.pyplot as plt
import io
import numpy
app = Flask(__name__)
from os import path
import os
import shutil

@app.route("/", methods=["POST", "GET"])
def home():
    if path.exists('/static/images/'):
        shutil.rmtree('/static/images/')
    if request.method == "POST":
        artist1name = request.form["artist1"]
        artist2name = request.form["artist2"]
        return redirect(url_for("comparisoninfo", name1=artist1name, name2=artist2name))
    else:
        return render_template("index.html")

@app.route("/compare/<name1>vs<name2>")
def comparisoninfo(name1, name2):
    tool = Scraper.Scraper()
    artist1 = tool.scrape_artist(name1)
    artist2 = tool.scrape_artist(name2)

    artist1_streams = [x.streams for x in artist1.songs]
    artist2_streams = [x.streams for x in artist2.songs]
    plt.switch_backend('Agg')
    width = 0.4
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    bar1 = numpy.arange(len(artist1.songs))
    bar2 = [i+width for i in bar1]

    plt.bar(bar1, artist1_streams, width, label = artist1.name)
    plt.bar(bar2, artist2_streams, width, label = artist2.name)

    plt.xlabel("Top Hits")
    plt.ylabel("Number of Streams")
    plt.title(artist1.name + " vs " + artist2.name)
    plt.xticks(bar1 + width/2, x)
    plt.legend()
    os.mkdir('/static/images/')
    plt.savefig('/static/images/plot.png')
    return render_template("comparisonpage.html", title = "artist1vsartist2", name1=name1, name2=name2, url='/static/images/plot.png')


if __name__ == "__main__":
    app.run()
    #x = Settings.settings()
    #print (x.get_setting("path"))

    #s = Scraper.Scraper()
    #print (s.scrape_artist("drake"))


