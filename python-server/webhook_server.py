from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive-alert', methods=['POST'])
def receive_alert():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON payload"}), 400
    
    print("Received alert:", data)

    # Process the alert (Example: Log data)
    if "symbol" in data and "price" in data:
        symbol = data["symbol"]
        price = data["price"]
        print(f"Symbol: {symbol}, Price: {price}")
    
    return jsonify({"message": "Alert received"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
