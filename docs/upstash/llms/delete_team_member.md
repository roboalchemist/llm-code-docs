# Source: https://upstash.com/docs/devops/developer-api/teams/delete_team_member.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Team Member

> This endpoint deletes a team member from the specified team.



## OpenAPI

````yaml devops/developer-api/openapi.yml delete /teams/member
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
    delete:
      tags:
        - teams
      summary: Delete Team Member
      description: This endpoint deletes a team member from the specified team.
      operationId: deleteTeamMember
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeleteTeamMemberRequest'
      responses:
        '200':
          description: Team member deleted successfully
          content:
            application/json:
              schema:
                type: string
                example: OK
      security:
        - basicAuth: []
components:
  schemas:
    DeleteTeamMemberRequest:
      type: object
      properties:
        team_id:
          type: string
          description: Id of the team to remove the member from
          example: 95849b27-40d0-4532-8695-d2028847f823
        member_email:
          type: string
          description: Email of the team member to remove
          example: example@upstash.com
      required:
        - team_id
        - member_email
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic

````