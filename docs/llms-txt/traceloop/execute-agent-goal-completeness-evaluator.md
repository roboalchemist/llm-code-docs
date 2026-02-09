# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-goal-completeness-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute agent-goal-completeness evaluator

> Measure if agent accomplished all user goals

**Request Body:**
- `input.trajectory_prompts` (string, required): JSON array of prompts in the agent trajectory
- `input.trajectory_completions` (string, required): JSON array of completions in the agent trajectory
- `config.threshold` (number, required): Score threshold for pass/fail determination (0.0-1.0)



## OpenAPI

````yaml post /v2/evaluators/execute/agent-goal-completeness
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/agent-goal-completeness:
    post:
      tags:
        - evaluators
      summary: Execute agent-goal-completeness evaluator
      description: >-
        Measure if agent accomplished all user goals


        **Request Body:**

        - `input.trajectory_prompts` (string, required): JSON array of prompts
        in the agent trajectory

        - `input.trajectory_completions` (string, required): JSON array of
        completions in the agent trajectory

        - `config.threshold` (number, required): Score threshold for pass/fail
        determination (0.0-1.0)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.AgentGoalCompletenessRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AgentGoalCompletenessResponse'
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
    request.AgentGoalCompletenessRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.AgentGoalCompletenessConfigRequest'
        input:
          $ref: '#/components/schemas/request.AgentGoalCompletenessInput'
      required:
        - input
      type: object
    response.AgentGoalCompletenessResponse:
      properties:
        reason:
          example: All user goals were accomplished
          type: string
        result:
          example: complete
          type: string
        score:
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
    request.AgentGoalCompletenessConfigRequest:
      properties:
        threshold:
          example: 0.5
          type: number
      required:
        - threshold
      type: object
    request.AgentGoalCompletenessInput:
      properties:
        trajectory_completions:
          example: '["Account created", "Preferences saved", "Notifications enabled"]'
          type: string
        trajectory_prompts:
          example: '["Create new account", "Set preferences", "Enable notifications"]'
          type: string
      required:
        - trajectory_completions
        - trajectory_prompts
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````