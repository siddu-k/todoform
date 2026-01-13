import os
from dotenv import load_dotenv
from flask import Flask, request, render_template
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")


client = MongoClient(MONGO_URI, tls=True)

db = client["signup_db"]
collection = db["users"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']

    password = request.form['password']


    user_data = {
        "username": username,
    
        "password": password
    }

    collection.insert_one(user_data)

    return "Signup successful! ."

if __name__ == "__main__":
    app.run(debug=True)
