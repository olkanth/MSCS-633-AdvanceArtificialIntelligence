from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('QAChatbot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english') 

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