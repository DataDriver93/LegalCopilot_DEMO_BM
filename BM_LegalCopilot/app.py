import streamlit as st
from openai_integration import get_relevant_documents, get_combined_answers
from UI.UI_components import render_input_page, render_output_page
from UI.styles import load_css

# Carica il CSS
load_css()

# Stato dell'applicazione
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Funzione per resettare lo stato
def reset_state():
    st.session_state.submitted = False

# Pagina di input iniziale
if not st.session_state.submitted:
    render_input_page()
else:
    question = st.session_state.question
    pdf_files = ["doc.pdf", "storia.pdf", "storia2.pdf"]

    with st.spinner('Processing...'):
        relevant_documents = get_relevant_documents(pdf_files, question)
        combined_answers = get_combined_answers(relevant_documents, question)

        render_output_page(question, relevant_documents, combined_answers)

        if combined_answers:
            st.text_input("Ask follow-up...", key="followup")

        st.button("Go Back", on_click=reset_state)