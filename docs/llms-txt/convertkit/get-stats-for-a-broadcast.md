# Source: https://developers.kit.com/api-reference/broadcasts/get-stats-for-a-broadcast.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get stats for a broadcast



## OpenAPI

````yaml api-reference/v4.json get /v4/broadcasts/{broadcast_id}/stats
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/broadcasts/{broadcast_id}/stats:
    get:
      tags:
        - Broadcasts
      summary: Get stats for a broadcast
      parameters:
        - name: broadcast_id
          in: path
          required: true
          schema:
            type: integer
          example: 178
      responses:
        '200':
          description: Returns stats for a broadcast
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
                      stats:
                        type: object
                        properties:
                          recipients:
                            type: integer
                          open_rate:
                            type: number
                            format: float
                          emails_opened:
                            type: integer
                          click_rate:
                            type: number
                            format: float
                          unsubscribe_rate:
                            type: number
                            format: float
                          unsubscribes:
                            type: integer
                          total_clicks:
                            type: integer
                          show_total_clicks:
                            type: boolean
                          status:
                            type: string
                          progress:
                            type: number
                            format: float
                          open_tracking_disabled:
                            type: boolean
                          click_tracking_disabled:
                            type: boolean
                        required:
                          - recipients
                          - open_rate
                          - emails_opened
                          - click_rate
                          - unsubscribe_rate
                          - unsubscribes
                          - total_clicks
                          - show_total_clicks
                          - status
                          - progress
                          - open_tracking_disabled
                          - click_tracking_disabled
                    required:
                      - id
                      - stats
                required:
                  - broadcast
              example:
                broadcast:
                  id: 177
                  stats:
                    recipients: 0
                    open_rate: 0
                    emails_opened: 0
                    click_rate: 0
                    unsubscribe_rate: 0
                    unsubscribes: 0
                    total_clicks: 0
                    show_total_clicks: false
                    status: draft
                    progress: 0
                    open_tracking_disabled: false
                    click_tracking_disabled: false
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