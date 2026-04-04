# Source: https://upstash.com/docs/qstash/api-refence/dlq/list-dlq-messages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List DLQ messages

> List and paginate through all messages currently in the DLQ



## OpenAPI

````yaml qstash/openapi.yaml get /v2/dlq
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
  /v2/dlq:
    get:
      tags:
        - DLQ
      summary: List DLQ messages
      description: List and paginate through all messages currently in the DLQ
      parameters:
        - name: cursor
          in: query
          schema:
            type: string
          description: >-
            By providing a cursor you can paginate through all of the messages
            in the DLQ
        - name: messageId
          in: query
          schema:
            type: string
          description: Filter DLQ messages by message ID
        - name: url
          in: query
          schema:
            type: string
          description: Filter DLQ messages by destination URL
        - name: topicName
          in: query
          schema:
            type: string
          description: Filter DLQ messages by URL Group name
        - name: scheduleId
          in: query
          schema:
            type: string
          description: Filter DLQ messages by schedule ID
        - name: queueName
          in: query
          schema:
            type: string
          description: Filter DLQ messages by queue name
        - name: fromDate
          in: query
          schema:
            type: integer
            format: int64
          description: >-
            Filter DLQ messages by starting date, in milliseconds (Unix
            timestamp). This is inclusive.
        - name: toDate
          in: query
          schema:
            type: integer
            format: int64
          description: >-
            Filter DLQ messages by ending date, in milliseconds (Unix
            timestamp). This is inclusive.
        - name: responseStatus
          in: query
          schema:
            type: integer
          description: >-
            Filter DLQ messages by HTTP response status code of the last
            delivery attempt
        - name: callerIp
          in: query
          schema:
            type: string
          description: Filter DLQ messages by IP address of the publisher
        - name: label
          in: query
          schema:
            type: string
          description: Filter DLQ messages by the label of the message assigned by the user
        - name: count
          in: query
          schema:
            type: integer
            default: 100
            maximum: 100
          description: The number of messages to return.
        - name: order
          in: query
          schema:
            type: string
            enum:
              - latestFirst
              - earliestFirst
            default: latestFirst
          description: The sorting order of DLQ messages by timestamp.
      responses:
        '200':
          description: List of DLQ messages
          content:
            application/json:
              schema:
                type: object
                properties:
                  cursor:
                    type: string
                    description: >
                      A cursor which you can use in subsequent requests to
                      paginate through all messages. 

                      If no cursor is returned, you have reached the end of the
                      messages.
                  messages:
                    type: array
                    items:
                      $ref: '#/components/schemas/DLQMessage'
components:
  schemas:
    DLQMessage:
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
        responseStatus:
          type: integer
          description: The HTTP status code received from the destination API.
        responseHeader:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
          description: The HTTP response headers received from the destination API.
        responseBody:
          type: string
          description: >-
            The body of the response if it is composed of utf8 chars only, empty
            otherwise.
        responseBodyBase64:
          type: string
          description: >-
            The base64 encoded body of the response if the body contains a
            non-utf8 char only, empty otherwise.
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