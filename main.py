from flask import Flask, jsonify, request

from arfcn_tab import arfcn_to_band

app = Flask(__name__)

def get_band(arfcn):
    for band_range, band_info_dict in arfcn_to_band.items():
        if arfcn in band_range:
            return band_info_dict
    return None

@app.route('/convert', methods=['GET'])
def convert_arfcn():
    arfcn = request.args.get('arfcn', type=int)
    if arfcn is None:
        return jsonify({"error": "ARFCN argument required"}), 400
    
    band_info_dict = get_band(arfcn)
    if band_info_dict is None:
        return jsonify({"arfcn": arfcn, "error": "Band not found"}), 404
    return jsonify({"arfcn": arfcn, "band_freq": band_info_dict["band_freq"], "band_name" : band_info_dict["band"]})


@app.route("/")
def main_route():
    return "<h1> Get info (LTE band frequency and LTE band name) from LTE ARFCN </h1>"

if __name__ == '__main__':
    #### DEV
    app.run(debug=True)
    ### PROD
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5123)