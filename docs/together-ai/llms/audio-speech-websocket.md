# Source: https://docs.together.ai/reference/audio-speech-websocket.md

# Create realtime text-to-speech

> Establishes a WebSocket connection for real-time text-to-speech generation. This endpoint uses WebSocket protocol (wss://api.together.ai/v1/audio/speech/websocket) for bidirectional streaming communication.

**Connection Setup:**
- Protocol: WebSocket (wss://)
- Authentication: Pass API key as Bearer token in Authorization header
- Parameters: Sent as query parameters (model, voice, max_partial_length)

**Client Events:**
- `tts_session.updated`: Update session parameters like voice
  ```json
  {
    "type": "tts_session.updated",
    "session": {
      "voice": "tara"
    }
  }
  ```
- `input_text_buffer.append`: Send text chunks for TTS generation
  ```json
  {
    "type": "input_text_buffer.append",
    "text": "Hello, this is a test."
  }
  ```
- `input_text_buffer.clear`: Clear the buffered text
  ```json
  {
    "type": "input_text_buffer.clear"
  }
  ```
- `input_text_buffer.commit`: Signal end of text input and process remaining text
  ```json
  {
    "type": "input_text_buffer.commit"
  }
  ```

**Server Events:**
- `session.created`: Initial session confirmation (sent first)
  ```json
  {
    "event_id": "evt_123456",
    "type": "session.created",
    "session": {
      "id": "session-id",
      "object": "realtime.tts.session",
      "modalities": ["text", "audio"],
      "model": "hexgrad/Kokoro-82M",
      "voice": "tara"
    }
  }
  ```
- `conversation.item.input_text.received`: Acknowledgment that text was received
  ```json
  {
    "type": "conversation.item.input_text.received",
    "text": "Hello, this is a test."
  }
  ```
- `conversation.item.audio_output.delta`: Audio chunks as base64-encoded data
  ```json
  {
    "type": "conversation.item.audio_output.delta",
    "item_id": "tts_1",
    "delta": "<base64_encoded_audio_chunk>"
  }
  ```
- `conversation.item.audio_output.done`: Audio generation complete for an item
  ```json
  {
    "type": "conversation.item.audio_output.done",
    "item_id": "tts_1"
  }
  ```
- `conversation.item.tts.failed`: Error occurred
  ```json
  {
    "type": "conversation.item.tts.failed",
    "error": {
      "message": "Error description",
      "type": "invalid_request_error",
      "param": null,
      "code": "invalid_api_key"
    }
  }
  ```

**Text Processing:**
- Partial text (no sentence ending) is held in buffer until:
  - We believe that the text is complete enough to be processed for TTS generation
  - The partial text exceeds `max_partial_length` characters (default: 250)
  - The `input_text_buffer.commit` event is received

**Audio Format:**
- Format: WAV (PCM s16le)
- Sample Rate: 24000 Hz
- Encoding: Base64
- Delivered via `conversation.item.audio_output.delta` events

**Error Codes:**
- `invalid_api_key`: Invalid API key provided (401)
- `missing_api_key`: Authorization header missing (401)
- `model_not_available`: Invalid or unavailable model (400)
- Invalid text format errors (400)




## OpenAPI

````yaml GET /audio/speech/websocket
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
  /audio/speech/websocket:
    get:
      tags:
        - Audio
      summary: Real-time text-to-speech via WebSocket
      description: >
        Establishes a WebSocket connection for real-time text-to-speech
        generation. This endpoint uses WebSocket protocol
        (wss://api.together.ai/v1/audio/speech/websocket) for bidirectional
        streaming communication.


        **Connection Setup:**

        - Protocol: WebSocket (wss://)

        - Authentication: Pass API key as Bearer token in Authorization header

        - Parameters: Sent as query parameters (model, voice,
        max_partial_length)


        **Client Events:**

        - `tts_session.updated`: Update session parameters like voice
          ```json
          {
            "type": "tts_session.updated",
            "session": {
              "voice": "tara"
            }
          }
          ```
        - `input_text_buffer.append`: Send text chunks for TTS generation
          ```json
          {
            "type": "input_text_buffer.append",
            "text": "Hello, this is a test."
          }
          ```
        - `input_text_buffer.clear`: Clear the buffered text
          ```json
          {
            "type": "input_text_buffer.clear"
          }
          ```
        - `input_text_buffer.commit`: Signal end of text input and process
        remaining text
          ```json
          {
            "type": "input_text_buffer.commit"
          }
          ```

        **Server Events:**

        - `session.created`: Initial session confirmation (sent first)
          ```json
          {
            "event_id": "evt_123456",
            "type": "session.created",
            "session": {
              "id": "session-id",
              "object": "realtime.tts.session",
              "modalities": ["text", "audio"],
              "model": "hexgrad/Kokoro-82M",
              "voice": "tara"
            }
          }
          ```
        - `conversation.item.input_text.received`: Acknowledgment that text was
        received
          ```json
          {
            "type": "conversation.item.input_text.received",
            "text": "Hello, this is a test."
          }
          ```
        - `conversation.item.audio_output.delta`: Audio chunks as base64-encoded
        data
          ```json
          {
            "type": "conversation.item.audio_output.delta",
            "item_id": "tts_1",
            "delta": "<base64_encoded_audio_chunk>"
          }
          ```
        - `conversation.item.audio_output.done`: Audio generation complete for
        an item
          ```json
          {
            "type": "conversation.item.audio_output.done",
            "item_id": "tts_1"
          }
          ```
        - `conversation.item.tts.failed`: Error occurred
          ```json
          {
            "type": "conversation.item.tts.failed",
            "error": {
              "message": "Error description",
              "type": "invalid_request_error",
              "param": null,
              "code": "invalid_api_key"
            }
          }
          ```

        **Text Processing:**

        - Partial text (no sentence ending) is held in buffer until:
          - We believe that the text is complete enough to be processed for TTS generation
          - The partial text exceeds `max_partial_length` characters (default: 250)
          - The `input_text_buffer.commit` event is received

        **Audio Format:**

        - Format: WAV (PCM s16le)

        - Sample Rate: 24000 Hz

        - Encoding: Base64

        - Delivered via `conversation.item.audio_output.delta` events


        **Error Codes:**

        - `invalid_api_key`: Invalid API key provided (401)

        - `missing_api_key`: Authorization header missing (401)

        - `model_not_available`: Invalid or unavailable model (400)

        - Invalid text format errors (400)
      operationId: realtime-tts
      parameters:
        - in: query
          name: model
          required: false
          schema:
            type: string
            enum:
              - hexgrad/Kokoro-82M
              - cartesia/sonic-english
            default: hexgrad/Kokoro-82M
          description: >-
            The TTS model to use for speech generation. Can also be set via
            `tts_session.updated` event.
        - in: query
          name: voice
          required: false
          schema:
            type: string
            default: tara
          description: >
            The voice to use for speech generation. Default is 'tara'.

            Available voices vary by model. Can also be updated via
            `tts_session.updated` event.
        - in: query
          name: max_partial_length
          required: false
          schema:
            type: integer
            default: 250
          description: >
            Maximum number of characters in partial text before forcing TTS
            generation

            even without a sentence ending. Helps reduce latency for long text
            without punctuation.
      responses:
        '101':
          description: |
            Switching Protocols - WebSocket connection established successfully.

            Error message format:
            ```json
            {
              "type": "conversation.item.tts.failed",
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