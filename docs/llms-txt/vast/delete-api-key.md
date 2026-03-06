# Source: https://docs.vast.ai/api-reference/accounts/delete-api-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# delete api key

> Deletes an existing API key belonging to the authenticated user.
The API key is soft-deleted by setting a deleted_at timestamp.

CLI Usage: `vastai delete api-key <id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/auth/apikeys/{id}/
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
  /api/v0/auth/apikeys/{id}/:
    delete:
      tags:
        - Accounts
      summary: delete api key
      description: |-
        Deletes an existing API key belonging to the authenticated user.
        The API key is soft-deleted by setting a deleted_at timestamp.

        CLI Usage: `vastai delete api-key <id>`
      parameters:
        - name: id
          in: path
          required: true
          description: ID of the API key to delete
          schema:
            type: integer
            minimum: 1
          example: 123
      responses:
        '200':
          description: API key successfully deleted
          content:
            application/json:
              schema:
                type: string
                example: Successfully Deleted API Key
        '400':
          description: Bad Request - API key ID not provided
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: API Key ID not provided.
        '401':
          description: Unauthorized - Invalid or missing authentication
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '403':
          description: Forbidden - API key belongs to a different user
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: You do not have permission to delete this API Key.
        '404':
          description: Not Found - API key does not exist
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: API Key not found.
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