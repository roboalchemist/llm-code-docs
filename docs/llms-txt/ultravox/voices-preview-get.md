# Source: https://docs.ultravox.ai/api-reference/voices/voices-preview-get.md

# Get Voice Sample

> Provides an audio sample for a voice, or the error caused by using it.



## OpenAPI

````yaml get /api/voices/{voice_id}/preview
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/voices/{voice_id}/preview:
    get:
      tags:
        - voices
      description: Provides an audio sample for a voice, or the error caused by using it.
      operationId: voices_preview_retrieve
      parameters:
        - in: path
          name: voice_id
          schema:
            type: string
            format: uuid
          required: true
      responses:
        '200':
          content:
            audio/wav:
              schema:
                type: string
                format: binary
          description: ''
        '302':
          description: No response body
        '400':
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: ''
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt