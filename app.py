from flask import Flask, jsonify, render_template, request
import json

from services.AddressCode import AddressCode
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
@app.route('/api/gerar', methods=['POST'])
def api_gerar():
    coordinates_service = FindCoordinates()
    code_service = AddressCode()

    user_address = request.form.get("address") if ("address" in request.form) else ""
    user_landmark = request.form.get("landmark") if ("landmark" in request.form) else ""

    coordinates_response = coordinates_service.get_coordinates_from_address(address=user_address)

    code_result = {}
    if (("success" in coordinates_response) and (coordinates_response["success"] is True)):
        coordinates_dict = coordinates_response["result"]
        code_result = code_service.generate_code(coordinate_lat=coordinates_dict["lat"], coordinate_lon=coordinates_dict["lon"], address_landmark=user_landmark)

    return jsonify(code_result)

## API: Decrypt novo CEP
@app.route('/api/decrypt', methods=['POST'])
def api_decrypt():
    code_service = AddressCode()
    decrypt_result = code_service.decrypt_code(code=request.form.get("code"))

    return jsonify(decrypt_result)


# Run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
