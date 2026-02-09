# Source: https://docs.helicone.ai/rest/evals/get-v1evalsscores.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Evaluation Scores

> Retrieve scoring metrics for evaluations

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml get /v1/evals/scores
openapi: 3.0.0
info:
  title: helicone-api
  version: 1.0.0
  license:
    name: MIT
  contact: {}
servers:
  - url: https://api.helicone.ai/
  - url: http://localhost:8585/
security: []
paths:
  /v1/evals/scores:
    get:
      tags:
        - Evals
      operationId: GetEvalScores
      parameters: []
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Result_string-Array.string_'
      security:
        - api_key: []
components:
  schemas:
    Result_string-Array.string_:
      anyOf:
        - $ref: '#/components/schemas/ResultSuccess_string-Array_'
        - $ref: '#/components/schemas/ResultError_string_'
    ResultSuccess_string-Array_:
      properties:
        data:
          items:
            type: string
          type: array
        error:
          type: number
          enum:
            - null
          nullable: true
      required:
        - data
        - error
      type: object
      additionalProperties: false
    ResultError_string_:
      properties:
        data:
          type: number
          enum:
            - null
          nullable: true
        error:
          type: string
      required:
        - data
        - error
      type: object
      additionalProperties: false
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````