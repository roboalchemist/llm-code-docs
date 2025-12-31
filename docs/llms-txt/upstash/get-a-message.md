# Source: https://upstash.com/docs/qstash/api-refence/messages/get-a-message.md

# Get a Message

> Retrieve details of a specific message

<Warning>Messages are removed from the database shortly after they’re delivered, so you will not be able to retrieve a message after. This endpoint is intended to be used for accessing messages that are in the process of being delivered/retried.</Warning>


## OpenAPI

````yaml qstash/openapi.yaml get /v2/messages/{messageId}
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
  /v2/messages/{messageId}:
    get:
      tags:
        - Messages
      summary: Get a Message
      description: Retrieve details of a specific message
      parameters:
        - name: messageId
          in: path
          required: true
          schema:
            type: string
          description: The identifier of the message to retrieve.
      responses:
        '200':
          description: Message details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Message'
        '404':
          description: Message not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Message:
      type: object
      properties:
        messageId:
          type: string
          description: Unique identifier for the message
        url:
          type: string
          description: The URL to which the message should be delivered.
        topicName:
          type: string
          description: >-
            The URL Group (a.k.a. topic) name if this message was sent to a URL
            Group.
        endpointName:
          type: string
          description: >-
            The endpoint name of the message if the endpoint is given a name
            within the URL group.
        method:
          type: string
          description: The HTTP method to use for the message.
        header:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
          description: The HTTP headers sent to your API.
        body:
          type: string
          description: >-
            The body of the message if it is composed of utf8 chars only, empty
            otherwise.
        bodyBase64:
          type: string
          description: >-
            The base64 encoded body if the body contains a non-utf8 char only,
            empty otherwise.
        maxRetries:
          type: integer
          description: >-
            The number of retries that should be attempted in case of delivery
            failure.
        notBefore:
          type: integer
          format: int64
          description: >-
            The unix timestamp in milliseconds before which the message should
            not be delivered.
        createdAt:
          type: integer
          format: int64
          description: The unix timestamp in milliseconds when the message was created.
        callback:
          type: string
          description: >-
            The url where we send a callback each time the message is attempted
            to be delivered.
        failureCallback:
          type: string
          description: The url where we send a callback to after the message is failed
        queueName:
          type: string
          description: The name of the queue if the message is enqueued to a queue.
        scheduleId:
          type: string
          description: >-
            The scheduleId of the message if the message is triggered by a
            schedule
        callerIP:
          type: string
          description: IP address of the publisher of this message.
        label:
          type: string
          description: The label of the message assigned by the user.
        flowControlKey:
          type: string
          description: The flow control key used for rate limiting.
        rate:
          type: integer
          description: The rate value used for flow control.
        period:
          type: integer
          description: The period value used for flow control.
        parallelism:
          type: integer
          description: The parallelism value used for flow control.
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://upstash.com/docs/llms.txt