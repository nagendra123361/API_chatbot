# api_example.py

import os
from huggingface_hub import InferenceClient

# Get API token from environment variable
api_key = os.getenv("HF_TOKEN")

# Initialize Hugging Face client
client = InferenceClient(token=api_key)


def query_api(prompt):
    """Query the Hugging Face API with a prompt"""
    try:
        # Check if prompt is valid
        if not prompt or not prompt.strip():
            return "Prompt cannot be empty."

        # Send request to Hugging Face model
        response = client.text_generation(
            model="gpt2",
            prompt=prompt,
            max_new_tokens=100
        )

        # Check if response is empty
        if not response:
            return "No response generated."

        # Return generated text
        return response

    except StopIteration:
        # Handle case where model returns no output
        return "Error: Model returned no output."

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