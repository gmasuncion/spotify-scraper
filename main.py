from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    print ("hello")



if __name__ == "__main__":
    app.run()
