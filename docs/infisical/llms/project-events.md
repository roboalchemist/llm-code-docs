# Source: https://infisical.com/docs/api-reference/endpoints/events/project-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Project Events

> Subscribe to project events



## OpenAPI

````yaml POST /api/v1/events/subscribe/project-events
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v1/events/subscribe/project-events:
    post:
      tags:
        - Event Subscriptions
      description: Subscribe to project events
      operationId: subscribeToProjectEvents
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                projectId:
                  type: string
                  description: The ID of the project to subscribe to events for.
                register:
                  type: array
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
              required:
                - projectId
                - register
              additionalProperties: false
        required: true
      responses:
        '200':
          description: Default Response

````