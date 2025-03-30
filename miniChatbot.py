# Mini Chatbot Python project Project 1
import time
responses = {
    "hello": "Hi there!, How can i assit you today?",
    "how are you": "I'm just a bot, but i'm doing great! How about you",
    "bye": "Goodbye! Have a great day!",
    "What is your name": " I'm miniBot, your friendly chatbot!",
    "help": "I can answer questions like: 'hello', 'how are you','what is your name', or 'bye'. ",
    
}

# Function to log Conversation
def log_conversation(user_input, bot_response):
    with open("chat_history.txt", "a") as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] User: {user_input} \n")
        file.write(f"[{timestamp}] Bot: {bot_response} \n\n")

# Chatbot Function
def chatbot():
    print("MiniBot: Hello! Type 'bye' to exit")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "bye":
            response = "Goodbye! Have a great day!"
            print(f"MiniBot: {response}")
            log_conversation(user_input, response)
            break
        response = responses.get(user_input , "I'm not sure how to respond to that. Try asking something else.")
        print(f"MiniBot: {response}")
        log_conversation(user_input, response)

# Run chatBot

chatbot()