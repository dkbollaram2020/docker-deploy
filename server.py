from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def get_home():
    return jsonify({"message": "server works..."})

@app.route('/predict_home_price')
def predict_home_price():
    try:
        bedrooms = int(request.args.get('bedrooms'))
        bathrooms = int(request.args.get('bathrooms'))
        square_footage = int(request.args.get('square_footage'))
        resident_type = request.args.get('resident_type')
        response = jsonify({
            'estimated_price': util.get_estimated_price(resident_type, bedrooms,bathrooms,square_footage)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except:
        return jsonify({"message": "Error occurred"})


if __name__ == "__main__":
    print("Starting server...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0')
    # app.run(debug=True)
