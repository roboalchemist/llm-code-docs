# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-answer-completeness-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute answer-completeness evaluator

> Evaluate whether the answer is complete and contains all the necessary information

**Request Body:**
- `input.question` (string, required): The original question
- `input.completion` (string, required): The completion to evaluate for completeness
- `input.context` (string, required): The context that provides the complete information



## OpenAPI

````yaml post /v2/evaluators/execute/answer-completeness
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/answer-completeness:
    post:
      tags:
        - evaluators
      summary: Execute answer-completeness evaluator
      description: >-
        Evaluate whether the answer is complete and contains all the necessary
        information


        **Request Body:**

        - `input.question` (string, required): The original question

        - `input.completion` (string, required): The completion to evaluate for
        completeness

        - `input.context` (string, required): The context that provides the
        complete information
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.AnswerCompletenessRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AnswerCompletenessResponse'
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
    request.AnswerCompletenessRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.AnswerCompletenessInput'
      required:
        - input
      type: object
    response.AnswerCompletenessResponse:
      properties:
        answer_completeness_score:
          example: 0.95
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.AnswerCompletenessInput:
      properties:
        completion:
          example: Paris.
          type: string
        context:
          example: The capital of France is Paris.
          type: string
        question:
          example: What is the capital of France?
          type: string
      required:
        - completion
        - context
        - question
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````