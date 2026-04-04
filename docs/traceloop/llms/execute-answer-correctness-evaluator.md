# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-answer-correctness-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute answer-correctness evaluator

> Evaluate factual accuracy by comparing answers against ground truth

**Request Body:**
- `input.question` (string, required): The original question
- `input.completion` (string, required): The completion to evaluate
- `input.ground_truth` (string, required): The expected correct answer



## OpenAPI

````yaml post /v2/evaluators/execute/answer-correctness
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/answer-correctness:
    post:
      tags:
        - evaluators
      summary: Execute answer-correctness evaluator
      description: |-
        Evaluate factual accuracy by comparing answers against ground truth

        **Request Body:**
        - `input.question` (string, required): The original question
        - `input.completion` (string, required): The completion to evaluate
        - `input.ground_truth` (string, required): The expected correct answer
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.AnswerCorrectnessRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AnswerCorrectnessResponse'
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
    request.AnswerCorrectnessRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.AnswerCorrectnessInput'
      required:
        - input
      type: object
    response.AnswerCorrectnessResponse:
      properties:
        correctness_score:
          example: 0.91
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.AnswerCorrectnessInput:
      properties:
        completion:
          example: World War II ended in 1945.
          type: string
        ground_truth:
          example: '1945'
          type: string
        question:
          example: What year did World War II end?
          type: string
      required:
        - completion
        - ground_truth
        - question
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````