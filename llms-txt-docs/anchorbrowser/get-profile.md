# Source: https://docs.anchorbrowser.io/api-reference/profiles/get-profile.md

# Get Profile

> Retrieves details of a specific profile by its name.

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/profiles/{name}
paths:
  path: /v1/profiles/{name}
  method: get
  servers:
    - url: https://api.anchorbrowser.io
      description: API server
  request:
    security:
      - title: api key header
        parameters:
          query: {}
          header:
            anchor-api-key:
              type: apiKey
              description: API key passed in the header
          cookie: {}
    parameters:
      path:
        name:
          schema:
            - type: string
              required: true
              description: The name of the profile to retrieve.
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
                  - $ref: '#/components/schemas/ProfileResponseSchema'
            refIdentifier: '#/components/schemas/ProfileResponse'
        examples:
          example:
            value:
              data:
                name: <string>
                description: <string>
                source: session
                session_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                status: <string>
                created_at: '2023-11-07T05:31:56Z'
        description: Profile details retrieved successfully.
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Invalid API Key.
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Profile not found.
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Unable to retrieve profile due to an unexpected error.
  deprecated: false
  type: path
components:
  schemas:
    ProfileResponseSchema:
      type: object
      properties:
        name:
          type: string
          description: The name of the profile.
        description:
          type: string
          description: A description of the profile.
        source:
          type: string
          description: The source of the profile data.
          enum:
            - session
        session_id:
          type: string
          format: uuid
          description: The browser session ID used to create this profile, if applicable.
        status:
          type: string
          description: The current status of the profile.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the profile was created.

````