from sarvamai import SarvamAI
import base64
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local")
api_key = os.getenv("SARVAM_API_KEY")
client = SarvamAI(api_subscription_key=api_key)

LANGUAGE_MAP = {
    "Hindi": "hi-IN",
    "Bengali": "bn-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Marathi": "mr-IN",
    "Gujarati": "gu-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
    "Punjabi": "pa-IN",
    "Odia": "or-IN",
    "English": "en-IN"
}

def get_language_code(language_name):
    # .title() makes sure "hindi" or "HINDI" both map to "Hindi" , here hindi is default
    return LANGUAGE_MAP.get(language_name.title(), "hi-IN")

def generate_and_save_tts(text_to_speak, language = "Hindi", speaker_name="ritu"):
    """
    Sends text to Sarvam AI and saves the resulting audio to a timestamped file.
    """
    language_code = get_language_code(language)
    try:
        response = client.text_to_speech.convert(
        text=text_to_speak,
        speaker=speaker_name,
        target_language_code=language_code,
        model="bulbul:v3" # Explicitly naming the model is good practice
        )

        # 1. Generate a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # The SDK returns a list, so we grab the first item [0]
        audio_data = response.audios[0] 
        filename = f"audio_{timestamp}.mp3"
        with open(filename, "wb") as f:
            f.write(base64.b64decode(audio_data))

        print(f"Audio saved successfully as {filename}")   
        return filename
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# generate_and_save_tts("नमस्ते, आप कैसे हैं?")
# generate_and_save_tts("आज का मौसम बहुत अच्छा है।", speaker_name="aayan")

def translate_text(input_text,target_language):
    # input text language auto detected , translates to target language and stores audio as mp3
    language_code = get_language_code(target_language)
    try:
        #response stores an encoded array for the audio
        response = client.text.translate(
            input= input_text,
            source_language_code= "auto",
            target_language_code=language_code,
            speaker_gender="Male",
            model="mayura:v1",
            output_script="roman"
        )
        #return translated text
        translated_text = response.translated_text
        return translated_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# input_txt = translate_text("Hey Rama, where is Lakshmana?","Hindi")
# generate_and_save_tts(input_txt, speaker_name="aayan")

def speech_to_text(input_audio):
    # audio input, detect langauge , text output
    try:
        response = client.speech_to_text.transcribe(
        file=open(input_audio, "rb"),
        model="saaras:v3",
        mode="transcribe"  # default mode        
        )    
        return response
    except Exception as e:
        print("Error found : ",e)
        return None

# output_text = speech_to_text("audio_2026-06-16_19-36-13.mp3")
# print(output_text.transcript)

