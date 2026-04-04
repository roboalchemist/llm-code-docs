# Source: https://upstash.com/docs/qstash/api-refence/url-groups/list-url-groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List URL Groups

> List all your URL Groups



## OpenAPI

````yaml qstash/openapi.yaml get /v2/topics
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
  /v2/topics:
    get:
      tags:
        - URL Groups
      summary: List URL Groups
      description: List all your URL Groups
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/URLGroup'
components:
  schemas:
    URLGroup:
      type: object
      properties:
        name:
          type: string
          description: URL Group name
        createdAt:
          type: integer
          description: Creation timestamp of URL Group in Unix milliseconds
        updatedAt:
          type: integer
          description: Last update timestamp of URL Group in Unix milliseconds
        endpoints:
          type: array
          items:
            $ref: '#/components/schemas/Endpoint'
    Endpoint:
      type: object
      properties:
        name:
          type: string
          description: The name of the endpoint
        url:
          type: string
          description: The URL of the endpoint
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