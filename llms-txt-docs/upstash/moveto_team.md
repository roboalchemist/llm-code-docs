# Source: https://upstash.com/docs/devops/developer-api/redis/moveto_team.md

# Move To Team

> This endpoint moves database under a target team

## OpenAPI

````yaml devops/developer-api/openapi.yml post /redis/move-to-team
paths:
  path: /redis/move-to-team
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
              team_id:
                allOf:
                  - type: string
                    description: The ID of the target team
              database_id:
                allOf:
                  - type: string
                    description: The ID of the database to be moved
            required: true
            requiredProperties:
              - team_id
              - database_id
        examples:
          example:
            value:
              team_id: <string>
              database_id: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Database moved successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/moveto_team
components:
  schemas: {}

````