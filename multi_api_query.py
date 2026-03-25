# app.py

import streamlit as st
from groq import Groq
from google import genai
import cohere
from huggingface_hub import InferenceClient


# API keys (replace with your keys)
GROQ_API_KEY = "groq_key"
GEMINI_API_KEY = "gemini_key"
COHERE_API_KEY = "cohere_key"
HF_API_KEY = "hf_key"


# Initialize clients
groq_client = Groq(api_key=GROQ_API_KEY)
gemini_client = genai.Client(api_key=GEMINI_API_KEY)
cohere_client = cohere.Client(COHERE_API_KEY)
hf_client = InferenceClient(token=HF_API_KEY)


def generate_response(model, prompt):
    """Route request to selected AI model"""
    try:
        if model == "Groq":
            res = groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )
            return res.choices[0].message.content

        elif model == "Gemini":
            res = gemini_client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return res.text

        elif model == "Cohere":
            res = cohere_client.chat(
                model="command-r-plus-08-2024",
                message=prompt
            )
            return res.text

        elif model == "Hugging Face":
            res = hf_client.text_generation(
                model="gpt2",
                prompt=prompt,
                max_new_tokens=100
            )
            return res

        else:
            return "Invalid model selected"

    except Exception as e:
        return f"Error: {e}"


# UI

st.set_page_config(page_title="AI Chat Interface", layout="centered")

st.header("AI Chat Interface")

# Model selection
selected_model = st.selectbox(
    "Choose an AI model",
    ["Groq", "Gemini", "Cohere", "Hugging Face"]
)

# Prompt input
prompt = st.text_area("Type your prompt here", height=120)

# Action button
if st.button("Submit"):

    if not prompt.strip():
        st.error("Prompt cannot be empty")

    else:
        with st.spinner("Processing..."):
            result = generate_response(selected_model, prompt)

        st.markdown("### Output")
        st.write(result)