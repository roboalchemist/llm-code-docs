# Source: https://docs.argil.ai/api-reference/endpoint/voices.list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List all voices

> Returns an array of Voice objects available for the user



## OpenAPI

````yaml get /voices
openapi: 3.0.1
info:
  title: Argil API
  description: API for AI clone video generation
  version: 1.0.0
  license:
    name: MIT
servers:
  - url: https://api.argil.ai/v1
security:
  - ApiKeyAuth: []
paths:
  /voices:
    get:
      summary: List all voices
      description: Returns an array of Voice objects available for the user
      parameters:
        - name: language
          in: query
          description: Filter voices by language
          required: false
          schema:
            $ref: '#/components/schemas/VoiceLanguage'
        - name: gender
          in: query
          description: Filter voices by gender
          required: false
          schema:
            $ref: '#/components/schemas/VoiceGender'
      responses:
        '200':
          description: An array of voices
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Voice'
        '400':
          description: Unexpected error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    VoiceLanguage:
      type: string
      enum:
        - ENGLISH
        - SPANISH
        - FRENCH
        - PORTUGUESE
        - BRAZILIAN_PORTUGUESE
        - GERMAN
        - RUSSIAN
        - HINDI
        - CHINESE
        - DUTCH
        - ARABIC
    VoiceGender:
      type: string
      enum:
        - MALE
        - FEMALE
    Voice:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        status:
          type: string
        sampleUrl:
          type: string
        language:
          allOf:
            - $ref: '#/components/schemas/VoiceLanguage'
            - nullable: true
        gender:
          allOf:
            - $ref: '#/components/schemas/VoiceGender'
            - nullable: true
    Error:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````