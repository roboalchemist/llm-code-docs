# Source: https://docs.agent.ai/api-reference/advanced/retrieve-variable.md

# Retrieve Variable

> Retrieve a variable from the agent's database

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_variable_from_database
paths:
  path: /action/get_variable_from_database
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
                    description: The variable to retrieve.
              variable_retrieval_depth:
                allOf:
                  - type: string
                    enum:
                      - most_recent_value
                      - historical_values
                    default: most_recent_value
                    description: How far back to retrieve data.
              agent_db_historical_values:
                allOf:
                  - type: string
                    enum:
                      - last hour
                      - last day
                      - last week
                      - last month
                      - all time
                    description: Historical data interval.
              agent_db_variable_retrieval_count:
                allOf:
                  - type: string
                    description: 'Number of items to retrieve (default: 10).'
            required: true
            requiredProperties:
              - variable
              - variable_retrieval_depth
        examples:
          example:
            value:
              variable: <string>
              variable_retrieval_depth: most_recent_value
              agent_db_historical_values: last hour
              agent_db_variable_retrieval_count: <string>
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
        description: Retrieved variable data
  deprecated: false
  type: path
components:
  schemas: {}

````