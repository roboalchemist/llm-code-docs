# Source: https://www.courier.com/docs/api-reference/user-preferences/update-or-create-user-preferences-for-a-specific-subscription-topic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update or Create user preferences for a specific subscription topic

> Update or Create user preferences for a specific subscription topic.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /users/{user_id}/preferences/{topic_id}
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
    put:
      tags:
        - User Preferences
      summary: Update or Create user preferences for a specific subscription topic
      description: Update or Create user preferences for a specific subscription topic.
      operationId: users_preferences_update
      parameters:
        - name: user_id
          in: path
          description: >-
            A unique identifier associated with the user whose preferences you
            wish to retrieve.
          required: true
          schema:
            type: string
          examples:
            Example1:
              value: abc-123
        - name: topic_id
          in: path
          description: A unique identifier associated with a subscription topic.
          required: true
          schema:
            type: string
          examples:
            Example1:
              value: 74Q4QGFBEX481DP6JRPMV751H4XT
        - name: tenant_id
          in: query
          description: Update the preferences of a user for this specific tenant context.
          required: false
          schema:
            type: string
            nullable: true
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                topic:
                  $ref: '#/components/schemas/UsersTopicPreferenceUpdate'
              required:
                - topic
            examples:
              Example1:
                value:
                  topic:
                    status: OPTED_IN
                    has_custom_routing: true
                    custom_routing:
                      - inbox
                      - email
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UsersUserPreferencesUpdateResponse'
              examples:
                Example1:
                  value:
                    message: success
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


            const response = await
            client.users.preferences.updateOrCreateTopic('topic_id', {
              user_id: 'user_id',
              topic: {
                status: 'OPTED_IN',
                has_custom_routing: true,
                custom_routing: ['inbox', 'email'],
              },
            });


            console.log(response.message);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.users.preferences.update_or_create_topic(
                topic_id="topic_id",
                user_id="user_id",
                topic={
                    "status": "OPTED_IN",
                    "has_custom_routing": True,
                    "custom_routing": ["inbox", "email"],
                },
            )
            print(response.message)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n\t\"github.com/trycourier/courier-go/shared\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Users.Preferences.UpdateOrNewTopic(\n\t\tcontext.TODO(),\n\t\t\"topic_id\",\n\t\tcourier.UserPreferenceUpdateOrNewTopicParams{\n\t\t\tUserID: \"user_id\",\n\t\t\tTopic: courier.UserPreferenceUpdateOrNewTopicParamsTopic{\n\t\t\t\tStatus:           shared.PreferenceStatusOptedIn,\n\t\t\t\tHasCustomRouting: courier.Bool(true),\n\t\t\t\tCustomRouting:    []shared.ChannelClassification{shared.ChannelClassificationInbox, shared.ChannelClassificationEmail},\n\t\t\t},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.Message)\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import com.courier.models.PreferenceStatus;

            import
            com.courier.models.users.preferences.PreferenceUpdateOrCreateTopicParams;

            import
            com.courier.models.users.preferences.PreferenceUpdateOrCreateTopicResponse;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    PreferenceUpdateOrCreateTopicParams params = PreferenceUpdateOrCreateTopicParams.builder()
                        .userId("user_id")
                        .topicId("topic_id")
                        .topic(PreferenceUpdateOrCreateTopicParams.Topic.builder()
                            .status(PreferenceStatus.OPTED_IN)
                            .build())
                        .build();
                    PreferenceUpdateOrCreateTopicResponse response = client.users().preferences().updateOrCreateTopic(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.users.preferences.update_or_create_topic(
              "topic_id",
              user_id: "user_id",
              topic: {status: :OPTED_IN}
            )

            puts(response)
components:
  schemas:
    UsersTopicPreferenceUpdate:
      title: UsersTopicPreferenceUpdate
      type: object
      properties:
        status:
          $ref: '#/components/schemas/PreferenceStatus'
        custom_routing:
          type: array
          items:
            $ref: '#/components/schemas/ChannelClassification'
          nullable: true
          description: >-
            The Channels a user has chosen to receive notifications through for
            this topic
        has_custom_routing:
          type: boolean
          nullable: true
      required:
        - status
    UsersUserPreferencesUpdateResponse:
      title: UsersUserPreferencesUpdateResponse
      type: object
      properties:
        message:
          type: string
          example: success
      required:
        - message
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
    PreferenceStatus:
      title: PreferenceStatus
      type: string
      enum:
        - OPTED_IN
        - OPTED_OUT
        - REQUIRED
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