# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-html-comparison-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute html-comparison evaluator

> Compare two HTML documents for structural and content similarity

**Request Body:**
- `input.html1` (string, required): The first HTML document to compare
- `input.html2` (string, required): The second HTML document to compare



## OpenAPI

````yaml post /v2/evaluators/execute/html-comparison
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/html-comparison:
    post:
      tags:
        - evaluators
      summary: Execute html-comparison evaluator
      description: |-
        Compare two HTML documents for structural and content similarity

        **Request Body:**
        - `input.html1` (string, required): The first HTML document to compare
        - `input.html2` (string, required): The second HTML document to compare
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.HtmlComparisonRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.HtmlComparisonResponse'
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
    request.HtmlComparisonRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.HtmlComparisonInput'
      required:
        - input
      type: object
    response.HtmlComparisonResponse:
      properties:
        similarity_score:
          example: 0.92
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.HtmlComparisonInput:
      properties:
        html1:
          example: <html><body><h1>Hello, world!</h1></body></html>
          type: string
        html2:
          example: <html><body><h1>Hello, world!</h1></body></html>
          type: string
      required:
        - html1
        - html2
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````