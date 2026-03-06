# Source: https://docs.vast.ai/api-reference/team/update-team-role.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# update team role

> Update an existing team role with new name and permissions.

CLI Usage: `vastai update team-role <id> --name <new_name> --permissions <new_permissions_json>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/team/roles/{id}/
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
    put:
      tags:
        - Team
      summary: update team role
      description: >-
        Update an existing team role with new name and permissions.


        CLI Usage: `vastai update team-role <id> --name <new_name> --permissions
        <new_permissions_json>`
      parameters:
        - name: id
          in: path
          required: true
          description: ID of the role to update.
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: New name for the role.
                permissions:
                  type: object
                  description: JSON encoded permissions for the role.
              required:
                - name
                - permissions
      responses:
        '200':
          description: Successfully updated team role.
          content:
            application/json:
              schema:
                type: string
                example: Successfully Updated Team Role For <role_name>
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````