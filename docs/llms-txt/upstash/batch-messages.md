# Source: https://upstash.com/docs/qstash/api-refence/messages/batch-messages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch Messages

> Send multiple messages in a single request



## OpenAPI

````yaml qstash/openapi.yaml post /v2/batch
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
  /v2/batch:
    post:
      tags:
        - Messages
      summary: Batch Messages
      description: Send multiple messages in a single request
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                required:
                  - destination
                properties:
                  destination:
                    type: string
                    description: >
                      Destination can either be a valid URL where the message
                      gets sent to, or a URL Group name. 

                      - If the destination is a URL, make sure the URL is
                      prefixed with a valid protocol (http:// or https://)

                      - If the destination is a URL Group, a new message will be
                      created for each endpoint in the group.


                      Note that destination must be publicly accessible over the
                      internet. If you are working with local endpoints,
                      consider using QStash local development server or a public
                      tunnel service.
                  body:
                    type: string
                    description: The raw request message passed to the endpoints as is
                  headers:
                    type: object
                    additionalProperties:
                      type: string
                    description: >-
                      HTTP headers of the message. You can pass all the headers
                      supported in the single publish API.
                  queue:
                    type: string
                    description: Queue name to enqueue the message to if desired.
      responses:
        '200':
          description: Messages published successfully
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/PublishResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    PublishResponse:
      type: object
      properties:
        messageId:
          type: string
          description: >-
            Unique identifier for the published message or the old message ID if
            deduplicated
        deduplicated:
          type: boolean
          description: >-
            Whether this message is a duplicate and was not sent to the
            destination.
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