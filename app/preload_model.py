import whisper

def preload_model():
    print("Preloading Whisper model...")
    whisper.load_model("base")
    print("Whisper model loaded successfully!")

if __name__ == "__main__":
    preload_model() 