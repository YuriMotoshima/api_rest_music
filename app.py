from flask import Flask, request, jsonify
from libs.genius import run
from libs.excepts import exceptions

app = Flask(__name__)

def validation_request(request:dict) -> dict:
    """
    ### Função que valida a entrada de dados.
    """
    try:
        if 'artista' in request.keys() and request["artista"] != None:
            data = {"status":True, "artista": request["artista"], "cache": request['cache'] if 'cache' in request.keys() else True}
            return data
        else:
            data = {"status":False}
            return data
    except Exception as e:
        raise exceptions(e)

@app.route("/artist", methods=['GET'])
def api_list_songs():
    data = request.get_json()
    valid_data = validation_request(request=data)
    response = {"status_code":400, "message":"Bad Request"}
    
    if valid_data['status']:
        response = run(artist=valid_data["artista"], cache_res=valid_data["cache"])
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port="1914", host="0.0.0.0")