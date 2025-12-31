# Source: https://upstash.com/docs/qstash/api-refence/url-groups/upsert-url-group-and-endpoint.md

# Upsert URL Group and Endpoint

> Add an endpoint to a URL Group

Add one or multiple endpoints to a URL Group. If the URL Group does not exist, it will be created.


## OpenAPI

````yaml qstash/openapi.yaml post /v2/topics/{urlGroupName}/endpoints
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
  /v2/topics/{urlGroupName}/endpoints:
    post:
      tags:
        - URL Groups
      summary: Upsert URL Group and Endpoint
      description: Add an endpoint to a URL Group
      parameters:
        - name: urlGroupName
          in: path
          required: true
          schema:
            type: string
          description: >-
            The name of your URL Group. If it doesn't exist yet, it will be
            created.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - endpoints
              properties:
                endpoints:
                  type: array
                  items:
                    type: object
                    required:
                      - url
                    properties:
                      url:
                        type: string
                        description: The URL of the endpoint
                      name:
                        type: string
                        description: Optional name for the endpoint
      responses:
        '200':
          description: Endpoint(s) added successfully
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