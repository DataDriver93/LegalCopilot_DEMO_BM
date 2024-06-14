import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    if os.path.exists(pdf_path):
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        return full_text
    else:
        return None

def get_preview(text, num_chars=200):
    return text[:num_chars] + '...' if len(text) > num_chars else text
