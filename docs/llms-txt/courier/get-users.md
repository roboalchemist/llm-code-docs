# Source: https://www.courier.com/docs/api-reference/bulk/get-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get users

> Get Bulk Job Users



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /bulk/{job_id}/users
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /bulk/{job_id}/users:
    get:
      tags:
        - Bulk
      summary: Get users
      description: Get Bulk Job Users
      operationId: bulk_getUsers
      parameters:
        - name: job_id
          in: path
          description: A unique identifier representing the bulk job
          required: true
          schema:
            type: string
        - name: cursor
          in: query
          description: >-
            A unique identifier that allows for fetching the next set of users
            added to the bulk job
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
                $ref: '#/components/schemas/BulkGetJobUsersResponse'
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

            const response = await client.bulk.listUsers('job_id');

            console.log(response.items);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.bulk.list_users(
                job_id="job_id",
            )
            print(response.items)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Bulk.ListUsers(\n\t\tcontext.TODO(),\n\t\t\"job_id\",\n\t\tcourier.BulkListUsersParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.Items)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.bulk.BulkListUsersParams;
            import com.courier.models.bulk.BulkListUsersResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    BulkListUsersResponse response = client.bulk().listUsers("job_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.bulk.list_users("job_id")

            puts(response)
components:
  schemas:
    BulkGetJobUsersResponse:
      title: BulkGetJobUsersResponse
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/BulkMessageUserResponse'
        paging:
          $ref: '#/components/schemas/Paging'
      required:
        - items
        - paging
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
    BulkMessageUserResponse:
      title: BulkMessageUserResponse
      type: object
      properties:
        status:
          $ref: '#/components/schemas/BulkJobUserStatus'
        messageId:
          type: string
          nullable: true
      required:
        - status
      allOf:
        - $ref: '#/components/schemas/InboundBulkMessageUser'
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
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
    BulkJobUserStatus:
      title: BulkJobUserStatus
      type: string
      enum:
        - PENDING
        - ENQUEUED
        - ERROR
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