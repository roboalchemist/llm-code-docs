# Source: https://upstash.com/docs/devops/developer-api/vector/set_index_plan.md

# Set Index Plan

> This endpoint is used to change the plan of an index.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /vector/index/{id}/setplan
paths:
  path: /vector/index/{id}/setplan
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The unique ID of the index to change plan for
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              target_plan:
                allOf:
                  - type: string
                    description: The new plan for the index
                    enum:
                      - free
                      - payg
                      - fixed
            required: true
            requiredProperties:
              - target_plan
        examples:
          example:
            value:
              target_plan: free
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Index plan changed successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/vector/set_index_plan
components:
  schemas: {}

````