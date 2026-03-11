# Source: https://www.courier.com/docs/api-reference/lists/subscribe-a-single-user-profile-to-a-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscribe a single user profile to a list

> Subscribe a user to an existing list (note: if the List does not exist, it will be automatically created).



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /lists/{list_id}/subscriptions/{user_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /lists/{list_id}/subscriptions/{user_id}:
    put:
      tags:
        - Lists
      summary: Subscribe a single user profile to a list
      description: >-
        Subscribe a user to an existing list (note: if the List does not exist,
        it will be automatically created).
      operationId: lists_subscribe
      parameters:
        - name: list_id
          in: path
          description: A unique identifier representing the list you wish to retrieve.
          required: true
          schema:
            type: string
        - name: user_id
          in: path
          description: >-
            A unique identifier representing the recipient associated with the
            list
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
                preferences:
                  $ref: '#/components/schemas/RecipientPreferences'
                  nullable: true
      responses:
        '204':
          description: ''
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            await client.lists.subscriptions.subscribeUser('user_id', { list_id:
            'list_id' });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.lists.subscriptions.subscribe_user(
                user_id="user_id",
                list_id="list_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Lists.Subscriptions.SubscribeUser(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.ListSubscriptionSubscribeUserParams{\n\t\t\tListID: \"list_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import
            com.courier.models.lists.subscriptions.SubscriptionSubscribeUserParams;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    SubscriptionSubscribeUserParams params = SubscriptionSubscribeUserParams.builder()
                        .listId("list_id")
                        .userId("user_id")
                        .build();
                    client.lists().subscriptions().subscribeUser(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.lists.subscriptions.subscribe_user("user_id",
            list_id: "list_id")


            puts(result)
components:
  schemas:
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