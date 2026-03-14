# Source: https://developers.kit.com/api-reference/tags/bulk-create-tags.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk create tags

> See "[Bulk & async processing](#bulk-amp-async-processing)" for more information.



## OpenAPI

````yaml api-reference/v4.json post /v4/bulk/tags
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/bulk/tags:
    post:
      tags:
        - Tags
      summary: Bulk create tags
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
                tags:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                    required:
                      - name
                callback_url:
                  type: string
                  nullable: true
              required:
                - tags
            example:
              tags:
                - name: Test Tag 0
                - name: Test Tag 1
                - name: Test Tag 2
                - name: Test Tag 3
              callback_url: null
      responses:
        '200':
          description: >-
            Creates or returns existing tags synchronously when 100 or less tags
            are requested
          content:
            application/json:
              schema:
                type: object
                properties:
                  tags:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        name:
                          type: string
                        created_at:
                          type: string
                      required:
                        - id
                        - name
                        - created_at
                  failures:
                    type: array
                    items: {}
                required:
                  - tags
                  - failures
              example:
                tags:
                  - id: 59
                    name: Existing Tag
                    created_at: '2023-02-17T11:43:55Z'
                  - id: 60
                    name: Attended Event
                    created_at: '2023-02-17T11:43:55Z'
                  - id: 61
                    name: Newsletter
                    created_at: '2023-02-17T11:43:55Z'
                  - id: 62
                    name: Re-engage
                    created_at: '2023-02-17T11:43:55Z'
                failures: []
        '202':
          description: >-
            Creates or returns existing tags asynchronously when more than 100
            tags are requested
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
          description: Returns a 422 when `tags` is empty or not an array
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
                  - No tags included for processing
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