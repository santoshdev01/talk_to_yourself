import os
from datetime import datetime

def log_conversation(user_input, bot_response):
    os.makedirs('talk_to_yourself/data/logs', exist_ok=True)
    with open('talk_to_yourself/data/logs/conversation_log.txt', 'a') as file:
        file.write(f"{datetime.now()}\nYou: {user_input}\nBot: {bot_response}\n\n")