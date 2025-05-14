from flask import Flask, request, jsonify
import json
import os
from phone_prediction import predictPhone

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict_phone_api():
    age_str = request.args.get('age')
    wealth_str = request.args.get('wealth')

    if age_str is None or wealth_str is None:
        return jsonify({"error": "Fehlende Parameter: 'age' und 'wealth' sind erforderlich."}), 400

    try:
        age = int(age_str)
        wealth = int(wealth_str)

        if age not in [0, 1] or wealth not in [0, 1]:
             return jsonify({"error": "Ungueltige Werte: 'age' und 'wealth' muessen 0 oder 1 sein."}), 400

    except ValueError:
        return jsonify({"error": "Ungueltiger Typ: 'age' und 'wealth' muessen ganze Zahlen sein."}), 400

    predicted_phone = predictPhone(age, wealth)
   
    return jsonify({
        "input_age": age,
        "input_wealth": wealth,
        "predicted_phone": predicted_phone
    })

if __name__ == '__main__':
    print("Starte Flask API...")
    app.run()