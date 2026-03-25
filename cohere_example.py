# COHERE API EXAMPLE

import cohere
import os

# Get API key from environment variable
api_key = os.getenv("COHERE_API_KEY")

# Initialize Cohere client
client = cohere.Client(api_key)

def query_api(prompt):
    """
    Query the Cohere API with a prompt
    """
    try:
        # Validate input
        if not prompt or not prompt.strip():
            return "Prompt cannot be empty."

        # Send request to Cohere API
        response = client.chat(
            model="command-r-plus-08-2024",
            message=prompt,
            temperature=0.7
        )

        # Extract and return response
        if response and response.text:
            return response.text.strip()
        else:
            return "No response generated."

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    # Take user input
    user_prompt = input("Enter your prompt: ")

    print("Querying API...")

    # Call API
    result = query_api(user_prompt)

    print("Response:")
    print(result)