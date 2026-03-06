# Source: https://docs.vast.ai/api-reference/accounts/show-user.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show user

> Retrieve information about the current authenticated user, excluding the API key.

CLI Usage: `vastai show user`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/users/current/
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
  /api/v0/users/current/:
    get:
      tags:
        - Accounts
      summary: show user
      description: >-
        Retrieve information about the current authenticated user, excluding the
        API key.


        CLI Usage: `vastai show user`
      responses:
        '200':
          description: Success response with user information
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    description: The unique identifier of the user.
                  key_id:
                    type: integer
                    description: The API key ID associated with the user.
                  email:
                    type: string
                    description: The email address of the user.
                  balance:
                    type: number
                    format: float
                    description: The current balance of the user.
                  ssh_key:
                    type: string
                    description: The SSH key associated with the user.
                  sid:
                    type: string
                    description: Server ID.
        '401':
          description: Unauthorized access due to invalid or missing authentication token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
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