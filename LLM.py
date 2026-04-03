import requests
import os

HF_TOKEN = os.environ.get("HF_TOKEN", "")
API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query_llm(user_message):
    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": [{"role": "user", "content": user_message}],
        "max_tokens": 200,
        "temperature": 0.7
    }
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"[API Error {response.status_code}: {response.text[:300]}]"
    except Exception as e:
        return f"[Error: {e}]"

def main():
    print("=" * 55)
    print("  Modern LLM Chatbot (Hugging Face)")
    print("  Model: meta-llama/llama-3.1-8b-instruct")
    print("  (Type 'quit' to exit)")
    print("=" * 55)

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "bye", "exit"):
            print("LLM: Goodbye!")
            break
        print("LLM: [thinking...]", end="\r")
        response = query_llm(user_input)
        print(f"LLM: {response}          ")

if __name__ == "__main__":
    main()
