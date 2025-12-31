# Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-tts-api-keys-partial-update.md

# Set TTS API keys

> Allows adding or updating TTS provider API keys to an account, enabling ExternalVoices

This is not necessary for using the service's included voices or your own voice clones added to the service.


## OpenAPI

````yaml patch /api/accounts/me/tts_api_keys
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
    patch:
      tags:
        - accounts
      operationId: accounts_me_tts_api_keys_partial_update
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedSetTtsApiKeysRequest'
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
    PatchedSetTtsApiKeysRequest:
      type: object
      properties:
        elevenLabs:
          type: string
          nullable: true
          description: |-
            Your ElevenLabs API key.
            https://elevenlabs.io/app/settings/api-keys
        cartesia:
          type: string
          nullable: true
          description: |-
            Your Cartesia API key.
            https://play.cartesia.ai/keys
        lmnt:
          type: string
          nullable: true
          description: |-
            Your LMNT API key.
            https://app.lmnt.com/account#api-keys
        google:
          type: string
          nullable: true
          description: >-
            A service account JSON key for your Google Cloud project with the
            Text-to-Speech API enabled.

            https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries#before-you-begin

            https://cloud.google.com/iam/docs/keys-create-delete#creating
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt