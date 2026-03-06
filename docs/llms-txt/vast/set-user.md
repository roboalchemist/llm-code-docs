# Source: https://docs.vast.ai/api-reference/accounts/set-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# set user

> Updates the user data for the authenticated user.

CLI Usage: `vastai set user --file <file_path>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/users/
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
    put:
      tags:
        - Accounts
      summary: set user
      description: |-
        Updates the user data for the authenticated user.

        CLI Usage: `vastai set user --file <file_path>`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                normalized_email:
                  type: string
                  description: Normalized email address.
                  example: user@example.com
                username:
                  type: string
                  description: Username of the user.
                  example: johndoe
                fullname:
                  type: string
                  description: Full name of the user.
                  example: John Doe
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
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
        '403':
          description: Forbidden
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
                    example: API requests too frequent endpoint threshold=5.0
      security:
        - BearerAuth: []
components:
  schemas:
    SuccessResponse:
      type: object
      properties:
        success:
          type: boolean
          example: true
        msg:
          type: string
          example: Operation completed successfully
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