# Source: https://docs.vast.ai/api-reference/accounts/create-env-var.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# create env-var

> Creates a new encrypted environment variable for the authenticated user.
Keys are automatically converted to uppercase. Values are encrypted before storage.
There is a limit on the total number of environment variables per user.

CLI Usage: `vastai create env-var <key> <value>`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/secrets/
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
    post:
      tags:
        - Accounts
      summary: create env-var
      description: >-
        Creates a new encrypted environment variable for the authenticated user.

        Keys are automatically converted to uppercase. Values are encrypted
        before storage.

        There is a limit on the total number of environment variables per user.


        CLI Usage: `vastai create env-var <key> <value>`
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
                    Environment variable key name (will be converted to
                    uppercase)
                  example: API_TOKEN
                value:
                  type: string
                  description: Secret value to be encrypted and stored
                  pattern: ^[a-zA-Z0-9_\-\.]+$
                  example: abc123xyz
      responses:
        '200':
          description: Environment variable created successfully
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
                    example: Environment variable added successfully
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  error:
                    type: string
                    enum:
                      - missing_input
                      - max_secrets
                      - existing_key
                  msg:
                    type: string
                    example: Both 'key' and 'value' are required.
        '401':
          description: Unauthorized - Invalid or missing API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '403':
          description: Forbidden - User is blacklisted
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