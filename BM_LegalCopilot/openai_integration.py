from openai import OpenAI
from Utils.pdf_utils import extract_text_from_pdf, get_preview
from dotenv import load_dotenv
import os

# Carica le variabili d'ambiente dal file .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def get_relevant_documents(pdf_files, question):
    relevant_documents = []

    for pdf_file in pdf_files:
        full_text = extract_text_from_pdf(pdf_file)
        if full_text:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": 
                     "Sei un assistente virtuale con l'obiettivo di supportare l'utente nel trovare documenti strettamente pertinenti e direttamente correlati ad un dato input.\n"
                     "La tua valutazione deve basarsi su criteri specifici di pertinenza e correlazione diretta tra il contenuto del documento e l'input fornito dall'utente.\n"
                     "Considera solo i documenti che trattano esattamente lo stesso argomento della domanda, fornendo informazioni rilevanti e utili per rispondere alla domanda posta.\n"
                     "Ignora i documenti che, pur essendo superficialmente correlati all'argomento, non sono strettamente pertinenti e direttamente correlati alla richiesta dell'utente.\n"
                     "Usa il seguente formato: '12345-breve spiegazione' se la risposta è 'Sì' e '67890-breve spiegazione' se la risposta è 'No'.\n\n"},
                    {"role": "user", "content": f"Il testo del seguente documento è rilevante, inerente e tratta dello stesso argomento di: '{question}'? Rispondi con '12345' per 'Sì' o '67890' per 'No' e una breve spiegazione.\n\nDocumento:\n{full_text}"}
                ]
            )

            relevance_response = response.choices[0].message.content.strip().lower()
            print(relevance_response)

            if '12345' in relevance_response:
                preview = get_preview(full_text)
                relevant_documents.append((pdf_file, preview, full_text))
    return relevant_documents

def get_combined_answers(relevant_documents, question):
    combined_answers = ""
    filtered_documents = []

    for pdf_file, preview, text in relevant_documents:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who answers questions in Italian."},
                {"role": "user", "content": f"Estrai i paragrafi relativi alla domanda: {question}\n\nDocumento:\n{text}\n\nRispondi in italiano e formatta la risposta in modo chiaro e organizzato, utilizzando elenchi puntati o numerati dove appropriato."}
            ]
        )

        answer = response.choices[0].message.content.strip()
        # Filtra risposte non pertinenti
        if not any(phrase in answer for phrase in ["Non ci sono paragrafi nel documento fornito che rispondono direttamente alla tua domanda", "Mi dispiace, ma non sono in grado di trovare i paragrafi relativi alla tua domanda nel documento fornito"]):
            # Aggiungi il nome del documento formattato alla risposta
            document_info = f"<div style='font-size: small; font-style: italic; color: #ABCDEF	;'>{pdf_file}</div>"
            combined_answers += f"{document_info}<div class='custom-answer'>{answer}</div>\n\n"
            filtered_documents.append((pdf_file, preview, text))

    return combined_answers, filtered_documents