from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('QAChatbot')
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train('chatterbot.corpus.english') 

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(chatbot)
trainer.train(conversation)

def get_response(user_input):
    return chatbot.get_response(user_input)


if __name__ == "__main__":
    print("Welcome to the QA Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("user: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")