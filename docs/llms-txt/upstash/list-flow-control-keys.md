# Source: https://upstash.com/docs/qstash/api-refence/flow-control/list-flow-control-keys.md

# List Flow Control Keys

> List all Flow Control keys



## OpenAPI

````yaml qstash/openapi.yaml get /v2/flowControl
openapi: 3.1.0
info:
  title: QStash REST API
  description: |
    QStash is a message queue and scheduler built on top of Upstash Redis.
  version: 2.0.0
  contact:
    name: Upstash
    url: https://upstash.com
servers:
  - url: https://qstash.upstash.io
security:
  - bearerAuth: []
  - bearerAuthQuery: []
tags:
  - name: Messages
    description: Publish and manage messages
  - name: Queues
    description: Manage message queues
  - name: Schedules
    description: Create and manage scheduled messages
  - name: URL Groups
    description: Manage URL groups and endpoints
  - name: DLQ
    description: Dead Letter Queue operations
  - name: Logs
    description: Log operations
  - name: Signing Keys
    description: Manage signing keys
  - name: Flow Control
    description: Monitor flow control keys
paths:
  /v2/flowControl:
    get:
      tags:
        - Flow Control
      summary: List Flow Control Keys
      description: List all Flow Control keys
      responses:
        '200':
          description: Flow control keys retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FlowControlKey'
components:
  schemas:
    FlowControlKey:
      type: object
      properties:
        flowControlKey:
          type: string
          description: The flow control key name
        waitlistSize:
          type: integer
          description: The number of messages waiting due to flow control configuration.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: QStash authentication token
    bearerAuthQuery:
      type: apiKey
      in: query
      name: qstash_token
      description: QStash authentication token passed as a query parameter

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://upstash.com/docs/llms.txt