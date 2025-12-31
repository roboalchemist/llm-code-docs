# Source: https://upstash.com/docs/qstash/api-refence/schedules/delete-a-schedule.md

# Delete a Schedule

> Delete a schedule



## OpenAPI

````yaml qstash/openapi.yaml delete /v2/schedules/{scheduleId}
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
  /v2/schedules/{scheduleId}:
    delete:
      tags:
        - Schedules
      summary: Delete a Schedule
      description: Delete a schedule
      parameters:
        - name: scheduleId
          in: path
          required: true
          schema:
            type: string
          description: The ID of the schedule to delete.
      responses:
        '200':
          description: Schedule deleted successfully
components:
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