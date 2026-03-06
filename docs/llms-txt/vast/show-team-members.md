# Source: https://docs.vast.ai/api-reference/team/show-team-members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show team members

> Retrieve a list of team members associated with the authenticated user's team.

CLI Usage: `vastai show team-members`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/team/members/
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
  /api/v0/team/members/:
    get:
      tags:
        - Team
      summary: show team members
      description: >-
        Retrieve a list of team members associated with the authenticated user's
        team.


        CLI Usage: `vastai show team-members`
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
                      description: User ID
                      example: 123
                    username:
                      type: string
                      description: Username of the team member
                      example: johndoe
                    email:
                      type: string
                      description: Email of the team member
                      example: johndoe@example.com
                    fullname:
                      type: string
                      description: Full name of the team member
                      example: John Doe
                    roles:
                      type: array
                      description: Roles assigned to the team member
                      items:
                        type: string
                      example:
                        - admin
                        - member
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