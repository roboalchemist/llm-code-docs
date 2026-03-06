# Source: https://docs.vast.ai/api-reference/accounts/delete-env-var.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# delete env var

> Deletes an environment variable associated with the authenticated user.
The variable must exist and belong to the requesting user.

CLI Usage: `vastai delete env-var <name>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/secrets/
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
    delete:
      tags:
        - Accounts
      summary: delete env var
      description: |-
        Deletes an environment variable associated with the authenticated user.
        The variable must exist and belong to the requesting user.

        CLI Usage: `vastai delete env-var <name>`
      operationId: deleteUserSecret
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - key
              properties:
                key:
                  type: string
                  description: Name of the environment variable to delete
                  example: MY_API_KEY
      responses:
        '200':
          description: Environment variable deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '400':
          description: Bad request - missing or invalid input
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/Error'
                  - type: object
                    properties:
                      error:
                        type: string
                        enum:
                          - missing_input
                          - nonexistent_key
                        example: missing_input
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
          description: Too many requests - rate limit exceeded
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