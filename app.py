# import nltk

# nltk.download('stopwords')
import google.generativeai as genai

import json
import os
import streamlit as st



genai.configure(api_key=os.getenv("api_key"))


# Set up the model configuration options
temperature = 0.1
top_p = 0.7
top_k = 57
max_output_tokens = 10000

 # Set up the model
generation_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
    }


safety_settings = "{}"
safety_settings = json.loads(safety_settings)



gemini = genai.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)


def generate_smart_contract(query):
    prompt = f"\nYou are an expert in developing Smart Contracts in the Cadence Language. Use pub instead of public and generate Code for the following Smart Contract without Signer:{ query }"
    return gemini.generate_content(prompt)

def generate_legal_contracts(query):
    prompt = f"You are an experienced Cadence Smart Contract Engineer, with extensive experience of converting legal agreements into smart contracts to be used as Ricardian contracts. Using the legal agreement below, generate a Cadence smart contract that will represent the legal agreement on the blockchain, create functions in the cntract that represents the condirions of the legal agreement. You are only required to generate the code without any explanation, you may only add comments to the codex. Here is the agreement: {query}"
    return gemini.generate_content(prompt)

def main():
    st.title("Flow For Layman")

    st.write("This is a tool to help you generate Smart Contracts in the Cadence Language. You can use this tool to generate Smart Contracts from plain English text. You can also use this tool to convert legal agreements into smart contracts to be used as Ricardian contracts.")


    documents, legal_documents = st.tabs(['Generate Smart Contracts Using Text', 'Generate Smart Contracts Using Legal Contracts'])
    
    with documents:
        query = st.text_input("Enter the description")
        if st.button("Generate Smart Contract"):
            with st.spinner("Please wait while we generate your response"):
                response = generate_smart_contract(query=query)
                st.markdown(f"{response.text}", unsafe_allow_html=True)

    with legal_documents:
        query = st.text_input("Enter your query")
        if st.button("Generate Smart Contract from Legal Agreement"):
            with st.spinner("Please wait while we generate your response"):
                response = generate_legal_contracts(query=query)
                st.markdown(f"{response.text}", unsafe_allow_html=True)
    
        

        
if __name__ == "__main__":  
    main()

