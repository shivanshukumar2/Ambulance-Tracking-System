from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary location storage
ambulance_location = {
    "latitude": 28.6139,
    "longitude": 77.2090,
    "speed": 0,
    "status": "Offline"
}

# Home Page (Map)
@app.route("/")
def home():
    return render_template("index.html")


# Update Ambulance Location
@app.route("/update_location", methods=["POST"])
def update_location():
    global ambulance_location

    data = request.get_json()

    ambulance_location["latitude"] = data.get("latitude", ambulance_location["latitude"])
    ambulance_location["longitude"] = data.get("longitude", ambulance_location["longitude"])
    ambulance_location["speed"] = data.get("speed", 0)
    ambulance_location["status"] = "Online"

    return jsonify({
        "success": True,
        "message": "Location Updated Successfully",
        "data": ambulance_location
    })


# Get Current Location
@app.route("/get_location", methods=["GET"])
def get_location():
    return jsonify(ambulance_location)


# Server Status
@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "server": "Running",
        "ambulance_status": ambulance_location["status"]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)