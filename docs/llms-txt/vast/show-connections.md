# Source: https://docs.vast.ai/api-reference/accounts/show-connections.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show connections

> Retrieves the list of cloud connections associated with the authenticated user.

CLI Usage: `vastai show connections`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/users/cloud_integrations/
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
  /api/v0/users/cloud_integrations/:
    get:
      tags:
        - Accounts
      summary: show connections
      description: >-
        Retrieves the list of cloud connections associated with the
        authenticated user.


        CLI Usage: `vastai show connections`
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      description: Unique identifier for the cloud connection.
                    cloud_type:
                      type: string
                      description: Type of cloud service.
                    name:
                      type: string
                      description: User-given name for the cloud connection.
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
                    example: API requests too frequent endpoint threshold=2.9
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