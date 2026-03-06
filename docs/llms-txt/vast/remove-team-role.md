# Source: https://docs.vast.ai/api-reference/team/remove-team-role.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# remove team role

> Removes a role from the team. Cannot remove the team owner role.

CLI Usage: `vastai remove team-role <name>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/team/roles/{name}
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
  /api/v0/team/roles/{name}:
    delete:
      tags:
        - Team
      summary: remove team role
      description: |-
        Removes a role from the team. Cannot remove the team owner role.

        CLI Usage: `vastai remove team-role <name>`
      parameters:
        - in: path
          name: name
          required: true
          schema:
            type: string
          description: Name of the role to remove
          example: developer
      responses:
        '200':
          description: Role removed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    enum:
                      - success
                    example: success
                  message:
                    type: string
                    example: Role removed from team
        '400':
          description: Bad request - role name is required
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: Role name is required
        '401':
          description: Unauthorized - invalid or missing API key
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
                    example: unauthorized
                  msg:
                    type: string
                    example: Invalid or missing API key
        '403':
          description: Forbidden - cannot delete owner role or user is blacklisted
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
                    example: forbidden
                  msg:
                    type: string
                    example: You cannot delete the owner role.
        '404':
          description: Role not found
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
                    example: not_found
                  msg:
                    type: string
                    example: Specified role not found
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````