from flask import Flask, request, jsonify
import PyPDF2
import io

app = Flask(__name__)

@app.route('/extract-pdf-fields', methods=['POST'])
def extract_pdf_fields():
    pdf_file = request.files['file']
    reader = PyPDF2.PdfReader(pdf_file)
    fields = reader.get_form_text_fields()
    return jsonify(fields)

if __name__ == '__main__':
    app.run()
