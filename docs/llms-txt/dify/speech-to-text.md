# Source: https://docs.dify.ai/api-reference/tts/speech-to-text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Speech to Text

> Convert audio file to text. Supported formats: mp3, mp4, mpeg, mpga, m4a, wav, webm. File size limit: 15MB.



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json post /audio-to-text
openapi: 3.0.1
info:
  title: Advanced Chat App API
  description: >-
    Chat applications support session persistence, allowing previous chat
    history to be used as context for responses. This can be applicable for
    chatbot, customer service AI, etc. This version includes advanced features
    like workflow events and more detailed file type support.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Advanced Chat App API. Replace {api_base_url} with
      the actual API base URL provided for your application (e.g., from
      props.appDetail.api_base_url).
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Chatflow
    description: Advanced chat operations with workflow events.
  - name: Files
    description: File upload and preview operations for advanced chat.
  - name: End Users
    description: Operations related to end user information.
  - name: Feedback
    description: User feedback operations for advanced chat.
  - name: Conversations
    description: Conversation management for advanced chat.
  - name: TTS
    description: Speech and Text conversion for advanced chat.
  - name: Application
    description: Application settings and info for advanced chat.
  - name: Annotations
    description: Annotation management for advanced chat.
paths:
  /audio-to-text:
    post:
      tags:
        - TTS
      summary: Speech to Text
      description: >-
        Convert audio file to text. Supported formats: mp3, mp4, mpeg, mpga,
        m4a, wav, webm. File size limit: 15MB.
      operationId: advancedAudioToText
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/AudioToTextRequest'
      responses:
        '200':
          description: Successfully converted audio to text.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AudioToTextResponse'
components:
  schemas:
    AudioToTextRequest:
      type: object
      required:
        - file
        - user
      properties:
        file:
          type: string
          format: binary
          description: >-
            Audio file. Formats: mp3, mp4, mpeg, mpga, m4a, wav, webm. Limit:
            15MB.
        user:
          type: string
    AudioToTextResponse:
      type: object
      properties:
        text:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).