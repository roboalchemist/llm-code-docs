# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-secrets-detector-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute secrets-detector evaluator

> Detect secrets and credentials in text

**Request Body:**
- `input.text` (string, required): The text to scan for secrets (API keys, passwords, etc.)



## OpenAPI

````yaml post /v2/evaluators/execute/secrets-detector
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/secrets-detector:
    post:
      tags:
        - evaluators
      summary: Execute secrets-detector evaluator
      description: >-
        Detect secrets and credentials in text


        **Request Body:**

        - `input.text` (string, required): The text to scan for secrets (API
        keys, passwords, etc.)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.SecretsDetectorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.SecretsDetectorResponse'
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
    request.SecretsDetectorRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.SecretsDetectorInput'
      required:
        - input
      type: object
    response.SecretsDetectorResponse:
      properties:
        has_secret:
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
    request.SecretsDetectorInput:
      properties:
        text:
          example: Here is some text without any API keys or passwords.
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