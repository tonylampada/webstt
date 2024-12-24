FROM python:3.11-slim

# Install FFmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Preload the Whisper model during build
RUN python -m app.preload_model

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "-m", "app.main"]