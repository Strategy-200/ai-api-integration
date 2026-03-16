import os
import cohere

# Initialize client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",
            message=prompt
        )

        return response.text

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    prompt = input("Enter prompt: ")

    result = query_cohere(prompt)

    print("\nResponse:")
    print(result)