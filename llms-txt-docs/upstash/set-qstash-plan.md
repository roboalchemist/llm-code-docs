# Source: https://upstash.com/docs/api-reference/qstash/set-qstash-plan.md

# Set QStash Plan

> Changes the QStash account to a different plan type.
This operation changes the plan and associated limits for the QStash account.


## OpenAPI

````yaml devops/developer-api/openapi.yml post /qstash-upgrade
paths:
  path: /qstash-upgrade
  method: post
  servers:
    - url: https://api.upstash.com
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
              customer_id:
                allOf:
                  - type: string
                    description: Customer identifier or team ID
                    example: example@upstash.com
              plan_name:
                allOf:
                  - type: string
                    description: Target plan to upgrade to
                    enum:
                      - paid
                      - qstash_enterprise_1m
                      - qstash_enterprise_10m
                    example: paid
            required: true
            requiredProperties:
              - customer_id
              - plan_name
        examples:
          example:
            value:
              customer_id: example@upstash.com
              plan_name: paid
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: QStash plan changed successfully
  deprecated: false
  type: path
components:
  schemas: {}

````