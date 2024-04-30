from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import PyPDF2

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/uploadFile", methods=["POST"])
def upload_file():
   
    if "file" not in request.files:
        return {"error": "No file part"}, 400

    file = request.files["file"]

    try:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        # Initialize an empty list to store extracted text from each page
        extracted_text = []
        
        # Iterate over each page and extract its text
        for page_number in range(num_pages):
            page_text = reader.pages[page_number].extract_text()
            extracted_text.append(page_text)
       
        # write to the file 
        try: 
            with open("Data.txt", "w") as f:
                for text in extracted_text:
                    f.write(text + "\n")  # Write each page's text to the file, separated by a newline
        except: 
            print("Failed to write to file")
        

        return jsonify({"message": "File uploaded successfully", "num_pages": num_pages, "extracted_text": extracted_text})
    except PyPDF2.PdfReadError:
        return {"error": "Invalid PDF file"}, 400

if __name__ == "__main__":
    app.run(debug=True)