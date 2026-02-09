# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-prompt-perplexity-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute prompt-perplexity evaluator

> Measure prompt perplexity to detect potential injection attempts

**Request Body:**
- `input.prompt` (string, required): The prompt to calculate perplexity for



## OpenAPI

````yaml post /v2/evaluators/execute/prompt-perplexity
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/prompt-perplexity:
    post:
      tags:
        - evaluators
      summary: Execute prompt-perplexity evaluator
      description: >-
        Measure prompt perplexity to detect potential injection attempts


        **Request Body:**

        - `input.prompt` (string, required): The prompt to calculate perplexity
        for
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.PromptPerplexityRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.PromptPerplexityResponse'
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
    request.PromptPerplexityRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.PromptPerplexityInput'
      required:
        - input
      type: object
    response.PromptPerplexityResponse:
      properties:
        perplexity_score:
          example: 8.3
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.PromptPerplexityInput:
      properties:
        prompt:
          example: What is the capital of France?
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