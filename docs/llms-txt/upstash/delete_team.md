# Source: https://upstash.com/docs/devops/developer-api/teams/delete_team.md

# Delete Team

> This endpoint deletes a team.

## OpenAPI

````yaml devops/developer-api/openapi.yml delete /team/{id}
paths:
  path: /team/{id}
  method: delete
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The ID of the team to delete
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Team deleted successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/teams/delete_team
components:
  schemas: {}

````