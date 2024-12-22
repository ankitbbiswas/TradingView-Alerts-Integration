Content:
markdown
Copy code
# TradingView Alerts Integration

This repository demonstrates how to create a simple **Moving Average Crossover strategy** in TradingView using Pine Script, send alerts (Buy/Sell signals), and optionally process them using a Python server.

---

## Features

1. **Moving Average Crossover Strategy**:
   - Alerts generated for Buy/Sell signals based on fast and slow moving averages.
   - Sends structured alert messages for integration with external systems.

2. **Python Webhook Server**:
   - A Flask-based server to receive TradingView alerts via webhooks or email forwarding.
   - Handles and logs the alert data for further processing.

---

## Repository Structure

- **`pine-script/`**:
  Contains the Pine Script for Moving Average Crossover alerts.
  
- **`python-server/`**:
  Contains the Python Flask server to receive alerts.

---

## Instructions

### 1. Using the Pine Script
1. Open TradingView and apply the script from `pine-script/moving_average_alert.pine` to your chart.
2. Set up alerts for the strategy:
   - Select conditions (`Buy Signal Alert` or `Sell Signal Alert`).
   - Include structured JSON in the alert message.
3. Use email alerts if you do not have a Premium subscription for webhooks.

### 2. Setting Up the Python Server
1. Navigate to the `python-server` directory:
   ```bash
   cd python-server
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run the server:
bash
Copy code
python webhook_server.py
The server will listen on http://127.0.0.1:5000/receive-alert.

3. Testing the Integration
Use a tool like Postman or curl to send test alerts to the Python server
curl -X POST http://127.0.0.1:5000/receive-alert \
-H "Content-Type: application/json" \
-d '{"symbol": "AAPL", "price": 150.25, "time": "2024-12-22T10:30:00Z"}'
