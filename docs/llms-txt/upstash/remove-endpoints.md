# Source: https://upstash.com/docs/qstash/api-refence/url-groups/remove-endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove Endpoints

> Remove one or more endpoints from a URL Group

Remove one or multiple endpoints from a URL Group. If all endpoints have been removed, the URL Group will be deleted.


## OpenAPI

````yaml qstash/openapi.yaml delete /v2/topics/{urlGroupName}/endpoints
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
    delete:
      tags:
        - URL Groups
      summary: Remove Endpoints
      description: Remove one or more endpoints from a URL Group
      parameters:
        - name: urlGroupName
          in: path
          required: true
          schema:
            type: string
          description: The name of your URL Group.
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
                  description: >-
                    Then list of endpoints to remove from URL Group. Either name
                    or url must be provided.
                  type: array
                  items:
                    $ref: '#/components/schemas/Endpoint'
      responses:
        '200':
          description: Endpoint(s) removed successfully
components:
  schemas:
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