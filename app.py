from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/wecom/event', methods=['POST'])
def handle_message():
    try:
        request_data = request.get_json()
        print(request_data)

        if not request_data:
            return jsonify({"error": "No JSON data received"}), 400
        return jsonify({
            "status": "success",
            "message": "Data received",
        }), 200
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
