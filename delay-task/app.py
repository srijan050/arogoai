from flask import Flask, request, jsonify
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

app = Flask(__name__)

mp = {"Traffic Conditions" : {'Heavy' : 0, 'Light' : 1, 'Moderate' : 2},
    "Weather Conditions" : {'Rain' : 2, 'Storm' : 3, 'Clear' : 0, 'Fog' : 1}}

rf_model = joblib.load('rf_model.pkl')
xgb_model = joblib.load('xgb_model.pkl')
nn_model = load_model('nn_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = ['Weather Conditions', 'Traffic Conditions']
        for field in features:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
        input_data = pd.DataFrame([{field: mp[field][data[field]] for field in features}])

        rf_prediction = rf_model.predict(input_data)[0]
        xgb_prediction = xgb_model.predict(input_data)[0]
        nn_prediction = (nn_model.predict(input_data)[0][0] > 0.5).astype(int)

        response = {
            'RandomForest': 'Delayed' if rf_prediction == 1 else 'On Time',
            'XGBoost': 'Delayed' if xgb_prediction == 1 else 'On Time',
            'NeuralNetwork': 'Delayed' if nn_prediction == 1 else 'On Time'
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
