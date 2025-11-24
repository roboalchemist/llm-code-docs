# Source: https://docs.agent.ai/api-reference/advanced/store-variable.md

# Store Variable

> Store a variable in the agent's database

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/store_variable_to_database
paths:
  path: /action/store_variable_to_database
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
              variable:
                allOf:
                  - type: string
                    description: The variable to store.
            required: true
            requiredProperties:
              - variable
        examples:
          example:
            value:
              variable: <string>
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
              status: 123
              response: {}
        description: Confirmation of variable storage
  deprecated: false
  type: path
components:
  schemas: {}

````