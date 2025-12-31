# Source: https://docs.anchorbrowser.io/api-reference/profiles/create-profile.md

# Create Profile

> Creates a new profile from a browser session. A Profile stores cookies, local storage, and cache.

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/profiles
paths:
  path: /v1/profiles
  method: post
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: The name of the profile.
              description:
                allOf:
                  - type: string
                    description: A description of the profile.
              source:
                allOf:
                  - type: string
                    description: >-
                      The source of the profile data. currently only `session`
                      is supported.
                    enum:
                      - session
              session_id:
                allOf:
                  - type: string
                    format: uuid
                    description: >-
                      The browser session ID is required if the source is set to
                      `session`. The browser session must be running, and the
                      profile will be stored once the browser session
                      terminates.
              dedicated_sticky_ip:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to use a dedicated sticky IP for this profile.
                      Defaults to false.
            required: true
            refIdentifier: '#/components/schemas/ProfileRequestSchema'
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: <string>
              description: <string>
              source: session
              session_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              dedicated_sticky_ip: true
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
                      status:
                        type: string
            refIdentifier: '#/components/schemas/SuccessResponse'
        examples:
          example:
            value:
              data:
                status: <string>
        description: Profile created successfully.
    '400':
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
        description: Invalid request or input.
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
        description: Session not found or unreachable.
    '409':
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
        description: Profile name already exists.
    '501':
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
        description: Feature not implemented.
  deprecated: false
  type: path
components:
  schemas: {}

````