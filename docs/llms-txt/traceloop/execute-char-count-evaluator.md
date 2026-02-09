# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-char-count-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute char-count evaluator

> Count the number of characters in text

**Request Body:**
- `input.text` (string, required): The text to count characters in



## OpenAPI

````yaml post /v2/evaluators/execute/char-count
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/char-count:
    post:
      tags:
        - evaluators
      summary: Execute char-count evaluator
      description: |-
        Count the number of characters in text

        **Request Body:**
        - `input.text` (string, required): The text to count characters in
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.CharCountRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.CharCountResponse'
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
    request.CharCountRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.CharCountInput'
      required:
        - input
      type: object
    response.CharCountResponse:
      properties:
        char_count:
          example: 42
          type: integer
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.CharCountInput:
      properties:
        text:
          example: Hello, world! This is a sample text.
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