# Source: https://developers.kit.com/api-reference/broadcasts/update-a-broadcast.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a broadcast

> Update an existing broadcast. Continue to draft or schedule to send a broadcast to all or a subset of your subscribers.<br/><br/>To save a draft, set `public` to false.<br/><br/>To schedule the broadcast for sending, set `public` to true and provide `send_at`. Scheduled broadcasts should contain a subject and your content, at a minimum.<br/><br/>We currently support targeting your subscribers based on segment or tag ids.



## OpenAPI

````yaml api-reference/v4.json put /v4/broadcasts/{id}
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/broadcasts/{id}:
    put:
      tags:
        - Broadcasts
      summary: Update a broadcast
      description: >-
        Update an existing broadcast. Continue to draft or schedule to send a
        broadcast to all or a subset of your subscribers.<br/><br/>To save a
        draft, set `public` to false.<br/><br/>To schedule the broadcast for
        sending, set `public` to true and provide `send_at`. Scheduled
        broadcasts should contain a subject and your content, at a
        minimum.<br/><br/>We currently support targeting your subscribers based
        on segment or tag ids.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          example: 64
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                email_template_id:
                  type: integer
                  description: >-
                    Id of the email template to use. Uses the account's default
                    template if not provided. 'Starting point' template is not
                    supported.
                email_address:
                  type: string
                  nullable: true
                  description: >-
                    The sending email address to use. Uses the account's sending
                    email address if not provided.
                content:
                  type: string
                  description: The HTML content of the email.
                description:
                  type: string
                public:
                  type: boolean
                  description: >-
                    `true` to publish this broadcast to the web. The broadcast
                    will appear in a newsletter feed on your Creator Profile and
                    Landing Pages.
                published_at:
                  type: string
                  description: >-
                    The published timestamp to display in ISO8601 format. If no
                    timezone is provided, UTC is assumed.
                send_at:
                  type: string
                  description: >-
                    The scheduled send time for this broadcast in ISO8601
                    format. If no timezone is provided, UTC is assumed.
                thumbnail_alt:
                  nullable: true
                thumbnail_url:
                  nullable: true
                preview_text:
                  type: string
                subject:
                  type: string
                subscriber_filter:
                  type: array
                  description: >-
                    Filters your subscribers. At this time, we only support
                    using only one filter group type via the API (e.g. `all`,
                    `any`, or `none` but no combinations). If nothing is
                    provided, will default to all of your subscribers.
                  items:
                    type: object
                    properties:
                      all:
                        type: array
                        description: >-
                          Filters your subscribers using a logical AND of all
                          provided segment and tag ids, i.e. a subscriber would
                          have to be part of all segments and tags provided
                        items:
                          type: object
                          properties:
                            type:
                              type: string
                              description: '`segment` or `tag`'
                            ids:
                              type: array
                              items:
                                type: integer
                          required:
                            - type
                            - ids
                      any:
                        type: array
                        description: >-
                          Filters your subscribers using a logical OR of all
                          provided segment and tag ids, i.e. a subscriber would
                          have to be part of at least one of the segments or
                          tags provided
                        items:
                          type: object
                          properties:
                            type:
                              type: string
                              description: '`segment` or `tag`'
                            ids:
                              type: array
                              items:
                                type: integer
                          required:
                            - type
                            - ids
                        nullable: true
                      none:
                        type: array
                        description: >-
                          Filters your subscribers using a logical NOT of all
                          provided segment and tag ids, i.e. a subscriber would
                          have to be in none of the segments or tags provided
                        items:
                          type: object
                          properties:
                            type:
                              type: string
                              description: '`segment` or `tag`'
                            ids:
                              type: array
                              items:
                                type: integer
                          required:
                            - type
                            - ids
                        nullable: true
                    minProperties: 1
                    required:
                      - all
                      - any
                      - none
              required:
                - email_template_id
                - email_address
                - content
                - description
                - public
                - published_at
                - send_at
                - thumbnail_alt
                - thumbnail_url
                - preview_text
                - subject
                - subscriber_filter
            example:
              email_template_id: 2
              email_address: null
              content: <p>Let me introduce myself</p>
              description: Intro email
              public: true
              published_at: '2023-02-17T11:43:55+00:00'
              send_at: '2023-02-17T11:43:55+00:00'
              thumbnail_alt: null
              thumbnail_url: null
              preview_text: Pleased to meet you!
              subject: Hello!
              subscriber_filter:
                - all:
                    - type: segment
                      ids:
                        - 47
                  any: null
                  none: null
      responses:
        '200':
          description: Updates the broadcast and returns its details
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
                      description:
                        type: string
                      content:
                        type: string
                      public:
                        type: boolean
                      published_at:
                        type: string
                      send_at:
                        type: string
                      thumbnail_alt:
                        nullable: true
                      thumbnail_url:
                        nullable: true
                      public_url:
                        type: string
                      email_address:
                        type: string
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
                                  ids:
                                    type: array
                                    items:
                                      type: integer
                                required:
                                  - type
                                  - ids
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
                  id: 55
                  publication_id: 55
                  created_at: '2023-02-17T11:43:55Z'
                  subject: Hello!
                  preview_text: Pleased to meet you!
                  description: Intro email
                  content: <p>Let me introduce myself</p>
                  public: true
                  published_at: '2023-02-17T11:43:55Z'
                  send_at: '2023-02-17T11:43:55Z'
                  thumbnail_alt: null
                  thumbnail_url: null
                  public_url: https://kit-greetings.kit.com/posts/hello
                  email_address: greetings@kit.dev
                  email_template:
                    id: 2
                    name: Classic
                  subscriber_filter:
                    - all:
                        - type: segment
                          ids:
                            - 47
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
        '403':
          description: >-
            Returns a 403 with an error message if the current account is
            unauthorized to create a broadcast
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
                  - >-
                    You do not have sufficient permissions to access this
                    resource. Please contact support.
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
        '422':
          description: >-
            Returns a 422 with an error message when one or more of the
            parameters are invalid or the campaign has already started sending
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
                  - Email template not found
                  - >-
                    Only a single filter group is supported. Use one of `all`,
                    `any`, or `none`.
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