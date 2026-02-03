# Source: https://upstash.com/docs/devops/developer-api/teams/list_teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Teams

> This endpoint lists all teams of user.



## OpenAPI

````yaml devops/developer-api/openapi.yml get /teams
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
  /teams:
    get:
      tags:
        - teams
      summary: List Teams
      description: This endpoint lists all teams of user.
      operationId: listTeams
      responses:
        '200':
          description: Teams retrieved successfully
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Team'
      security:
        - basicAuth: []
components:
  schemas:
    Team:
      type: object
      properties:
        team_id:
          type: string
          description: ID of the team
          example: 95849b27-40d0-4532-8695-d2028847f823
        team_name:
          type: string
          description: Name of the team
          example: test_team_name
        copy_cc:
          type: boolean
          description: Whether creditcard information added to team during creation or not
          example: true
      xml:
        name: team
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic

````