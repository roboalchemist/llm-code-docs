# Source: https://developers.kit.com/api-reference/accounts/get-email-stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get email stats



## OpenAPI

````yaml api-reference/v4.json get /v4/account/email_stats
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/account/email_stats:
    get:
      tags:
        - Accounts
      summary: Get email stats
      parameters: []
      responses:
        '200':
          description: Returns your email stats for the last 90 days
          content:
            application/json:
              schema:
                type: object
                properties:
                  stats:
                    type: object
                    properties:
                      sent:
                        type: integer
                      clicked:
                        type: integer
                      opened:
                        type: integer
                      email_stats_mode:
                        type: string
                      open_tracking_enabled:
                        type: boolean
                      click_tracking_enabled:
                        type: boolean
                      starting:
                        type: string
                      ending:
                        type: string
                    required:
                      - sent
                      - clicked
                      - opened
                      - email_stats_mode
                      - open_tracking_enabled
                      - click_tracking_enabled
                      - starting
                      - ending
                required:
                  - stats
              example:
                stats:
                  sent: 6
                  clicked: 3
                  opened: 6
                  email_stats_mode: last_90
                  open_tracking_enabled: true
                  click_tracking_enabled: true
                  starting: '2022-11-19T11:43:55Z'
                  ending: '2023-02-17T11:43:55Z'
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