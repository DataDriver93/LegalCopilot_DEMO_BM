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

        .custom-source {
            background-color: #1E2222; 
            color: #FFFFFF; 
            padding: 10px; 
            border-radius: 5px; 
            display: inline-block; 
            margin-right: 10px; 
            margin-bottom: 20px; 
            max-width: 30%; 
            max-height: 150px; 
            overflow: hidden; 
            vertical-align: top; 
        }

        .source-title {
            font-weight: bold;
            margin-bottom: 5px;
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
