# Orchestrates input/output and processing
from app.speech.recognizer import listen
from app.speech.synthesizer import speak
from app.nlp.chatbot import get_reply
from app.journal.logger import log_conversation

def start():
    while True:
        text = listen()
        if text.lower() in ['exit', 'quit', 'bye']:
            speak('Goodbye!')
            break
        response = get_reply(text)
        speak(response)
        log_conversation(text, response)