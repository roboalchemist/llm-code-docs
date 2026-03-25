# Source: https://www.courier.com/docs/api-reference/sent-messages/list-messages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List messages

> Fetch the statuses of messages you've previously sent.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /messages
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /messages:
    get:
      tags:
        - Sent Messages
      summary: List messages
      description: Fetch the statuses of messages you've previously sent.
      operationId: messages_list
      parameters:
        - name: archived
          in: query
          description: >-
            A boolean value that indicates whether archived messages should be
            included in the response.
          required: false
          schema:
            type: boolean
            nullable: true
        - name: cursor
          in: query
          description: >-
            A unique identifier that allows for fetching the next set of
            messages.
          required: false
          schema:
            type: string
            nullable: true
        - name: event
          in: query
          description: >-
            A unique identifier representing the event that was used to send the
            event.
          required: false
          schema:
            type: string
            nullable: true
        - name: list
          in: query
          description: A unique identifier representing the list the message was sent to.
          required: false
          schema:
            type: string
            nullable: true
        - name: messageId
          in: query
          description: >-
            A unique identifier representing the message_id returned from either
            /send or /send/list.
          required: false
          schema:
            type: string
            nullable: true
        - name: notification
          in: query
          description: >-
            A unique identifier representing the notification that was used to
            send the event.
          required: false
          schema:
            type: string
            nullable: true
        - name: provider
          in: query
          description: >-
            The key assocated to the provider you want to filter on. E.g.,
            sendgrid, inbox, twilio, slack, msteams, etc. Allows multiple values
            to be set in query parameters.
          required: false
          schema:
            type: array
            items:
              type: string
              nullable: true
        - name: recipient
          in: query
          description: >-
            A unique identifier representing the recipient associated with the
            requested profile.
          required: false
          schema:
            type: string
            nullable: true
        - name: status
          in: query
          description: >-
            An indicator of the current status of the message. Allows multiple
            values to be set in query parameters.
          required: false
          schema:
            type: array
            items:
              type: string
              nullable: true
        - name: tag
          in: query
          description: >-
            A tag placed in the metadata.tags during a notification send. Allows
            multiple values to be set in query parameters.
          required: false
          schema:
            type: array
            items:
              type: string
              nullable: true
        - name: tags
          in: query
          description: >-
            A comma delimited list of 'tags'. Messages will be returned if they
            match any of the tags passed in.
          required: false
          schema:
            type: string
            nullable: true
        - name: tenant_id
          in: query
          description: Messages sent with the context of a Tenant
          required: false
          schema:
            type: string
            nullable: true
        - name: enqueued_after
          in: query
          description: >-
            The enqueued datetime of a message to filter out messages received
            before.
          required: false
          schema:
            type: string
            nullable: true
        - name: traceId
          in: query
          description: The unique identifier used to trace the requests
          required: false
          schema:
            type: string
            nullable: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListMessagesResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const messages = await client.messages.list();

            console.log(messages.paging);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            messages = client.messages.list()
            print(messages.paging)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tmessages, err := client.Messages.List(context.TODO(), courier.MessageListParams{})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", messages.Paging)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.messages.MessageListParams;
            import com.courier.models.messages.MessageListResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    MessageListResponse messages = client.messages().list();
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            messages = courier.messages.list

            puts(messages)
components:
  schemas:
    ListMessagesResponse:
      title: ListMessagesResponse
      type: object
      properties:
        paging:
          $ref: '#/components/schemas/Paging'
          description: Paging information for the result set.
        results:
          type: array
          items:
            $ref: '#/components/schemas/MessageDetails'
          description: An array of messages with their details.
      required:
        - paging
        - results
    Paging:
      title: Paging
      type: object
      properties:
        cursor:
          type: string
          nullable: true
        more:
          type: boolean
      required:
        - more
    MessageDetails:
      title: MessageDetails
      type: object
      properties:
        id:
          type: string
          description: >-
            A unique identifier associated with the message you wish to retrieve
            (results from a send).
        status:
          $ref: '#/components/schemas/MessageStatus'
          description: The current status of the message.
        enqueued:
          type: integer
          format: int64
          description: >-
            A UTC timestamp at which Courier received the message request.
            Stored as a millisecond representation of the Unix epoch.
        sent:
          type: integer
          format: int64
          description: >-
            A UTC timestamp at which Courier passed the message to the
            Integration provider. Stored as a millisecond representation of the
            Unix epoch.
        delivered:
          type: integer
          format: int64
          description: >-
            A UTC timestamp at which the Integration provider delivered the
            message. Stored as a millisecond representation of the Unix epoch.
        opened:
          type: integer
          format: int64
          description: >-
            A UTC timestamp at which the recipient opened a message for the
            first time. Stored as a millisecond representation of the Unix
            epoch.
        clicked:
          type: integer
          format: int64
          description: >-
            A UTC timestamp at which the recipient clicked on a tracked link for
            the first time. Stored as a millisecond representation of the Unix
            epoch.
        recipient:
          type: string
          description: >-
            A unique identifier associated with the recipient of the delivered
            message.
        event:
          type: string
          description: >-
            A unique identifier associated with the event of the delivered
            message.
        notification:
          type: string
          description: >-
            A unique identifier associated with the notification of the
            delivered message.
        error:
          type: string
          nullable: true
          description: A message describing the error that occurred.
        reason:
          $ref: '#/components/schemas/Reason'
          nullable: true
          description: The reason for the current status of the message.
      required:
        - id
        - status
        - enqueued
        - sent
        - delivered
        - opened
        - clicked
        - recipient
        - event
        - notification
    MessageStatus:
      title: MessageStatus
      type: string
      enum:
        - CANCELED
        - CLICKED
        - DELAYED
        - DELIVERED
        - DIGESTED
        - ENQUEUED
        - FILTERED
        - OPENED
        - ROUTED
        - SENT
        - SIMULATED
        - THROTTLED
        - UNDELIVERABLE
        - UNMAPPED
        - UNROUTABLE
    Reason:
      title: Reason
      type: string
      enum:
        - BOUNCED
        - FAILED
        - FILTERED
        - NO_CHANNELS
        - NO_PROVIDERS
        - OPT_IN_REQUIRED
        - PROVIDER_ERROR
        - UNPUBLISHED
        - UNSUBSCRIBED
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````