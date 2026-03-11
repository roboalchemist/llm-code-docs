# Source: https://www.courier.com/docs/api-reference/sent-messages/cancel-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel message

> Cancel a message that is currently in the process of being delivered. A well-formatted API call to the cancel message API will return either `200` status code for a successful cancellation or `409` status code for an unsuccessful cancellation. Both cases will include the actual message record in the response body (see details below).



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /messages/{message_id}/cancel
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /messages/{message_id}/cancel:
    post:
      tags:
        - Sent Messages
      summary: Cancel message
      description: >-
        Cancel a message that is currently in the process of being delivered. A
        well-formatted API call to the cancel message API will return either
        `200` status code for a successful cancellation or `409` status code for
        an unsuccessful cancellation. Both cases will include the actual message
        record in the response body (see details below).
      operationId: messages_cancel
      parameters:
        - name: message_id
          in: path
          description: A unique identifier representing the message ID
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MessageDetails'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const messageDetails = await client.messages.cancel('message_id');

            console.log(messageDetails.id);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            message_details = client.messages.cancel(
                "message_id",
            )
            print(message_details.id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tmessageDetails, err := client.Messages.Cancel(context.TODO(), \"message_id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", messageDetails.ID)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.messages.MessageCancelParams;
            import com.courier.models.messages.MessageDetails;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    MessageDetails messageDetails = client.messages().cancel("message_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            message_details = courier.messages.cancel("message_id")

            puts(message_details)
components:
  schemas:
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