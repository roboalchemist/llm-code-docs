# Source: https://ngrok.com/docs/api-reference/tunnelsessions/restart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Restart a specific tunnel session, re-establishing the connection to the ngrok service.

# Restart



## OpenAPI

````yaml post /tunnel_sessions/{id}/restart
openapi: 3.0.0
info:
  title: ngrok OpenAPI
  version: 1.0.0
servers:
  - url: https://api.ngrok.com
security:
  - authentication: []
paths:
  /tunnel_sessions/{id}/restart:
    post:
      tags:
        - TunnelSessions
      summary: Restart
      description: >
        Issues a command instructing the ngrok agent to restart. The agent
        restarts itself by calling exec() on platforms that support it. This
        operation is notably not supported on Windows. When an agent restarts,
        it reconnects with a new tunnel session ID.
      operationId: TunnelSessionsRestart
      parameters:
        - $ref: '#/components/parameters/ngrokVersion'
        - name: id
          description: |
            a resource identifier
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Item'
      responses:
        '204':
          description: >
            Issues a command instructing the ngrok agent to restart. The agent
            restarts itself by calling exec() on platforms that support it. This
            operation is notably not supported on Windows. When an agent
            restarts, it reconnects with a new tunnel session ID.
components:
  parameters:
    ngrokVersion:
      name: ngrok-version
      in: header
      required: true
      schema:
        type: integer
        default: 2
  schemas:
    Item:
      type: object
      properties:
        id:
          description: |
            a resource identifier
          type: string
  securitySchemes:
    authentication:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).