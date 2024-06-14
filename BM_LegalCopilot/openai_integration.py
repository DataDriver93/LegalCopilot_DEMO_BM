from openai import OpenAI
import os
from Utils.pdf_utils import extract_text_from_pdf, get_preview
from dotenv import load_dotenv

def get_openai_client():
    api_key = os.getenv('OPEN_AI_KEY')
    if not api_key:
        raise ValueError("La chiave API di OpenAI non è stata trovata. Assicurati di aver configurato la variabile d'ambiente correttamente.")
    return OpenAI(api_key=api_key)

def get_relevant_documents(pdf_files, question):
    client = get_openai_client()
    relevant_documents = []

    for pdf_file in pdf_files:
        full_text = extract_text_from_pdf(pdf_file)
        if full_text:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Is the following document text relevant to the question: '{question}'? Respond with 'Yes' or 'No' and a brief explanation.\n\nDocument:\n{full_text}"}
                ]
            )

            relevance_response = response.choices[0].message.content.strip().lower()

            if 'yes' in relevance_response:
                preview = get_preview(full_text)
                relevant_documents.append((pdf_file, preview, full_text))

    return relevant_documents

def get_combined_answers(relevant_documents, question):
    client = get_openai_client()
    combined_answers = ""

    for pdf_file, _, text in relevant_documents:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Extract the paragraphs related to the question: {question}\n\nDocument:\n{text}"}
            ]
        )

        answer = response.choices[0].message.content.strip()
        combined_answers += f"<div class='custom-answer'>{answer}</div>\n\n"

    return combined_answers
