import json
import requests
import urllib.parse


class FindCoordinates:
    maps_api_url = "https://nominatim.openstreetmap.org/search.php?q="

    def get_coordinates_from_address(self, address):
        try:
            address = address.replace(",", "")

            url = self.maps_api_url + urllib.parse.quote_plus(address) + "&format=jsonv2&limit=1"
            req = requests.get(url, timeout=30)

            if req.status_code == 200:
                return {"success": True, "result": {
                    "address": address,
                    "lat": req.json()[0]["lat"],
                    "lon": req.json()[0]["lon"],
                    }, "message": "Pesquisa realizada com sucesso."}
            else:
                return {"success": False, "result": None, "message": "Ocorreu um erro ao processar a requisição. Tente novamente."}

        except Exception as err:
            print(err)
            return {"success": False, "message": "Ocorreu um erro ao conectar à API. Favor contactar os desenvolvedores."}
