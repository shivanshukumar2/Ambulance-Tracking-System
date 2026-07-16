from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary location storage
ambulance_location = {
    "latitude": 0,
    "longitude": 0
}

@app.route("/")
def home():
    return "Ambulance Tracking Server Running"

@app.route("/update_location", methods=["POST"])
def update_location():
    global ambulance_location

    data = request.get_json()

    ambulance_location["latitude"] = data["latitude"]
    ambulance_location["longitude"] = data["longitude"]

    return jsonify({
        "status": "success",
        "message": "Location Updated"
    })

@app.route("/get_location")
def get_location():
    return jsonify(ambulance_location)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)