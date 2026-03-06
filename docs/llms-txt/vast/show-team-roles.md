# Source: https://docs.vast.ai/api-reference/team/show-team-roles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show team roles

> Retrieve a list of all roles for a team, excluding the owner' role.

CLI Usage: `vastai show team-roles`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/team/roles-full/
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
  /api/v0/team/roles-full/:
    get:
      tags:
        - Team
      summary: show team roles
      description: |-
        Retrieve a list of all roles for a team, excluding the owner' role.

        CLI Usage: `vastai show team-roles`
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
                    name:
                      type: string
                      description: Name of the role
                      example: admin
                    permissions:
                      type: array
                      description: Permissions associated with the role
                      items:
                        type: string
                      example:
                        - read
                        - write
                    identifier:
                      type: string
                      description: Unique identifier for the role
                      example: admin_role
                    id:
                      type: integer
                      description: Role ID
                      example: 1234
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Invalid API key
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
                    example: auth_error
                  msg:
                    type: string
                    example: Invalid user key
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