# Source: https://docs.vast.ai/api-reference/team/invite-team-member.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# invite team member

> Sends an invitation email to the specified user to join the team with the given role.

CLI Usage: `vastai invite team-member --email <email> --role <role>`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/team/invite/
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
  /api/v0/team/invite/:
    post:
      tags:
        - Team
      summary: invite team member
      description: >-
        Sends an invitation email to the specified user to join the team with
        the given role.


        CLI Usage: `vastai invite team-member --email <email> --role <role>`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - email
                - role
              properties:
                email:
                  type: string
                  description: Email address of the user to invite
                  format: email
                  example: user@example.com
                role:
                  type: string
                  description: Role to assign to the new team member
                  example: developer
      responses:
        '200':
          description: Invitation sent successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  msg:
                    type: string
                    example: New invitation sent to ${email}
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    enum:
                      - User is a not a team member
                      - User cannot be invited to their own team.
                      - User is already a member of this team.
        '403':
          description: Forbidden - User not authenticated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Team metadata not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: Team metadata not found
        '429':
          description: Too Many Requests - Duplicate invitation
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: >-
                      Error: invitation already sent to user@example.com only
                      300 seconds ago.
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