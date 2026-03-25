# AI Chatbot with API Keys

## Project Description

This project implements a multi-AI chatbot system that integrates multiple AI providers, including Groq, Google Gemini, Cohere, and Hugging Face. It enables users to enter prompts and receive responses from different AI models.

A Streamlit-based interface is included to provide an interactive and user-friendly experience. The project demonstrates how to work with multiple AI APIs in a modular and scalable way.

---

## Setup Instructions

### Clone or Download

Clone the repository or download the project files to your local system.

### Install Dependencies

Using requirements.txt:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests groq google-genai cohere huggingface_hub streamlit
```

### Python Version

Recommended Python version: 3.10 or above

---

## How to Obtain API Keys

### Groq API

Go to: https://console.groq.com
Create an account and generate an API key.

### Google Gemini API

Go to: https://aistudio.google.com
Create an API key and enable the required services.

### Cohere API

Go to: https://dashboard.cohere.com
Sign up and generate an API key.

### Hugging Face API

Go to: https://huggingface.co/settings/tokens
Create a token with read and inference permissions.

---

## How to Run

### Run Python Programs

```bash
python filename.py
```

### Run Streamlit Application

```bash
streamlit run multi_api_query.py
```

---

## Notes

* Ensure all API keys are correctly set before running the programs.
* Internet connection is required for API-based models.
* Some APIs may have usage limits depending on the plan.

---
