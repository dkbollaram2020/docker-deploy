from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def get_home():
    return jsonify({"message": "server works"})

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        postedData = request.get_json()
        total_sqft = float(postedData['total_sqft'])
        bhk = int(postedData['bhk'])
        bath = int(postedData['bath'])
        response = jsonify({
            'estimated_price': util.get_estimated_price(total_sqft,bhk,bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except:
        return jsonify({"message": "Error occurred"})


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0')
    # app.run(debug=True)
