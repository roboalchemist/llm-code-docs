# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-intent-change-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute intent-change evaluator

> Detect changes in user intent between prompts and completions

**Request Body:**
- `input.prompts` (string, required): JSON array of prompts in the conversation
- `input.completions` (string, required): JSON array of completions in the conversation



## OpenAPI

````yaml post /v2/evaluators/execute/intent-change
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/intent-change:
    post:
      tags:
        - evaluators
      summary: Execute intent-change evaluator
      description: >-
        Detect changes in user intent between prompts and completions


        **Request Body:**

        - `input.prompts` (string, required): JSON array of prompts in the
        conversation

        - `input.completions` (string, required): JSON array of completions in
        the conversation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.IntentChangeRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.IntentChangeResponse'
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
    request.IntentChangeRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.IntentChangeInput'
      required:
        - input
      type: object
    response.IntentChangeResponse:
      properties:
        pass:
          example: true
          type: boolean
        reason:
          example: User intent remained consistent throughout the conversation
          type: string
        score:
          example: 1
          type: integer
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.IntentChangeInput:
      properties:
        completions:
          example: >-
            ["Sure, I can help with hotel booking", "No problem, let me search
            for flights"]
          type: string
        prompts:
          example: '["I want to book a hotel", "Actually, I need a flight instead"]'
          type: string
      required:
        - completions
        - prompts
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````