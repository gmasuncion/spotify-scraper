from flask import Flask, render_template, redirect, url_for, request
from flask.helpers import send_file
from services import Scraper
from services import Settings
from services import GraphService
import matplotlib.pyplot 

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        artist1name = request.form["artist1"]
        artist2name = request.form["artist2"]
        return redirect(url_for("comparisoninfo", name1=artist1name, name2=artist2name))
    else:
        return render_template("homepage.html")

@app.route("/compare/<name1>vs<name2>")
def comparisoninfo(name1, name2):
    return render_template("comparisonpage.html", title = "artist1vsartist2", name1=name1, name2=name2)

@app.route("/fig/<name1>vs<name2>")
def graph(name1,name2):
    matplotlib.pyplot.switch_backend('Agg')
    finder = Scraper.Scraper()
    artist1 = finder.scrape_artist(name1)
    artist2 = finder.scrape_artist(name2)
    gs = GraphService.GraphService(artist1, artist2)
    graph = gs.createPlot()
    img = StringIO()
    graph.saveFig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


if __name__ == "__main__":
    app.run()
    #x = Settings.settings()
    #print (x.get_setting("path"))

    #s = Scraper.Scraper()
    #print (s.scrape_artist("drake"))


