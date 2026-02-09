# Source: https://docs.ultravox.ai/api-reference/calls/calls-stages-message-audio-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Call Stage Message Audio

> Gets the audio for the specified message



## OpenAPI

````yaml get /api/calls/{call_id}/stages/{call_stage_id}/messages/{call_stage_message_index}/audio
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/calls/{call_id}/stages/{call_stage_id}/messages/{call_stage_message_index}/audio:
    get:
      tags:
        - calls
      operationId: calls_stages_messages_audio_retrieve
      parameters:
        - in: path
          name: call_id
          schema:
            type: string
            format: uuid
          required: true
        - in: path
          name: call_stage_id
          schema:
            type: string
            format: uuid
          required: true
        - in: path
          name: call_stage_message_index
          schema:
            type: integer
          required: true
      responses:
        '200':
          description: No response body
      security:
        - apiKeyAuth: []
components:
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````