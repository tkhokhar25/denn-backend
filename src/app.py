from flask import Flask, request, jsonify
from flask_cors import CORS
import registration as registration
import action_change as action_change

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/signup", methods = ['POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()

        response = registration.create_user(data["email"], data["password"])
        
        return jsonify(response)

    return 'Welcome'

@app.route("/signin", methods = ['POST'])
def signin():
    if request.method == 'POST':
        data = request.get_json()

        response = registration.check_credentials(data["email"], data["password"], data["friend_email"])

        return jsonify(response)

@app.route("/status-change", methods = ['POST'])
def status_change():
    if request.method == 'POST':
        data = request.get_json()

        action_change.update_action(data["id"], data["friend_id"], data["action"])

        return jsonify({"success" : "success"})

@app.route('/watch', methods = ['POST'])
def watch():
    if request.method == 'POST':
        data = request.get_json()
        response = action_change.trigger(data['id'], data['friend_id'])

        return jsonify(response)

if __name__ == "__main__":
    app.run()