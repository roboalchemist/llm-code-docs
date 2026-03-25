# Source: https://www.courier.com/docs/api-reference/tenants/remove-default-preferences-for-topic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove Default Preferences For Topic



## OpenAPI

````yaml openapi-specs/openapi.documented.yml delete /tenants/{tenant_id}/default_preferences/items/{topic_id}
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
    delete:
      tags:
        - Tenants
      summary: Remove Default Preferences For Topic
      operationId: tenants_removeDefaultPreferencesForTopic
      parameters:
        - name: tenant_id
          in: path
          description: Id of the tenant to update the default preferences for.
          required: true
          schema:
            type: string
        - name: topic_id
          in: path
          description: >-
            Id of the subscription topic you want to have a default preference
            for.
          required: true
          schema:
            type: string
      responses:
        '204':
          description: ''
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            await client.tenants.preferences.items.delete('topic_id', {
            tenant_id: 'tenant_id' });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.tenants.preferences.items.delete(
                topic_id="topic_id",
                tenant_id="tenant_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Tenants.Preferences.Items.Delete(\n\t\tcontext.TODO(),\n\t\t\"topic_id\",\n\t\tcourier.TenantPreferenceItemDeleteParams{\n\t\t\tTenantID: \"tenant_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import
            com.courier.models.tenants.preferences.items.ItemDeleteParams;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ItemDeleteParams params = ItemDeleteParams.builder()
                        .tenantId("tenant_id")
                        .topicId("topic_id")
                        .build();
                    client.tenants().preferences().items().delete(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.tenants.preferences.items.delete("topic_id",
            tenant_id: "tenant_id")


            puts(result)
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````