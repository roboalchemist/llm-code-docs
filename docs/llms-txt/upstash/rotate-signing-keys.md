# Source: https://upstash.com/docs/qstash/api-refence/signing-keys/rotate-signing-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rotate Signing Keys

> Rotate your signing keys

Rotating signing keys lets you switch the keys used to sign messages without causing downtime.
This ensures that signatures remain valid and that the application can continue verifying new messages seamlessly.

During a rotation, the next key becomes the new current key, and a fresh next key is generated.

Make sure to update your application to use the new current and next keys after rotation.


## OpenAPI

````yaml qstash/openapi.yaml post /v2/keys/rotate
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
  /v2/keys/rotate:
    post:
      tags:
        - Signing Keys
      summary: Rotate Signing Keys
      description: Rotate your signing keys
      responses:
        '200':
          description: Keys rotated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SigningKeys'
components:
  schemas:
    SigningKeys:
      type: object
      properties:
        current:
          type: string
          description: The current signing key.
        next:
          type: string
          description: The next signing key.
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