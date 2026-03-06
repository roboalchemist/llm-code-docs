# Source: https://docs.vast.ai/api-reference/team/remove-team-member.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# remove team member

> Removes a member from the team by revoking their team-related API keys and updating membership status. Cannot remove the team owner.

CLI Usage: `vastai remove team-member <id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/team/members/{id}
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
  /api/v0/team/members/{id}:
    delete:
      tags:
        - Team
      summary: remove team member
      description: >-
        Removes a member from the team by revoking their team-related API keys
        and updating membership status. Cannot remove the team owner.


        CLI Usage: `vastai remove team-member <id>`
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: integer
          description: User ID of the team member to remove
          example: 12345
      responses:
        '200':
          description: Member removed successfully
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
                    example: User removed from the team.
        '400':
          description: Bad request - cannot remove team owner
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: Cannot remove the team owner from the team
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
          description: Forbidden - user is blacklisted
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
                    example: User is blacklisted
        '404':
          description: Member not found or already removed
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    enum:
                      - failure
                    example: failure
                  message:
                    type: string
                    example: No user was removed from the team.
        '429':
          description: Too many requests
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
                    example: rate_limit_exceeded
                  msg:
                    type: string
                    example: API requests too frequent endpoint threshold=3.0
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````