from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

# Define the Google API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model="gemini-pro", temperature=0.2)

# Streamlit app
st.title("TubeTrove AI")

# Text input for user prompt
prompt = st.text_input("Plug in your Prompt below")
    
# Define prompt template
prompt_template = PromptTemplate(
    input_variables=['topic'],
    template="Write me a Youtube video title about {topic}",
)

# Initialize the LLMChain object
llm_title_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)

# Button to generate response
if st.button("Generate Response"):
    # Main execution block
    if prompt:
        response = llm_title_chain.run(topic=prompt)
        st.write("Generated Response:")
        st.write(response)
    else:
        st.warning("Please provide a prompt.")
