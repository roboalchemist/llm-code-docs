# Source: https://developers.kit.com/api-reference/broadcasts/list-broadcasts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List broadcasts



## OpenAPI

````yaml api-reference/v4.json get /v4/broadcasts
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/broadcasts:
    get:
      tags:
        - Broadcasts
      summary: List broadcasts
      parameters:
        - name: after
          description: To fetch next page of results, use `?after=<end_cursor>`
          in: query
          required: false
          schema:
            nullable: true
        - name: before
          description: To fetch previous page of results, use `?before=<start_cursor>`
          in: query
          required: false
          schema:
            nullable: true
        - name: include_total_count
          description: >-
            To include the total count of records in the response, use `true`.
            For large collections, expect a slightly slower response.
          in: query
          required: false
          schema:
            type: boolean
          example: false
        - name: per_page
          description: Number of results per page. Default 500, maximum 1000.
          in: query
          required: false
          schema:
            nullable: true
      responses:
        '200':
          description: >-
            Returns a paginated list of all broadcasts for your account
            (including draft, scheduled, and already sent)
          content:
            application/json:
              schema:
                type: object
                properties:
                  broadcasts:
                    type: array
                    items:
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
                  pagination:
                    type: object
                    properties:
                      has_previous_page:
                        type: boolean
                      has_next_page:
                        type: boolean
                      start_cursor:
                        type: string
                      end_cursor:
                        type: string
                      per_page:
                        type: integer
                    required:
                      - has_previous_page
                      - has_next_page
                      - start_cursor
                      - end_cursor
                      - per_page
                required:
                  - broadcasts
                  - pagination
              example:
                broadcasts:
                  - id: 3
                    publication_id: 3
                    created_at: '2023-02-17T11:43:55Z'
                    subject: Campaign subject 3
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
                  - id: 2
                    publication_id: 2
                    created_at: '2023-02-17T11:43:55Z'
                    subject: Campaign subject 2
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
                  - id: 1
                    publication_id: 1
                    created_at: '2023-02-17T11:43:55Z'
                    subject: Campaign subject 1
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
                pagination:
                  has_previous_page: false
                  has_next_page: false
                  start_cursor: WzNd
                  end_cursor: WzFd
                  per_page: 500
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