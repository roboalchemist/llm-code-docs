# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-tool-error-detector-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute agent-tool-error-detector evaluator

> Detect errors or failures during tool execution

**Request Body:**
- `input.tool_input` (string, required): JSON string of the tool input
- `input.tool_output` (string, required): JSON string of the tool output



## OpenAPI

````yaml post /v2/evaluators/execute/agent-tool-error-detector
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/agent-tool-error-detector:
    post:
      tags:
        - evaluators
      summary: Execute agent-tool-error-detector evaluator
      description: |-
        Detect errors or failures during tool execution

        **Request Body:**
        - `input.tool_input` (string, required): JSON string of the tool input
        - `input.tool_output` (string, required): JSON string of the tool output
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.AgentToolErrorDetectorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AgentToolErrorDetectorResponse'
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
    request.AgentToolErrorDetectorRequest:
      properties:
        input:
          $ref: '#/components/schemas/request.AgentToolErrorDetectorInput'
      required:
        - input
      type: object
    response.AgentToolErrorDetectorResponse:
      properties:
        reason:
          example: Tool executed successfully without errors
          type: string
        result:
          example: success
          type: string
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.AgentToolErrorDetectorInput:
      properties:
        tool_input:
          example: '{"action": "search", "query": "flights to Paris"}'
          type: string
        tool_output:
          example: >-
            {"status": "success", "results": [{"flight": "AF123", "price":
            450}]}
          type: string
      required:
        - tool_input
        - tool_output
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````