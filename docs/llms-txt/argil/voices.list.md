# Source: https://docs.argil.ai/api-reference/endpoint/voices.list.md

# List all voices

> Returns an array of Voice objects available for the user

## OpenAPI

````yaml get /voices
paths:
  path: /voices
  method: get
  servers:
    - url: https://api.argil.ai/v1
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: API key to be included in the x-api-key header
          cookie: {}
    parameters:
      path: {}
      query:
        language:
          schema:
            - type: enum<string>
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
              required: false
              description: Filter voices by language
        gender:
          schema:
            - type: enum<string>
              enum:
                - MALE
                - FEMALE
              required: false
              description: Filter voices by gender
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Voice'
        examples:
          example:
            value:
              - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                createAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                status: <string>
                sampleUrl: <string>
                language: ENGLISH
                gender: MALE
        description: An array of voices
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - type: integer
                    format: int32
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              code: 123
              message: <string>
        description: Unexpected error
  deprecated: false
  type: path
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
        createAt:
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

````