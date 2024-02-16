from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

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
    template="Suggets a nane for the title : {title} and Write me a Youtube video Script about on this title : {title}",
)

# Initialize the LLMChain for title generation
llm_title_chain = LLMChain(llm=llm, prompt=title_prompt_template, verbose=True)

# Initialize the LLMChain for script generation
llm_script_chain = LLMChain(llm=llm, prompt=script_prompt_template, verbose=True)

# Joining the above chains to work sequentially
seq_chain = SimpleSequentialChain(chains=[llm_title_chain, llm_script_chain], verbose=True)

# Button to generate response
if st.button("Generate Response"):
    # Main execution block
    if prompt:
        # Generate response using the sequential chain
        response = seq_chain.run(prompt)
        
        # Display the generated response
        st.markdown("**Generated Response:**")
        for line in response.split("\n"):
            st.write(line.strip())
    else:
        st.warning("Please provide a prompt.")
