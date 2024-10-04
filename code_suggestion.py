from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_code_suggestion(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",  # You can use "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are an AI code assistant."},
        {"role": "user", "content": prompt}
    ])

    # Extract and return the generated code from the response
    return response.choices[0].message.content.strip()


# Example of prompting the AI
def main():
    while True:
        user_prompt = input("\nDescribe what code you need help with (or type 'exit' to quit): ")
        if user_prompt.lower() == 'exit':
            break

        suggestion = get_code_suggestion(user_prompt)
        print("\nSuggested code snippet:\n", suggestion)


if __name__ == "__main__":
    main()
