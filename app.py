from langchain.llms import GooglePalm
import streamlit as st
import os
from dotenv import load_dotenv

# Google Palm LLM Setup
llm = GooglePalm(google_api_key=os.getenv('GOOGLE_API_KEY'), temperature=0.2)

# Streamlit app
st.title("Google Palm LLM Test")

# Function to generate text using the model
def generate_text(prompt):
    response = llm.generate(prompt)
    return response

# Input prompt from the user
prompt = st.text_input("Enter a prompt:", "Once upon a time")

# Button to trigger text generation
if st.button("Generate Text"):
    with st.spinner("Generating..."):
        # Generate text
        generated_text = generate_text(prompt)
    # Display generated text
    st.write("Generated Text:")
    st.write(generated_text)
