# Transcribe the audio with timestamps
transcription_response = client.audio.transcriptions.complete(
    model=model,
    file_url="https://docs.mistral.ai/audio/obama.mp3",
    timestamp_granularities="segment"
)