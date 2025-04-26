import io
import os
from app import app

def test_extract_pdf_fields():
    # Initialize Flask test client
    client = app.test_client()

    # Load a sample PDF file that contains form fields
    pdf_path = "sample_form.pdf"
    assert os.path.exists(pdf_path), "Test PDF file not found"

    with open(pdf_path, "rb") as f:
        data = {
            'file': (f, 'sample_form.pdf')
        }
        response = client.post('/extract-pdf-fields', content_type='multipart/form-data', data=data)

    assert response.status_code == 200
    assert isinstance(response.json, dict)
    print("Extracted form fields:", response.json)
