from flask import Flask, render_template, url_for, request, redirect
import food


# Setup
app = Flask(__name__)
fridge = food.Fridge()
fridge.stock()

# Pages
@app.route('/')
def index():
    return render_template('main.html')

# Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('error/500.html'), 500


# Built Ins
@app.context_processor
def utility_processor():
    return dict(get_food=food.get_food)
