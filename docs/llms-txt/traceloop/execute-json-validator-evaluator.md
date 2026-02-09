# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-json-validator-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute json-validator evaluator

> Validate JSON syntax

**Request Body:**
- `input.text` (string, required): The text to validate as JSON
- `config.enable_schema_validation` (bool, optional): Enable JSON schema validation
- `config.schema_string` (string, optional): JSON schema to validate against



## OpenAPI

````yaml post /v2/evaluators/execute/json-validator
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/json-validator:
    post:
      tags:
        - evaluators
      summary: Execute json-validator evaluator
      description: >-
        Validate JSON syntax


        **Request Body:**

        - `input.text` (string, required): The text to validate as JSON

        - `config.enable_schema_validation` (bool, optional): Enable JSON schema
        validation

        - `config.schema_string` (string, optional): JSON schema to validate
        against
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.JSONValidatorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.JSONValidatorResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
      security:
        - BearerAuth: []
components:
  schemas:
    request.JSONValidatorRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.JSONValidatorConfigRequest'
        input:
          $ref: '#/components/schemas/request.JSONValidatorInput'
      required:
        - input
      type: object
    response.JSONValidatorResponse:
      properties:
        is_valid_json:
          example: true
          type: boolean
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.JSONValidatorConfigRequest:
      properties:
        enable_schema_validation:
          example: true
          type: boolean
        schema_string:
          example: '{}'
          type: string
      type: object
    request.JSONValidatorInput:
      properties:
        text:
          example: '{"name": "John", "age": 30}'
          type: string
      required:
        - text
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````