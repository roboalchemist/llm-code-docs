# Source: https://developers.kit.com/api-reference/tags/bulk-tag-subscribers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk tag subscribers

> The subscribers being tagged must already exist. Subscribers can be created in bulk using the "[Bulk create subscriber](#bulk-create-subscribers)" endpoint.<br/><br/>See "[Bulk & async processing](#bulk-amp-async-processing)" for more information.



## OpenAPI

````yaml api-reference/v4.json post /v4/bulk/tags/subscribers
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/bulk/tags/subscribers:
    post:
      tags:
        - Tags
      summary: Bulk tag subscribers
      description: >-
        The subscribers being tagged must already exist. Subscribers can be
        created in bulk using the "[Bulk create
        subscriber](#bulk-create-subscribers)" endpoint.<br/><br/>See "[Bulk &
        async processing](#bulk-amp-async-processing)" for more information.
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                taggings:
                  type: array
                  items:
                    type: object
                    properties:
                      tag_id:
                        type: integer
                        nullable: true
                      subscriber_id:
                        type: integer
                        nullable: true
                    required:
                      - tag_id
                      - subscriber_id
                callback_url:
                  type: string
                  nullable: true
              required:
                - taggings
            example:
              taggings:
                - tag_id: 0
                  subscriber_id: 0
                - tag_id: 1
                  subscriber_id: 1
                - tag_id: 2
                  subscriber_id: 2
                - tag_id: 3
                  subscriber_id: 3
              callback_url: null
      responses:
        '200':
          description: >-
            Creates the taggings synchronously when 100 or less tags/subscribers
            are requested
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
                        email_address:
                          type: string
                        created_at:
                          type: string
                        tagged_at:
                          type: string
                      required:
                        - id
                        - first_name
                        - email_address
                        - created_at
                        - tagged_at
                  failures:
                    type: array
                    items:
                      type: object
                      properties:
                        errors:
                          type: array
                          items:
                            type: string
                        tagging:
                          type: object
                          properties:
                            tag_id:
                              type: integer
                              nullable: true
                            subscriber_id:
                              type: integer
                              nullable: true
                          required:
                            - tag_id
                            - subscriber_id
                      required:
                        - errors
                        - tagging
                required:
                  - subscribers
                  - failures
              example:
                subscribers:
                  - id: 560
                    first_name: Sub
                    email_address: sub@example.com
                    created_at: '2023-02-17T11:43:55Z'
                    tagged_at: '2023-02-17T11:43:55Z'
                  - id: 560
                    first_name: Sub
                    email_address: sub@example.com
                    created_at: '2023-02-17T11:43:55Z'
                    tagged_at: '2023-02-17T11:43:55Z'
                failures:
                  - errors:
                      - Subscriber does not exist
                    tagging:
                      tag_id: 74
                      subscriber_id: null
                  - errors:
                      - Tag does not exist
                    tagging:
                      tag_id: null
                      subscriber_id: 560
        '202':
          description: >-
            Creates or updates taggings asynchronously when more than 100
            tags/subscribers are requested
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
          description: Returns a 422 when `taggings` is empty or not an array
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
                  - No taggings included for processing
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