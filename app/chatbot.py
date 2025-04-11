
from speech.recognizer import recognize_speech_from_mic
from speech.synthesizer import clone_and_speak

def get_reply(text):
    if "how are you" in text.lower():
        return "I'm doing fine, thank you for asking!"
    elif "your name" in text.lower():
        return "I am your voice assistant, powered by AI!"
    else:
        return "I'm sorry, I don't understand that. Can you say something else?"

def main():
    api_key = ""
    while True:
        print("Waiting for your command...")
        user_input = recognize_speech_from_mic()
        if user_input:
            print(f"User said: {user_input}")
            response = get_reply(user_input)
            print(f"Bot reply: {response}")
            clone_and_speak(response, api_key)
