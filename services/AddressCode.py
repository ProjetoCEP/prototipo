import base64
import json
from geopy.geocoders import Nominatim
from database.NewDbCode import AcessDbForInsert

class AddressCode:
    algorithm = "base64"

    def generate_code(self, coordinate_lat, coordinate_lon, address_landmark = None, algorithm = None):
        input = []

        input.append(coordinate_lat)
        input.append(coordinate_lon)
        if address_landmark is not None:
            input.append(address_landmark)

        try:
            address_fingerprint = json.dumps(input)
            address_encoded = address_fingerprint.encode("UTF-8")

            final_code = base64.b64encode(address_encoded)
            final_code_str = final_code.decode("UTF-8")

            try:
                db_acess = AcessDbForInsert(final_code_str).InsertCode()
            except Exception as err:
                print("Ocorreu um erro ao inserir os dados na base de dados.")
                print(err)

            # @TODO: Testar decrypt, antes de retornar, para validar o resultado

            return {"success": True, "format": "string", "code": final_code_str, "algorithm": self.algorithm, "message": "Código gerado com sucesso."}

        except Exception as err:
            print(err)
            return {"success": False, "message": "Ocorreu um erro ao gerar o código. Favor contactar os desenvolvedores."}

    def get_data_from_code(self, code, algorithm = None):
        if algorithm == None:
            algorithm = self.algorithm

        try:
            data_byte = base64.b64decode(code).decode("UTF-8")
            data_dict = json.loads(data_byte)

            latitude = data_dict[0]
            longitude = data_dict[1]

            geolocator = Nominatim(user_agent="geoapiExemplo")
            location = geolocator.reverse((latitude, longitude), exactly_one=True)
            address = location.raw.get("address", {})
            cep = address.get("postcode")

            if cep:
                output = {
                    "lat": data_dict[0],
                    "lon": data_dict[1],
                    "landmark": data_dict[2] or "",
                    "cep": cep
                }
            else:
                output = {
                    "lat": data_dict[0],
                    "lon": data_dict[1],
                    "landmark": data_dict[2] or "",
                }

            return {"success": True, "result": output, "algorithm": self.algorithm, "message": "Dados retornados com sucesso."}

        except Exception as err:
            print(err)
            return {"success": False, "message": "Ocorreu um erro ao processar o código. Favor contactar os desenvolvedores."}
