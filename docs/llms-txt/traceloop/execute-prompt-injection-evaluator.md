# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-prompt-injection-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute prompt-injection evaluator

> Detect prompt injection attempts

**Request Body:**
- `input.prompt` (string, required): The prompt to check for injection attempts
- `config.threshold` (float, optional): Detection threshold (default: 0.5)



## OpenAPI

````yaml post /v2/evaluators/execute/prompt-injection
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/prompt-injection:
    post:
      tags:
        - evaluators
      summary: Execute prompt-injection evaluator
      description: >-
        Detect prompt injection attempts


        **Request Body:**

        - `input.prompt` (string, required): The prompt to check for injection
        attempts

        - `config.threshold` (float, optional): Detection threshold (default:
        0.5)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.PromptInjectionRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.PromptInjectionResponse'
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
    request.PromptInjectionRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.PromptInjectionConfigRequest'
        input:
          $ref: '#/components/schemas/request.PromptInjectionInput'
      required:
        - input
      type: object
    response.PromptInjectionResponse:
      properties:
        has_injection:
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
    request.PromptInjectionConfigRequest:
      properties:
        threshold:
          example: 0.5
          type: number
      type: object
    request.PromptInjectionInput:
      properties:
        prompt:
          example: What is the weather like today?
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