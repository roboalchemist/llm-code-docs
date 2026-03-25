# Source: https://developers.kit.com/api-reference/accounts/get-creator-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Creator Profile



## OpenAPI

````yaml api-reference/v4.json get /v4/account/creator_profile
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/account/creator_profile:
    get:
      tags:
        - Accounts
      summary: Get Creator Profile
      parameters: []
      responses:
        '200':
          description: Returns Creator Profile details
          content:
            application/json:
              schema:
                type: object
                properties:
                  profile:
                    type: object
                    properties:
                      name:
                        type: string
                      byline:
                        type: string
                      bio:
                        type: string
                      image_url:
                        type: string
                      profile_url:
                        type: string
                    required:
                      - name
                      - byline
                      - bio
                      - image_url
                      - profile_url
                required:
                  - profile
              example:
                profile:
                  name: A Creator's Journey
                  byline: A Creator
                  bio: Follow my Journey as a Creator
                  image_url: https://convertkit.dev/image.jpg?fit=crop&h=320&w=320
                  profile_url: https://kit-greetings.kit.com/profile
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
          description: Returns a 404 if the creator profile doesn't exist
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