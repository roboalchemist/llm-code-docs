# Source: https://www.courier.com/docs/api-reference/lists/unsubscribe-a-user-profile-from-a-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Unsubscribe a user profile from a list

> Delete a subscription to a list by list ID and user ID.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml delete /lists/{list_id}/subscriptions/{user_id}
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
    delete:
      tags:
        - Lists
      summary: Unsubscribe a user profile from a list
      description: Delete a subscription to a list by list ID and user ID.
      operationId: lists_unsubscribe
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
      responses:
        '204':
          description: ''
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


            await client.lists.subscriptions.unsubscribeUser('user_id', {
            list_id: 'list_id' });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.lists.subscriptions.unsubscribe_user(
                user_id="user_id",
                list_id="list_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Lists.Subscriptions.UnsubscribeUser(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.ListSubscriptionUnsubscribeUserParams{\n\t\t\tListID: \"list_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import
            com.courier.models.lists.subscriptions.SubscriptionUnsubscribeUserParams;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    SubscriptionUnsubscribeUserParams params = SubscriptionUnsubscribeUserParams.builder()
                        .listId("list_id")
                        .userId("user_id")
                        .build();
                    client.lists().subscriptions().unsubscribeUser(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.lists.subscriptions.unsubscribe_user("user_id",
            list_id: "list_id")


            puts(result)
components:
  schemas:
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