# Source: https://docs.venice.ai/api-reference/endpoint/characters/get.md

# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/get.md

# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/get.md

# Source: https://docs.venice.ai/api-reference/endpoint/characters/get.md

# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/get.md

# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/get.md

# Source: https://docs.venice.ai/api-reference/endpoint/characters/get.md

# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/get.md

# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/get.md

# Source: https://docs.venice.ai/api-reference/endpoint/characters/get.md

# Get Character

> This is a preview API and may change. Returns a single character by its slug.

## OpenAPI

````yaml GET /characters/{slug}
paths:
  path: /characters/{slug}
  method: get
  servers:
    - url: https://api.venice.ai/api/v1
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        slug:
          schema:
            - type: string
              required: true
              description: The slug of the character to retrieve
              example: alan-watts
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
              data:
                allOf:
                  - type: object
                    properties:
                      adult:
                        type: boolean
                        description: Whether the character is considered adult content
                        example: false
                      createdAt:
                        type: string
                        description: Date when the character was created
                        example: '2024-12-20T21:28:08.934Z'
                      description:
                        type: string
                        nullable: true
                        description: Description of the character
                        example: >-
                          Alan Watts (6 January 1915 – 16 November 1973) was a
                          British and American writer, speaker, and self-styled
                          "philosophical entertainer", known for interpreting
                          and popularizing Buddhist, Taoist, and Hindu
                          philosophy for a Western audience.
                      name:
                        type: string
                        description: Name of the character
                        example: Alan Watts
                      shareUrl:
                        type: string
                        nullable: true
                        description: Share URL of the character
                        example: https://venice.ai/c/alan-watts
                      photoUrl:
                        type: string
                        nullable: true
                        description: URL of the character photo
                        example: >-
                          https://outerface.venice.ai/api/characters/2f460055-7595-4640-9cb6-c442c4c869b0/photo
                      slug:
                        type: string
                        description: >-
                          Slug of the character to be used in the completions
                          API
                        example: alan-watts
                      stats:
                        type: object
                        properties:
                          imports:
                            type: number
                            description: Number of imports for the character
                            example: 112
                        required:
                          - imports
                      tags:
                        type: array
                        items:
                          type: string
                        description: Tags associated with the character
                        example:
                          - AlanWatts
                          - Philosophy
                          - Buddhism
                          - Taoist
                          - Hindu
                      updatedAt:
                        type: string
                        description: Date when the character was last updated
                        example: '2025-02-09T03:23:53.708Z'
                      webEnabled:
                        type: boolean
                        description: Whether the character is enabled for web use
                        example: true
                      modelId:
                        type: string
                        description: API model ID for the character
                        example: venice-uncensored
                    required:
                      - adult
                      - createdAt
                      - description
                      - name
                      - shareUrl
                      - photoUrl
                      - slug
                      - stats
                      - tags
                      - updatedAt
                      - webEnabled
                      - modelId
              object:
                allOf:
                  - type: string
                    enum:
                      - character
            requiredProperties:
              - data
              - object
        examples:
          example:
            value:
              data:
                adult: false
                createdAt: '2024-12-20T21:28:08.934Z'
                description: >-
                  Alan Watts (6 January 1915 – 16 November 1973) was a British
                  and American writer, speaker, and self-styled "philosophical
                  entertainer", known for interpreting and popularizing
                  Buddhist, Taoist, and Hindu philosophy for a Western audience.
                name: Alan Watts
                shareUrl: https://venice.ai/c/alan-watts
                photoUrl: >-
                  https://outerface.venice.ai/api/characters/2f460055-7595-4640-9cb6-c442c4c869b0/photo
                slug: alan-watts
                stats:
                  imports: 112
                tags:
                  - AlanWatts
                  - Philosophy
                  - Buddhism
                  - Taoist
                  - Hindu
                updatedAt: '2025-02-09T03:23:53.708Z'
                webEnabled: true
                modelId: venice-uncensored
              object: character
        description: OK
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: &ref_1
              - error
        examples:
          example:
            value:
              error: <string>
        description: Authentication failed
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Character not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: An unknown error occurred
  deprecated: false
  type: path
components:
  schemas: {}

````