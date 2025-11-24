# Source: https://upstash.com/docs/devops/developer-api/teams/list_teams.md

# List Teams

> This endpoint lists all teams of user.

## OpenAPI

````yaml devops/developer-api/openapi.yml get /teams
paths:
  path: /teams
  method: get
  servers:
    - url: https://api.upstash.com/v2
  request:
    security:
      - title: basicAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Team'
        examples:
          example:
            value:
              - team_id: 95849b27-40d0-4532-8695-d2028847f823
                team_name: test_team_name
                copy_cc: true
        description: Teams retrieved successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/teams/list_teams
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

````