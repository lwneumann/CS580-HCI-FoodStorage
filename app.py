from flask import Flask, render_template, url_for, request, redirect
import food


# --- Setup ---
app = Flask(__name__)
fridge = food.Fridge()
fridge.stock()

# --- Pages ---
# Base Page
@app.route('/')
def index():
    return render_template('main.html')

# Example Page
@app.route('/example/')
def expample_page():
    f = [
        ["Banana", "Like 3 days idk", "11/3", "11/6"],
        ["Meat Paste", "4 months", "10/3", "2/3/25"],
        ["Yogurt", "1 week", "11/5", "11/12"]
    ]
    return render_template('example.html', food = f)


# --- Errors ---
# Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

# Server Error (bad code)
@app.errorhandler(500)
def internal_error(e):
    return render_template('error/500.html'), 500


# --- Built Ins ---
# Functions accessible within the html pages
@app.context_processor
def utility_processor():
    global fridge
    return dict(get_food=fridge.get_all)
