from website import app
from flask import render_template


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/en')
def english():
    return render_template('home_en.html')
