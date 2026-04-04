# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-perplexity-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute perplexity evaluator

> Measure text perplexity from logprobs

**Request Body:**
- `input.logprobs` (string, required): JSON array of log probabilities from the model



## OpenAPI

````yaml post /v2/evaluators/execute/perplexity
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/perplexity:
    post:
      tags:
        - evaluators
      summary: Execute perplexity evaluator
      description: >-
        Measure text perplexity from logprobs


        **Request Body:**

        - `input.logprobs` (string, required): JSON array of log probabilities
        from the model
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.PerplexityRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.PerplexityResponse'
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
    request.PerplexityRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.PerplexityInput'
      required:
        - input
      type: object
    response.PerplexityResponse:
      properties:
        perplexity_score:
          example: 12.5
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.PerplexityInput:
      properties:
        logprobs:
          example: '[-2.3, -1.5, -0.8, -1.2, -0.5]'
          type: string
      required:
        - logprobs
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````