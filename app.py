from flask import Flask, jsonify
import socket

app = Flask(__name__)

HOST = "gl-n8.galactichosting.net"
PORT = 2022

def is_port_open(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            return True
    except Exception:
        return False

@app.route("/")
def health_check():
    status = "ONLINE" if is_port_open(HOST, PORT) else "OFFLINE"
    return jsonify({
        "host": HOST,
        "port": PORT,
        "protocol": "SFTP",
        "status": status
    }), 200 if status == "ONLINE" else 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
