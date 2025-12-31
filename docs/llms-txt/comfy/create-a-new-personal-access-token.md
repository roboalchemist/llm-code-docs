# Source: https://docs.comfy.org/api-reference/registry/create-a-new-personal-access-token.md

# Create a new personal access token

## OpenAPI

````yaml https://api.comfy.org/openapi post /publishers/{publisherId}/tokens
paths:
  path: /publishers/{publisherId}/tokens
  method: post
  servers:
    - url: https://api.comfy.org
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
        publisherId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              createdAt:
                allOf:
                  - description: '[Output Only]The date and time the token was created.'
                    format: date-time
                    type: string
              description:
                allOf:
                  - description: >-
                      Optional. A more detailed description of the token's
                      intended use.
                    type: string
              id:
                allOf:
                  - description: Unique identifier for the GitCommit
                    format: uuid
                    type: string
              name:
                allOf:
                  - description: >-
                      Required. The name of the token. Can be a simple
                      description.
                    type: string
              token:
                allOf:
                  - description: >-
                      [Output Only]. The personal access token. Only returned
                      during creation.
                    type: string
            required: true
            refIdentifier: '#/components/schemas/PersonalAccessToken'
        examples:
          example:
            value:
              createdAt: '2023-11-07T05:31:56Z'
              description: <string>
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              name: <string>
              token: <string>
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              token:
                allOf:
                  - description: The newly created personal access token.
                    type: string
        examples:
          example:
            value:
              token: <string>
        description: Token created successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
              message:
                allOf:
                  - &ref_1
                    type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_2
              - error
              - message
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Bad request, invalid input data.
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Forbidden
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas: {}

````