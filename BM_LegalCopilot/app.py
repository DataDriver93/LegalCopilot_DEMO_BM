import streamlit as st
from openai_integration import get_relevant_documents, get_combined_answers
from UI.UI_components import render_input_page, render_output_page
from UI.styles import load_css
import os

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
    pdf_files = ["Docs/202401_Specifiche tecniche_gestionale.pdf", "Docs/202402_Contratto_987645.pdf", "Docs/Determina_N_ 202402.pdf", "Docs/Determina_N_ 202405.pdf", "Docs/Determina_N_202403.pdf"]
    with st.spinner('Processing...'):
        relevant_documents = get_relevant_documents(pdf_files, question)
        combined_answers, filtered_documents = get_combined_answers(relevant_documents, question)

        render_output_page(question, filtered_documents, combined_answers)

        if combined_answers:
            st.text_input("Ask follow-up...", key="followup")

        st.button("Go Back", on_click=reset_state)
