from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # 🔥 LIBERA ACESSO DO FRONT

@app.route("/clima")
def clima():
    lat = -12.6975
    lon = -38.3242

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    res = requests.get(url)
    data = res.json()

    return jsonify(data["current_weather"])

if __name__ == "__main__":
    app.run(debug=True)