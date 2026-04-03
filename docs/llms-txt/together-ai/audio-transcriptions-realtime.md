# Source: https://docs.together.ai/reference/audio-transcriptions-realtime.md

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
            enum:
              - openai/whisper-large-v3
            default: openai/whisper-large-v3
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
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt