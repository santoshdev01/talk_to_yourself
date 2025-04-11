
# Talk to Yourself - Voice Assistant with Voice Cloning

This project integrates **speech-to-text**, **AI-based responses**, and **voice cloning** to create a voice assistant that listens to your commands and speaks back in your cloned voice.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/santoshdev01/talk_to_yourself_ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Resemble.AI account:
   - Sign up at [Resemble.AI](https://www.resemble.ai/).
   - Record and upload your voice.
   - Get the **API Key** and **Voice ID**.

4. Replace the placeholders `your_project_id`, `your_voice_id`, and `your_resemble_api_key` in the code.

5.Register with OpenAI and setup an api key to get GPT responses from OpenAI through APIs

5. Run the assistant:
   ```bash
   python run.py
   ```

This will run the assistant, listening for your voice, processing it, and responding using your cloned voice!

