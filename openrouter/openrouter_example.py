from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def query_openrouter(prompt):
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    result = query_openrouter(prompt)

    print("\nResponse:")
    print(result)