# Source: https://www.courier.com/docs/api-reference/sent-messages/get-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get message

> Fetch the status of a message you've previously sent.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /messages/{message_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /messages/{message_id}:
    get:
      tags:
        - Sent Messages
      summary: Get message
      description: Fetch the status of a message you've previously sent.
      operationId: messages_get
      parameters:
        - name: message_id
          in: path
          description: >-
            A unique identifier associated with the message you wish to retrieve
            (results from a send).
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MessageDetailsExtended'
        '400':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequest'
        '404':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MessageNotFound'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const message = await client.messages.retrieve('message_id');

            console.log(message);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            message = client.messages.retrieve(
                "message_id",
            )
            print(message)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tmessage, err := client.Messages.Get(context.TODO(), \"message_id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", message)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.messages.MessageRetrieveParams;
            import com.courier.models.messages.MessageRetrieveResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    MessageRetrieveResponse message = client.messages().retrieve("message_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            message = courier.messages.retrieve("message_id")

            puts(message)
components:
  schemas:
    MessageDetailsExtended:
      title: MessageDetailsExtended
      type: object
      properties:
        providers:
          type: array
          items:
            type: object
            additionalProperties: true
          nullable: true
      allOf:
        - $ref: '#/components/schemas/MessageDetails'
    BadRequest:
      title: BadRequest
      type: object
      properties:
        type:
          type: string
          enum:
            - invalid_request_error
      required:
        - type
      allOf:
        - $ref: '#/components/schemas/BaseError'
    MessageNotFound:
      title: MessageNotFound
      type: object
      properties:
        type:
          type: string
          enum:
            - invalid_request_error
      required:
        - type
      allOf:
        - $ref: '#/components/schemas/BaseError'
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
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
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