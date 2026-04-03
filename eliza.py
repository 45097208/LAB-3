import re
import random

# Custom rule-based ELIZA chatbot
# Each rule: (pattern, [list of responses])
rules = [
    # Rule 1: Greeting
    (r'hello|hi|hey',
     ["Hello! How are you feeling today?",
      "Hi there! What's on your mind?",
      "Hey! How can I help you?"]),

    # Rule 2: Name introduction
    (r'my name is (\w+)',
     ["Hello, {0}! How are you feeling today?",
      "Nice to meet you, {0}! What brings you here?",
      "Hi {0}, what would you like to talk about?"]),

    # Rule 3: Feelings - stressed
    (r'i feel stressed|i am stressed|i\'m stressed',
     ["Why do you feel stressed?",
      "What is causing your stress?",
      "Stress can be difficult. Can you tell me more about what's troubling you?"]),

    # Rule 4: Feelings - tired
    (r'i am tired|i\'m tired|i feel tired',
     ["Why are you tired?",
      "What has been draining your energy?",
      "Have you been getting enough sleep?"]),

    # Rule 5: Reason/because
    (r'because (.*)',
     ["Is that the main reason?",
      "Does that reason make sense to you?",
      "How long has {0} been affecting you?"]),

    # Rule 6: Family - mother
    (r'my mother (.*)',
     ["Tell me more about your mother.",
      "How does that make you feel about your mother?",
      "What is your relationship with your mother like?"]),

    # Rule 7: Family - father
    (r'my father (.*)',
     ["Tell me more about your father.",
      "How does your father's behaviour affect you?",
      "What do you wish were different about your father?"]),

    # Rule 8: Need
    (r'i need (.*)',
     ["Why do you need {0}?",
      "Would getting {0} really help you?",
      "What would change if you had {0}?"]),

    # Rule 9: Sleep
    (r'(.*) sleep(.*)',
     ["Sleep is very important. Are you getting enough rest?",
      "What is keeping you from sleeping well?",
      "How many hours of sleep do you usually get?"]),

    # Rule 10: Exams / study
    (r'(.*)(exam|test|study|assignment)(.*)',
     ["Academic pressure can be tough. How are you managing?",
      "Do you have support when studying?",
      "What subject is giving you the most trouble?"]),

    # Rule 11: I am (general)
    (r'i am (.*)',
     ["Why do you say you are {0}?",
      "How long have you been {0}?",
      "How does being {0} make you feel?"]),

    # Rule 12: I think
    (r'i think (.*)',
     ["Why do you think {0}?",
      "Do you really believe {0}?",
      "What makes you think that?"]),

    # Rule 13: I want
    (r'i want (.*)',
     ["Why do you want {0}?",
      "What would it mean to you if you got {0}?",
      "How long have you wanted {0}?"]),

    # Rule 14: Quit
    (r'quit|bye|exit',
     ["Goodbye! Take care of yourself.",
      "It was good talking to you. Bye!",
      "See you next time. Stay well."]),

    # Rule 15: Default / fallback
    (r'(.*)',
     ["Can you tell me more about that?",
      "I see. Why do you feel that way?",
      "Interesting. Please continue.",
      "How does that make you feel?",
      "Could you elaborate on that?"])
]


def eliza_response(user_input):
    user_input = user_input.lower().strip()

    for pattern, responses in rules:
        match = re.search(pattern, user_input)
        if match:
            response = random.choice(responses)
            # Fill in any captured groups
            try:
                groups = match.groups()
                if groups:
                    response = response.format(*groups)
            except (IndexError, KeyError):
                pass
            return response

    return "Please tell me more."


def main():
    print("=" * 50)
    print("  ELIZA - Rule-Based Chatbot")
    print("  (Type 'quit' to exit)")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        response = eliza_response(user_input)
        print(f"ELIZA: {response}")
        if re.search(r'quit|bye|exit', user_input.lower()):
            break


if __name__ == "__main__":
    main()
