# Source: https://developers.kit.com/api-reference/accounts/get-current-account.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get current account



## OpenAPI

````yaml api-reference/v4.json get /v4/account
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/account:
    get:
      tags:
        - Accounts
      summary: Get current account
      parameters: []
      responses:
        '200':
          description: Returns current account and user info
          content:
            application/json:
              schema:
                type: object
                properties:
                  user:
                    type: object
                    properties:
                      email:
                        type: string
                      id:
                        type: integer
                    required:
                      - email
                  account:
                    type: object
                    properties:
                      id:
                        type: integer
                      name:
                        type: string
                      plan_type:
                        type: string
                      primary_email_address:
                        type: string
                      created_at:
                        type: string
                      timezone:
                        type: object
                        properties:
                          name:
                            type: string
                            description: Product name
                          friendly_name:
                            type: string
                          utc_offset:
                            type: string
                        required:
                          - name
                          - friendly_name
                          - utc_offset
                    required:
                      - id
                      - name
                      - plan_type
                      - primary_email_address
                      - created_at
                      - timezone
                required:
                  - user
                  - account
              example:
                user:
                  email: test@kit.dev
                  id: 27
                account:
                  id: 27
                  name: Kit Greetings
                  plan_type: creator
                  primary_email_address: test@kit.dev
                  created_at: '2023-02-17T11:43:55Z'
                  timezone:
                    name: America/New_York
                    friendly_name: Eastern Time (US & Canada)
                    utc_offset: '-05:00'
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