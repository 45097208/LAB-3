import re
import random
import requests
import os

rules = [
    (r'hello|hi|hey', ["Hello! How are you feeling today?", "Hi there! What's on your mind?"]),
    (r'my name is (\w+)', ["Hello, {0}! How are you feeling today?", "Nice to meet you, {0}!"]),
    (r'i feel stressed|i am stressed', ["Why do you feel stressed?", "What is causing your stress?"]),
    (r'i am tired|i\'m tired', ["Why are you tired?", "Have you been getting enough sleep?"]),
    (r'because (.*)', ["Is that the main reason?", "How long has {0} been affecting you?"]),
    (r'my mother (.*)', ["Tell me more about your mother.", "How does that make you feel?"]),
    (r'i need (.*)', ["Why do you need {0}?", "Would getting {0} really help you?"]),
    (r'(.*) sleep(.*)', ["Sleep is important. Are you getting enough rest?"]),
    (r'(.*)', ["Can you tell me more about that?", "How does that make you feel?"]),
]

def eliza_response(user_input):
    user_input = user_input.lower().strip()
    for pattern, responses in rules:
        match = re.search(pattern, user_input)
        if match:
            response = random.choice(responses)
            try:
                groups = match.groups()
                if groups:
                    response = response.format(*groups)
            except (IndexError, KeyError):
                pass
            return response
    return "Please tell me more."

HF_TOKEN = os.environ.get("HF_TOKEN", "")
API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
HEADERS = {"Content-Type": "application/json", "Authorization": f"Bearer {HF_TOKEN}"}

def llm_response(user_input):
    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": [{"role": "user", "content": user_input}],
        "max_tokens": 100,
        "temperature": 0.7
    }
    try:
        r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        if r.status_code == 200:
            return r.json()["choices"][0]["message"]["content"].strip()
        return f"[API Error {r.status_code}]"
    except Exception as e:
        return f"[Error: {e}]"

TEST_PROMPTS = [
    "Hello",
    "My name is Thandolwethu",
    "I feel stressed",
    "I am tired",
    "Because I have exams",
    "My mother is strict",
    "I need more sleep",
]

def main():
    print("=" * 90)
    print("  COMPARISON: ELIZA vs Modern LLM")
    print("=" * 90)

    for prompt in TEST_PROMPTS:
        print(f"\nPROMPT: {prompt}")
        print(f"  ELIZA : {eliza_response(prompt)}")
        print(f"  LLM   : {llm_response(prompt)}")
        print("-" * 90)

    print("\nComparison complete!")

if __name__ == "__main__":
    main()
