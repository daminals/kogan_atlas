# app.py
# Daniel Kogan
# 12.30.2021

# Flask Imports
from flask import Flask, escape, request, render_template, session, redirect, send_file, url_for
from flask import Flask
# os
import os
from dotenv import load_dotenv

#key = os.environ.get('key', 3)
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        return "hey post request"
    return "Hello World"

@app.route('/chain', methods=['GET','POST'])
def network():
    pass


if __name__ == '__main__':
    app.run(use_reloader=True,host='0.0.0.0')