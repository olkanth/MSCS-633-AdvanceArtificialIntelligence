from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('QAChatbot')

# training with the English corpus data which includes general conversations
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train('chatterbot.corpus.english') 

# training with a simple conversation
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

# ListTrainer allows us to train the chatbot with a list of strings we want it to learn from
trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Function to get a response from the chatbot
def get_response(user_input):
    return chatbot.get_response(user_input)


if __name__ == "__main__":
    print("Welcome to the QA Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("user : ")

        # Exit condition for the chatbot
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot :  {response}")