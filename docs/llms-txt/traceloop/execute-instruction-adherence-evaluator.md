# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-instruction-adherence-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute instruction-adherence evaluator

> Evaluate how well responses follow given instructions

**Request Body:**
- `input.instructions` (string, required): The instructions that should be followed
- `input.response` (string, required): The response to evaluate for instruction adherence



## OpenAPI

````yaml post /v2/evaluators/execute/instruction-adherence
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/instruction-adherence:
    post:
      tags:
        - evaluators
      summary: Execute instruction-adherence evaluator
      description: >-
        Evaluate how well responses follow given instructions


        **Request Body:**

        - `input.instructions` (string, required): The instructions that should
        be followed

        - `input.response` (string, required): The response to evaluate for
        instruction adherence
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.InstructionAdherenceRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.InstructionAdherenceResponse'
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
    request.InstructionAdherenceRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.InstructionAdherenceInput'
      required:
        - input
      type: object
    response.InstructionAdherenceResponse:
      properties:
        instruction_adherence_score:
          example: 0.87
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.InstructionAdherenceInput:
      properties:
        instructions:
          example: Respond in exactly 3 bullet points and use formal language.
          type: string
        response:
          example: |-
            - First point about the topic
            - Second relevant consideration
            - Final concluding thought
          type: string
      required:
        - instructions
        - response
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````