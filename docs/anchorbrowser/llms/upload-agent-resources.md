# Source: https://docs.anchorbrowser.io/api-reference/agentic-capabilities/upload-agent-resources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload Agent Resources

> Upload files as agent resources to a browser session using multipart/form-data. 
If you upload a ZIP file, it will be automatically extracted and the files will be made available as agent resources.
If you upload a single file, it will be saved directly as an agent resource.
Resources are then accessible to AI agents for task completion and automation.




## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/agent/files
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
    post:
      tags:
        - Agentic capabilities
      summary: Upload Agent Resources
      description: >
        Upload files as agent resources to a browser session using
        multipart/form-data. 

        If you upload a ZIP file, it will be automatically extracted and the
        files will be made available as agent resources.

        If you upload a single file, it will be saved directly as an agent
        resource.

        Resources are then accessible to AI agents for task completion and
        automation.
      parameters:
        - name: sessionId
          in: path
          required: true
          description: The browser session ID
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - file
              properties:
                file:
                  type: string
                  format: binary
                  description: >-
                    File to upload as agent resource (ZIP files will be
                    extracted automatically)
      responses:
        '200':
          description: Agent resources uploaded successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      status:
                        type: string
                      message:
                        type: string
        '400':
          description: Invalid request (no resource uploaded or file too large)
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
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
          description: Failed to upload or process agent resources
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