# app.py
from flask import Flask, render_template

app = Flask(__name__)


# Home Route
@app.route('/')
def home():
    data = "hi"
    return render_template('index.html')

# About Route
@app.route('/about')
def about():
    
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)