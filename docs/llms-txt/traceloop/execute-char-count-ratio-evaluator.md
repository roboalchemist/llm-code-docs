# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-char-count-ratio-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute char-count-ratio evaluator

> Calculate the ratio of characters between two texts

**Request Body:**
- `input.numerator_text` (string, required): The numerator text (will be divided by denominator)
- `input.denominator_text` (string, required): The denominator text (divides the numerator)



## OpenAPI

````yaml post /v2/evaluators/execute/char-count-ratio
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/char-count-ratio:
    post:
      tags:
        - evaluators
      summary: Execute char-count-ratio evaluator
      description: >-
        Calculate the ratio of characters between two texts


        **Request Body:**

        - `input.numerator_text` (string, required): The numerator text (will be
        divided by denominator)

        - `input.denominator_text` (string, required): The denominator text
        (divides the numerator)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.CharCountRatioRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.CharCountRatioResponse'
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
    request.CharCountRatioRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.CharCountRatioInput'
      required:
        - input
      type: object
    response.CharCountRatioResponse:
      properties:
        char_ratio:
          example: 0.75
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.CharCountRatioInput:
      properties:
        denominator_text:
          example: This is a longer text for comparison
          type: string
        numerator_text:
          example: Short text
          type: string
      required:
        - denominator_text
        - numerator_text
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````