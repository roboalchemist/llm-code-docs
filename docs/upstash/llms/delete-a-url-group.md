# Source: https://upstash.com/docs/qstash/api-refence/url-groups/delete-a-url-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a URL Group

> Delete a topic and all its endpoints

The URL Group and all its endpoints are removed.
In flight messages in the URL Group are not removed but you will not be able to send messages to the URL Group anymore.

<Warning>
  If you have a schedule that is publishing to this URL Group, you need to delete the schedule first before deleting the URL Group.
</Warning>


## OpenAPI

````yaml qstash/openapi.yaml delete /v2/topics/{urlGroupName}
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
  /v2/topics/{urlGroupName}:
    delete:
      tags:
        - URL Groups
      summary: Delete a URL Group
      description: Delete a topic and all its endpoints
      parameters:
        - name: urlGroupName
          in: path
          required: true
          schema:
            type: string
          description: The name of the URL Group to delete.
      responses:
        '200':
          description: URL Group deleted successfully
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