# Source: https://upstash.com/docs/qstash/api-refence/dlq/delete-a-dlq-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a DLQ message

> Manually remove a message from the DLQ



## OpenAPI

````yaml qstash/openapi.yaml delete /v2/dlq/{dlqId}
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
  /v2/dlq/{dlqId}:
    delete:
      tags:
        - DLQ
      summary: Delete a DLQ message
      description: Manually remove a message from the DLQ
      parameters:
        - name: dlqId
          in: path
          required: true
          schema:
            type: string
          description: |
            The DLQ ID of the message you want to remove.
      responses:
        '200':
          description: Message deleted successfully
        '404':
          description: >
            If the message is not found in the DLQ, (either is has been removed
            by you, or automatically), the endpoint returns a 404 status code.
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