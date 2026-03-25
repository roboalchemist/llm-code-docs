# Source: https://www.courier.com/docs/api-reference/user-profiles/get-list-subscriptions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get list subscriptions

> Returns the subscribed lists for a specified user.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /profiles/{user_id}/lists
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
    get:
      tags:
        - User Profiles
      summary: Get list subscriptions
      description: Returns the subscribed lists for a specified user.
      operationId: profiles_getListSubscriptions
      parameters:
        - name: user_id
          in: path
          description: >-
            A unique identifier representing the user associated with the
            requested user profile.
          required: true
          schema:
            type: string
        - name: cursor
          in: query
          description: >-
            A unique identifier that allows for fetching the next set of message
            statuses.
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
                $ref: '#/components/schemas/GetListSubscriptionsResponse'
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

            const list = await client.profiles.lists.retrieve('user_id');

            console.log(list.paging);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            list = client.profiles.lists.retrieve(
                user_id="user_id",
            )
            print(list.paging)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tlist, err := client.Profiles.Lists.Get(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.ProfileListGetParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", list.Paging)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.profiles.lists.ListRetrieveParams;
            import com.courier.models.profiles.lists.ListRetrieveResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ListRetrieveResponse list = client.profiles().lists().retrieve("user_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            list = courier.profiles.lists.retrieve("user_id")

            puts(list)
components:
  schemas:
    GetListSubscriptionsResponse:
      title: GetListSubscriptionsResponse
      type: object
      properties:
        paging:
          $ref: '#/components/schemas/Paging'
        results:
          type: array
          items:
            $ref: '#/components/schemas/GetListSubscriptionsItem'
          description: An array of lists
      required:
        - paging
        - results
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
    GetListSubscriptionsItem:
      title: GetListSubscriptionsItem
      type: object
      properties:
        id:
          type: string
        name:
          type: string
          description: List name
        created:
          type: string
          description: >-
            The date/time of when the list was created. Represented as a string
            in ISO format.
        updated:
          type: string
          description: >-
            The date/time of when the list was updated. Represented as a string
            in ISO format.
        preferences:
          $ref: '#/components/schemas/RecipientPreferences'
          nullable: true
      required:
        - id
        - name
        - created
        - updated
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