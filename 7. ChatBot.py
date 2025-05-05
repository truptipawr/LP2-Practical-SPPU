import random

class Chatbot:
    def __init__(self):
        self.name = "Customer Support Bot"
        self.faqs = {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi! How can I assist you?",
            "how are you": "I'm just a bot, but I'm doing fine. How can I assist you?",
            "what is your name": "I am the Customer Support Bot.",
            "support": "You can reach support at support@company.com or call us at 123-456-7890.",
            "hours": "We are open from 9 AM to 6 PM, Monday to Friday.",
            "goodbye": "Goodbye! Have a great day!"
        }

    def greet(self):
        greetings = ["Hi there!", "Hello!", "Greetings!", "Hey!"]
        return random.choice(greetings)

    def handle_message(self, message):
        message = message.lower().strip()

        if message in self.faqs:
            return self.faqs[message]
        else:
            return "I'm sorry, I don't understand that. Can you please rephrase?"

    def start_chat(self):
        print(f"{self.greet()} I'm {self.name}. How can I assist you today?")
        
        while True:
            user_message = input("You: ")
            if user_message.lower().strip() == "exit":
                print("Goodbye! If you need further assistance, feel free to reach out again.")
                break

            response = self.handle_message(user_message)
            print(f"{self.name}: {response}")

# Example usage
if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()
