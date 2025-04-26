from flask import Flask, request, jsonify
import io
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/extract_pdf_form', methods=['POST'])
def extract_pdf_form():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    pdf_bytes = file.read()

    reader = PdfReader(io.BytesIO(pdf_bytes))
    fields = {}

    if reader.get_fields():
        for field_name, field_info in reader.get_fields().items():
            fields[field_name] = field_info.get('/V', '')

    return jsonify(fields)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)  # Listen on port 8000 for Azure

