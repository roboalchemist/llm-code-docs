# Source: https://infisical.com/docs/api-reference/endpoints/events/project-events.md

# Project Events

> Subscribe to project events

## OpenAPI

````yaml POST /api/v1/events/subscribe/project-events
paths:
  path: /api/v1/events/subscribe/project-events
  method: post
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security: []
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
              projectId:
                allOf:
                  - type: string
                    description: The ID of the project to subscribe to events for.
              register:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        event:
                          type: string
                          enum:
                            - secret:create
                            - secret:update
                            - secret:delete
                            - secret:import-mutation
                        conditions:
                          type: object
                          properties:
                            secretPath:
                              type: string
                              default: /
                            environmentSlug:
                              type: string
                          required:
                            - environmentSlug
                          additionalProperties: false
                      required:
                        - event
                      additionalProperties: false
                    minItems: 1
                    maxItems: 10
            required: true
            requiredProperties:
              - projectId
              - register
            additionalProperties: false
        examples:
          example:
            value:
              projectId: <string>
              register:
                - event: secret:create
                  conditions:
                    secretPath: /
                    environmentSlug: <string>
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Default Response
        examples: {}
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````