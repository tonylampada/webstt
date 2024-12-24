import whisper
import os

def preload_model():
    model_name = os.getenv("WHISPER_MODEL", "turbo")
    print(f"Preloading Whisper model: {model_name}")
    whisper.load_model(model_name)
    print("Whisper model loaded successfully!")

if __name__ == "__main__":
    preload_model() 