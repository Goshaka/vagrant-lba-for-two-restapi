from flask import Flask
import os
import socket
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def home():

    html = "<h3>The system is up and running: {name3}!</h3>" \
           "<b>Docker 2</b> <br/>"
    return html.format(name3=os.getenv("NAME", "health-test"))

@app.route("/rest1")
def rest1():
    html = "<h3>Connecting to  {name4}!</h3>" \
           "<b>Docker 2 hostname:</b> {hostname}<br/>"
    return html.format(name4=os.getenv("NAME", "REST-API1"), hostname=socket.gethostname())

@app.route("/rest2")
def rest2():
    html = "<h3>Connecting {name5}!</h3>" \
           "<b>Docker 2:</b> {now}<br/>"
    return html.format(name5=os.getenv("NAME", "REST-API2"), now=datetime.now())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)