# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-tone-detection-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute tone-detection evaluator

> Detect the tone of the text

**Request Body:**
- `input.text` (string, required): The text to detect the tone of



## OpenAPI

````yaml post /v2/evaluators/execute/tone-detection
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/tone-detection:
    post:
      tags:
        - evaluators
      summary: Execute tone-detection evaluator
      description: |-
        Detect the tone of the text

        **Request Body:**
        - `input.text` (string, required): The text to detect the tone of
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.ToneDetectionRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ToneDetectionResponse'
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
    request.ToneDetectionRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.ToneDetectionInput'
      required:
        - input
      type: object
    response.ToneDetectionResponse:
      properties:
        score:
          example: 0.95
          type: number
        tone:
          example: neutral
          type: string
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.ToneDetectionInput:
      properties:
        text:
          example: The capital of France is Paris.
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