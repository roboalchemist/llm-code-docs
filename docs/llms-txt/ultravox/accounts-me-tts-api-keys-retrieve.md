# Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-tts-api-keys-retrieve.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Account TTS API Keys

> Returns the TTS provider API keys associated with the active account

Only key prefixes are included and only for providers for which a key has been added.


## OpenAPI

````yaml get /api/accounts/me/tts_api_keys
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/accounts/me/tts_api_keys:
    get:
      tags:
        - accounts
      operationId: accounts_me_tts_api_keys_retrieve
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountTtsKeys'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    AccountTtsKeys:
      type: object
      properties:
        elevenLabs:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The ElevenLabs API key.
        cartesia:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The Cartesia API key.
        lmnt:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The LMNT API key.
        google:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The Google service account key.
        inworld:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The Inworld API key.
        respeecher:
          allOf:
            - $ref: '#/components/schemas/KeyPrefix'
          description: The Respeecher API key.
    KeyPrefix:
      type: object
      properties:
        prefix:
          type: string
          description: The prefix of the API key.
      required:
        - prefix
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````