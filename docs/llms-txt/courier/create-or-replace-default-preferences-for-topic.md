# Source: https://www.courier.com/docs/api-reference/tenants/create-or-replace-default-preferences-for-topic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create or Replace Default Preferences For Topic



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /tenants/{tenant_id}/default_preferences/items/{topic_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /tenants/{tenant_id}/default_preferences/items/{topic_id}:
    put:
      tags:
        - Tenants
      summary: Create or Replace Default Preferences For Topic
      operationId: tenants_createOrReplaceDefaultPreferencesForTopic
      parameters:
        - name: tenant_id
          in: path
          description: Id of the tenant to update the default preferences for.
          required: true
          schema:
            type: string
          examples:
            Example1:
              value: tenantABC
        - name: topic_id
          in: path
          description: >-
            Id of the subscription topic you want to have a default preference
            for.
          required: true
          schema:
            type: string
          examples:
            Example1:
              value: HB529N49MD4D5PMX9WR5P4JH78NA
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SubscriptionTopicNew'
            examples:
              Example1:
                value:
                  status: OPTED_IN
                  has_custom_routing: true
                  custom_routing:
                    - inbox
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

            await client.tenants.preferences.items.update('topic_id', {
              tenant_id: 'tenant_id',
              status: 'OPTED_IN',
              custom_routing: ['inbox'],
              has_custom_routing: true,
            });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.tenants.preferences.items.update(
                topic_id="topic_id",
                tenant_id="tenant_id",
                status="OPTED_IN",
                custom_routing=["inbox"],
                has_custom_routing=True,
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Tenants.Preferences.Items.Update(\n\t\tcontext.TODO(),\n\t\t\"topic_id\",\n\t\tcourier.TenantPreferenceItemUpdateParams{\n\t\t\tTenantID: \"tenant_id\",\n\t\t\tSubscriptionTopicNew: courier.SubscriptionTopicNewParam{\n\t\t\t\tStatus: courier.SubscriptionTopicNewStatusOptedIn,\n\t\t\t},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import com.courier.models.tenants.SubscriptionTopicNew;

            import
            com.courier.models.tenants.preferences.items.ItemUpdateParams;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ItemUpdateParams params = ItemUpdateParams.builder()
                        .tenantId("tenant_id")
                        .topicId("topic_id")
                        .subscriptionTopicNew(SubscriptionTopicNew.builder()
                            .status(SubscriptionTopicNew.Status.OPTED_IN)
                            .build())
                        .build();
                    client.tenants().preferences().items().update(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.tenants.preferences.items.update("topic_id",
            tenant_id: "tenant_id", status: :OPTED_IN)


            puts(result)
components:
  schemas:
    SubscriptionTopicNew:
      title: SubscriptionTopicNew
      type: object
      properties:
        status:
          $ref: '#/components/schemas/SubscriptionTopicStatus'
        has_custom_routing:
          type: boolean
          nullable: true
          description: >-
            Override channel routing with custom preferences. This will override
            any template preferences that are set, but a user can still
            customize their preferences
        custom_routing:
          type: array
          items:
            $ref: '#/components/schemas/ChannelClassification'
          nullable: true
          description: >-
            The default channels to send to this tenant when has_custom_routing
            is enabled
      required:
        - status
    SubscriptionTopicStatus:
      title: SubscriptionTopicStatus
      type: string
      enum:
        - OPTED_OUT
        - OPTED_IN
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````