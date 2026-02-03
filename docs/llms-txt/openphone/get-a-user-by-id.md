# Source: https://www.quo.com/docs/mdx/api-reference/users/get-a-user-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a user by ID

> Retrieve detailed information about a specific user in your OpenPhone workspace using the user's unique identifier.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/users/{userId}
openapi: 3.1.0
info:
  title: OpenPhone Public API
  version: 1.0.0
  description: API for connecting with OpenPhone.
  contact:
    name: OpenPhone Support
    email: support@openphone.com
    url: https://support.openphone.com/hc/en-us
  termsOfService: https://www.openphone.com/terms
servers:
  - description: Production server
    url: https://api.openphone.com
security:
  - apiKey: []
tags:
  - description: Operations related to calls
    name: Calls
  - description: >-
      Operations related to call summaries, including AI-generated summaries and
      Sona voice assistant summaries
    name: Call Summaries
  - description: >-
      Operations related to call transcripts, including AI-generated transcripts
      and Sona voice assistant transcripts
    name: Call Transcripts
  - description: Operations related to contacts
    name: Contacts
  - description: Operations related to conversations
    name: Conversations
  - description: Operations related to text messages
    name: Messages
  - description: Operations related to phone numbers
    name: Phone Numbers
  - description: Operations related to users
    name: Users
  - description: Operations related to webhooks
    name: Webhooks
paths:
  /v1/users/{userId}:
    get:
      tags:
        - Users
      summary: Get a user by ID
      description: >-
        Retrieve detailed information about a specific user in your OpenPhone
        workspace using the user's unique identifier.
      operationId: getUserById_v1
      parameters:
        - in: path
          name: userId
          required: true
          schema:
            description: The unique identifier of the user being retrieved.
            examples:
              - US123abc
            pattern: ^US(.*)$
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      id:
                        pattern: ^US(.*)$
                        type: string
                      email:
                        description: The user's email address.
                        examples:
                          - my@email.com
                        format: email
                        type: string
                      firstName:
                        anyOf:
                          - description: The user's first name.
                            examples:
                              - John
                            type: string
                          - type: 'null'
                      lastName:
                        anyOf:
                          - description: The user's last name.
                            examples:
                              - Doe
                            type: string
                          - type: 'null'
                      pictureUrl:
                        anyOf:
                          - description: The user's picture URL.
                            examples:
                              - https://example.com/picture.jpg
                            format: uri
                            type: string
                          - type: 'null'
                      role:
                        type: string
                        enum:
                          - owner
                          - admin
                          - member
                        description: The user's role in the organization.
                        examples:
                          - owner
                          - admin
                          - member
                      createdAt:
                        description: Timestamp of user creation in ISO 8601 format.
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                      updatedAt:
                        description: Timestamp of last user update in ISO 8601 format.
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                    required:
                      - id
                      - email
                      - firstName
                      - lastName
                      - pictureUrl
                      - role
                      - createdAt
                      - updatedAt
                required:
                  - data
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '1100400'
                    type: string
                  status:
                    const: 400
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Bad Request
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '1100401'
                    type: string
                  status:
                    const: 401
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unauthorized
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '1100403'
                    type: string
                  status:
                    const: 403
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Forbidden
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '1100404'
                    type: string
                  status:
                    const: 404
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Not Found
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '500':
          description: Unknown Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '1101500'
                    type: string
                  status:
                    const: 500
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unknown
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      in: header
      name: Authorization
      type: apiKey

````