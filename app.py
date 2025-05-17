from flask import Flask, request, redirect, render_template, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import string
import random
from datetime import datetime

# Load .env variables
load_dotenv()

# Flask App
app = Flask(__name__)

# MongoDB Setup
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["url_db"]
collection = db["urls"]

# Base URL
BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")


# Utility to generate short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choices(characters, k=length))
        if not collection.find_one({"short_code": short_code}):
            return short_code


# Home Page (Form)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Handle URL Submission
@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('long_url')

    if not original_url:
        return render_template("index.html")

    # Check if already exists
    existing = collection.find_one({"original_url": original_url})
    if existing:
        short_code = existing["short_code"]
    else:
        short_code = generate_short_code()
        collection.insert_one({
            "original_url": original_url,
            "short_code": short_code,
            "created_at": datetime.utcnow(),
            "clicks": 0
        })

    short_url = f"{BASE_URL}/{short_code}"
    return render_template("index.html", short_url=short_url)


# Redirect Route
@app.route('/<short_code>')
def redirect_short_url(short_code):
    entry = collection.find_one({"short_code": short_code})
    if entry:
        collection.update_one(
            {"short_code": short_code},
            {"$inc": {"clicks": 1}}
        )
        return redirect(entry["original_url"])
    else:
        return "URL not found", 404


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
