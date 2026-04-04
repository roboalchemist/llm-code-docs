# Source: https://www.courier.com/docs/api-reference/user-preferences/get-users-preferences.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get user's preferences

> Fetch all user preferences.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /users/{user_id}/preferences
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /users/{user_id}/preferences:
    get:
      tags:
        - User Preferences
      summary: Get user's preferences
      description: Fetch all user preferences.
      operationId: users_preferences_list
      parameters:
        - name: user_id
          in: path
          description: >-
            A unique identifier associated with the user whose preferences you
            wish to retrieve.
          required: true
          schema:
            type: string
        - name: tenant_id
          in: query
          description: Query the preferences of a user for this specific tenant context.
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
                $ref: '#/components/schemas/UsersUserPreferencesListResponse'
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


            const preference = await
            client.users.preferences.retrieve('user_id');


            console.log(preference.items);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            preference = client.users.preferences.retrieve(
                user_id="user_id",
            )
            print(preference.items)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tpreference, err := client.Users.Preferences.Get(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.UserPreferenceGetParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", preference.Items)\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import
            com.courier.models.users.preferences.PreferenceRetrieveParams;

            import
            com.courier.models.users.preferences.PreferenceRetrieveResponse;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    PreferenceRetrieveResponse preference = client.users().preferences().retrieve("user_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            preference = courier.users.preferences.retrieve("user_id")

            puts(preference)
components:
  schemas:
    UsersUserPreferencesListResponse:
      title: UsersUserPreferencesListResponse
      type: object
      properties:
        paging:
          $ref: '#/components/schemas/Paging'
          description: Deprecated - Paging not implemented on this endpoint
        items:
          type: array
          items:
            $ref: '#/components/schemas/UsersTopicPreference'
          description: The Preferences associated with the user_id.
      required:
        - paging
        - items
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
    UsersTopicPreference:
      title: UsersTopicPreference
      type: object
      properties:
        custom_routing:
          type: array
          items:
            $ref: '#/components/schemas/ChannelClassification'
          nullable: true
          description: >-
            The Channels a user has chosen to receive notifications through for
            this topic
        default_status:
          $ref: '#/components/schemas/PreferenceStatus'
        has_custom_routing:
          type: boolean
          nullable: true
        status:
          $ref: '#/components/schemas/PreferenceStatus'
        topic_id:
          type: string
        topic_name:
          type: string
      required:
        - default_status
        - status
        - topic_id
        - topic_name
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
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
    PreferenceStatus:
      title: PreferenceStatus
      type: string
      enum:
        - OPTED_IN
        - OPTED_OUT
        - REQUIRED
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````