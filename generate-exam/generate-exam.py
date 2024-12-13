openai.api_key = "your-api-key-here"

# Function to interact with GPT-4 Turbo
def chat_with_gpt_turbo(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Specify the model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,  # Adjust as needed
            temperature=0.7  # Controls randomness; lower values make the output more deterministic
        )
        # Extract and return the assistant's reply
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    user_input = "Can you explain how photosynthesis works?"
    reply = chat_with_gpt_turbo(user_input)
    print("GPT-4 Turbo says:")
    print(reply)