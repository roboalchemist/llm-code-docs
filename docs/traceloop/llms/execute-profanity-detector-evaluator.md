# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-profanity-detector-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute profanity-detector evaluator

> Detect profanity in text

**Request Body:**
- `input.text` (string, required): The text to scan for profanity



## OpenAPI

````yaml post /v2/evaluators/execute/profanity-detector
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/profanity-detector:
    post:
      tags:
        - evaluators
      summary: Execute profanity-detector evaluator
      description: |-
        Detect profanity in text

        **Request Body:**
        - `input.text` (string, required): The text to scan for profanity
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.ProfanityDetectorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ProfanityDetectorResponse'
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
    request.ProfanityDetectorRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.ProfanityDetectorInput'
      required:
        - input
      type: object
    response.ProfanityDetectorResponse:
      properties:
        has_profanity:
          example: false
          type: boolean
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.ProfanityDetectorInput:
      properties:
        text:
          example: This is a clean and professional message.
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