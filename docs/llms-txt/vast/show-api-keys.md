# Source: https://docs.vast.ai/api-reference/accounts/show-api-keys.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show api keys

> Retrieves all API keys associated with the authenticated user.

CLI Usage: `vastai show api-keys`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/auth/apikeys/
openapi: 3.1.0
info:
  title: Vast.ai API
  description: >-
    Welcome to Vast.ai 's API documentation. Our API allows you to
    programmatically manage GPU instances, handle machine operations, and
    automate your AI/ML workflow. Whether you're running individual GPU
    instances or managing a fleet of machines, our API provides comprehensive
    control over all Vast.ai  platform features.
  version: 1.0.0
  contact:
    name: Vast.ai Support
    url: https://discord.gg/vast
servers:
  - url: https://console.vast.ai
    description: Production server
security:
  - BearerAuth: []
paths:
  /api/v0/auth/apikeys/:
    get:
      tags:
        - Accounts
      summary: show api keys
      description: |-
        Retrieves all API keys associated with the authenticated user.

        CLI Usage: `vastai show api-keys`
      responses:
        '200':
          description: API keys successfully retrieved
          content:
            application/json:
              schema:
                type: object
                properties:
                  apikeys:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 123
                        user_id:
                          type: integer
                          example: 456
                        rights:
                          type: string
                          example: read
                        team_id:
                          type: integer
                          example: 789
                        team_name:
                          type: string
                          example: Team Alpha
        '400':
          description: Bad Request - API Key not provided or not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: API Key not provided as bearer token.
        '401':
          description: Unauthorized - Invalid or missing authentication
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=1.0
      security:
        - BearerAuth: []
components:
  schemas:
    Error:
      type: object
      properties:
        success:
          type: boolean
          example: false
        error:
          type: string
        msg:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````