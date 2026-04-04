# Source: https://www.courier.com/docs/api-reference/bulk/add-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add users

> Ingest user data into a Bulk Job. 

**Important**: For email-based bulk jobs, each user must include `profile.email` 
for provider routing to work correctly. The `to.email` field is not sufficient 
for email provider routing.




## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /bulk/{job_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /bulk/{job_id}:
    post:
      tags:
        - Bulk
      summary: Add users
      description: >
        Ingest user data into a Bulk Job. 


        **Important**: For email-based bulk jobs, each user must include
        `profile.email` 

        for provider routing to work correctly. The `to.email` field is not
        sufficient 

        for email provider routing.
      operationId: bulk_ingestUsers
      parameters:
        - name: job_id
          in: path
          description: A unique identifier representing the bulk job
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BulkIngestUsersParams'
      responses:
        '204':
          description: ''
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            await client.bulk.addUsers('job_id', { users: [{}] });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.bulk.add_users(
                job_id="job_id",
                users=[{}],
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Bulk.AddUsers(\n\t\tcontext.TODO(),\n\t\t\"job_id\",\n\t\tcourier.BulkAddUsersParams{\n\t\t\tUsers: []courier.InboundBulkMessageUserParam{{}},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.bulk.BulkAddUsersParams;
            import com.courier.models.bulk.InboundBulkMessageUser;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    BulkAddUsersParams params = BulkAddUsersParams.builder()
                        .jobId("job_id")
                        .addUser(InboundBulkMessageUser.builder().build())
                        .build();
                    client.bulk().addUsers(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            result = courier.bulk.add_users("job_id", users: [{}])

            puts(result)
components:
  schemas:
    BulkIngestUsersParams:
      title: BulkIngestUsersParams
      type: object
      properties:
        users:
          type: array
          items:
            $ref: '#/components/schemas/InboundBulkMessageUser'
      required:
        - users
    InboundBulkMessageUser:
      title: InboundBulkMessageUser
      type: object
      properties:
        preferences:
          $ref: '#/components/schemas/RecipientPreferences'
          nullable: true
        profile:
          type: object
          nullable: true
          description: >
            User profile information. For email-based bulk jobs, `profile.email`
            is required 

            for provider routing to determine if the message can be delivered.
            The email 

            address should be provided here rather than in `to.email`.
          additionalProperties: true
        recipient:
          type: string
          nullable: true
          description: User ID (legacy field, use profile or to.user_id instead)
        data:
          nullable: true
          description: User-specific data that will be merged with message.data
        to:
          $ref: '#/components/schemas/UserRecipient'
          nullable: true
          description: >
            Optional recipient information. Note: For email provider routing,
            use 

            `profile.email` instead of `to.email`. The `to` field is primarily
            used 

            for recipient identification and data merging.
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
    UserRecipient:
      title: User Recipient
      description: Send to a specific user by user_id, email, phone_number, or list_id
      type: object
      properties:
        user_id:
          type: string
          nullable: true
          description: >-
            The user's unique identifier. Typically, this will match the user id
            of a user in your system.
        account_id:
          type: string
          nullable: true
          description: Deprecated - Use `tenant_id` instead.
        context:
          $ref: '#/components/schemas/MessageContext'
          nullable: true
          description: Context such as tenant_id to send the notification with.
        data:
          $ref: '#/components/schemas/MessageData'
          nullable: true
        email:
          type: string
          nullable: true
          description: The user's email address.
        locale:
          type: string
          nullable: true
          description: The user's preferred ISO 639-1 language code.
        phone_number:
          type: string
          nullable: true
          description: The user's phone number.
        list_id:
          type: string
          nullable: true
          description: The id of the list to send the message to.
        preferences:
          $ref: '#/components/schemas/ProfilePreferences'
          nullable: true
        tenant_id:
          type: string
          nullable: true
          description: The id of the tenant the user is associated with.
      allOf:
        - $ref: '#/components/schemas/UserRecipientType'
    NotificationPreferences:
      title: NotificationPreferences
      type: object
      additionalProperties:
        $ref: '#/components/schemas/NotificationPreferenceDetails'
    MessageContext:
      title: MessageContext
      type: object
      properties:
        tenant_id:
          type: string
          nullable: true
          description: Tenant id used to load brand/default preferences/context.
    MessageData:
      title: MessageData
      type: object
      additionalProperties: true
    ProfilePreferences:
      title: ProfilePreferences
      type: object
      properties:
        categories:
          $ref: '#/components/schemas/Preferences'
          nullable: true
        notifications:
          $ref: '#/components/schemas/Preferences'
        templateId:
          type: string
          nullable: true
      required:
        - notifications
    UserRecipientType:
      title: UserRecipientType
      type: object
      properties: {}
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
    Preferences:
      title: Preferences
      type: object
      additionalProperties:
        $ref: '#/components/schemas/Preference'
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
    Preference:
      title: Preference
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
        source:
          $ref: '#/components/schemas/ChannelSource'
          nullable: true
      required:
        - status
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
    ChannelSource:
      title: ChannelSource
      type: string
      enum:
        - subscription
        - list
        - recipient
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````