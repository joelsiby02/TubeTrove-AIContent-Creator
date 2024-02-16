from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the Google API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Check if the GOOGLE_API_KEY is defined
if GOOGLE_API_KEY is None:
    st.error("Error: Google API Key not found. Please make sure to define the GOOGLE_API_KEY environment variable in your .env file.")
else:
    # Initialize the ChatGoogleGenerativeAI object with the Gemini model
    llm = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model="gemini-pro")

    # Streamlit app
    st.title("TubeTrove AI")

    # Text input for user prompt
    prompt = st.text_input("Plug in your Prompt below")

    # Button to generate response
    if st.button("Generate Response"):
        # Generate response using the invoke method of the llm object
        result = llm.invoke(prompt)
        # Display the generated response
        st.write("Generated Response:")
        st.write(result.content)
