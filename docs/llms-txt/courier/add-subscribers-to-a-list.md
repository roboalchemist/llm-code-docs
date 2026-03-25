# Source: https://www.courier.com/docs/api-reference/lists/add-subscribers-to-a-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add subscribers to a list

> Subscribes additional users to the list, without modifying existing subscriptions. If the list does not exist, it will be automatically created.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /lists/{list_id}/subscriptions
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /lists/{list_id}/subscriptions:
    post:
      tags:
        - Lists
      summary: Add subscribers to a list
      description: >-
        Subscribes additional users to the list, without modifying existing
        subscriptions. If the list does not exist, it will be automatically
        created.
      operationId: lists_addSubscribers
      parameters:
        - name: list_id
          in: path
          description: A unique identifier representing the list you wish to retrieve.
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                recipients:
                  type: array
                  items:
                    $ref: '#/components/schemas/PutSubscriptionsRecipient'
              required:
                - recipients
      responses:
        '202':
          description: ''
        '204':
          description: ''
        '400':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequest'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            await client.lists.subscriptions.add('list_id', { recipients: [{
            recipientId: 'recipientId' }] });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.lists.subscriptions.add(
                list_id="list_id",
                recipients=[{
                    "recipient_id": "recipientId"
                }],
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Lists.Subscriptions.Add(\n\t\tcontext.TODO(),\n\t\t\"list_id\",\n\t\tcourier.ListSubscriptionAddParams{\n\t\t\tRecipients: []courier.PutSubscriptionsRecipientParam{{\n\t\t\t\tRecipientID: \"recipientId\",\n\t\t\t}},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.lists.PutSubscriptionsRecipient;
            import com.courier.models.lists.subscriptions.SubscriptionAddParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    SubscriptionAddParams params = SubscriptionAddParams.builder()
                        .listId("list_id")
                        .addRecipient(PutSubscriptionsRecipient.builder()
                            .recipientId("recipientId")
                            .build())
                        .build();
                    client.lists().subscriptions().add(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.lists.subscriptions.add("list_id", recipients:
            [{recipientId: "recipientId"}])


            puts(result)
components:
  schemas:
    PutSubscriptionsRecipient:
      title: PutSubscriptionsRecipient
      type: object
      properties:
        recipientId:
          type: string
        preferences:
          $ref: '#/components/schemas/RecipientPreferences'
          nullable: true
      required:
        - recipientId
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
    RecipientPreferences:
      title: RecipientPreferences
      type: object
      properties:
        categories:
          $ref: '#/components/schemas/NotificationPreferences'
          nullable: true
        notifications:
          $ref: '#/components/schemas/NotificationPreferences'
          nullable: true
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
    NotificationPreferences:
      title: NotificationPreferences
      type: object
      additionalProperties:
        $ref: '#/components/schemas/NotificationPreferenceDetails'
    NotificationPreferenceDetails:
      title: NotificationPreferenceDetails
      type: object
      properties:
        status:
          $ref: '#/components/schemas/PreferenceStatus'
        rules:
          type: array
          items:
            $ref: '#/components/schemas/Rule'
          nullable: true
        channel_preferences:
          type: array
          items:
            $ref: '#/components/schemas/ChannelPreference'
          nullable: true
      required:
        - status
    PreferenceStatus:
      title: PreferenceStatus
      type: string
      enum:
        - OPTED_IN
        - OPTED_OUT
        - REQUIRED
    Rule:
      title: Rule
      type: object
      properties:
        start:
          type: string
          nullable: true
        until:
          type: string
      required:
        - until
    ChannelPreference:
      title: ChannelPreference
      type: object
      properties:
        channel:
          $ref: '#/components/schemas/ChannelClassification'
      required:
        - channel
    ChannelClassification:
      title: ChannelClassification
      type: string
      enum:
        - direct_message
        - email
        - push
        - sms
        - webhook
        - inbox
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````