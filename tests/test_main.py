from fastapi.testclient import TestClient
from app.main import app
import base64
from unittest.mock import patch
import os
import json

client = TestClient(app)

def test_transcribe_endpoint_with_real_audio():
    # Load the real audio file
    audio_path = os.path.join("tests", "fixtures", "test.ogg")
    with open(audio_path, "rb") as f:
        audio_content = f.read()
    
    # Convert to base64
    base64_audio = base64.b64encode(audio_content).decode('utf-8')
    
    # Make the request with the base64 audio
    response = client.post(
        "/transcribe/",
        json={"audio": base64_audio}
    )
    
    # Assert the response
    assert response.status_code == 200
    assert "transcription" in response.json()
    assert isinstance(response.json()["transcription"], str)
    assert len(response.json()["transcription"]) > 0
    assert response.json()["transcription"] == " Hello, this is a test."

def test_transcribe_endpoint_mock():
    # Create mock audio data
    mock_audio_content = b"mock audio data"
    base64_audio = base64.b64encode(mock_audio_content).decode('utf-8')
    
    # Mock the transcribe function
    with patch('app.main.transcribe') as mock_transcribe:
        mock_transcribe.return_value = "Hello, this is a test transcription"
        
        # Make the request with the mock data
        response = client.post(
            "/transcribe/",
            json={"audio": base64_audio}
        )
        
        # Assert the response
        assert response.status_code == 200
        assert response.json() == {"transcription": "Hello, this is a test transcription"}
        
        # Verify the transcribe function was called with correct base64 data
        mock_transcribe.assert_called_once_with(base64_audio)

def test_transcribe_endpoint_invalid_base64():
    # Test with invalid base64 data
    response = client.post(
        "/transcribe/",
        json={"audio": "not-valid-base64!@#"}
    )
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid base64 audio data"}

