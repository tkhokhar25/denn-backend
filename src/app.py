from flask import Flask, request, jsonify
import registration as registration

app = Flask(__name__)

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

        response = registration.check_credentials(data["email"], data["password"])

        return jsonify(response)

if __name__ == "__main__":
    app.run()