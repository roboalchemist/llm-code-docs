# Get the transcription
with open("/path/to/file/audio.mp3", "rb") as f:
    transcription_response = client.audio.transcriptions.complete(
        model=model,
        file={
            "content": f,
            "file_name": "audio.mp3",
        },
        ## language="en"
    )