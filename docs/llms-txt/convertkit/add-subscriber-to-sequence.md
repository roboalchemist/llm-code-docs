# Source: https://developers.kit.com/api-reference/sequences/add-subscriber-to-sequence.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add subscriber to sequence

> The subscriber being added to the sequence must already exist. Subscribers can be created using the "[Create a subscriber](#create-a-subscriber)" endpoint.



## OpenAPI

````yaml api-reference/v4.json post /v4/sequences/{sequence_id}/subscribers/{id}
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/sequences/{sequence_id}/subscribers/{id}:
    post:
      tags:
        - Sequences
      summary: Add subscriber to sequence
      description: >-
        The subscriber being added to the sequence must already exist.
        Subscribers can be created using the "[Create a
        subscriber](#create-a-subscriber)" endpoint.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          example: 881
        - name: sequence_id
          in: path
          required: true
          schema:
            type: integer
          example: 66
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
            example: {}
      responses:
        '200':
          description: >-
            Returns a 200 when the subscriber has already been added to the
            sequence
          content:
            application/json:
              schema:
                type: object
                properties:
                  subscriber:
                    type: object
                    properties:
                      id:
                        type: integer
                      first_name:
                        type: string
                        nullable: true
                      email_address:
                        type: string
                      state:
                        type: string
                        enum:
                          - active
                          - cancelled
                          - bounced
                          - complained
                          - inactive
                      created_at:
                        type: string
                      added_at:
                        type: string
                      fields:
                        type: object
                        properties: {}
                    required:
                      - id
                      - first_name
                      - email_address
                      - state
                      - created_at
                      - added_at
                      - fields
                required:
                  - subscriber
              example:
                subscriber:
                  id: 877
                  first_name: Alice
                  email_address: alice@convertkit.dev
                  state: active
                  created_at: '2023-02-17T11:43:55Z'
                  added_at: '2023-02-17T11:43:55Z'
                  fields: {}
        '201':
          description: Adds the subscriber to the sequence
          content:
            application/json:
              schema:
                type: object
                properties:
                  subscriber:
                    type: object
                    properties:
                      id:
                        type: integer
                      first_name:
                        type: string
                        nullable: true
                      email_address:
                        type: string
                      state:
                        type: string
                        enum:
                          - active
                          - cancelled
                          - bounced
                          - complained
                          - inactive
                      created_at:
                        type: string
                      added_at:
                        type: string
                      fields:
                        type: object
                        properties: {}
                    required:
                      - id
                      - first_name
                      - email_address
                      - state
                      - created_at
                      - added_at
                      - fields
                required:
                  - subscriber
              example:
                subscriber:
                  id: 878
                  first_name: Alice
                  email_address: alice@convertkit.dev
                  state: active
                  created_at: '2023-02-17T11:43:55Z'
                  added_at: '2023-02-17T11:43:55Z'
                  fields: {}
        '401':
          description: Returns a 401 if the token and/or account cannot be authenticated
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - The access token is invalid
        '404':
          description: Returns a 404 when the provided id does not exist
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - Not Found
      security:
        - API Key: []
        - OAuth2: []
components:
  securitySchemes:
    API Key:
      description: Authenticate API requests via an API Key
      type: apiKey
      in: header
      name: X-Kit-Api-Key
    OAuth2:
      description: Authenticate API requests via an OAuth token
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://api.kit.com/v4/oauth/authorize
          tokenUrl: https://api.kit.com/v4/oauth/token
          refreshUrl: https://api.kit.com/v4/oauth/token
          scopes:
            read: Read access to Kit API v4
            write: Write access to Kit API v4

````

Built with [Mintlify](https://mintlify.com).