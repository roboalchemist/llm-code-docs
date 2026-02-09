# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-efficiency-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute agent-efficiency evaluator

> Evaluate agent efficiency - detect redundant calls, unnecessary follow-ups

**Request Body:**
- `input.trajectory_prompts` (string, required): JSON array of prompts in the agent trajectory
- `input.trajectory_completions` (string, required): JSON array of completions in the agent trajectory



## OpenAPI

````yaml post /v2/evaluators/execute/agent-efficiency
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/agent-efficiency:
    post:
      tags:
        - evaluators
      summary: Execute agent-efficiency evaluator
      description: >-
        Evaluate agent efficiency - detect redundant calls, unnecessary
        follow-ups


        **Request Body:**

        - `input.trajectory_prompts` (string, required): JSON array of prompts
        in the agent trajectory

        - `input.trajectory_completions` (string, required): JSON array of
        completions in the agent trajectory
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.AgentEfficiencyRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AgentEfficiencyResponse'
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
    request.AgentEfficiencyRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.AgentEfficiencyInput'
      required:
        - input
      type: object
    response.AgentEfficiencyResponse:
      properties:
        step_efficiency_reason:
          example: Agent completed task with minimal redundant steps
          type: string
        step_efficiency_score:
          example: 0.85
          type: number
        task_completion_reason:
          example: All required tasks were completed successfully
          type: string
        task_completion_score:
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
    request.AgentEfficiencyInput:
      properties:
        trajectory_completions:
          example: '["User found", "Email updated", "Changes saved"]'
          type: string
        trajectory_prompts:
          example: '["Find user info", "Update email", "Save changes"]'
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