# Source: https://docs.vast.ai/api-reference/accounts/show-team-role.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show team role

> Retrieve details of a specific team role by its name.

CLI Usage: `vastai show team-role <name>`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/team/roles/{id}/
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
  /api/v0/team/roles/{id}/:
    get:
      tags:
        - Accounts
      summary: show team role
      description: |-
        Retrieve details of a specific team role by its name.

        CLI Usage: `vastai show team-role <name>`
      parameters:
        - name: id
          in: path
          required: true
          description: Name of the team role
          schema:
            type: string
          example: admin
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    description: Role ID
                    example: 1
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
        '404':
          description: Role not found
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