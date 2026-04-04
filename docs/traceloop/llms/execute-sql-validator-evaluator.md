# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-sql-validator-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute sql-validator evaluator

> Validate SQL query syntax

**Request Body:**
- `input.text` (string, required): The text to validate as SQL



## OpenAPI

````yaml post /v2/evaluators/execute/sql-validator
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/sql-validator:
    post:
      tags:
        - evaluators
      summary: Execute sql-validator evaluator
      description: |-
        Validate SQL query syntax

        **Request Body:**
        - `input.text` (string, required): The text to validate as SQL
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.SQLValidatorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.SQLValidatorResponse'
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
    request.SQLValidatorRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.SQLValidatorInput'
      required:
        - input
      type: object
    response.SQLValidatorResponse:
      properties:
        is_valid_sql:
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
    request.SQLValidatorInput:
      properties:
        text:
          example: SELECT * FROM users WHERE id = 1;
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