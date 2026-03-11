# Source: https://www.courier.com/docs/api-reference/lists/get-a-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a list

> Returns a list based on the list ID provided.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /lists/{list_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /lists/{list_id}:
    get:
      tags:
        - Lists
      summary: Get a list
      description: Returns a list based on the list ID provided.
      operationId: lists_get
      parameters:
        - name: list_id
          in: path
          description: A unique identifier representing the list you wish to retrieve.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubscriptionList'
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
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const subscriptionList = await client.lists.retrieve('list_id');

            console.log(subscriptionList.id);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            subscription_list = client.lists.retrieve(
                "list_id",
            )
            print(subscription_list.id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tsubscriptionList, err := client.Lists.Get(context.TODO(), \"list_id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", subscriptionList.ID)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.lists.ListRetrieveParams;
            import com.courier.models.lists.SubscriptionList;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    SubscriptionList subscriptionList = client.lists().retrieve("list_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            subscription_list = courier.lists.retrieve("list_id")

            puts(subscription_list)
components:
  schemas:
    SubscriptionList:
      title: SubscriptionList
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        created:
          type: string
          nullable: true
        updated:
          type: string
          nullable: true
      required:
        - id
        - name
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