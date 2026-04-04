# Source: https://www.courier.com/docs/api-reference/user-profiles/delete-list-subscriptions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete list subscriptions

> Removes all list subscriptions for given user.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml delete /profiles/{user_id}/lists
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
    delete:
      tags:
        - User Profiles
      summary: Delete list subscriptions
      description: Removes all list subscriptions for given user.
      operationId: profiles_deleteListSubscription
      parameters:
        - name: user_id
          in: path
          description: >-
            A unique identifier representing the user associated with the
            requested profile.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteListSubscriptionResponse'
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

            const list = await client.profiles.lists.delete('user_id');

            console.log(list.status);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            list = client.profiles.lists.delete(
                "user_id",
            )
            print(list.status)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tlist, err := client.Profiles.Lists.Delete(context.TODO(), \"user_id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", list.Status)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.profiles.lists.ListDeleteParams;
            import com.courier.models.profiles.lists.ListDeleteResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ListDeleteResponse list = client.profiles().lists().delete("user_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            list = courier.profiles.lists.delete("user_id")

            puts(list)
components:
  schemas:
    DeleteListSubscriptionResponse:
      title: DeleteListSubscriptionResponse
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