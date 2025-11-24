# Source: https://upstash.com/docs/devops/developer-api/redis/change_plan.md

# Change Database Plan

> This endpoint changes the plan of a Redis database.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /redis/change-plan/{id}
paths:
  path: /redis/change-plan/{id}
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
              description: The ID of the database whose plan will be changed
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              database_id:
                allOf:
                  - type: string
                    description: ID of the database
                    example: 6gcefvfd-9627-2tz5-4l71-c5679g19d2g4
              plan_name:
                allOf:
                  - type: string
                    description: The new plan for the database
                    enum:
                      - free
                      - payg
                      - fixed_250mb
                      - fixed_1gb
                      - fixed_5gb
                      - fixed_10gb
                      - fixed_50gb
                      - fixed_100gb
                      - fixed_500gb
                    example: fixed_1gb
              auto_upgrade:
                allOf:
                  - type: boolean
                    description: Whether to enable automatic upgrade for the database
                    example: true
              prod_pack_enabled:
                allOf:
                  - type: boolean
                    description: Whether to enable the production pack for the database
                    example: false
            required: true
            refIdentifier: '#/components/schemas/ChangePlanRequest'
            requiredProperties:
              - plan_name
        examples:
          example:
            value:
              database_id: 6gcefvfd-9627-2tz5-4l71-c5679g19d2g4
              plan_name: fixed_1gb
              auto_upgrade: true
              prod_pack_enabled: false
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Plan changed successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/change_plan
components:
  schemas: {}

````