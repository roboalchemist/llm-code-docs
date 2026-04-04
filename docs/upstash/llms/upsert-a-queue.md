# Source: https://upstash.com/docs/qstash/api-refence/queues/upsert-a-queue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upsert a Queue

> Updates or creates a queue

<Warning>
  For rate-limiting use cases, we've introduced a more performant and less restrictive Flow Control feature for the Publish API. 
  
  We are planning to deprecate setting parallelism greater than 1 for the Queue API in future. If you're currently using Queue API with parallelism greater than 1 for rate limiting, consider using Flow Control. 
  
  Queues with parallelism set to 1 provide FIFO guarantees, which remains a valid use case for the Queue API.
</Warning>


## OpenAPI

````yaml qstash/openapi.yaml post /v2/queues
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
    post:
      tags:
        - Queues
      summary: Upsert a Queue
      description: Updates or creates a queue
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - queueName
                - parallelism
              properties:
                queueName:
                  type: string
                  description: The name of the queue
                parallelism:
                  type: integer
                  default: 1
                  description: |
                    The number of parallel consumers consuming from the queue
      responses:
        '200':
          description: Queue created or updated successfully
        '400':
          description: >-
            Queue name is invalid. Queue names can only contain alphanumeric
            characters, hyphens, periods, and underscores.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '412':
          description: >-
            Either exceeded the maximum number of queues allowed or the maximum
            parallelism per queue.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
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