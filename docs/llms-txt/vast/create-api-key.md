# Source: https://docs.vast.ai/api-reference/accounts/create-api-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# create api-key

> Creates a new API key with specified permissions for the authenticated user.

CLI Usage: `vastai create api-key --name <name> --permission_file <permissions_file> [--key_params <params>]`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/auth/apikeys/
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
    post:
      tags:
        - Accounts
      summary: create api-key
      description: >-
        Creates a new API key with specified permissions for the authenticated
        user.


        CLI Usage: `vastai create api-key --name <name> --permission_file
        <permissions_file> [--key_params <params>]`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - name
              properties:
                name:
                  type: string
                  description: Name for the API key
                  example: read-only-key
                permissions:
                  type: object
                  description: JSON object containing permission definitions
                  example:
                    read: true
                    write: false
                key_params:
                  type: object
                  description: Optional wildcard parameters for advanced keys
                  example:
                    ip_whitelist:
                      - 1.2.3.4
      responses:
        '200':
          description: API key created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    description: The ID of the created API key
                    example: 12345
                  key:
                    type: string
                    description: The newly generated API key
                    example: vast-123456789abcdef
                  permissions:
                    anyOf:
                      - type: boolean
                        description: False when permissions are disabled
                        example: false
                      - type: object
                        description: Object defining the permissions when enabled
                        example:
                          read: true
                          write: false
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
                      - invalid_permissions
                      - missing_permissions
                  msg:
                    type: string
                    example: Invalid permission format
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  msg:
                    type: string
                    example: Unauthorized
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=2.0
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````