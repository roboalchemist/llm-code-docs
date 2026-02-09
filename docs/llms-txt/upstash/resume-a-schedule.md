# Source: https://upstash.com/docs/qstash/api-refence/schedules/resume-a-schedule.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Resume a Schedule

> Resume a paused Schedule

Resuming a schedule marks the schedule as active. This means the upcoming messages will be delivered and will not be ignored. 

If the schedule is already active, this action has no effect.


## OpenAPI

````yaml qstash/openapi.yaml post /v2/schedules/{scheduleId}/resume
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
  /v2/schedules/{scheduleId}/resume:
    post:
      tags:
        - Schedules
      summary: Resume a Schedule
      description: Resume a paused Schedule
      parameters:
        - name: scheduleId
          in: path
          required: true
          schema:
            type: string
          description: The ID of the schedule to resume.
      responses:
        '200':
          description: Schedule resumed successfully
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