# Source: https://docs.vast.ai/api-reference/team/destroy-team.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# destroy team

> Deletes a team and all associated data including API keys, rights, invitations, memberships and metadata. The team owner's master API key is converted to a normal client key.

CLI Usage: `vastai destroy team`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/team/
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
  /api/v0/team/:
    delete:
      tags:
        - Team
      summary: destroy team
      description: >-
        Deletes a team and all associated data including API keys, rights,
        invitations, memberships and metadata. The team owner's master API key
        is converted to a normal client key.


        CLI Usage: `vastai destroy team`
      responses:
        '200':
          description: Team successfully deleted
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
                    example: Team Successfully Deleted!
                  pkey_id:
                    type: integer
                    description: >-
                      ID of the user's team API key which was converted back to
                      a client key.
                    example: 12345
        '401':
          description: Unauthorized - Invalid or missing API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              example:
                success: false
                error: auth_error
                msg: Invalid user key
        '403':
          description: Forbidden - Only the Team's Owner may delete the team
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              example:
                success: false
                error: not_allowed
                msg: Only the Team's Owner may delete the team
        '404':
          description: Not Found - Team does not exist or user is not a team account
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              examples:
                not_a_team:
                  summary: User is not a team account
                  value:
                    success: false
                    error: not_found
                    msg: Cannot Delete Team. User is not a team account
                owner_not_found:
                  summary: Team owner not found
                  value:
                    success: false
                    error: not_found
                    msg: Team owner not found
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