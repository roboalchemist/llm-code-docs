# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-semantic-similarity-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute semantic-similarity evaluator

> Calculate semantic similarity between completion and reference

**Request Body:**
- `input.completion` (string, required): The completion text to compare
- `input.reference` (string, required): The reference text to compare against



## OpenAPI

````yaml post /v2/evaluators/execute/semantic-similarity
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/semantic-similarity:
    post:
      tags:
        - evaluators
      summary: Execute semantic-similarity evaluator
      description: >-
        Calculate semantic similarity between completion and reference


        **Request Body:**

        - `input.completion` (string, required): The completion text to compare

        - `input.reference` (string, required): The reference text to compare
        against
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.SemanticSimilarityRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.SemanticSimilarityResponse'
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
    request.SemanticSimilarityRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.SemanticSimilarityInput'
      required:
        - input
      type: object
    response.SemanticSimilarityResponse:
      properties:
        similarity_score:
          example: 0.92
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.SemanticSimilarityInput:
      properties:
        completion:
          example: The cat sat on the mat.
          type: string
        reference:
          example: A feline was resting on the rug.
          type: string
      required:
        - completion
        - reference
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````