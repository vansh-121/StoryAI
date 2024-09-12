import requests
import streamlit as st

def ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/story/invoke",
        json={'input':{'topic': input_text}}
    )

    return response.json()['output']

st.title('StoryAI : Generate your Dream stories')
input_text=st.text_input("Write a story on :")

if input_text:
    st.write(ollama_response(input_text))