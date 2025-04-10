
import requests

def clone_and_speak(text, api_key=None):
    project_id = "415251f5-default"
    api_key = "wdoJIX2RKduZDczNRwjAwgtt"
    voice_id = "dd47c982"

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
