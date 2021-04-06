import flask
import jne
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    query = request.args
    resi = query['no_resi']
    info_resi = jne.cek_resi(resi)
    return jsonify(info_resi)


app.run()
