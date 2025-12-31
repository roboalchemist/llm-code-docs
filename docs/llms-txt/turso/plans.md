# Source: https://docs.turso.tech/api-reference/organizations/plans.md

# List Plans

> Returns a list of available plans and their quotas.

## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/plans
paths:
  path: /v1/organizations/{organizationSlug}/plans
  method: get
  servers:
    - url: https://api.turso.tech
      description: Turso's Platform API
  request:
    security: []
    parameters:
      path:
        organizationSlug:
          schema:
            - type: string
              required: true
              description: The slug of the organization or user account.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              plans:
                allOf:
                  - type: array
                    description: List of available plans.
                    items:
                      $ref: '#/components/schemas/OrganizationPlan'
        examples:
          example:
            value:
              plans:
                - name: starter
                  price: '0'
                  prices:
                    - value: '29'
                      timeline: monthly
                  quotas:
                    rowsRead: 1000000000
                    rowsWritten: 25000000
                    databases: 500
                    locations: 3
                    storage: 9000000000
                    groups: 1
                    bytesSynced: 3000000000
        description: Successful response
  deprecated: false
  type: path
components:
  schemas:
    OrganizationPlan:
      type: object
      properties:
        name:
          type: string
          description: The name of the plan.
          example: starter
        price:
          type: string
          description: The monthly price of the plan.
          example: '0'
        prices:
          type: array
          items:
            $ref: '#/components/schemas/PlanPrice'
        quotas:
          $ref: '#/components/schemas/PlanQuotas'
    PlanPrice:
      type: object
      properties:
        value:
          type: string
          description: Price of the available plan.
          example: '29'
        timeline:
          type: string
          description: Payment regularity.
          example: monthly
    PlanQuotas:
      type: object
      properties:
        rowsRead:
          type: integer
          description: The number of rows read allowed for the specific plan.
          example: 1000000000
        rowsWritten:
          type: integer
          description: The number of rows written allowed for the specific plan.
          example: 25000000
        databases:
          type: integer
          nullable: true
          description: The number of databases allowed for the specific plan.
          example: 500
        locations:
          type: integer
          description: The number of locations allowed for the specific plan.
          example: 3
        storage:
          type: integer
          description: The amount of storage allowed for the specific plan, in bytes.
          example: 9000000000
        groups:
          type: integer
          description: The number of groups allowed for the specific plan.
          example: 1
        bytesSynced:
          type: integer
          description: The number of bytes synced allowed for the specific plan, in bytes.
          example: 3000000000

````