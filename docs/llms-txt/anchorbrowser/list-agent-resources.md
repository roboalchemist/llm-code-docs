# Source: https://docs.anchorbrowser.io/api-reference/agentic-capabilities/list-agent-resources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Agent Resources

> List all resources that have been uploaded to the browser session for agent use.
Returns resource metadata including name, size, type, and last modified timestamp.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{sessionId}/agent/files
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
  /v1/sessions/{sessionId}/agent/files:
    get:
      tags:
        - Agentic capabilities
      summary: List Agent Resources
      description: >
        List all resources that have been uploaded to the browser session for
        agent use.

        Returns resource metadata including name, size, type, and last modified
        timestamp.
      parameters:
        - name: sessionId
          in: path
          required: true
          description: The browser session ID
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Agent resources listed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      files:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                              description: The resource name
                            size:
                              type: integer
                              description: Resource size in bytes
                            type:
                              type: string
                              description: Resource extension/type
                            lastModified:
                              type: string
                              format: date-time
                              description: When the resource was last modified
        '400':
          description: Session is not running
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Session not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to list agent resources
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
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