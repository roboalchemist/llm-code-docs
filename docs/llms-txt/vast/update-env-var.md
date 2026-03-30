# Source: https://docs.vast.ai/api-reference/accounts/update-env-var.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# update env var

> Updates the value of an existing environment variable for the authenticated user.

CLI Usage: `vastai update env-var <key> <value>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/secrets/
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
  /api/v0/secrets/:
    put:
      tags:
        - Accounts
      summary: update env var
      description: >-
        Updates the value of an existing environment variable for the
        authenticated user.


        CLI Usage: `vastai update env-var <key> <value>`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - key
                - value
              properties:
                key:
                  type: string
                  description: >-
                    The key of the environment variable to update (will be
                    converted to uppercase)
                  example: MY_API_KEY
                  pattern: ^[a-zA-Z_]\w*$
                value:
                  type: string
                  description: The new value for the environment variable
                  example: xyz123
      responses:
        '200':
          description: Environment variable updated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  msg:
                    type: string
                    example: Environment variable updated successfully
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/Error'
                properties:
                  error:
                    type: string
                    enum:
                      - missing_input
                      - empty_input
                      - input_too_long
                      - invalid_characters
                      - nonexistent_key
        '401':
          description: Unauthorized
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
                    example: API requests too frequent endpoint threshold=3.0
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