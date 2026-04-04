# Source: https://upstash.com/docs/devops/developer-api/teams/get_team_members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Team Members

> This endpoint list all members of a team.



## OpenAPI

````yaml devops/developer-api/openapi.yml get /teams/{team_id}
openapi: 3.0.4
info:
  title: Developer API - Upstash
  description: >-
    This is a documentation to specify Developer API endpoints based on the
    OpenAPI 3.0 specification.
  contact:
    name: Support Team
    email: support@upstash.com
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
  version: 1.0.0
servers:
  - url: https://api.upstash.com/v2
security: []
tags:
  - name: redis
    description: Manage redis databases.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: teams
    description: Manage teams and team members.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: vector
    description: Manage vector indices.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: search
    description: Manage search indices.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: qstash
    description: Manage QStash.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
externalDocs:
  description: Find out more about Upstash
  url: https://upstash.com/
paths:
  /teams/{team_id}:
    get:
      tags:
        - teams
      summary: Get Team Members
      description: This endpoint list all members of a team.
      operationId: getTeamMembers
      parameters:
        - name: team_id
          in: path
          description: ID of the team
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Team members retrieved successfully
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/TeamMember'
      security:
        - basicAuth: []
components:
  schemas:
    TeamMember:
      type: object
      properties:
        team_id:
          type: string
          description: ID of the team
          example: 3423cb72-e50d-43ec-a9c0-f0f359941223
        team_name:
          type: string
          description: Name of the team
          example: test_team_name_2
        member_email:
          type: string
          description: Email of the team member
          example: example@upstash.com
        member_role:
          type: string
          description: Role of the team member
          enum:
            - owner
            - admin
            - dev
            - finance
          example: dev
        copy_cc:
          type: boolean
          description: >-
            Whether to copy existing credit card information to team member or
            not
          example: true
      xml:
        name: teamMember
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic

````