# Source: https://developers.kit.com/api-reference/tags/create-a-tag.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a tag



## OpenAPI

````yaml api-reference/v4.json post /v4/tags
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/tags:
    post:
      tags:
        - Tags
      summary: Create a tag
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
              required:
                - name
            example:
              name: Completed
      responses:
        '200':
          description: Returns the tag if it already exists
          content:
            application/json:
              schema:
                type: object
                properties:
                  tag:
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
                required:
                  - tag
              example:
                tag:
                  id: 12
                  name: Completed
                  created_at: '2023-02-17T11:43:55Z'
        '201':
          description: Creates the tag
          content:
            application/json:
              schema:
                type: object
                properties:
                  tag:
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
                required:
                  - tag
              example:
                tag:
                  id: 11
                  name: Completed
                  created_at: '2023-02-17T11:43:55Z'
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
          description: Returns a 422 if a name is not provided
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
                  - Name can't be blank
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