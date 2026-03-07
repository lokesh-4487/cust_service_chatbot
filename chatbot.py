import json
import random

# Load responses
with open("responses.json") as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()

    for intent in data:
        for pattern in data[intent]["patterns"]:
            if pattern in user_input:
                return random.choice(data[intent]["responses"])

    return "Sorry, I didn't understand that. Please try again."

print("Customer Service Chatbot")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Bot: Thank you for contacting us!")
        break

    response = get_response(user_input)
    print("Bot:", response)
