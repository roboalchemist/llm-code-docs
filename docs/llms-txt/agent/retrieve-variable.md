# Source: https://docs.agent.ai/api-reference/advanced/retrieve-variable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Variable

> Retrieve a variable from the agent's database



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_variable_from_database
openapi: 3.0.0
info:
  version: 1.0.0
  title: AI Actions - Get Data
  description: API specifications for 'Get Data' category AI actions.
  license:
    name: MIT
servers:
  - url: https://api-lr.agent.ai/v1
security:
  - bearerAuth: []
paths:
  /action/get_variable_from_database:
    post:
      tags:
        - Advanced
      summary: Retrieve Variable
      description: Retrieve a variable from the agent's database
      operationId: getVariableFromDatabase
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                variable:
                  type: string
                  description: The variable to retrieve.
                variable_retrieval_depth:
                  type: string
                  enum:
                    - most_recent_value
                    - historical_values
                  default: most_recent_value
                  description: How far back to retrieve data.
                agent_db_historical_values:
                  type: string
                  enum:
                    - last hour
                    - last day
                    - last week
                    - last month
                    - all time
                  description: Historical data interval.
                agent_db_variable_retrieval_count:
                  type: string
                  description: 'Number of items to retrieve (default: 10).'
              required:
                - variable
                - variable_retrieval_depth
      responses:
        '200':
          description: Retrieved variable data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
components:
  schemas:
    ActionResponse:
      type: object
      properties:
        status:
          type: integer
          format: int32
          description: HTTP status code of the action response
        response:
          type: object
          description: Response data from the action
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer token from your account
        ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))

````