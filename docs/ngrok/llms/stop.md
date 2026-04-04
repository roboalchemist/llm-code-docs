# Source: https://ngrok.com/docs/api-reference/tunnelsessions/stop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Stop a specific tunnel session, terminating the connection to the ngrok service.

# Stop



## OpenAPI

````yaml post /tunnel_sessions/{id}/stop
openapi: 3.0.0
info:
  title: ngrok OpenAPI
  version: 1.0.0
servers:
  - url: https://api.ngrok.com
security:
  - authentication: []
paths:
  /tunnel_sessions/{id}/stop:
    post:
      tags:
        - TunnelSessions
      summary: Stop
      description: >
        Issues a command instructing the ngrok agent that started this tunnel
        session to exit.
      operationId: TunnelSessionsStop
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
            Issues a command instructing the ngrok agent that started this
            tunnel session to exit.
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