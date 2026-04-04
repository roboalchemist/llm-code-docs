# Source: https://docs.argil.ai/api-reference/endpoint/voices.get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a Voice by id

> Returns a single Voice identified by its id



## OpenAPI

````yaml get /voices/{id}
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
  /voices/{id}:
    get:
      summary: Get a Voice by id
      description: Returns a single Voice identified by its id
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            description: The id of the Voice to retrieve
      responses:
        '200':
          description: Detailed information about the Voice
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Voice'
        '404':
          description: Voice not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
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
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````