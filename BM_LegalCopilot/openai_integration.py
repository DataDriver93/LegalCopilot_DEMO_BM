from openai import OpenAI
from Utils.pdf_utils import extract_text_from_pdf, get_preview
from dotenv import load_dotenv
import os

# Carica le variabili d'ambiente dal file .env
load_dotenv()

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
                    {"role": "system", "content": "You are a helpful assistant who answers questions in Italian."},
                    {"role": "user", "content": f"Il testo del seguente documento è rilevante per la domanda: '{question}'? Rispondi con 'Sì' o 'No' e una breve spiegazione.\n\nDocumento:\n{full_text}"}
                ]
            )

            relevance_response = response.choices[0].message.content.strip().lower()

            if 'sì' in relevance_response or 'si' in relevance_response:
                preview = get_preview(full_text)
                relevant_documents.append((pdf_file, preview, full_text))

    return relevant_documents

def get_combined_answers(relevant_documents, question):
    client = get_openai_client()
    combined_answers = ""
    filtered_documents = []

    for pdf_file, preview, text in relevant_documents:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who answers questions in Italian."},
                {"role": "user", "content": f"Estrai i paragrafi relativi alla domanda: {question}\n\nDocumento:\n{text}\n\nRispondi in italiano e formatta la risposta in modo chiaro e organizzato, utilizzando elenchi puntati o numerati dove appropriato."}
            ]
        )

        answer = response.choices[0].message.content.strip()
        if "Non ci sono paragrafi nel documento fornito che rispondono direttamente alla tua domanda" not in answer:
            combined_answers += f"<div class='custom-answer'>{answer}</div>\n\n"
            filtered_documents.append((pdf_file, preview, text))

    return combined_answers, filtered_documents
