# Source: https://developers.kit.com/api-reference/subscribers/bulk-create-subscribers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk create subscribers

> See "[Bulk & async processing](#bulk-amp-async-processing)" for more information.



## OpenAPI

````yaml api-reference/v4.json post /v4/bulk/subscribers
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/bulk/subscribers:
    post:
      tags:
        - Subscribers
      summary: Bulk create subscribers
      description: >-
        See "[Bulk & async processing](#bulk-amp-async-processing)" for more
        information.
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                subscribers:
                  type: array
                  items:
                    type: object
                    properties:
                      first_name:
                        type: string
                        nullable: true
                      email_address:
                        type: string
                        nullable: true
                      state:
                        type: string
                        nullable: true
                        enum:
                          - active
                          - cancelled
                          - bounced
                          - complained
                          - inactive
                callback_url:
                  type: string
                  nullable: true
              required:
                - subscribers
            example:
              subscribers:
                - first_name: Test Subscriber 0
                  email_address: subscriber_0@convertkit.dev
                - first_name: Test Subscriber 1
                  email_address: subscriber_1@convertkit.dev
                - first_name: Test Subscriber 2
                  email_address: subscriber_2@convertkit.dev
                - first_name: Test Subscriber 3
                  email_address: subscriber_3@convertkit.dev
              callback_url: null
      responses:
        '200':
          description: >-
            Creates or updates the subscribers synchronously when 100 or less
            subscribers are requested
          content:
            application/json:
              schema:
                type: object
                properties:
                  subscribers:
                    type: array
                    items:
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
                      required:
                        - id
                        - first_name
                        - email_address
                        - state
                        - created_at
                  failures:
                    type: array
                    items:
                      type: object
                      properties:
                        subscriber:
                          type: object
                          properties:
                            first_name:
                              type: string
                            email_address:
                              type: string
                              nullable: true
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
                              nullable: true
                          required:
                            - first_name
                            - email_address
                            - state
                            - created_at
                        errors:
                          type: array
                          items:
                            type: string
                      required:
                        - subscriber
                        - errors
                required:
                  - subscribers
                  - failures
              example:
                subscribers:
                  - id: 508
                    first_name: null
                    email_address: brooke@convertkit.dev
                    state: active
                    created_at: '2023-02-17T11:43:55Z'
                  - id: 509
                    first_name: Camille
                    email_address: camille@convertkit.dev
                    state: active
                    created_at: '2023-02-17T11:43:55Z'
                  - id: 507
                    first_name: Alice
                    email_address: alice@convertkit.dev
                    state: active
                    created_at: '2023-02-17T11:43:55Z'
                failures:
                  - subscriber:
                      first_name: Benito
                      email_address: null
                      state: active
                      created_at: null
                    errors:
                      - Email address is invalid
        '202':
          description: >-
            Creates or updates subscribers asynchronously when more than 100
            subscribers are requested
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example: {}
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
            Returns a 403 when the number of subscribers in the request would
            exceed the account's subscriber limit
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
                  - This request would exceed your subscriber limit
        '413':
          description: >-
            Returns a 413 when the size of the request would exceed the
            account's data limit for enqueued bulk requests
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
                    This request exceeds your queued bulk requests limit. Please
                    wait while we process your existing requests and try again
                    later.
        '422':
          description: Returns a 422 when `subscribers` is empty or not an array
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
                  - No subscribers included for processing
      security:
        - OAuth2: []
components:
  securitySchemes:
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