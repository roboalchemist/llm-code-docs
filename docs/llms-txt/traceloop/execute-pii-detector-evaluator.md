# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-pii-detector-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute pii-detector evaluator

> Detect personally identifiable information in text

**Request Body:**
- `input.text` (string, required): The text to scan for personally identifiable information
- `config.probability_threshold` (float, optional): Detection threshold (default: 0.8)



## OpenAPI

````yaml post /v2/evaluators/execute/pii-detector
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/pii-detector:
    post:
      tags:
        - evaluators
      summary: Execute pii-detector evaluator
      description: >-
        Detect personally identifiable information in text


        **Request Body:**

        - `input.text` (string, required): The text to scan for personally
        identifiable information

        - `config.probability_threshold` (float, optional): Detection threshold
        (default: 0.8)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.PIIDetectorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.PIIDetectorResponse'
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
    request.PIIDetectorRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.PIIDetectorConfigRequest'
        input:
          $ref: '#/components/schemas/request.PIIDetectorInput'
      required:
        - input
      type: object
    response.PIIDetectorResponse:
      properties:
        has_pii:
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
    request.PIIDetectorConfigRequest:
      properties:
        probability_threshold:
          example: 0.8
          type: number
      type: object
    request.PIIDetectorInput:
      properties:
        text:
          example: >-
            Please contact John Smith at john.smith@email.com or call
            555-123-4567.
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