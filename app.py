import webbrowser
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
    #return render_template('main.html')
    return redirect('/storage/')

# Storage
@app.route('/storage/', methods=['GET', 'POST'])
def storage():
    global fridge
    text = request.form.get('foodInput')
    return render_template('storage.html', f_search = text)

@app.route('/storage/<string:addf>/', methods=['GET', 'POST'])
def add_food(addf):
    global fridge
    fridge.add(addf)
    return redirect('/storage/')

@app.route("/remove/<int:index>/", methods = ["POST"])
def remove_item(index):
    fridge.contents[index] = None
    fridge.save()
    return redirect('/storage/')

@app.route('/user_guide/')
def user_guide():
    return render_template('userguide.html')

@app.route('/delete_all/', methods=['POST'])
def delete_all():
    fridge.purge()
    return redirect('/storage/')

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
    return dict(get_food=fridge.get_all,
                food_search=search.search,
                food_counts=fridge.count_food(),
                delete_all=fridge.purge,
                none=None)
