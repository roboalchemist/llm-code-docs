# Source: https://upstash.com/docs/devops/developer-api/redis/update_budget.md

# Update Database Budget

> This endpoint updates the monthly budget of a Redis database.

## OpenAPI

````yaml devops/developer-api/openapi.yml patch /redis/update-budget/{id}
paths:
  path: /redis/update-budget/{id}
  method: patch
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
              description: The ID of the database whose budget will be updated
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              budget:
                allOf:
                  - type: integer
                    description: The new monthly budget for the database
            required: true
            requiredProperties:
              - budget
        examples:
          example:
            value:
              budget: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Budget updated successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/update_budget
components:
  schemas: {}

````