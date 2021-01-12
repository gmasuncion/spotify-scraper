from flask import Flask, render_template, redirect, url_for, request
from services import Scraper
from services import Settings



app = Flask(__name__)

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        artist1name = request.form["artist1"]
        artist2name = request.form["artist2"]
        # invoke your services..
        return redirect(url_for("comparisoninfo", artist1=artist1name, artist2=artist2name))
    else:
        return render_template("homepage.html")

@app.route("/compare/<artist1>vs<artist2>")
def comparisoninfo(artist1, artist2):
    return render_template("comparisonpage.html")



if __name__ == "__main__":
    app.run()
    #x = Settings.settings()
    #print (x.get_setting("path"))

    #s = Scraper.Scraper()
    #print (s.scrape_artist("drake"))


