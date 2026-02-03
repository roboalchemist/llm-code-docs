# Source: https://upstash.com/docs/qstash/api-refence/logs/list-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Logs

> Paginate through logs of published messages



## OpenAPI

````yaml qstash/openapi.yaml get /v2/logs
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
  /v2/logs:
    get:
      tags:
        - Logs
      summary: List Logs
      description: Paginate through logs of published messages
      parameters:
        - name: cursor
          in: query
          schema:
            type: string
          description: By providing a cursor you can paginate through all of the logs
        - name: messageId
          in: query
          schema:
            type: string
          description: Filter logs by message ID
        - name: state
          in: query
          schema:
            type: string
            enum:
              - CREATED
              - ACTIVE
              - RETRY
              - ERROR
              - IN_PROGRESS
              - DELIVERED
              - CANCEL_REQUESTED
              - CANCELLED
          description: "Filter logs by message state\n\n|Value\t|Description|\n|-------|------------|\n| CREATED\t|The message has been accepted and stored in QStash|\n| ACTIVE\t|The task is currently being processed by a worker.|\n| RETRY\t|The task has been scheduled to retry.|\n| ERROR\t|The execution threw an error and the task is waiting to be retried or failed.|\n| IN_PROGRESS\t|The task is in one of ACTIVE, RETRY or ERROR state.|\n| DELIVERED\t|The message was successfully delivered.|\n| FAILED\t|The task has errored too many times or encountered an error that it cannot recover from.|\n| CANCEL_REQUESTED\t|The cancel request from the user is recorded.|\n| CANCELLED\t|The cancel request from the user is honored.|\n"
        - name: url
          in: query
          schema:
            type: string
          description: Filter logs by destination URL
        - name: topicName
          in: query
          schema:
            type: string
          description: Filter logs by URL Group name
        - name: scheduleId
          in: query
          schema:
            type: string
          description: Filter logs by schedule ID
        - name: queueName
          in: query
          schema:
            type: string
          description: Filter logs by queue name
        - name: fromDate
          in: query
          schema:
            type: integer
            format: int64
          description: >-
            Filter logs by starting date, in milliseconds (Unix timestamp). This
            is inclusive.
        - name: toDate
          in: query
          schema:
            type: integer
            format: int64
          description: >-
            Filter logs by ending date, in milliseconds (Unix timestamp). This
            is inclusive.
        - name: count
          in: query
          schema:
            type: integer
            default: 100
            maximum: 100
          description: The number of log entries to return.
        - name: order
          in: query
          schema:
            type: string
            enum:
              - latestFirst
              - earliestFirst
            default: latestFirst
          description: The sorting order of logs by timestamp.
        - name: label
          in: query
          schema:
            type: string
          description: Filter logs by the label of the message assigned by the user
      responses:
        '200':
          description: List of logs
          content:
            application/json:
              schema:
                type: object
                properties:
                  cursor:
                    type: string
                    description: >
                      A cursor which you can use in subsequent requests to
                      paginate through all logs. 

                      If no cursor is returned, you have reached the end of the
                      logs.
                  logs:
                    type: array
                    items:
                      $ref: '#/components/schemas/LogEntry'
components:
  schemas:
    LogEntry:
      type: object
      properties:
        time:
          type: integer
          format: int64
          description: The timestamp of the log entry in Unix milliseconds
        messageId:
          type: string
          description: The message ID associated with the log entry
        header:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
          description: The headers of the message.
        body:
          type: string
          description: Base64 encoded body of the message.
        state:
          type: string
          enum:
            - CREATED
            - ACTIVE
            - RETRY
            - ERROR
            - DELIVERED
            - FAILED
            - CANCEL_REQUESTED
            - CANCELLED
          description: The state of the message at the time of the log entry.
        error:
          type: string
          description: The error message if the log entry corresponds to an error state.
        nextDeliveryTime:
          type: integer
          format: int64
          description: >-
            The next scheduled time of the message. (Unix timestamp in
            milliseconds)
        url:
          type: string
          description: The URL to which the message is being delivered.
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
        scheduleId:
          type: string
          description: >-
            The scheduleId of the message if the message is triggered by a
            schedule
        queueName:
          type: string
          description: The name of the queue if the message is enqueued to a queue.
        responseStatus:
          type: integer
          description: The status code of the response. Only set if the state is ERROR
        responseBody:
          type: string
          description: >-
            The base64 encoded body of the response. Only set if the state is
            ERROR
        responseHeaders:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
          description: The headers of the response. Only set if the state is ERROR
        timeout:
          type: integer
          description: >-
            The timeout(in milliseconds) of the outgoing http requests, after
            which Qstash cancels the request
        method:
          type: string
          description: HTTP method of the message for outgoing request
        callback:
          type: string
          description: >-
            Callback is the URL address where QStash sends the response of a
            publish
        callbackHeaders:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
          description: The headers sent to the callback URL
        failureCallback:
          type: string
          description: >-
            Failur eCallback is the URL address where QStash sends the response
            of a failed message after all retries are exhausted
        failureCallbackHeaders:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
          description: The headers sent to the failure callback URL
        maxRetries:
          type: integer
          description: The maximum number of retries for the message
        retryDelayExpression:
          type: string
          description: The retry delay expression used for calculating retry delays
        label:
          type: string
          description: The label assigned to the message
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