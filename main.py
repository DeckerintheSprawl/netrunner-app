import subprocess
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows your React UI to talk to Termux

# Your signature key
SECRET_TOKEN = "AKIRA_OMEGA_99"

@app.route('/api/shell', methods=['POST'])
def execute_command():
    # Security handshake
    client_token = request.headers.get('Authorization')
    if client_token != SECRET_TOKEN:
        return jsonify({"error": "Unauthorized Access"}), 403

    data = request.json
    command = data.get('command', '')

    try:
        # The heart of the machine: Execute real commands
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=30
        )
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "code": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("\n[!] NETRUNNER CORE: INITIALIZING...")
    print(f"[+] ENGINE: Python {sys.version.split()[0]}")
    print("[+] LINK: Listening on Port 5000")
    print("[!] SYSTEM STABLE - AWAITING DECK CONNECTION\n")
    app.run(host='0.0.0.0', port=5000)
