# Source: https://www.courier.com/docs/api-reference/user-preferences/get-user-subscription-topic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get user subscription topic

> Fetch user preferences for a specific subscription topic.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /users/{user_id}/preferences/{topic_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /users/{user_id}/preferences/{topic_id}:
    get:
      tags:
        - User Preferences
      summary: Get user subscription topic
      description: Fetch user preferences for a specific subscription topic.
      operationId: users_preferences_get
      parameters:
        - name: user_id
          in: path
          description: >-
            A unique identifier associated with the user whose preferences you
            wish to retrieve.
          required: true
          schema:
            type: string
        - name: topic_id
          in: path
          description: A unique identifier associated with a subscription topic.
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
                $ref: '#/components/schemas/UsersUserPreferencesGetResponse'
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


            const response = await
            client.users.preferences.retrieveTopic('topic_id', { user_id:
            'user_id' });


            console.log(response.topic);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.users.preferences.retrieve_topic(
                topic_id="topic_id",
                user_id="user_id",
            )
            print(response.topic)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Users.Preferences.GetTopic(\n\t\tcontext.TODO(),\n\t\t\"topic_id\",\n\t\tcourier.UserPreferenceGetTopicParams{\n\t\t\tUserID: \"user_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.Topic)\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import
            com.courier.models.users.preferences.PreferenceRetrieveTopicParams;

            import
            com.courier.models.users.preferences.PreferenceRetrieveTopicResponse;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    PreferenceRetrieveTopicParams params = PreferenceRetrieveTopicParams.builder()
                        .userId("user_id")
                        .topicId("topic_id")
                        .build();
                    PreferenceRetrieveTopicResponse response = client.users().preferences().retrieveTopic(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            response = courier.users.preferences.retrieve_topic("topic_id",
            user_id: "user_id")


            puts(response)
components:
  schemas:
    UsersUserPreferencesGetResponse:
      title: UsersUserPreferencesGetResponse
      type: object
      properties:
        topic:
          $ref: '#/components/schemas/UsersTopicPreference'
      required:
        - topic
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