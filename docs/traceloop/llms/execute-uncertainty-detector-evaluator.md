# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-uncertainty-detector-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute uncertainty-detector evaluator

> Detect uncertainty in the text

**Request Body:**
- `input.prompt` (string, required): The text to detect uncertainty in



## OpenAPI

````yaml post /v2/evaluators/execute/uncertainty-detector
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/uncertainty-detector:
    post:
      tags:
        - evaluators
      summary: Execute uncertainty-detector evaluator
      description: |-
        Detect uncertainty in the text

        **Request Body:**
        - `input.prompt` (string, required): The text to detect uncertainty in
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.UncertaintyDetectorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.UncertaintyDetectorResponse'
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
    request.UncertaintyDetectorRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.UncertaintyDetectorInput'
      required:
        - input
      type: object
    response.UncertaintyDetectorResponse:
      properties:
        answer:
          example: Paris
          type: string
        uncertainty:
          example: 0.95
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.UncertaintyDetectorInput:
      properties:
        prompt:
          example: I am not sure, I think the capital of France is Paris.
          type: string
      required:
        - prompt
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````