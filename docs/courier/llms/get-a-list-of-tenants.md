# Source: https://www.courier.com/docs/api-reference/tenants/get-a-list-of-tenants.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a List of Tenants



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /tenants
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /tenants:
    get:
      tags:
        - Tenants
      summary: Get a List of Tenants
      operationId: tenants_list
      parameters:
        - name: parent_tenant_id
          in: query
          description: Filter the list of tenants by parent_id
          required: false
          schema:
            type: string
            nullable: true
        - name: limit
          in: query
          description: |-
            The number of tenants to return 
            (defaults to 20, maximum value of 100)
          required: false
          schema:
            type: integer
            nullable: true
        - name: cursor
          in: query
          description: Continue the pagination with the next cursor
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
                $ref: '#/components/schemas/TenantListResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const tenants = await client.tenants.list();

            console.log(tenants.has_more);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            tenants = client.tenants.list()
            print(tenants.has_more)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\ttenants, err := client.Tenants.List(context.TODO(), courier.TenantListParams{})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", tenants.HasMore)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.tenants.TenantListParams;
            import com.courier.models.tenants.TenantListResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TenantListResponse tenants = client.tenants().list();
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            tenants = courier.tenants.list

            puts(tenants)
components:
  schemas:
    TenantListResponse:
      title: TenantListResponse
      type: object
      properties:
        cursor:
          type: string
          nullable: true
          description: >-
            A pointer to the next page of results. Defined only when has_more is
            set to true.
        has_more:
          type: boolean
          description: Set to true when there are more pages that can be retrieved.
        items:
          type: array
          items:
            $ref: '#/components/schemas/Tenant'
          description: An array of Tenants
        next_url:
          type: string
          nullable: true
          description: |-
            A url that may be used to generate fetch the next set of results. 
            Defined only when has_more is set to true
        url:
          type: string
          description: A url that may be used to generate these results.
        type:
          type: string
          enum:
            - list
          description: Always set to "list". Represents the type of this object.
      required:
        - has_more
        - items
        - url
        - type
    Tenant:
      title: Tenant
      type: object
      properties:
        id:
          type: string
          description: Id of the tenant.
        name:
          type: string
          description: Name of the tenant.
        parent_tenant_id:
          type: string
          nullable: true
          description: Tenant's parent id (if any).
        default_preferences:
          $ref: '#/components/schemas/DefaultPreferences'
          nullable: true
          description: >-
            Defines the preferences used for the account when the user hasn't
            specified their own.
        properties:
          type: object
          additionalProperties: true
          nullable: true
          description: Arbitrary properties accessible to a template.
        user_profile:
          type: object
          additionalProperties: true
          nullable: true
          description: A user profile object merged with user profile on send.
        brand_id:
          type: string
          nullable: true
          description: >-
            Brand to be used for the account when one is not specified by the
            send call.
      required:
        - id
        - name
    DefaultPreferences:
      title: DefaultPreferences
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/SubscriptionTopic'
          nullable: true
    SubscriptionTopic:
      title: SubscriptionTopic
      type: object
      properties:
        id:
          type: string
          description: Topic ID
      required:
        - id
      allOf:
        - $ref: '#/components/schemas/SubscriptionTopicNew'
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