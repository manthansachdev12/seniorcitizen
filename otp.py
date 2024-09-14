from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Simulating OTP storage in-memory (this should ideally be in a database)
otp_storage = {}

@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.json
    aadhaar = data.get('aadhaar')

    if len(aadhaar) == 12 and aadhaar.isdigit():
        otp = str(random.randint(100000, 999999))
        otp_storage[aadhaar] = otp
        # Simulate sending OTP to the user's mobile via SMS (integration with an SMS gateway like Twilio or Msg91)
        print(f"Sending OTP {otp} to Aadhaar {aadhaar}")  # Log it for now
        return jsonify({'success': True})
    return jsonify({'success': False}), 400

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json
    otp = data.get('otp')
    aadhaar = list(otp_storage.keys())[0]  # For demo purposes, we use the first entry

    if otp_storage.get(aadhaar) == otp:
        del otp_storage[aadhaar]  # OTP should be one-time use
        return jsonify({'success': True})
    return jsonify({'success': False}), 400

if __name__ == '__main__':
    app.run(debug=True)
