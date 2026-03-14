# Source: https://developers.kit.com/api-reference/broadcasts/get-a-broadcast.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a broadcast



## OpenAPI

````yaml api-reference/v4.json get /v4/broadcasts/{id}
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/broadcasts/{id}:
    get:
      tags:
        - Broadcasts
      summary: Get a broadcast
      parameters:
        - name: '[]'
          in: query
          required: false
          schema:
            type: string
          example: ''
        - name: id
          in: path
          required: true
          schema:
            type: integer
          example: 24
      responses:
        '200':
          description: Returns the broadcast details
          content:
            application/json:
              schema:
                type: object
                properties:
                  broadcast:
                    type: object
                    properties:
                      id:
                        type: integer
                      publication_id:
                        type: integer
                      created_at:
                        type: string
                      subject:
                        type: string
                      preview_text:
                        type: string
                        nullable: true
                      description:
                        type: string
                        nullable: true
                      content:
                        type: string
                        nullable: true
                      public:
                        type: boolean
                      published_at:
                        type: string
                        nullable: true
                      send_at:
                        type: string
                        nullable: true
                      thumbnail_alt:
                        type: string
                        nullable: true
                      thumbnail_url:
                        type: string
                        nullable: true
                      public_url:
                        type: string
                        nullable: true
                      email_address:
                        type: string
                        nullable: true
                      email_template:
                        type: object
                        properties:
                          id:
                            type: integer
                          name:
                            type: string
                        required:
                          - id
                          - name
                      subscriber_filter:
                        type: array
                        items:
                          type: object
                          properties:
                            all:
                              type: array
                              items:
                                type: object
                                properties:
                                  type:
                                    type: string
                                required:
                                  - type
                          required:
                            - all
                    required:
                      - id
                      - publication_id
                      - created_at
                      - subject
                      - preview_text
                      - description
                      - content
                      - public
                      - published_at
                      - send_at
                      - thumbnail_alt
                      - thumbnail_url
                      - public_url
                      - email_address
                      - email_template
                      - subscriber_filter
                required:
                  - broadcast
              example:
                broadcast:
                  id: 22
                  publication_id: 22
                  created_at: '2023-02-17T11:43:55Z'
                  subject: You'll never guess...
                  preview_text: null
                  description: null
                  content: null
                  public: false
                  published_at: null
                  send_at: null
                  thumbnail_alt: null
                  thumbnail_url: null
                  public_url: null
                  email_address: greetings@kit.dev
                  email_template:
                    id: 6
                    name: Text Only
                  subscriber_filter:
                    - all:
                        - type: all_subscribers
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