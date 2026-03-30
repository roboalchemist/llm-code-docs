# Source: https://docs.vast.ai/api-reference/accounts/transfer-credit.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# transfer credit

> Transfers specified amount of credits from the authenticated user's account to another user's account.

The recipient can be specified by either email address or user ID.

CLI Usage: `vastai transfer credit <recipient_email> <amount>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/commands/transfer_credit/
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
  /api/v0/commands/transfer_credit/:
    put:
      tags:
        - Accounts
      summary: transfer credit
      description: >-
        Transfers specified amount of credits from the authenticated user's
        account to another user's account.


        The recipient can be specified by either email address or user ID.


        CLI Usage: `vastai transfer credit <recipient_email> <amount>`
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - recipient
                - amount
              properties:
                recipient:
                  type: string
                  description: Email address or user ID of the recipient
                  example: user@example.com
                amount:
                  type: number
                  format: float
                  description: Amount of credits to transfer (must be positive)
                  minimum: 0.01
                  example: 100
                client_id:
                  type: string
                  description: Client identifier (usually "me")
                  example: me
                apikey_id:
                  type: string
                  description: Optional API key identifier for audit logging
      responses:
        '200':
          description: Transfer completed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
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
                      - invalid_args
                      - invalid_params
                      - invalid_recipient
                      - insufficient_balance
                  msg:
                    type: string
                    example: Invalid amount
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
                    example: API requests too frequent endpoint threshold=2.5
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