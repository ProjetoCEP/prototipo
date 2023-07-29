from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from models.Cepx import Base
import json

from services.AddressCode import AddressCode
from services.FindCoordinates import FindCoordinates
from settings import SECRET_KEY


# Initialization
app = Flask(__name__)
app_version = "0.1.0"
app.config['SECRET_KEY'] = SECRET_KEY

engine = create_engine("sqlite:///datacode.db")
Base.metadata.create_all(engine)

# Routes

## Homepage
@app.route('/', methods=['GET'])
def home():
    welcomeText = "Hello, World."
    return render_template('home.html', textFromBackend=welcomeText)

## API: Obter coordenadas geográficas a partir de endereço
@app.route('/api/find', methods=['POST'])
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

    code_result = {}
    if ((request.form.get("lat") is not None) and (request.form.get("lon") is not None)):
        code_result = code_service.generate_code(coordinate_lat=request.form.get("lat"), coordinate_lon=request.form.get("lon"), address_landmark=user_landmark)
    else:
        coordinates_response = coordinates_service.get_coordinates_from_address(address=user_address)
        if (("success" in coordinates_response) and (coordinates_response["success"] is True)):
            coordinates_dict = coordinates_response["result"]
            code_result = code_service.generate_code(coordinate_lat=coordinates_dict["lat"], coordinate_lon=coordinates_dict["lon"], address_landmark=user_landmark)
    return jsonify(code_result)

## API: Decode novo CEP
@app.route('/api/ler', methods=['POST'])
def api_decode():
    code_service = AddressCode()
    decode_result = code_service.get_data_from_code(code=request.form.get("code"))

    return jsonify(decode_result)


# Run
if __name__ == '__main__':
    app.run()
