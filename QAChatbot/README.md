# QA Chatbot

This is a simple question-answering chatbot built with Python and the ChatterBot library.

## Implementation Details

The chatbot is implemented in the `bot.py` file. It uses the `ChatterBot` library to create a chatbot instance and trains it with a small conversation corpus. The bot is trained using the `ListTrainer`.

The `get_response` function takes a user's input as a string and returns the chatbot's response.

The main part of the script (`if __name__ == "__main__":`) runs a simple command-line interface for interacting with the chatbot.

## Packages Needed

To run this chatbot, you will need to install the following package:

```bash
pip install chatterbot
```

## How to Run

1.  **Install the required packages:**
    ```bash
    pip install chatterbot
    pip install spacy 
    pip install chatterbot_corpus
    python -m spacy download en_core_web_sm
    ```

2.  **Run the bot:**
    ```bash
    python bot.py
    ```

3.  **Interact with the bot:**
    You can start typing your questions or greetings in the terminal. To exit the chatbot, type `exit`.
