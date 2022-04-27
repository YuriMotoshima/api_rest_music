from flask import Flask

app = Flask(__name__)

@app.route("/artist/<int:id_artist>", methods=['GET'])
def api_list_songs():
    return "<p>Hellow World</p>"