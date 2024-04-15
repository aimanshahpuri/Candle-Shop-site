from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import requests
import gridfs
from bs4 import BeautifulSoup
from pymongo import MongoClient
uri = "mongodb+srv://test:sparta@cluster0.ramr5rz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client  = MongoClient(uri)
db = client.spartapedia

@app.route('/')
def index():
        return render_template('candle.html')

@app.route('/movie', methods=['POST'])
def movie():
        Username = request.form['name']
        Quantity = request.form['quantity']
        Number = request.form['number']
        Address = request.form['address']
        # TO ACCESS POST METHOD
        db.movies.insert_one({
                'name': Username,
                'quantity': Quantity,
                'number': Number,
                'address': Address,
        })
        return jsonify({'msg': 'Order Succesfull'})
                # TO ACCESS GET METHOD
@app.route('/movie', methods=['GET'])
def movie_get():
        movies = list(db.movies.find({}, {'_id': False}))
        return jsonify({'movies': movies})
if __name__ == '__main__':
        app.run('0.0.0.0', port=5000, debug=True)