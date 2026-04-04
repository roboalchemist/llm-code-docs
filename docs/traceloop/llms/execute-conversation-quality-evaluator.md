# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-conversation-quality-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute conversation-quality evaluator

> Evaluate conversation quality based on tone, clarity, flow, responsiveness, and transparency

**Request Body:**
- `input.prompts` (string, required): JSON array of prompts in the conversation
- `input.completions` (string, required): JSON array of completions in the conversation



## OpenAPI

````yaml post /v2/evaluators/execute/conversation-quality
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/conversation-quality:
    post:
      tags:
        - evaluators
      summary: Execute conversation-quality evaluator
      description: >-
        Evaluate conversation quality based on tone, clarity, flow,
        responsiveness, and transparency


        **Request Body:**

        - `input.prompts` (string, required): JSON array of prompts in the
        conversation

        - `input.completions` (string, required): JSON array of completions in
        the conversation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.ConversationQualityRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ConversationQualityResponse'
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
    request.ConversationQualityRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.ConversationQualityInput'
      required:
        - input
      type: object
    response.ConversationQualityResponse:
      properties:
        conversation_quality_score:
          example: 0.82
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.ConversationQualityInput:
      properties:
        completions:
          example: >-
            ["Hi! I'd be happy to assist you today.", "We offer consulting,
            development, and support services."]
          type: string
        prompts:
          example: '["Hello, how can I help?", "What services do you offer?"]'
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