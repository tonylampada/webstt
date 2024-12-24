from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
from .transcribe_audio import transcribe

app = FastAPI(title="Audio Transcription API")

class AudioData(BaseModel):
    audio: str  # base64 encoded audio data

@app.post("/transcribe/")
async def transcribe_audio(data: AudioData):
    # Validate base64 data first
    try:
        base64.b64decode(data.audio)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 audio data")
    
    # If base64 is valid, proceed with transcription
    try:
        text = transcribe(data.audio)
        return {"transcription": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
