# Source: https://docs.agent.ai/api-reference/advanced/store-variable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Store Variable

> Store a variable in the agent's database



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/store_variable_to_database
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
  /action/store_variable_to_database:
    post:
      tags:
        - Advanced
      summary: Store Variable
      description: Store a variable in the agent's database
      operationId: storeVariableToDatabase
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                variable:
                  type: string
                  description: The variable to store.
              required:
                - variable
      responses:
        '200':
          description: Confirmation of variable storage
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