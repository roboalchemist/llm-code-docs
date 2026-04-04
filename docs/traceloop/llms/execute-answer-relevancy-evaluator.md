# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-answer-relevancy-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute answer-relevancy evaluator

> Check if an answer is relevant to a question

**Request Body:**
- `input.answer` (string, required): The answer to evaluate for relevancy
- `input.question` (string, required): The question that the answer should be relevant to



## OpenAPI

````yaml post /v2/evaluators/execute/answer-relevancy
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/answer-relevancy:
    post:
      tags:
        - evaluators
      summary: Execute answer-relevancy evaluator
      description: >-
        Check if an answer is relevant to a question


        **Request Body:**

        - `input.answer` (string, required): The answer to evaluate for
        relevancy

        - `input.question` (string, required): The question that the answer
        should be relevant to
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.AnswerRelevancyRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AnswerRelevancyResponse'
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
    request.AnswerRelevancyRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.AnswerRelevancyInput'
      required:
        - input
      type: object
    response.AnswerRelevancyResponse:
      properties:
        is_relevant:
          example: true
          type: boolean
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.AnswerRelevancyInput:
      properties:
        answer:
          example: The capital of France is Paris.
          type: string
        question:
          example: What is the capital of France?
          type: string
      required:
        - answer
        - question
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````