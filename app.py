# app.py
from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    translator = Translator()
    translation = translator.translate(text, dest='en').text
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
