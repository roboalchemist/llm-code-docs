# Source: https://docs.vast.ai/api-reference/accounts/create-subaccount.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# create subaccount

> Creates either a standalone user account or a subaccount under a parent account. Subaccounts can be restricted to host-only functionality.

CLI Usage: `vastai create subaccount --email <email> --username <username> --password <password> [--type host]`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/users/
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
  /api/v0/users/:
    post:
      tags:
        - Accounts
      summary: create subaccount
      description: >-
        Creates either a standalone user account or a subaccount under a parent
        account. Subaccounts can be restricted to host-only functionality.


        CLI Usage: `vastai create subaccount --email <email> --username
        <username> --password <password> [--type host]`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - email
                - username
                - password
              properties:
                email:
                  type: string
                  description: User's email address
                  maxLength: 64
                  example: user@example.com
                  pattern: ^(?!.*@vast)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
                username:
                  type: string
                  description: Desired username
                  maxLength: 64
                  example: testuser123
                password:
                  type: string
                  description: Account password
                  maxLength: 256
                  example: securepass123
                host_only:
                  type: boolean
                  description: If true, account is restricted to host functionality only
                  example: true
                parent_id:
                  type: string
                  description: >-
                    Parent account ID for subaccounts. Use "me" for current
                    user.
                  example: me
                ssh_key:
                  type: string
                  description: Optional SSH public key
                  maxLength: 4096
                captcha:
                  type: string
                  description: Captcha token (required for non-subaccounts)
                  maxLength: 8192
      responses:
        '200':
          description: Account created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    description: User ID
                  username:
                    type: string
                  email:
                    type: string
                  key_id:
                    type: integer
                    description: API key for the new account
                example:
                  id: 12345
                  username: testuser
                  email: user@example.com
                  key_id: 67890
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    enum:
                      - invalid_email
                      - invalid_request
                      - missing_auth_value
                  msg:
                    type: string
                example:
                  error: invalid_email
                  msg: Email address not allowed
        '403':
          description: Forbidden - billing blacklisted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '409':
          description: User already exists
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    enum:
                      - user_exists
                  msg:
                    type: string
                example:
                  error: user_exists
                  msg: user already exists.
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