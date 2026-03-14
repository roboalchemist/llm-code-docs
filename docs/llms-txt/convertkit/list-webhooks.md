# Source: https://developers.kit.com/api-reference/webhooks/list-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List webhooks

> Webhooks are automations that will receive subscriber data when a subscriber event is triggered, such as when a subscriber completes a sequence.<br/><br/>When a webhook is triggered, a `POST` request will be made to your URL with a JSON payload.



## OpenAPI

````yaml api-reference/v4.json get /v4/webhooks
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/webhooks:
    get:
      tags:
        - Webhooks
      summary: List webhooks
      description: >-
        Webhooks are automations that will receive subscriber data when a
        subscriber event is triggered, such as when a subscriber completes a
        sequence.<br/><br/>When a webhook is triggered, a `POST` request will be
        made to your URL with a JSON payload.
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
          description: Returns a paginated list of webhooks
          content:
            application/json:
              schema:
                type: object
                properties:
                  webhooks:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        account_id:
                          type: integer
                        event:
                          type: object
                          properties:
                            name:
                              type: string
                              description: Product name
                            tag_id:
                              type: integer
                              nullable: true
                            form_id:
                              type: integer
                              nullable: true
                          required:
                            - name
                        target_url:
                          type: string
                      required:
                        - id
                        - account_id
                        - event
                        - target_url
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
                  - webhooks
                  - pagination
              example:
                webhooks:
                  - id: 2
                    account_id: 1083
                    event:
                      name: tag_add
                      tag_id: 36
                    target_url: http://example.convertkit.dev/tags
                  - id: 1
                    account_id: 1083
                    event:
                      name: form_subscribe
                      form_id: 10
                    target_url: http://example.convertkit.dev/
                pagination:
                  has_previous_page: false
                  has_next_page: false
                  start_cursor: WzJd
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