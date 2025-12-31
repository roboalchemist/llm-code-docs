# Source: https://upstash.com/docs/qstash/api-refence/flow-control/get-flow-control-key.md

# Get Flow Control Key

> Get details of a specific Flow Control key



## OpenAPI

````yaml qstash/openapi.yaml get /v2/flowControl/{flowControlKey}
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
  /v2/flowControl/{flowControlKey}:
    get:
      tags:
        - Flow Control
      summary: Get Flow Control Key
      description: Get details of a specific Flow Control key
      parameters:
        - name: flowControlKey
          in: path
          required: true
          schema:
            type: string
          description: The Flow Control key to retrieve
      responses:
        '200':
          description: Flow control key details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FlowControlKey'
        '404':
          description: Flow Control key not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
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
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
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