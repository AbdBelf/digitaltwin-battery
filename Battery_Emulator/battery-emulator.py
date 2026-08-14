from flask import Flask, jsonify
from datetime import datetime, timezone
import random

app = Flask(__name__)

# ==========================================
# Battery State
# ==========================================

battery = {
    "batteryId": "battery-001",
    "soc": 100.0,           # State of Charge (%)
    "temperature": 25.0     # °C
}


def simulate_battery():
    """
    Simulate a realistic Lithium-Ion battery behavior.
    """

    # Simulate discharge
    battery["soc"] -= random.uniform(0.05, 0.20)

    # Automatically recharge when nearly empty
    if battery["soc"] <= 5:
        battery["soc"] = 100.0

    soc = battery["soc"]

    # Approximate Li-Ion voltage curve
    # 100% SOC -> ~4.2V
    # 0% SOC   -> ~3.0V
    voltage = 3.0 + (soc / 100) * 1.2

    # Add measurement noise
    voltage += random.uniform(-0.02, 0.02)

    # Simulated current consumption
    current = random.uniform(0.5, 2.0)

    # Temperature evolution
    target_temperature = 22 + current * 5

    battery["temperature"] += (
        target_temperature - battery["temperature"]
    ) * 0.1

    battery["temperature"] += random.uniform(-0.2, 0.2)

    return {
        "batteryId": battery["batteryId"],
        "Voltage_measured": round(voltage, 3),
        "Current_measured": round(current, 3),
        "Temperature_measured": round(
            battery["temperature"], 2
        ),
        "StateOfCharge": round(soc, 1),
        "Time": datetime.now(
            timezone.utc
        ).isoformat()
    }


@app.route("/battery", methods=["GET"])
def get_battery():
    return jsonify(simulate_battery())


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Battery Simulator",
        "endpoint": "/battery"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )