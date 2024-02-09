from langchain.llms import GooglePalm
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Google Palm LLM Setup
# llm = GooglePalm(google_api_key=os.getenv('GOOGLE_API_KEY'), temperature=0.2)

# Streamlit app
st.title("TubeTrove AI")
prompt = st.text_input("Plug in your Prompt below")
