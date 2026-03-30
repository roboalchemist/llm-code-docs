# Get the chat response
chat_response = client.chat.complete(
    model=model,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "input_audio",
                "input_audio": audio_base64,
            },
            {
                "type": "text",
                "text": "What's in this file?"
            },
        ]
    }],
)