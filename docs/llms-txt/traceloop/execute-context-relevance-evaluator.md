# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-context-relevance-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute context-relevance evaluator

> Evaluate whether retrieved context contains sufficient information to answer the query

**Request Body:**
- `input.query` (string, required): The query/question to evaluate context relevance for
- `input.context` (string, required): The context to evaluate for relevance to the query
- `config.model` (string, optional): Model to use for evaluation (default: gpt-4o)



## OpenAPI

````yaml post /v2/evaluators/execute/context-relevance
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/context-relevance:
    post:
      tags:
        - evaluators
      summary: Execute context-relevance evaluator
      description: >-
        Evaluate whether retrieved context contains sufficient information to
        answer the query


        **Request Body:**

        - `input.query` (string, required): The query/question to evaluate
        context relevance for

        - `input.context` (string, required): The context to evaluate for
        relevance to the query

        - `config.model` (string, optional): Model to use for evaluation
        (default: gpt-4o)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.ContextRelevanceRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ContextRelevanceResponse'
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
    request.ContextRelevanceRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.ContextRelevanceConfigRequest'
        input:
          $ref: '#/components/schemas/request.ContextRelevanceInput'
      required:
        - input
      type: object
    response.ContextRelevanceResponse:
      properties:
        relevance_score:
          example: 0.88
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.ContextRelevanceConfigRequest:
      properties:
        model:
          example: gpt-4o
          type: string
      type: object
    request.ContextRelevanceInput:
      properties:
        context:
          example: >-
            Our store is open Monday to Friday from 9am to 6pm, and Saturday
            from 10am to 4pm. We are closed on Sundays.
          type: string
        query:
          example: What are the business hours?
          type: string
      required:
        - context
        - query
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````