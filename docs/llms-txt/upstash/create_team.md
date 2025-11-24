# Source: https://upstash.com/docs/devops/developer-api/teams/create_team.md

# Create Team

> This endpoint creates a new team.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /team
paths:
  path: /team
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              team_name:
                allOf:
                  - type: string
                    description: Name of the new team
                    example: myteam
              copy_cc:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to copy existing credit card information to team
                      or not
                    example: true
            required: true
            refIdentifier: '#/components/schemas/CreateTeamRequest'
            requiredProperties:
              - team_name
              - copy_cc
        examples:
          example:
            value:
              team_name: myteam
              copy_cc: true
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              team_id:
                allOf:
                  - type: string
                    description: ID of the team
                    example: 95849b27-40d0-4532-8695-d2028847f823
              team_name:
                allOf:
                  - type: string
                    description: Name of the team
                    example: test_team_name
              copy_cc:
                allOf:
                  - type: boolean
                    description: >-
                      Whether creditcard information added to team during
                      creation or not
                    example: true
            refIdentifier: '#/components/schemas/Team'
        examples:
          example:
            value:
              team_id: 95849b27-40d0-4532-8695-d2028847f823
              team_name: test_team_name
              copy_cc: true
        description: Team created successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/teams/create_team
components:
  schemas: {}

````