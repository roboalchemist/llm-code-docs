# Source: https://developers.kit.com/api-reference/accounts/get-growth-stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get growth stats

> Get growth stats for a specific time period. Defaults to last 90 days.<br/><br/>NOTE: We return your stats in your sending time zone. This endpoint does not return timestamps in UTC.



## OpenAPI

````yaml api-reference/v4.json get /v4/account/growth_stats
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/account/growth_stats:
    get:
      tags:
        - Accounts
      summary: Get growth stats
      description: >-
        Get growth stats for a specific time period. Defaults to last 90
        days.<br/><br/>NOTE: We return your stats in your sending time zone.
        This endpoint does not return timestamps in UTC.
      parameters:
        - name: ending
          in: query
          description: >-
            Get stats for time period ending on this date (format yyyy-mm-dd).
            Defaults to today.
          required: false
          schema:
            type: string
          example: 02/09/2023
        - name: starting
          in: query
          description: >-
            Get stats for time period beginning on this date (format
            yyyy-mm-dd). Defaults to 90 days ago.
          required: false
          schema:
            type: string
          example: 02/10/2023
      responses:
        '200':
          description: Returns your growth stats for the provided starting and ending dates
          content:
            application/json:
              schema:
                type: object
                properties:
                  stats:
                    type: object
                    properties:
                      cancellations:
                        type: integer
                      net_new_subscribers:
                        type: integer
                      new_subscribers:
                        type: integer
                      subscribers:
                        type: integer
                      starting:
                        type: string
                      ending:
                        type: string
                    required:
                      - cancellations
                      - net_new_subscribers
                      - new_subscribers
                      - subscribers
                      - starting
                      - ending
                required:
                  - stats
              example:
                stats:
                  cancellations: 0
                  net_new_subscribers: 3
                  new_subscribers: 3
                  subscribers: 3
                  starting: '2023-02-10T00:00:00-05:00'
                  ending: '2023-02-24T23:59:59-05:00'
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
        '422':
          description: >-
            Returns a 422 with an error message if the starting or ending params
            are misformatted or the range is invalid
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
                  - Starting date is incorrectly formatted. Use YYYY-MM-DD.
                  - Ending date is incorrectly formatted. Use YYYY-MM-DD.
                  - Starting date must be before the ending date.
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