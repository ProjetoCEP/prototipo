from flask import Flask, jsonify, render_template, request
import json

from services.FindCoordinates import FindCoordinates
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

## API: Obter coordenadas geográficas a partir de endereço
@app.route('/api/find', methods=['GET'])
def api_find():
    coordinates_service = FindCoordinates()
    address = request.form.get("address")

    return jsonify(
        coordinates_service.get_coordinates_from_address(address=address)
    )

# Run

## Start the Externally Visible Server, with Debug mode enabled
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
