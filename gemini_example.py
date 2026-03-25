# api_example.py

import os
from google import genai

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client using API key
client = genai.Client(api_key=api_key)


def query_api(prompt):
    """Query the Gemini API with a prompt"""
    try:
        # Check if prompt is valid
        if not prompt or not prompt.strip():
            return "Prompt cannot be empty."

        # Send request to Gemini API
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        # Check if response is valid
        if not response or not response.text:
            return "No response generated."

        # Return generated text
        return response.text

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