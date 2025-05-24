"""
app.py - Personal Diary Flask Application

This application provides a simple web-based personal diary using Flask and MongoDB.
It allows users to create diary entries with optional file and profile image uploads.
"""

# Import necessary modules
from fileinput import filename
# Flask web framework and utilities
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient  # MongoDB client
from datetime import datetime  # For handling date and time
import os  # For environment variables and file operations
from os.path import join, dirname  # For file path operations
from dotenv import load_dotenv  # For loading environment variables from .env file

# Load environment variables from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Retrieve MongoDB connection URI and database name from environment variables
MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

# Initialize Flask application
app = Flask(__name__)

# Home route: renders the main page


@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

# GET /diary: Returns all diary entries as JSON


@app.route('/diary', methods=['GET'])
def show_diary():
    """Return all diary entries as JSON."""
    articles = list(db.diary.find({}, {'_id': False}))
    return jsonify({'articles': articles})

# POST /diary: Saves a new diary entry


@app.route('/diary', methods=['POST'])
def save_diary():
    """
    Save a new diary entry with optional file and profile image uploads.
    Expects form data: title_give, content_give, file_give (optional), profile_give (optional).
    """
    title_receive = request.form['title_give']  # Diary title
    content_receive = request.form['content_give']   # Diary content
    filename = ''  # Uploaded file name (if any)
    profile_name = ''  # Uploaded profile image name (if any)
    today = datetime.now()  # Current datetime
    # Timestamp for unique filenames
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    # Handle file upload if present
    if ('file_give' in request.files):
        file_receive = request.files['file_give']
        extension = file_receive.filename.split('.')[-1]
        filename = f'file-{mytime}.{extension}'
        file_receive.save(f'static/{filename}')
        print(filename)

    # Handle profile image upload if present
    if ('profile_give' in request.files):
        profile_receive = request.files['profile_give']
        profile_extension = profile_receive.filename.split('.')[-1]
        profile_name = f'profile-{mytime}.{profile_extension}'
        profile_receive.save(f'static/{profile_name}')

    # Format date for diary entry
    time = today.strftime('%Y.%m.%d')

    # Create diary document
    doc = {
        'file': filename,
        'profile': profile_name,
        'title': title_receive,
        'content': content_receive,
        'time': time
    }
    db.diary.insert_one(doc)  # Insert into MongoDB
    return jsonify({'msg': 'Data was saved'})


# Run the Flask app
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
