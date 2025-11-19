# Source: https://docs.turso.tech/api-reference/organizations/subscription.md

# Current Subscription

> Returns the current subscription details for the organization.

## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/subscription
paths:
  path: /v1/organizations/{organizationSlug}/subscription
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
              subscription:
                allOf:
                  - type: object
                    properties:
                      name:
                        type: string
                        description: The name of the plan for the current subscription.
                        example: scaler
                      overages:
                        type: boolean
                        description: Whether overages are enabled for the organization.
                      plan:
                        type: string
                        description: The name of the plan for the current subscription.
                        example: scaler
                      timeline:
                        type: string
                        description: Whether the plan is billed monthly or yearly.
                        example: monthly
        examples:
          example:
            value:
              subscription:
                name: scaler
                overages: true
                plan: scaler
                timeline: monthly
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````