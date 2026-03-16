import requests

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    result = query_ollama(prompt)

    print("\nResponse:")
    print(result)