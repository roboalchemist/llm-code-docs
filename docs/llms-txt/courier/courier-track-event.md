# Source: https://www.courier.com/docs/api-reference/inbound/courier-track-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Track Event



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /inbound/courier
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /inbound/courier:
    post:
      tags:
        - Inbound
      summary: Courier Track Event
      operationId: inbound_track
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/InboundTrackEvent'
            examples:
              Example1:
                value:
                  event: New Order Placed
                  messageId: 4c62c457-b329-4bea-9bfc-17bba86c393f
                  userId: '1234'
                  type: track
                  properties:
                    order_id: 123
                    total_orders: 5
                    last_order_id: 122
      responses:
        '202':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TrackAcceptedResponse'
              examples:
                Example1:
                  value:
                    messageId: 1-6952feeb-7fed6092da5363f2af38eb42
        '400':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequest'
        '409':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Conflict'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const response = await client.inbound.trackEvent({
              event: 'New Order Placed',
              messageId: '4c62c457-b329-4bea-9bfc-17bba86c393f',
              properties: {
                order_id: 123,
                total_orders: 5,
                last_order_id: 122,
              },
              type: 'track',
              userId: '1234',
            });

            console.log(response.messageId);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.inbound.track_event(
                event="New Order Placed",
                message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
                properties={
                    "order_id": 123,
                    "total_orders": 5,
                    "last_order_id": 122,
                },
                type="track",
                user_id="1234",
            )
            print(response.message_id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Inbound.TrackEvent(context.TODO(), courier.InboundTrackEventParams{\n\t\tEvent:     \"New Order Placed\",\n\t\tMessageID: \"4c62c457-b329-4bea-9bfc-17bba86c393f\",\n\t\tProperties: map[string]any{\n\t\t\t\"order_id\":      123,\n\t\t\t\"total_orders\":  5,\n\t\t\t\"last_order_id\": 122,\n\t\t},\n\t\tType:   courier.InboundTrackEventParamsTypeTrack,\n\t\tUserID: courier.String(\"1234\"),\n\t})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.MessageID)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.core.JsonValue;
            import com.courier.models.inbound.InboundTrackEventParams;
            import com.courier.models.inbound.InboundTrackEventResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    InboundTrackEventParams params = InboundTrackEventParams.builder()
                        .event("New Order Placed")
                        .messageId("4c62c457-b329-4bea-9bfc-17bba86c393f")
                        .properties(InboundTrackEventParams.Properties.builder()
                            .putAdditionalProperty("order_id", JsonValue.from("bar"))
                            .putAdditionalProperty("total_orders", JsonValue.from("bar"))
                            .putAdditionalProperty("last_order_id", JsonValue.from("bar"))
                            .build())
                        .type(InboundTrackEventParams.Type.TRACK)
                        .build();
                    InboundTrackEventResponse response = client.inbound().trackEvent(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.inbound.track_event(
              event: "New Order Placed",
              message_id: "4c62c457-b329-4bea-9bfc-17bba86c393f",
              properties: {order_id: "bar", total_orders: "bar", last_order_id: "bar"},
              type: :track
            )

            puts(response)
components:
  schemas:
    InboundTrackEvent:
      title: InboundTrackEvent
      type: object
      properties:
        event:
          type: string
          description: >-
            A descriptive name of the event. This name will appear as a trigger
            in the Courier Automation Trigger node.
          example: New Order Placed
        messageId:
          type: string
          description: >-
            A required unique identifier that will be used to de-duplicate
            requests. If not unique, will respond with 409 Conflict status
          example: 4c62c457-b329-4bea-9bfc-17bba86c393f
        properties:
          type: object
          additionalProperties: true
        type:
          type: string
          enum:
            - track
        userId:
          type: string
          nullable: true
          description: The user id associated with the track
      required:
        - event
        - messageId
        - properties
        - type
    TrackAcceptedResponse:
      title: TrackAcceptedResponse
      type: object
      properties:
        messageId:
          type: string
          description: >-
            A successful call returns a `202` status code along with a
            `requestId` in the response body.
          example: 1-65f240a0-47a6a120c8374de9bcf9f22c
      required:
        - messageId
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
    Conflict:
      title: Conflict
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
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````