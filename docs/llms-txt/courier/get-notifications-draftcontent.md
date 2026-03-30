# Source: https://www.courier.com/docs/api-reference/notification-templates/get-notifications-draftcontent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get notifications draftcontent



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /notifications/{id}/draft/content
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /notifications/{id}/draft/content:
    get:
      tags:
        - Notification Templates
      operationId: notifications_getDraftContent
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotificationGetContentResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const notificationGetContent = await
            client.notifications.draft.retrieveContent('id');


            console.log(notificationGetContent.blocks);
        - lang: Python
          source: >-
            import os

            from courier import Courier


            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )

            notification_get_content =
            client.notifications.draft.retrieve_content(
                "id",
            )

            print(notification_get_content.blocks)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tnotificationGetContent, err := client.Notifications.Draft.GetContent(context.TODO(), \"id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", notificationGetContent.Blocks)\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import com.courier.models.notifications.NotificationGetContent;

            import
            com.courier.models.notifications.draft.DraftRetrieveContentParams;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    NotificationGetContent notificationGetContent = client.notifications().draft().retrieveContent("id");
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            notification_get_content =
            courier.notifications.draft.retrieve_content("id")


            puts(notification_get_content)
components:
  schemas:
    NotificationGetContentResponse:
      title: NotificationGetContentResponse
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/NotificationBlock'
          nullable: true
        channels:
          type: array
          items:
            $ref: '#/components/schemas/NotificationChannel'
          nullable: true
        checksum:
          type: string
          nullable: true
    NotificationBlock:
      title: NotificationBlock
      type: object
      properties:
        alias:
          type: string
          nullable: true
        context:
          type: string
          nullable: true
        id:
          type: string
        type:
          $ref: '#/components/schemas/BlockType'
        content:
          $ref: '#/components/schemas/NotificationContent'
          nullable: true
        locales:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/NotificationContent'
          nullable: true
        checksum:
          type: string
          nullable: true
      required:
        - id
        - type
    NotificationChannel:
      title: NotificationChannel
      type: object
      properties:
        id:
          type: string
        type:
          type: string
          nullable: true
        content:
          $ref: '#/components/schemas/NotificationChannelContent'
          nullable: true
        locales:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/NotificationChannelContent'
          nullable: true
        checksum:
          type: string
          nullable: true
      required:
        - id
    BlockType:
      title: BlockType
      type: string
      enum:
        - action
        - divider
        - image
        - jsonnet
        - list
        - markdown
        - quote
        - template
        - text
    NotificationContent:
      title: NotificationContent
      oneOf:
        - type: string
        - $ref: '#/components/schemas/NotificationContentHierarchy'
    NotificationChannelContent:
      title: NotificationChannelContent
      type: object
      properties:
        subject:
          type: string
          nullable: true
        title:
          type: string
          nullable: true
    NotificationContentHierarchy:
      title: NotificationContentHierarchy
      type: object
      properties:
        parent:
          type: string
          nullable: true
        children:
          type: string
          nullable: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````