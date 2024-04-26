from flask import Flask, request
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/uploadFile", methods=["POST", "GET"])
def upload_file():
    if request.method == 'POST': 
        if "file" not in request.files:
            return {"error": "No file part"}, 400

        file = request.files["file"]

        if file.filename == "":
            return {"error": "No selected file"}, 400

        # Read the file content
        file_content = file.read()

        # Print the file content
        print("File Content:")
        print(file_content)

        return {"message": "File uploaded successfully"}, 200
    else:
        return {"hi": "hi"}

if __name__ == "__main__":
    app.run(debug=True)
