# Source: https://upstash.com/docs/qstash/api-refence/schedules/list-schedules.md

# List schedules

> List all schedules



## OpenAPI

````yaml qstash/openapi.yaml get /v2/schedules
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
  /v2/schedules:
    get:
      tags:
        - Schedules
      summary: List schedules
      description: List all schedules
      responses:
        '200':
          description: List of schedules
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Schedule'
components:
  schemas:
    Schedule:
      type: object
      required:
        - scheduleId
        - cron
        - destination
        - createdAt
        - method
        - isPaused
      properties:
        scheduleId:
          type: string
          description: Unique identifier for the schedule
        cron:
          type: string
          description: The cron expression used to schedule the message
        destination:
          type: string
          description: The destination URL or URL Group name
        createdAt:
          type: integer
          format: int64
          description: The creation timestamp of the schedule in unix milliseconds
        method:
          type: string
          description: The HTTP method used for the scheduled message
        header:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
          description: Map of header names to arrays of header values
        body:
          type: string
          description: The body of the scheduled message
        retries:
          type: integer
          description: The number of retries for the scheduled message
        delay:
          type: integer
          description: The delay in seconds before the scheduled message is sent
        callback:
          type: string
          description: The callback URL for the scheduled message
        failureCallback:
          type: string
          description: The failure callback URL for the scheduled message
        callerIp:
          type: string
          description: The IP address of the client that created the schedule
        isPaused:
          type: boolean
          description: Whether the schedule is paused
        flowControlKey:
          type: string
          description: The flow control key used for rate limiting
        parallelism:
          type: integer
          description: The parallelism value used for flow control
        rate:
          type: integer
          description: The rate value used for flow control
        period:
          type: integer
          description: The period value used for flow control
        retryDelayExpression:
          type: string
          description: The retry delay expression used for calculating retry delays
        label:
          type: string
          description: The label assigned to the scheduled message
        lastScheduleTime:
          type: integer
          format: int64
          description: The last time the schedule was triggered in unix milliseconds
        nextScheduleTime:
          type: integer
          format: int64
          description: The next scheduled trigger time in unix milliseconds
        lastScheduleStates:
          type: object
          description: The states of the last scheduled messages
          additionalProperties:
            type: string
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