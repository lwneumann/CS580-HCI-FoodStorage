from flask import Flask, render_template, url_for, request, redirect
import food, search
import datetime


# --- Setup ---
app = Flask(__name__)
fridge = food.Fridge()

# --- Pages ---
# Base Page
@app.route('/')
def index():
    # return render_template('main.html')
    return redirect('/storage/')

# Storage
@app.route('/storage/', methods=['GET', 'POST'])
def storage():
    global fridge

    print([ (type(f), f) for f in fridge.contents])
    return render_template('storage.html')

@app.route("/remove/<int:index>/", methods = ["POST"])
def remove_item(index):
    fridge.contents.pop(int(index))
    return redirect('/storage/')

# Add
@app.route('/add/', methods=['GET', 'POST'])
def add():
    text = request.form.get('foodInput')
    return render_template('add.html', f_search = text)

@app.route('/add/<string:addf>/<list:filters>', methods=['GET', 'POST'])
def add_food(addf, filters=[]):
    global fridge
    fridge.add(addf, filters)
    return redirect('/storage/')

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
    return dict(get_food=fridge.get_all, food_search=search.search)
