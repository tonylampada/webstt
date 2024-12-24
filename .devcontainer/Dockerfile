FROM python:3.11-slim

# Install FFmpeg and development tools
RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install development dependencies
RUN pip install --no-cache-dir \
    black \
    pylint \
    pytest \
    pytest-asyncio \
    httpx \
    ipython

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code for preloading model
COPY app/ ./app/

# Preload the Whisper model during build
RUN python -m app.preload_model

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 