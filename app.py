import os
import uuid
from dotenv import load_dotenv
from flask import Flask, request, render_template
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI, tls=True)

db = client["todo_db"]
collection = db["todo_items"]

@app.route('/')
def home():
    return render_template("todo.html")

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form['itemName']
    item_description = request.form['itemDescription']

    # Generate UUID
    item_uuid = str(uuid.uuid4())

    todo_data = {
        "itemUUID": item_uuid,
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(todo_data)

    return f"Todo item saved successfully! UUID: {item_uuid}"

if __name__ == "__main__":
    app.run(debug=True)
