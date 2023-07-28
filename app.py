from flask import Flask, jsonify, render_template, request
import json

from services.AddressHash import AddressHash
from services.FindCoordinates import FindCoordinates
from settings import SECRET_KEY


# Initialization
app = Flask(__name__)
app_version = "0.1.0"
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

## API: Gerar novo CEP
@app.route('/api/gerar', methods=['GET'])
def api_gerar():
    coordinates_service = FindCoordinates()
    hash_service = AddressHash()

    user_address = request.form.get("address")
    user_landmark = request.form.get("landmark")
    coordinates_response = coordinates_service.get_coordinates_from_address(address=user_address)

    hash_result = {}
    if (("success" in coordinates_response) and (coordinates_response["success"] is True)):
        coordinates_dict = coordinates_response["result"]
        hash_result = hash_service.generate_hash(coordinate_lat=coordinates_dict["lat"], coordinate_lon=coordinates_dict["lon"], address_landmark=user_landmark, export_binary=False)

    return jsonify(hash_result)


# Run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
