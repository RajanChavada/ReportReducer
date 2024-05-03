from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2
import openai  # Import OpenAIClient from openai module
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/uploadFile": {"origins": "*"}})

# Access the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Set the API key for the openai module
openai.api_key = api_key

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
        
        # Make a request to OpenAI API using the created client instance
        # Replace this with your actual OpenAI API request
        res = openai.ChatCompletion.create ( 
            model="gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
            ]
        )

        print(res)

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
