# Audio Transcription API

A simple FastAPI server that transcribes audio files using OpenAI's Whisper model.

## Requirements

- Python 3.8+
- FFmpeg (for audio processing)

## Development

### Using VS Code Dev Containers (Recommended)

1. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code
2. Open this repository in VS Code
3. When prompted, click "Reopen in Container"
   - This will build the development container with all necessary tools and extensions

The devcontainer includes:
- Python 3.11
- FFmpeg
- Development tools (git, curl)
- Python packages (black, pylint, pytest, ipython)
- VS Code extensions for Python development

## Installation

### Using Docker (Production)

1. Build the Docker image:
```bash
docker build -t audio-transcription-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 audio-transcription-api
```

### Manual Installation

1. Install FFmpeg (if not already installed):
   - macOS: `brew install ffmpeg`
   - Ubuntu: `sudo apt-get install ffmpeg`

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

### With Docker
```bash
docker run -p 8000:8000 audio-transcription-api
```

### Without Docker
```bash
python -m app.main
```

The server will start at `http://localhost:8000`

## API Usage

Send a POST request to `/transcribe/` with an .ogg audio file:

```bash
curl -X POST "http://localhost:8000/transcribe/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_audio.ogg"
```

The response will be in JSON format:
```json
{
  "transcription": "Your transcribed text here..."
}
```

## Notes

- Only .ogg audio files are supported
- The Whisper model will be downloaded on first use
- Transcription may take some time depending on the audio length and your hardware
- When using Docker, the first build will take some time as it downloads dependencies