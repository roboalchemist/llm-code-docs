# Source: https://www.courier.com/docs/api-reference/notification-templates/get-notifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get notifications



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /notifications
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /notifications:
    get:
      tags:
        - Notification Templates
      operationId: notifications_list
      parameters:
        - name: cursor
          in: query
          required: false
          schema:
            type: string
            nullable: true
        - name: notes
          in: query
          description: Retrieve the notes from the Notification template settings.
          required: false
          schema:
            type: boolean
            nullable: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotificationListResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const notifications = await client.notifications.list();

            console.log(notifications.paging);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            notifications = client.notifications.list()
            print(notifications.paging)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tnotifications, err := client.Notifications.List(context.TODO(), courier.NotificationListParams{})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", notifications.Paging)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.notifications.NotificationListParams;
            import com.courier.models.notifications.NotificationListResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    NotificationListResponse notifications = client.notifications().list();
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            notifications = courier.notifications.list

            puts(notifications)
components:
  schemas:
    NotificationListResponse:
      title: NotificationListResponse
      type: object
      properties:
        paging:
          $ref: '#/components/schemas/Paging'
        results:
          type: array
          items:
            $ref: '#/components/schemas/Notification'
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
    Notification:
      title: Notification
      type: object
      properties:
        created_at:
          type: integer
          format: int64
        updated_at:
          type: integer
          format: int64
        id:
          type: string
        routing:
          $ref: '#/components/schemas/MessageRouting'
        tags:
          $ref: '#/components/schemas/NotificationTag'
          nullable: true
        title:
          type: string
          nullable: true
        topic_id:
          type: string
        note:
          type: string
        event_ids:
          type: array
          items:
            type: string
          description: Array of event IDs associated with this notification
      required:
        - created_at
        - updated_at
        - id
        - routing
        - topic_id
        - note
        - event_ids
    MessageRouting:
      title: MessageRouting
      type: object
      properties:
        method:
          $ref: '#/components/schemas/MessageRoutingMethod'
        channels:
          type: array
          items:
            $ref: '#/components/schemas/MessageRoutingChannel'
      required:
        - method
        - channels
    NotificationTag:
      title: NotificationTag
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/NotificationTagData'
      required:
        - data
    MessageRoutingMethod:
      title: MessageRoutingMethod
      type: string
      enum:
        - all
        - single
    MessageRoutingChannel:
      title: MessageRoutingChannel
      oneOf:
        - type: string
        - $ref: '#/components/schemas/MessageRouting'
    NotificationTagData:
      title: NotificationTagData
      type: object
      properties:
        id:
          type: string
        name:
          type: string
      required:
        - id
        - name
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````