# app.py
# Daniel Kogan
# 12.30.2021

# Flask Imports
from flask import Flask, escape, request, render_template, session, redirect, send_file, url_for, jsonify
from flask import Flask
# os
import os, json
from dotenv import load_dotenv
# atlas
from atlas import Blockchain
# firebase
import firebase_admin
from firebase_admin import db
firebase_admin.get_app()

#key = os.environ.get('key', 3)
app = Flask(__name__)
BLOCKCHAIN = Blockchain(db.reference('/'))

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        return "hey post request"
    return "Hello World"

@app.route('/chain', methods=['GET','POST'])
def network():
    if request.method == "POST":
        if not request.is_json:
            return 'not a json object. Please try again with request in format {\'data\': \'your block data\'}'
        json_data = request.get_json()
        BLOCKCHAIN.add_new_data(json_data['data'])
        BLOCKCHAIN.mine()
        BLOCKCHAIN.to_json()
        return BLOCKCHAIN.chain[-1].to_json()
    return BLOCKCHAIN.to_json()

if __name__ == '__main__':
    app.run(use_reloader=True,host='0.0.0.0')