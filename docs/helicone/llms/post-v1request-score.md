# Source: https://docs.helicone.ai/rest/request/post-v1request-score.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit Score

> Submit a score for a specific request.

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml post /v1/request/{requestId}/score
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
  /v1/request/{requestId}/score:
    post:
      tags:
        - Request
      operationId: AddScores
      parameters:
        - in: path
          name: requestId
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ScoreRequest'
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Result_null.string_'
      security:
        - api_key: []
components:
  schemas:
    ScoreRequest:
      properties:
        scores:
          $ref: '#/components/schemas/Scores'
      required:
        - scores
      type: object
      additionalProperties: false
    Result_null.string_:
      anyOf:
        - $ref: '#/components/schemas/ResultSuccess_null_'
        - $ref: '#/components/schemas/ResultError_string_'
    Scores:
      $ref: '#/components/schemas/Record_string.number-or-boolean-or-undefined_'
    ResultSuccess_null_:
      properties:
        data:
          type: number
          enum:
            - null
          nullable: true
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
    Record_string.number-or-boolean-or-undefined_:
      properties: {}
      additionalProperties:
        anyOf:
          - type: number
            format: double
          - type: boolean
      type: object
      description: Construct a type with a set of properties K of type T
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````