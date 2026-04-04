# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-sexism-detector-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute sexism-detector evaluator

> Detect sexist language and bias

**Request Body:**
- `input.text` (string, required): The text to scan for sexist content
- `config.threshold` (float, optional): Detection threshold (default: 0.5)



## OpenAPI

````yaml post /v2/evaluators/execute/sexism-detector
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/sexism-detector:
    post:
      tags:
        - evaluators
      summary: Execute sexism-detector evaluator
      description: >-
        Detect sexist language and bias


        **Request Body:**

        - `input.text` (string, required): The text to scan for sexist content

        - `config.threshold` (float, optional): Detection threshold (default:
        0.5)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.SexismDetectorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.SexismDetectorResponse'
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
    request.SexismDetectorRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.SexismDetectorConfigRequest'
        input:
          $ref: '#/components/schemas/request.SexismDetectorInput'
      required:
        - input
      type: object
    response.SexismDetectorResponse:
      properties:
        is_safe:
          example: safe
          type: string
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.SexismDetectorConfigRequest:
      properties:
        threshold:
          example: 0.5
          type: number
      type: object
    request.SexismDetectorInput:
      properties:
        text:
          example: All team members should be treated equally regardless of gender.
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