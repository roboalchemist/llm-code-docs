# Source: https://www.courier.com/docs/api-reference/tenants/create-or-replace-a-tenant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create or Replace a Tenant



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /tenants/{tenant_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /tenants/{tenant_id}:
    put:
      tags:
        - Tenants
      summary: Create or Replace a Tenant
      operationId: tenants_createOrReplace
      parameters:
        - name: tenant_id
          in: path
          description: A unique identifier representing the tenant to be returned.
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
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
                    Defines the preferences used for the tenant when the user
                    hasn't specified their own.
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
                    Brand to be used for the account when one is not specified
                    by the send call.
              required:
                - name
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Tenant'
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


            const tenant = await client.tenants.update('tenant_id', { name:
            'name' });


            console.log(tenant.id);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            tenant = client.tenants.update(
                tenant_id="tenant_id",
                name="name",
            )
            print(tenant.id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\ttenant, err := client.Tenants.Update(\n\t\tcontext.TODO(),\n\t\t\"tenant_id\",\n\t\tcourier.TenantUpdateParams{\n\t\t\tName: \"name\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", tenant.ID)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.tenants.Tenant;
            import com.courier.models.tenants.TenantUpdateParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TenantUpdateParams params = TenantUpdateParams.builder()
                        .tenantId("tenant_id")
                        .name("name")
                        .build();
                    Tenant tenant = client.tenants().update(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            tenant = courier.tenants.update("tenant_id", name: "name")

            puts(tenant)
components:
  schemas:
    DefaultPreferences:
      title: DefaultPreferences
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/SubscriptionTopic'
          nullable: true
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
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
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