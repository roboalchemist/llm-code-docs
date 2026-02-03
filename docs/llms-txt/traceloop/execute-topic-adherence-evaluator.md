# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-topic-adherence-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute topic-adherence evaluator

> Evaluate topic adherence

**Request Body:**
- `input.question` (string, required): The original question
- `input.completion` (string, required): The completion to evaluate
- `input.reference_topics` (string, required): Comma-separated list of expected topics



## OpenAPI

````yaml post /v2/evaluators/execute/topic-adherence
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/topic-adherence:
    post:
      tags:
        - evaluators
      summary: Execute topic-adherence evaluator
      description: >-
        Evaluate topic adherence


        **Request Body:**

        - `input.question` (string, required): The original question

        - `input.completion` (string, required): The completion to evaluate

        - `input.reference_topics` (string, required): Comma-separated list of
        expected topics
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.TopicAdherenceRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.TopicAdherenceResponse'
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
    request.TopicAdherenceRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.TopicAdherenceInput'
      required:
        - input
      type: object
    response.TopicAdherenceResponse:
      properties:
        adherence_score:
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
    request.TopicAdherenceInput:
      properties:
        completion:
          example: >-
            Machine learning is a subset of AI that enables systems to learn
            from data.
          type: string
        question:
          example: Tell me about machine learning
          type: string
        reference_topics:
          example: artificial intelligence, data science, algorithms
          type: string
      required:
        - completion
        - question
        - reference_topics
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````