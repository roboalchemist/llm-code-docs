# Source: https://docs.pipecat.ai/deployment/pipecat-cloud/rest-reference/endpoint/stop.md

# Stop an Agent session

> Stop a running agent session and clean up its resources.



## OpenAPI

````yaml DELETE /agents/{agentName}/sessions/{sessionId}
openapi: 3.0.0
info:
  title: Pipecat Cloud - Stop Agent Session
  version: 1.0.0
  description: Stop an agent session via Pipecat Cloud Private API
servers:
  - url: https://api.pipecat.daily.co/v1
    description: API server
security:
  - PrivateKeyAuth: []
paths:
  /agents/{agentName}/sessions/{sessionId}:
    delete:
      summary: Stop an agent session
      description: Stops an active session of a deployed agent and cleans up its resources.
      operationId: stopSession
      parameters:
        - name: agentName
          in: path
          required: true
          description: Name of the agent
          schema:
            type: string
        - name: sessionId
          in: path
          required: true
          description: UUID of the session to stop
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Session stopped successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StopResponse'
        '400':
          description: Invalid request (e.g., invalid session ID format)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Service or session not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - PrivateKeyAuth: []
components:
  schemas:
    StopResponse:
      type: object
      properties:
        status:
          type: string
          description: Status of the stop operation
          example: terminated
        session_id:
          type: string
          format: uuid
          description: Session ID of the stopped session
          example: 639f91d8-d511-4677-a83b-bd7564d5d92f
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Error message
        code:
          type: string
          description: Error code
  securitySchemes:
    PrivateKeyAuth:
      type: http
      scheme: bearer
      description: >-
        Authentication requires a Pipecat Cloud Private API token.


        Generate a Private API key from your Dashboard (Settings > API Keys >
        Private > Create key) and include it as a Bearer token in the
        Authorization header.

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.pipecat.ai/llms.txt