from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import requests

load_dotenv()

llm = Ollama(model='llama3')

app = Flask(__name__)
CORS(app, resources={r"/uploadFile": {"origins": "*"}})

@app.route("/uploadFile", methods=["POST", "GET"])
def upload_file():
    if request.method == "GET":
        return "Upload File API here"
    
    if "file" not in request.files:
        print("No file part in request")
        return {"error": "No file part"}, 400

    file = request.files["file"]
    if file.filename == '':
        print("No selected file")
        return {"error": "No selected file"}, 400

    try:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        extracted_text = []

        for page_number in range(num_pages):
            page_text = reader.pages[page_number].extract_text()
            extracted_text.append(page_text)

        extracted_text_combined = "\n".join(extracted_text)

        with open("Data.txt", "w") as f:
            f.write(extracted_text_combined)
        
        with open("initial.txt", "r") as f:
            initial_text = f.read()

        print('File read successfully')

        # Invoke the LLM with the initial and extracted text
        response = llm.invoke(f"{initial_text}\n{extracted_text_combined}")
        
        # Log the response for debugging
        print('LLM response:', response)

        with open("final.txt", "w") as f:
            f.write(response)

        return jsonify({
            "message": "File uploaded successfully",
            "num_pages": num_pages,
            "extracted_text": extracted_text_combined,
            "output": response
        })
    except Exception as e:
        print('Error:', str(e))
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run(debug=True)
