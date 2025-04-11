
import requests
import io
import pyaudio
from pydub import AudioSegment
import base64
import json 
from playsound import playsound
import os

def clone_and_speak_old(text, api_key=None):
    project_id = ""
    api_key = ""
    voice_id = ""

    url = f"https://api.resemble.ai/v1/projects/{project_id}/speak"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "voice": voice_id,  # Your cloned voice ID from Resemble.AI
        "text": text
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        audio_url = response.json()['audio_url']
        print(f"Audio generated: {audio_url}")
        return audio_url
    else:
        print(f"Error: {response.text}")
        return None
    


def clone_and_speak(text, api_key=None):
    project_id = "415251f5-default"
    api_key = "wdoJIX2RKduZDczNRwjAwgtt"
    voice_id = "dd47c982"
    url = "https://p.cluster.resemble.ai/synthesize"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "voice_uuid": voice_id,
        "data": text
    }

    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code)
    print(response.json().keys())
    

    if response.status_code == 200:
        print("Content-Type:", response.headers.get('Content-Type'))
        print("First few bytes:", response.content[:100])
        response_content = response.content
        decoded_response = response_content.decode('utf-8')

        # Parse the JSON string into a Python dictionary
        response_json = json.loads(decoded_response)

        # Check if the audio_content is present
        if 'audio_content' in response_json:
            # Extract the base64-encoded audio content
            audio_content = response_json["audio_content"]

            # Decode the base64 audio content
            decoded_audio = base64.b64decode(audio_content)

            # Load the decoded audio content into pydub (Assuming it's WAV format)
            audio = AudioSegment.from_wav(io.BytesIO(decoded_audio))  # If it's a different format, use from_file()
            audio.export("output.wav", format="wav")
            playsound("output.wav")
            os.remove("output.wav")
        else:
            print(f"Error: {response.text}")
            return None
    else:
        print(f"Error: {response.text}")
        return None
