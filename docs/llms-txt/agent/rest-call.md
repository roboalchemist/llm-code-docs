# Source: https://docs.agent.ai/api-reference/advanced/rest-call.md

# REST call

> Make a REST API call to a specified endpoint.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/rest_call
paths:
  path: /action/rest_call
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
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
              url:
                allOf:
                  - type: string
                    description: API endpoint URL.
                    example: https://api.example.com/data
              method:
                allOf:
                  - type: string
                    enum:
                      - POST
                      - GET
                      - PUT
                      - HEAD
                    default: POST
                    description: HTTP method.
              headers:
                allOf:
                  - type: object
                    description: Request headers (JSON format)
              body:
                allOf:
                  - type: string
                    description: Request body (string)
            required: true
            requiredProperties:
              - url
              - method
              - body
        examples:
          example:
            value:
              url: https://api.example.com/data
              method: POST
              headers: {}
              body: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response:
                version: 0.92.0 AUG 21 2025
        description: API response
  deprecated: false
  type: path
components:
  schemas: {}

````