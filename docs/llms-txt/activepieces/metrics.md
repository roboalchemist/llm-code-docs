# Source: https://www.activepieces.com/docs/endpoints/queue-metrics/metrics.md

# Queue Stats

> Get metrics

## OpenAPI

````yaml GET /v1/queue-metrics
paths:
  path: /v1/queue-metrics
  method: get
  servers:
    - url: https://cloud.activepieces.com/api
      description: Production Server
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Use your api key generated from the admin console
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
          - type: object
            properties:
              stats:
                allOf:
                  - type: object
                    properties:
                      active:
                        type: number
                      delayed:
                        type: number
                      prioritized:
                        type: number
                      waiting:
                        type: number
                      waiting-children:
                        type: number
                      completed:
                        type: number
                      failed:
                        type: number
                      paused:
                        type: number
                    required:
                      - active
                      - delayed
                      - prioritized
                      - waiting
                      - waiting-children
                      - completed
                      - failed
                      - paused
            requiredProperties:
              - stats
        examples:
          example:
            value:
              stats:
                active: 123
                delayed: 123
                prioritized: 123
                waiting: 123
                waiting-children: 123
                completed: 123
                failed: 123
                paused: 123
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````