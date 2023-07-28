from flask import Flask, render_template
import json

from settings import SECRET_KEY


# Initialization

## Set Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Routes

## Homepage
@app.route('/', methods=['GET'])
def home():
    welcomeText = "Hello, World."
    return render_template('home.html', textFromBackend=welcomeText)


# Run

## Start the Externally Visible Server, with Debug mode enabled
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
