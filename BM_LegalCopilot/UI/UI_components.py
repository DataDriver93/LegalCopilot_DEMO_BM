import streamlit as st
import urllib.parse

def render_input_page():
    st.title(":grey_question: Docs Copilot, for legal")

    question = st.text_input("Ask anything...")

    if st.button("Submit"):
        st.session_state.submitted = True
        st.session_state.question = question

def render_output_page(question, relevant_documents, combined_answers):
    if relevant_documents:
        sources = [f"<div class='custom-source'><div class='source-title'>{pdf_file}</div><div class='source-preview'>{preview}</div></div>" for pdf_file, preview, _ in relevant_documents]
        st.markdown(f"<div class='user-question'>{question}</div>", unsafe_allow_html=True)
        st.markdown("<div class='custom-title'>📂 Sorgenti</div>", unsafe_allow_html=True)
        st.markdown("\n".join(sources), unsafe_allow_html=True)
        st.markdown("<div class='custom-title'>📌 Risposta</div>", unsafe_allow_html=True)
        st.markdown(combined_answers, unsafe_allow_html=True)

        subject = urllib.parse.quote(f"Risposta alla tua domanda: {question}")
        body = urllib.parse.quote(combined_answers.replace('\n', '%0A'))
        mailto_link = f"mailto:?subject={subject}&body={body}"

        st.markdown(f'<a href="{mailto_link}" class="email-link">Share via email</a>', unsafe_allow_html=True)
    else:
        st.error("Nessun documento pertinente trovato.")
