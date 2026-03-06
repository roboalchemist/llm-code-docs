# Source: https://docs.vast.ai/api-reference/accounts/show-ipaddrs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show ipaddrs

> This endpoint retrieves the history of IP address accesses for the authenticated user.

CLI Usage: `vastai show ipaddrs`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/users/{user_id}/ipaddrs/
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
  /api/v0/users/{user_id}/ipaddrs/:
    get:
      tags:
        - Accounts
      summary: show ipaddrs
      description: >-
        This endpoint retrieves the history of IP address accesses for the
        authenticated user.


        CLI Usage: `vastai show ipaddrs`
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: string
          description: The ID of the user whose IP address history is being retrieved.
          example: me
      responses:
        '200':
          description: Success response with IP address history
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 123
                        user_id:
                          type: integer
                          example: 456
                        ip_address:
                          type: string
                          example: 192.168.1.1
                        timestamp:
                          type: string
                          format: date-time
                          example: '2023-10-01T12:00:00Z'
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