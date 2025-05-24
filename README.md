# Personal Diary Flask Application

This project is a simple web-based personal diary built with Flask and MongoDB. It allows users to create, view, and manage diary entries, with optional file and profile image uploads. This project is part of the MSIB LearningX Full Stack Web Development program.

## Features

- Create diary entries with a title and content
- Optional file upload for each entry
- Optional profile image upload for each entry
- View all diary entries in a list
- Data stored in MongoDB

## Technologies Used

- Python 3
- Flask
- MongoDB
- HTML/CSS (Jinja2 templates)
- dotenv (for environment variable management)

## Project Structure

```
app.py                # Main Flask application
requirements.txt      # Python dependencies
start.sh              # Shell script to start the app
static/               # Static files (uploaded files, images)
templates/
  index.html          # Main HTML template
```

## Getting Started

### Prerequisites

- Python 3.x
- pip
- MongoDB (local or cloud instance)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/MuhammadAlifBudiman/personal-diary.git
   cd personal-diary
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with the following content:
   ```env
   MONGODB_URI=<your-mongodb-uri>
   DB_NAME=<your-database-name>
   ```
4. Start the Flask app:
   ```bash
   python app.py
   # or
   ./start.sh
   ```
5. Open your browser and go to `http://localhost:5000`

## Usage

- The homepage allows you to create new diary entries and view existing ones.
- Uploaded files and profile images are saved in the `static/` directory.

## License

This project is for educational purposes as part of the MSIB LearningX Full Stack Web Development program.

## Acknowledgments

- MSIB LearningX
- Flask and MongoDB documentation
