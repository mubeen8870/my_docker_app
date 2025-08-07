
# Docker is an open-source platform that allows developers to
# build, package, and run applications in
# lightweight, portable containers, which include everything the software needs-cod



from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return {"message": "Hello World"}

@app.route("/data", methods=["GET"])
def get_data():
    # Example: Read a file from data folder
    file_path = os.path.join("data", "sample.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        return jsonify({"file_content": content})
    else:
        return jsonify({"error": "File not found"}), 404
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)    