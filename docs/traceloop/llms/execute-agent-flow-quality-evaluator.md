# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-flow-quality-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute agent-flow-quality evaluator

> Validate agent trajectory against user-defined conditions

**Request Body:**
- `input.trajectory_prompts` (string, required): JSON array of prompts in the agent trajectory
- `input.trajectory_completions` (string, required): JSON array of completions in the agent trajectory
- `config.conditions` (array of strings, required): Array of evaluation conditions/rules to validate against
- `config.threshold` (number, required): Score threshold for pass/fail determination (0.0-1.0)



## OpenAPI

````yaml post /v2/evaluators/execute/agent-flow-quality
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/agent-flow-quality:
    post:
      tags:
        - evaluators
      summary: Execute agent-flow-quality evaluator
      description: >-
        Validate agent trajectory against user-defined conditions


        **Request Body:**

        - `input.trajectory_prompts` (string, required): JSON array of prompts
        in the agent trajectory

        - `input.trajectory_completions` (string, required): JSON array of
        completions in the agent trajectory

        - `config.conditions` (array of strings, required): Array of evaluation
        conditions/rules to validate against

        - `config.threshold` (number, required): Score threshold for pass/fail
        determination (0.0-1.0)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.AgentFlowQualityRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AgentFlowQualityResponse'
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
    request.AgentFlowQualityRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.AgentFlowQualityConfigRequest'
        input:
          $ref: '#/components/schemas/request.AgentFlowQualityInput'
      required:
        - config
        - input
      type: object
    response.AgentFlowQualityResponse:
      properties:
        reason:
          example: Agent followed the expected flow correctly
          type: string
        result:
          example: pass
          type: string
        score:
          example: 0.89
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.AgentFlowQualityConfigRequest:
      properties:
        conditions:
          example:
            - no tools called
            - agent completed task
          items:
            type: string
          type: array
        threshold:
          example: 0.5
          type: number
      required:
        - conditions
        - threshold
      type: object
    request.AgentFlowQualityInput:
      properties:
        trajectory_completions:
          example: '["Found 5 flights", "Selected $299 flight", "Booking confirmed"]'
          type: string
        trajectory_prompts:
          example: >-
            ["Search for flights", "Select the cheapest option", "Confirm
            booking"]
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