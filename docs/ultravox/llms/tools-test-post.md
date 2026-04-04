# Source: https://docs.ultravox.ai/api-reference/tools/tools-test-post.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Tool

> Tests a tool by executing it with the provided parameters



## OpenAPI

````yaml post /api/tools/{tool_id}/test
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/tools/{tool_id}/test:
    post:
      tags:
        - tools
      description: Test a tool by executing it with the provided parameters.
      operationId: tools_test_create
      parameters:
        - in: path
          name: tool_id
          schema:
            type: string
            format: uuid
          required: true
      responses:
        default:
          content:
            '*/*':
              schema: {}
          description: ''
      security:
        - apiKeyAuth: []
components:
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````