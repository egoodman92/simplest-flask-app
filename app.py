from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World--from Easy-fi! Stop managing your finances like an animal"
