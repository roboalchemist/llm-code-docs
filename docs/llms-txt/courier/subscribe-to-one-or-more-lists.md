# Source: https://www.courier.com/docs/api-reference/user-profiles/subscribe-to-one-or-more-lists.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscribe to one or more lists

> Subscribes the given user to one or more lists. If the list does not exist, it will be created.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /profiles/{user_id}/lists
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /profiles/{user_id}/lists:
    post:
      tags:
        - User Profiles
      summary: Subscribe to one or more lists
      description: >-
        Subscribes the given user to one or more lists. If the list does not
        exist, it will be created.
      operationId: profiles_subscribeToList
      parameters:
        - name: user_id
          in: path
          description: >-
            A unique identifier representing the user associated with the
            requested user profile.
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SubscribeToListsRequest'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubscribeToListsResponse'
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
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const response = await client.profiles.lists.subscribe('user_id', {
              lists: [{ listId: 'listId' }],
            });

            console.log(response.status);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.profiles.lists.subscribe(
                user_id="user_id",
                lists=[{
                    "list_id": "listId"
                }],
            )
            print(response.status)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Profiles.Lists.Subscribe(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.ProfileListSubscribeParams{\n\t\t\tLists: []courier.SubscribeToListsRequestItemParam{{\n\t\t\t\tListID: \"listId\",\n\t\t\t}},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.Status)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.profiles.SubscribeToListsRequestItem;
            import com.courier.models.profiles.lists.ListSubscribeParams;
            import com.courier.models.profiles.lists.ListSubscribeResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ListSubscribeParams params = ListSubscribeParams.builder()
                        .userId("user_id")
                        .addList(SubscribeToListsRequestItem.builder()
                            .listId("listId")
                            .build())
                        .build();
                    ListSubscribeResponse response = client.profiles().lists().subscribe(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            response = courier.profiles.lists.subscribe("user_id", lists:
            [{listId: "listId"}])


            puts(response)
components:
  schemas:
    SubscribeToListsRequest:
      title: SubscribeToListsRequest
      type: object
      properties:
        lists:
          type: array
          items:
            $ref: '#/components/schemas/SubscribeToListsRequestItem'
      required:
        - lists
    SubscribeToListsResponse:
      title: SubscribeToListsResponse
      type: object
      properties:
        status:
          type: string
          enum:
            - SUCCESS
      required:
        - status
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
    SubscribeToListsRequestItem:
      title: SubscribeToListsRequestItem
      type: object
      properties:
        listId:
          type: string
        preferences:
          $ref: '#/components/schemas/RecipientPreferences'
          nullable: true
      required:
        - listId
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