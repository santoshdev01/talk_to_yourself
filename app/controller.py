from app.speech.recognizer import recognize_speech_from_mic
from app.speech.synthesizer import clone_and_speak
from app.nlp.chatbot import get_reply
from app.journal.logger import log_conversation

def start():
    while True:
        text = recognize_speech_from_mic()
        if not text or text.lower() in ['exit', 'quit', 'bye']:
            clone_and_speak('Good Bye See you later')
            break
        response = get_reply(text)
        clone_and_speak(response)
        log_conversation(text, response)