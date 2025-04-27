from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
from io import BytesIO

app = Flask(__name__)

def extract_pdf_form_data(pdf_file):
    reader = PdfReader(pdf_file)
    fields = reader.get_form_text_fields()
    return fields

@app.route('/extract-pdf', methods=['POST'])
def extract_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.pdf'):
        try:
            fields = extract_pdf_form_data(file)
            return jsonify(fields)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Invalid file format"}), 400

if __name__ == '__main__':
    app.run(debug=True)
