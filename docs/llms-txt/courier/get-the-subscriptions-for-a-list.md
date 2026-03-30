# Source: https://www.courier.com/docs/api-reference/lists/get-the-subscriptions-for-a-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the subscriptions for a list

> Get the list's subscriptions.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /lists/{list_id}/subscriptions
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
    get:
      tags:
        - Lists
      summary: Get the subscriptions for a list
      description: Get the list's subscriptions.
      operationId: lists_getSubscribers
      parameters:
        - name: list_id
          in: path
          description: A unique identifier representing the list you wish to retrieve.
          required: true
          schema:
            type: string
        - name: cursor
          in: query
          description: >-
            A unique identifier that allows for fetching the next set of list
            subscriptions
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
                $ref: '#/components/schemas/ListGetSubscriptionsResponse'
        '404':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFound'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const subscriptions = await
            client.lists.subscriptions.list('list_id');


            console.log(subscriptions.items);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            subscriptions = client.lists.subscriptions.list(
                list_id="list_id",
            )
            print(subscriptions.items)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tsubscriptions, err := client.Lists.Subscriptions.List(\n\t\tcontext.TODO(),\n\t\t\"list_id\",\n\t\tcourier.ListSubscriptionListParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", subscriptions.Items)\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import
            com.courier.models.lists.subscriptions.SubscriptionListParams;

            import
            com.courier.models.lists.subscriptions.SubscriptionListResponse;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    SubscriptionListResponse subscriptions = client.lists().subscriptions().list("list_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            subscriptions = courier.lists.subscriptions.list("list_id")

            puts(subscriptions)
components:
  schemas:
    ListGetSubscriptionsResponse:
      title: ListGetSubscriptionsResponse
      type: object
      properties:
        paging:
          $ref: '#/components/schemas/Paging'
        items:
          type: array
          items:
            $ref: '#/components/schemas/ListSubscriptionRecipient'
      required:
        - paging
        - items
    NotFound:
      title: NotFound
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
    ListSubscriptionRecipient:
      title: ListSubscriptionRecipient
      type: object
      properties:
        recipientId:
          type: string
        created:
          type: string
          nullable: true
        preferences:
          $ref: '#/components/schemas/RecipientPreferences'
          nullable: true
      required:
        - recipientId
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
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