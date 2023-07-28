import json


class AddressHash:
    algorithm = "sha256"

    def generate_hash(self, coordinate_lat, coordinate_lon, address_landmark = None, export_binary = False):
        input = []

        input.append(coordinate_lat)
        input.append(coordinate_lon)
        if address_landmark is not None:
            input.append(address_landmark)

        try:
            address_fingerprint = json.dumps(input)
            address_encoded = address_fingerprint.encode("UTF-8")

            # @TODO: Adiciona algoritmo para encriptar dados
            final_hash = "9dc70305c61d4e7cb485fa6634cb195e"
            final_hash_b = ""
            final_hash_hex = "9dc70305c61d4e7cb485fa6634cb195e"

            # @TODO: Testar decrypt, antes de retornar, para validar o resultado

            if export_binary:
                return {"sucess": True, "format": "binary", "hash": final_hash_b, "algorithm": self.algorithm, "message": "Hash gerado com sucesso."}
            else:
                return {"sucess": True, "format": "hex", "hash": final_hash_hex, "algorithm": self.algorithm, "message": "Hash gerado com sucesso."}

        except Exception as err:
            print(err)
            return {"success": False, "message": "Ocorreu um erro ao gerar o hash. Favor contactar os desenvolvedores."}

    def decrypt_hash(self, hash, algorithm):
        pass
