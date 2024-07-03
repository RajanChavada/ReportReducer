from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/uploadFile": {"origins": "*"}})



@app.route("/uploadFile", methods=["POST", "GET"])
def upload_file():
    if request.method == "GET":
        return "Upload File API"
    
    if "file" not in request.files:
        return {"error": "No file part"}, 400

    file = request.files["file"]
    try:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        extracted_text = []

        # Iterate over each page and extract its text
        for page_number in range(num_pages):
            page_text = reader.pages[page_number].extract_text()
            extracted_text.append(page_text)

        # Write extracted text to a file 
        with open("Data.txt", "w") as f:
            for text in extracted_text:
                f.write(text + "\n")
        

        
        return jsonify({
            "message": "File uploaded successfully",
            "num_pages": num_pages,
            "extracted_text": extracted_text,

        })
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run(debug=True)
