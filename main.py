from flask import Flask, render_template, redirect, url_for, request
from flask.helpers import send_file
from services import Scraper
from services import Settings
from services import GraphService



app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        artist1name = request.form["artist1"]
        artist2name = request.form["artist2"]
        return redirect(url_for("comparisoninfo", artist1=artist1name, artist2=artist2name))
    else:
        return render_template("homepage.html")

@app.route("/compare/<artist1>vs<artist2>")
def comparisoninfo(artist1, artist2):
    return render_template("comparisonpage.html", title = "artist1vsartist2")

@app.route("/fig/<artist1>vs<artist2>")
def graph(artist1, artist2):
    gs = GraphService(artist1, artist2)
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


