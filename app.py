from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

# Load environment variables from .env file
load_dotenv()

# Define the Google API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model="gemini-pro", temperature=0.2)

# Streamlit app
st.title("TubeTrove AI")

# Text input for user prompt
prompt = st.text_input("Plug in your Prompt below")
    
# Define prompt template for title generation
title_prompt_template = PromptTemplate(
    input_variables=['topic'],
    template="Write me a Youtube video title about {topic}",
)

# Define prompt template for script generation
script_prompt_template = PromptTemplate(
    input_variables=['title'],
    template="Write me a Youtube video Script about on this title : {title}",
)

# Initialize the LLMChain for title generation
llm_title_chain = LLMChain(llm=llm, prompt=title_prompt_template, verbose=True, output_key='title')

# Initialize the LLMChain for script generation
llm_script_chain = LLMChain(llm=llm, prompt=script_prompt_template, verbose=True, output_key='script')

# Joining the above chains to work sequentially
seq_chain = SequentialChain(chains=[llm_title_chain, llm_script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose=True)

# Button to generate response
if st.button("Generate Response"):
    # Main execution block
    if prompt:
        # Generate response using the sequential chain
        response = seq_chain({'topic': prompt})
        
        # Display the generated response
        st.markdown("**Generated Response:**")
        title_response = response.get('title', '')
        script_response = response.get('script', '')
        st.subheader("Generated Title:")
        st.write(title_response.strip())
        st.subheader("Generated Script:")
        st.write(script_response.strip())
    else:
        st.warning("Please provide a prompt.")
