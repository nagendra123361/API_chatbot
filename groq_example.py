# api_example.py

import os
from groq import Groq

# Get API key from environment variable
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)


def query_api(prompt):
    """Query the Groq API with a prompt"""
    try:
        # Check if prompt is valid
        if not prompt or not prompt.strip():
            return "Prompt cannot be empty."

        # Send request to Groq API
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        # Extract and return response text
        return response.choices[0].message.content

    except Exception as e:
        # Handle API errors
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    # Take user input
    user_prompt = input("Enter your prompt: ")

    print("Querying API...")

    # Call API function
    result = query_api(user_prompt)

    # Print response
    print("Response:")
    print(result)