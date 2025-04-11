import requests
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import openai

api_key= "openapi key"
openai.api_key = api_key

def get_reply(text):
    if 'how are you' in text.lower():
        return "I'm just a voice, but I'm doing fine!"
    return get_llm_reply(text)

def get_llm_reply(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  
        messages=[{"role": "user", "content": prompt}],
        #max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=1.2,
        presence_penalty=0.5,
    )

    # Extract the generated text from the response
    generated_text = response['choices'][0]['message']['content']
    return generated_text
