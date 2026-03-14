# Source: https://developers.kit.com/api-reference/tags/remove-tag-from-subscriber.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove tag from subscriber



## OpenAPI

````yaml api-reference/v4.json delete /v4/tags/{tag_id}/subscribers/{id}
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/tags/{tag_id}/subscribers/{id}:
    delete:
      tags:
        - Tags
      summary: Remove tag from subscriber
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          example: 1130
        - name: tag_id
          in: path
          required: true
          schema:
            type: integer
          example: 209
      responses:
        '204':
          description: Removes the tag from the subscriber
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