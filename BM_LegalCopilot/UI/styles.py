import streamlit as st

def load_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Open Sans', sans-serif;
            font-weight: 300;
        }

        .user-question {
            font-size: 2rem;
            margin-bottom: 20px;
        }

        .custom-title {
            font-size: 12pt;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .custom-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .custom-source {
            background-color: #1E2222; 
            color: #FFFFFF; 
            padding: 10px; 
            border-radius: 5px; 
            flex: 1 1 calc(33.333% - 10px); /* Tre colonne con gap di 10px */
            max-width: calc(33.333% - 10px);
            box-sizing: border-box;
            margin-bottom: 20px; 
            overflow: hidden; 
        }

        .source-title {
            font-weight: bold;
            margin-bottom: 5px;
            white-space: nowrap; /* Evita che il testo vada a capo */
            overflow: hidden; /* Nasconde il testo in eccesso */
            text-overflow: ellipsis; /* Aggiunge i tre puntini di sospensione */
        }

        .source-preview {
            font-size: 10pt; 
            display: -webkit-box; 
            -webkit-line-clamp: 2; 
            -webkit-box-orient: vertical; 
            overflow: hidden; 
            text-overflow: ellipsis; 
            white-space: normal; 
        }

        .custom-answer {
            margin-top: 1px; 
            margin-bottom: 1px; 
        }

        .email-link {
            display: block; 
            color: blue; 
            text-decoration: underline;
            cursor: pointer;
            margin-bottom: 1px; 
        }
        </style>
    """, unsafe_allow_html=True)
