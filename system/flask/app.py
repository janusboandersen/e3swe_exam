from flask import Flask

app = Flask(__name__)

@app.route("/")
def e3swe():
    return "Hej Anders og E3SWE!"