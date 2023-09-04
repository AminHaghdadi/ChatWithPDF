import streamlit as st
from pdf_helper import chat_with_your_pdf
from gtts import gTTS
from io import BytesIO

st.title('Chat with your pdf')

uploaded_file = st.file_uploader("Upload your PDF file Here", type="pdf")
qu = st.text_input('ask your question here')

if uploaded_file and qu:
    response = chat_with_your_pdf(uploaded_file, qu)
    st.write(response)

    # Create a gTTS object with the response text and language
    tts = gTTS(text=response, lang='en')

    # Save the speech as an audio file in memory
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    # Play the audio file in the Streamlit app
    st.audio(fp, format='audio/mp3')
