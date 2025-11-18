# Source: https://docs.argil.ai/api-reference/endpoint/voices.get.md

# Get a Voice by id

> Returns a single Voice identified by its id

## OpenAPI

````yaml get /voices/{id}
paths:
  path: /voices/{id}
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The id of the Voice to retrieve
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
              name:
                allOf:
                  - type: string
              createAt:
                allOf:
                  - type: string
                    format: date-time
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
              status:
                allOf:
                  - type: string
              sampleUrl:
                allOf:
                  - type: string
              language:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/VoiceLanguage'
                      - nullable: true
              gender:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/VoiceGender'
                      - nullable: true
            refIdentifier: '#/components/schemas/Voice'
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              name: <string>
              createAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
              status: <string>
              sampleUrl: <string>
              language: ENGLISH
              gender: MALE
        description: Detailed information about the Voice
    '404':
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
        description: Voice not found
  deprecated: false
  type: path
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

````