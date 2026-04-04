# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-goal-accuracy-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute agent-goal-accuracy evaluator

> Evaluate agent goal accuracy

**Request Body:**
- `input.question` (string, required): The original question or goal
- `input.completion` (string, required): The agent's completion/response
- `input.reference` (string, required): The expected reference answer



## OpenAPI

````yaml post /v2/evaluators/execute/agent-goal-accuracy
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/agent-goal-accuracy:
    post:
      tags:
        - evaluators
      summary: Execute agent-goal-accuracy evaluator
      description: |-
        Evaluate agent goal accuracy

        **Request Body:**
        - `input.question` (string, required): The original question or goal
        - `input.completion` (string, required): The agent's completion/response
        - `input.reference` (string, required): The expected reference answer
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.AgentGoalAccuracyRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AgentGoalAccuracyResponse'
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
    request.AgentGoalAccuracyRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.AgentGoalAccuracyInput'
      required:
        - input
      type: object
    response.AgentGoalAccuracyResponse:
      properties:
        accuracy_score:
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
    request.AgentGoalAccuracyInput:
      properties:
        completion:
          example: >-
            I have booked your flight from New York to Los Angeles departing
            Monday at 9am.
          type: string
        question:
          example: Book a flight from NYC to LA for next Monday
          type: string
        reference:
          example: 'Flight booked: NYC to LA, Monday departure'
          type: string
      required:
        - completion
        - question
        - reference
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````