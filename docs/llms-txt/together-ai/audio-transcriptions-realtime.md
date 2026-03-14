# Source: https://docs.together.ai/reference/audio-transcriptions-realtime.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a realtime audio transcription

> Establishes a WebSocket connection for real-time audio transcription. This endpoint uses WebSocket protocol (wss://api.together.ai/v1/realtime) for bidirectional streaming communication.

**Connection Setup:**
- Protocol: WebSocket (wss://)
- Authentication: Pass API key as Bearer token in Authorization header
- Parameters: Sent as query parameters (model, input_audio_format)

**Client Events:**
- `input_audio_buffer.append`: Send audio chunks as base64-encoded data
  ```json
  {
    "type": "input_audio_buffer.append",
    "audio": "<base64_encoded_audio_chunk>"
  }
  ```
- `input_audio_buffer.commit`: Signal end of audio stream
  ```json
  {
    "type": "input_audio_buffer.commit"
  }
  ```

**Server Events:**
- `session.created`: Initial session confirmation (sent first)
  ```json
  {
    "type": "session.created",
    "session": {
      "id": "session-id",
      "object": "realtime.session",
      "modalities": ["audio"],
      "model": "openai/whisper-large-v3"
    }
  }
  ```
- `conversation.item.input_audio_transcription.delta`: Partial transcription results
  ```json
  {
    "type": "conversation.item.input_audio_transcription.delta",
    "delta": "The quick brown"
  }
  ```
- `conversation.item.input_audio_transcription.completed`: Final transcription
  ```json
  {
    "type": "conversation.item.input_audio_transcription.completed",
    "transcript": "The quick brown fox jumps over the lazy dog"
  }
  ```
- `conversation.item.input_audio_transcription.failed`: Error occurred
  ```json
  {
    "type": "conversation.item.input_audio_transcription.failed",
    "error": {
      "message": "Error description",
      "type": "invalid_request_error",
      "param": null,
      "code": "invalid_api_key"
    }
  }
  ```

**Error Codes:**
- `invalid_api_key`: Invalid API key provided (401)
- `missing_api_key`: Authorization header missing (401)
- `model_not_available`: Invalid or unavailable model (400)
- Unsupported audio format errors (400)




## OpenAPI

````yaml GET /realtime
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /realtime:
    get:
      tags:
        - Audio
      summary: Real-time audio transcription via WebSocket
      description: >
        Establishes a WebSocket connection for real-time audio transcription.
        This endpoint uses WebSocket protocol
        (wss://api.together.ai/v1/realtime) for bidirectional streaming
        communication.


        **Connection Setup:**

        - Protocol: WebSocket (wss://)

        - Authentication: Pass API key as Bearer token in Authorization header

        - Parameters: Sent as query parameters (model, input_audio_format)


        **Client Events:**

        - `input_audio_buffer.append`: Send audio chunks as base64-encoded data
          ```json
          {
            "type": "input_audio_buffer.append",
            "audio": "<base64_encoded_audio_chunk>"
          }
          ```
        - `input_audio_buffer.commit`: Signal end of audio stream
          ```json
          {
            "type": "input_audio_buffer.commit"
          }
          ```

        **Server Events:**

        - `session.created`: Initial session confirmation (sent first)
          ```json
          {
            "type": "session.created",
            "session": {
              "id": "session-id",
              "object": "realtime.session",
              "modalities": ["audio"],
              "model": "openai/whisper-large-v3"
            }
          }
          ```
        - `conversation.item.input_audio_transcription.delta`: Partial
        transcription results
          ```json
          {
            "type": "conversation.item.input_audio_transcription.delta",
            "delta": "The quick brown"
          }
          ```
        - `conversation.item.input_audio_transcription.completed`: Final
        transcription
          ```json
          {
            "type": "conversation.item.input_audio_transcription.completed",
            "transcript": "The quick brown fox jumps over the lazy dog"
          }
          ```
        - `conversation.item.input_audio_transcription.failed`: Error occurred
          ```json
          {
            "type": "conversation.item.input_audio_transcription.failed",
            "error": {
              "message": "Error description",
              "type": "invalid_request_error",
              "param": null,
              "code": "invalid_api_key"
            }
          }
          ```

        **Error Codes:**

        - `invalid_api_key`: Invalid API key provided (401)

        - `missing_api_key`: Authorization header missing (401)

        - `model_not_available`: Invalid or unavailable model (400)

        - Unsupported audio format errors (400)
      operationId: realtime-transcription
      parameters:
        - in: query
          name: model
          required: true
          schema:
            type: string
            description: The Whisper model to use for transcription
        - in: query
          name: input_audio_format
          required: true
          schema:
            type: string
            enum:
              - pcm_s16le_16000
            default: pcm_s16le_16000
          description: >-
            Audio format specification. Currently supports 16-bit PCM at 16kHz
            sample rate.
      responses:
        '101':
          description: |
            Switching Protocols - WebSocket connection established successfully.

            Error message format:
            ```json
            {
              "type": "conversation.item.input_audio_transcription.failed",
              "error": {
                "message": "Error description",
                "type": "invalid_request_error",
                "param": null,
                "code": "error_code"
              }
            }
            ```
      x-codeSamples:
        - lang: Python
          label: Python WebSocket Client
          source: |
            import asyncio
            import websockets
            import json
            import base64
            import os

            async def transcribe_audio():
                api_key = os.environ.get("TOGETHER_API_KEY")
                url = "wss://api.together.ai/v1/realtime?model=openai/whisper-large-v3&input_audio_format=pcm_s16le_16000"

                headers = {
                    "Authorization": f"Bearer {api_key}"
                }

                async with websockets.connect(url, additional_headers=headers) as ws:
                    # Read audio file
                    with open("audio.wav", "rb") as f:
                        audio_data = f.read()

                    # Send audio in chunks with delay to simulate real-time
                    chunk_size = 8192
                    bytes_per_second = 16000 * 2  # 16kHz * 2 bytes (16-bit)
                    delay_per_chunk = chunk_size / bytes_per_second

                    for i in range(0, len(audio_data), chunk_size):
                        chunk = audio_data[i:i+chunk_size]
                        base64_chunk = base64.b64encode(chunk).decode('utf-8')
                        await ws.send(json.dumps({
                            "type": "input_audio_buffer.append",
                            "audio": base64_chunk
                        }))
                        # Simulate real-time streaming
                        if i + chunk_size < len(audio_data):
                            await asyncio.sleep(delay_per_chunk)

                    # Commit the audio buffer
                    await ws.send(json.dumps({
                        "type": "input_audio_buffer.commit"
                    }))

                    # Receive transcription results
                    async for message in ws:
                        data = json.loads(message)
                        if data["type"] == "conversation.item.input_audio_transcription.delta":
                            print(f"Partial: {data['delta']}")
                        elif data["type"] == "conversation.item.input_audio_transcription.completed":
                            print(f"Final: {data['transcript']}")
                            break
                        elif data["type"] == "conversation.item.input_audio_transcription.failed":
                            error = data.get("error", {})
                            print(f"Error: {error.get('message')}")
                            break

            asyncio.run(transcribe_audio())
        - lang: JavaScript
          label: Node.js WebSocket Client
          source: >
            import WebSocket from 'ws';

            import fs from 'fs';


            const apiKey = process.env.TOGETHER_API_KEY;

            const url =
            'wss://api.together.ai/v1/realtime?model=openai/whisper-large-v3&input_audio_format=pcm_s16le_16000';


            const ws = new WebSocket(url, {
              headers: {
                'Authorization': `Bearer ${apiKey}`
              }
            });


            ws.on('open', async () => {
              console.log('WebSocket connection established!');

              // Read audio file
              const audioData = fs.readFileSync('audio.wav');

              // Send audio in chunks with delay to simulate real-time
              const chunkSize = 8192;
              const bytesPerSecond = 16000 * 2;  // 16kHz * 2 bytes (16-bit)
              const delayPerChunk = (chunkSize / bytesPerSecond) * 1000;  // Convert to ms

              for (let i = 0; i < audioData.length; i += chunkSize) {
                const chunk = audioData.slice(i, i + chunkSize);
                const base64Chunk = chunk.toString('base64');
                ws.send(JSON.stringify({
                  type: 'input_audio_buffer.append',
                  audio: base64Chunk
                }));

                // Simulate real-time streaming
                if (i + chunkSize < audioData.length) {
                  await new Promise(resolve => setTimeout(resolve, delayPerChunk));
                }
              }

              // Commit audio buffer
              ws.send(JSON.stringify({
                type: 'input_audio_buffer.commit'
              }));
            });


            ws.on('message', (data) => {
              const message = JSON.parse(data.toString());

              if (message.type === 'conversation.item.input_audio_transcription.delta') {
                console.log(`Partial: ${message.delta}`);
              } else if (message.type === 'conversation.item.input_audio_transcription.completed') {
                console.log(`Final: ${message.transcript}`);
                ws.close();
              } else if (message.type === 'conversation.item.input_audio_transcription.failed') {
                const errorMessage = message.error?.message ?? message.message ?? 'Unknown error';
                console.error(`Error: ${errorMessage}`);
                ws.close();
              }
            });


            ws.on('error', (error) => {
              console.error('WebSocket error:', error);
            });
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).