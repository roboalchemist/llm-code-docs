# Define the messages for the chat
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "input_audio",
                "input_audio": signed_url.url,
            },
            {
                "type": "text",
                "text": "What's in this file?"
            }
        ]
    }
]