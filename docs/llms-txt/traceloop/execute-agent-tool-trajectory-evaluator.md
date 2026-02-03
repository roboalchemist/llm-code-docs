# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-tool-trajectory-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute agent-tool-trajectory evaluator

> Compare actual tool calls against expected reference tool calls

**Request Body:**
- `input.executed_tool_calls` (string, required): JSON array of actual tool calls made by the agent
- `input.expected_tool_calls` (string, required): JSON array of expected/reference tool calls
- `config.threshold` (float, optional): Score threshold for pass/fail determination (default: 0.5)
- `config.mismatch_sensitive` (bool, optional): Whether tool calls must match exactly (default: false)
- `config.order_sensitive` (bool, optional): Whether order of tool calls matters (default: false)
- `config.input_params_sensitive` (bool, optional): Whether to compare input parameters (default: true)



## OpenAPI

````yaml post /v2/evaluators/execute/agent-tool-trajectory
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/agent-tool-trajectory:
    post:
      tags:
        - evaluators
      summary: Execute agent-tool-trajectory evaluator
      description: >-
        Compare actual tool calls against expected reference tool calls


        **Request Body:**

        - `input.executed_tool_calls` (string, required): JSON array of actual
        tool calls made by the agent

        - `input.expected_tool_calls` (string, required): JSON array of
        expected/reference tool calls

        - `config.threshold` (float, optional): Score threshold for pass/fail
        determination (default: 0.5)

        - `config.mismatch_sensitive` (bool, optional): Whether tool calls must
        match exactly (default: false)

        - `config.order_sensitive` (bool, optional): Whether order of tool calls
        matters (default: false)

        - `config.input_params_sensitive` (bool, optional): Whether to compare
        input parameters (default: true)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.AgentToolTrajectoryRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AgentToolTrajectoryResponse'
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
    request.AgentToolTrajectoryRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.AgentToolTrajectoryConfigRequest'
        input:
          $ref: '#/components/schemas/request.AgentToolTrajectoryInput'
      required:
        - input
      type: object
    response.AgentToolTrajectoryResponse:
      properties:
        reason:
          example: Tool calls match the expected trajectory
          type: string
        result:
          example: pass
          type: string
        score:
          example: 0.85
          type: number
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.AgentToolTrajectoryConfigRequest:
      properties:
        input_params_sensitive:
          example: true
          type: boolean
        mismatch_sensitive:
          example: false
          type: boolean
        order_sensitive:
          example: false
          type: boolean
        threshold:
          example: 0.5
          type: number
      type: object
    request.AgentToolTrajectoryInput:
      properties:
        executed_tool_calls:
          example: '[{"name": "search", "input": {"query": "weather"}}]'
          type: string
        expected_tool_calls:
          example: '[{"name": "search", "input": {"query": "weather"}}]'
          type: string
      required:
        - executed_tool_calls
        - expected_tool_calls
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````