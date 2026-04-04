# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-faithfulness-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute faithfulness evaluator

> Check if a completion is faithful to the provided context

**Request Body:**
- `input.completion` (string, required): The LLM completion to check for faithfulness
- `input.context` (string, required): The context that the completion should be faithful to
- `input.question` (string, required): The original question asked



## OpenAPI

````yaml post /v2/evaluators/execute/faithfulness
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/faithfulness:
    post:
      tags:
        - evaluators
      summary: Execute faithfulness evaluator
      description: >-
        Check if a completion is faithful to the provided context


        **Request Body:**

        - `input.completion` (string, required): The LLM completion to check for
        faithfulness

        - `input.context` (string, required): The context that the completion
        should be faithful to

        - `input.question` (string, required): The original question asked
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.FaithfulnessRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.FaithfulnessResponse'
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
    request.FaithfulnessRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.FaithfulnessInput'
      required:
        - input
      type: object
    response.FaithfulnessResponse:
      properties:
        is_faithful:
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
    request.FaithfulnessInput:
      properties:
        completion:
          example: The Eiffel Tower is located in Paris and was built in 1889.
          type: string
        context:
          example: >-
            The Eiffel Tower is a wrought-iron lattice tower on the Champ de
            Mars in Paris, France. It was constructed from 1887 to 1889.
          type: string
        question:
          example: When was the Eiffel Tower built?
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