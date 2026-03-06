# Source: https://docs.vast.ai/api-reference/team/create-team.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# create team

> Creates a new [team](https://docs.vast.ai/documentation/teams/teams-overview) with given name and following default roles:
- **Owner**: Full access to all team resources, settings, and member management. The team owner is the user who creates the team.
- **Manager**: All permissions of owner except team deletion.
- **Member**: Can view, create, and interact with instances, but cannot access billing, team management, autoscaler, or machines.

- The API key used to create the team becomes the team key and is used for all team operations (e.g., creating roles, deleting the team).
- You can optionally transfer credits from your personal account to the new team account using the `transfer_credit` field.

CLI Usage: `vastai create team --team_name <team_name> [--transfer_credit <amount>]`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/team/
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
    post:
      tags:
        - Team
      summary: create team
      description: >-
        Creates a new
        [team](https://docs.vast.ai/documentation/teams/teams-overview) with
        given name and following default roles:

        - **Owner**: Full access to all team resources, settings, and member
        management. The team owner is the user who creates the team.

        - **Manager**: All permissions of owner except team deletion.

        - **Member**: Can view, create, and interact with instances, but cannot
        access billing, team management, autoscaler, or machines.


        - The API key used to create the team becomes the team key and is used
        for all team operations (e.g., creating roles, deleting the team).

        - You can optionally transfer credits from your personal account to the
        new team account using the `transfer_credit` field.


        CLI Usage: `vastai create team --team_name <team_name>
        [--transfer_credit <amount>]`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - team_name
                - permissions
              properties:
                team_name:
                  type: string
                  example: my-awesome-team
                transfer_credit:
                  type: number
                  format: float
                  description: Credits to transfer from personal account to team
                  example: 0
      responses:
        '200':
          description: Team Successfully Created!
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
                    example: Team Successfully Created!
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
                    example: Team name already exists
        '401':
          description: Unauthorized - Invalid or missing API key
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````