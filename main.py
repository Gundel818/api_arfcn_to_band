from flask import Flask, jsonify, request

app = Flask(__name__)

arfcn_to_band = {
    range(0, 600): {
        "band_freq" : "2100",
        "band" : "B1",
    },
    range(1200, 1950): {
        "band_freq" : "1800",
        "band" : "B3",
    },
    range(617, 1280): {
        "band_freq" : "2600",
        "band" : "B7",
    },
    range(600, 800): {
        "band_freq" : "800",
        "band" : "B20",
    },
    range(9210, 9659) : {
        "band_freq" : "700",
        "band" : "B28",
    },
    range(3450, 3799) : {
        "band_freq" : "900", 
        "band" : "B8",
    }

}

def get_band(arfcn):
    for band_range, band_name in arfcn_to_band.items():
        if arfcn in band_range:
            return band_name
    return None

@app.route('/convert', methods=['GET'])
def convert_arfcn():
    arfcn = request.args.get('arfcn', type=int)
    if arfcn is None:
        return jsonify({"error": "ARFCN argument required"}), 400
    
    band_dict = get_band(arfcn)
    if band_dict is None:
        return jsonify({"arfcn": arfcn, "error": "Band not found"}), 404
    return jsonify({"arfcn": arfcn, "band": band_dict["band_freq"], "band_name" : band_dict["band"]})


@app.route("/")
def main_route():
    return "<h1> Get info (LTE band frequency and LTE band name) from LTE ARFCN </h1>"

if __name__ == '__main__':
    #### DEV
    app.run(debug=True)
    ### PROD
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)