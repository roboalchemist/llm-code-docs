# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-word-count-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute word-count evaluator

> Count the number of words in text

**Request Body:**
- `input.text` (string, required): The text to count words in



## OpenAPI

````yaml post /v2/evaluators/execute/word-count
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/word-count:
    post:
      tags:
        - evaluators
      summary: Execute word-count evaluator
      description: |-
        Count the number of words in text

        **Request Body:**
        - `input.text` (string, required): The text to count words in
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.WordCountRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.WordCountResponse'
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
    request.WordCountRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.WordCountInput'
      required:
        - input
      type: object
    response.WordCountResponse:
      properties:
        word_count:
          example: 10
          type: integer
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.WordCountInput:
      properties:
        text:
          example: This is a sample text with several words.
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