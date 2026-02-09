# Source: https://docs.agent.ai/api-reference/advanced/rest-call.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# REST call

> Make a REST API call to a specified endpoint.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/rest_call
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
  /action/rest_call:
    post:
      tags:
        - Advanced
      summary: REST call
      description: Make a REST API call to a specified endpoint.
      operationId: restCall
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  description: API endpoint URL.
                  example: https://api.example.com/data
                method:
                  type: string
                  enum:
                    - POST
                    - GET
                    - PUT
                    - HEAD
                  default: POST
                  description: HTTP method.
                headers:
                  type: object
                  description: Request headers (JSON format)
                body:
                  type: string
                  description: Request body (string)
              required:
                - url
                - method
                - body
      responses:
        '200':
          description: API response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  version: 0.92.0 AUG 21 2025
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