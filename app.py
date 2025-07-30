from flask import Flask, jsonify
import paramiko
import os

app = Flask(__name__)

# Configuration from environment variables
HOST = os.getenv("SFTP_HOST", "gl-n8.galactichosting.net")
PORT = int(os.getenv("SFTP_PORT", 2022))
USERNAME = os.getenv("SFTP_USERNAME", "")
PASSWORD = os.getenv("SFTP_PASSWORD", "")

@app.route("/")
def home():
    return jsonify({
        "message": "SFTP Monitor is running.",
        "endpoints": ["/health"]
    }), 200

@app.route("/health")
def health_check():
    try:
        transport = paramiko.Transport((HOST, PORT))
        transport.connect(username=USERNAME, password=PASSWORD)
        transport.close()
        return jsonify({"status": "OK"}), 200
    except Exception as e:
        return jsonify({"status": "FAILED", "error": str(e)}), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
