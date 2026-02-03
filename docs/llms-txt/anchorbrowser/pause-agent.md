# Source: https://docs.anchorbrowser.io/api-reference/agentic-capabilities/pause-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Pause Agent

> Pauses the AI agent for the specified browser session.



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{session_id}/agent/pause
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/sessions/{session_id}/agent/pause:
    post:
      tags:
        - Agentic capabilities
      summary: Pause Agent
      description: Pauses the AI agent for the specified browser session.
      parameters:
        - name: session_id
          in: path
          required: true
          description: The ID of the browser session
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Agent paused successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '400':
          description: Session is not running
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Session not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to pause agent
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    SuccessResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            status:
              type: string
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````