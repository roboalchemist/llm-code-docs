# Source: https://upstash.com/docs/qstash/api-refence/queues/list-queues.md

# List Queues

> List all your queues



## OpenAPI

````yaml qstash/openapi.yaml get /v2/queues
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
  /v2/queues:
    get:
      tags:
        - Queues
      summary: List Queues
      description: List all your queues
      responses:
        '200':
          description: List of queues
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Queue'
components:
  schemas:
    Queue:
      type: object
      properties:
        name:
          type: string
          description: The name of the queue.
        createdAt:
          type: integer
          format: int64
          description: The creation timestamp of the queue in Unix milliseconds
        updatedAt:
          type: integer
          format: int64
          description: The last update timestamp of the queue in Unix milliseconds
        parallelism:
          type: integer
          description: The number of parallel consumers consuming from the queue
        paused:
          type: boolean
          description: Whether the queue is paused
        lag:
          type: integer
          description: The number of unprocessed messages that exist in the queue
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