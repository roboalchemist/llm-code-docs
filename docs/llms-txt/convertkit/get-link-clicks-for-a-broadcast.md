# Source: https://developers.kit.com/api-reference/broadcasts/get-link-clicks-for-a-broadcast.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get link clicks for a broadcast

> NOTE: Pagination parameters control the list of clicks for the top level broadcast.



## OpenAPI

````yaml api-reference/v4.json get /v4/broadcasts/{broadcast_id}/clicks
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/broadcasts/{broadcast_id}/clicks:
    get:
      tags:
        - Broadcasts
      summary: Get link clicks for a broadcast
      description: >-
        NOTE: Pagination parameters control the list of clicks for the top level
        broadcast.
      parameters:
        - name: broadcast_id
          in: path
          required: true
          schema:
            type: integer
          example: 123
      responses:
        '200':
          description: Returns clicks for a broadcast
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
                      clicks:
                        type: array
                        items:
                          type: object
                          properties:
                            url:
                              type: string
                            unique_clicks:
                              type: integer
                            click_to_delivery_rate:
                              type: number
                              format: float
                            click_to_open_rate:
                              type: number
                              format: float
                          required:
                            - url
                            - unique_clicks
                            - click_to_delivery_rate
                            - click_to_open_rate
                    required:
                      - id
                      - clicks
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
                  - broadcast
                  - pagination
              example:
                broadcast:
                  id: 121
                  clicks:
                    - url: https://example.com/52
                      unique_clicks: 3
                      click_to_delivery_rate: 0.006
                      click_to_open_rate: 0.03
                    - url: https://example.com/53
                      unique_clicks: 3
                      click_to_delivery_rate: 0.006
                      click_to_open_rate: 0.03
                    - url: https://example.com/54
                      unique_clicks: 3
                      click_to_delivery_rate: 0.006
                      click_to_open_rate: 0.03
                pagination:
                  has_previous_page: false
                  has_next_page: false
                  start_cursor: WzIwXQ==
                  end_cursor: WzIwXQ==
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