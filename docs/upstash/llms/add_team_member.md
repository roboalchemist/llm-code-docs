# Source: https://upstash.com/docs/devops/developer-api/teams/add_team_member.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Team Member

> This endpoint adds a new team member to the specified team.



## OpenAPI

````yaml devops/developer-api/openapi.yml post /teams/member
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
  /teams/member:
    post:
      tags:
        - teams
      summary: Add Team Member
      description: This endpoint adds a new team member to the specified team.
      operationId: addTeamMember
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddTeamMemberRequest'
      responses:
        '200':
          description: Team member added successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TeamMember'
      security:
        - basicAuth: []
components:
  schemas:
    AddTeamMemberRequest:
      type: object
      properties:
        team_id:
          type: string
          description: Id of the team to add the member to
          example: 95849b27-40d0-4532-8695-d2028847f823
        member_email:
          type: string
          description: Email of the new team member
          example: example@upstash.com
        member_role:
          type: string
          description: Role of the new team member
          enum:
            - admin
            - dev
            - finance
          example: dev
      required:
        - team_id
        - member_email
        - member_role
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