# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-toxicity-detector-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute toxicity-detector evaluator

> Detect toxic or harmful language

**Request Body:**
- `input.text` (string, required): The text to scan for toxic content
- `config.threshold` (float, optional): Detection threshold (default: 0.5)



## OpenAPI

````yaml post /v2/evaluators/execute/toxicity-detector
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/toxicity-detector:
    post:
      tags:
        - evaluators
      summary: Execute toxicity-detector evaluator
      description: >-
        Detect toxic or harmful language


        **Request Body:**

        - `input.text` (string, required): The text to scan for toxic content

        - `config.threshold` (float, optional): Detection threshold (default:
        0.5)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.ToxicityDetectorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ToxicityDetectorResponse'
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
    request.ToxicityDetectorRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.ToxicityDetectorConfigRequest'
        input:
          $ref: '#/components/schemas/request.ToxicityDetectorInput'
      required:
        - input
      type: object
    response.ToxicityDetectorResponse:
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
    request.ToxicityDetectorConfigRequest:
      properties:
        threshold:
          example: 0.5
          type: number
      type: object
    request.ToxicityDetectorInput:
      properties:
        text:
          example: Thank you for your help with this project.
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