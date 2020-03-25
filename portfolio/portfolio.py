from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    pics = os.listdir('static/img/kotoslaw_mrasny/')
    return render_template('index.html', name='Kotoslaw Mrasny', pics=pics)

@app.route("/about")
def about():
    return render_template('about.html', title='About', name='Kotoslaw Mrasny')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact', name='Kotoslaw Mrasny')

if __name__ == "__main__":
    app.run(debug==True)
