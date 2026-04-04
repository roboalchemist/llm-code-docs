# Source: https://docs.vast.ai/api-reference/team/create-team-role.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# create team role

> Creates a new role within a team. Only team owners or managers with the appropriate permissions can perform this operation.

CLI Usage: `vastai create team role --name <role_name> --permissions <permissions_json>`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/team/roles/
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
  /api/v0/team/roles/:
    post:
      tags:
        - Team
      summary: create team role
      description: >-
        Creates a new role within a team. Only team owners or managers with the
        appropriate permissions can perform this operation.


        CLI Usage: `vastai create team role --name <role_name> --permissions
        <permissions_json>`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - permissions
              properties:
                name:
                  type: string
                  description: Name for the new role
                  example: developer
                permissions:
                  type: object
                  description: JSON object containing permission definitions
                  properties:
                    api:
                      type: object
                      description: API permissions
                      allOf:
                        - title: User Read
                          type: object
                          properties:
                            user_read:
                              type: object
                              description: Permission to read user info
                              default: {}
                            instance_write:
                              type: object
                              description: Permission to write instances
                              default: {}
      responses:
        '200':
          description: Role created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: success
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
                  msg:
                    type: string
                    example: Missing permissions parameter
        '401':
          description: Unauthorized - Invalid or missing API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '403':
          description: Forbidden - User lacks permission
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