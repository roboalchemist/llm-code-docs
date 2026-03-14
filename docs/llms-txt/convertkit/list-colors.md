# Source: https://developers.kit.com/api-reference/accounts/list-colors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List colors



## OpenAPI

````yaml api-reference/v4.json get /v4/account/colors
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/account/colors:
    get:
      tags:
        - Accounts
      summary: List colors
      parameters: []
      responses:
        '200':
          description: Returns list of colors for the current account
          content:
            application/json:
              schema:
                type: object
                properties:
                  colors:
                    type: array
                    items:
                      type: string
                required:
                  - colors
              example:
                colors:
                  - '#008000'
                  - '#FF0000'
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