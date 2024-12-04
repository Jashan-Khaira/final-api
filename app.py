from flask import Flask, jsonify
import socket

app = Flask(__name__)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
    try:
        return jsonify({
            'message': 'Welcome to Jashanpreet Final Test API Server',
            'status': 'healthy'
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/host')
def host_name():
    return hostname

@app.route('/ip')
def host_ip():
    return ip_address

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
