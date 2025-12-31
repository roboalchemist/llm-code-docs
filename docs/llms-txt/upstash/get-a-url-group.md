# Source: https://upstash.com/docs/qstash/api-refence/url-groups/get-a-url-group.md

# Get a URL Group

> Retrieve details of a specific URL Group



## OpenAPI

````yaml qstash/openapi.yaml get /v2/topics/{urlGroupName}
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
    get:
      tags:
        - URL Groups
      summary: Get a URL Group
      description: Retrieve details of a specific URL Group
      parameters:
        - name: urlGroupName
          in: path
          required: true
          schema:
            type: string
          description: The name of the URL Group to retrieve.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/URLGroup'
        '404':
          description: URL Group not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
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
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://upstash.com/docs/llms.txt