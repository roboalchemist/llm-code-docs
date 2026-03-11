# Source: https://www.courier.com/docs/api-reference/user-tenants/remove-user-from-a-tenant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove User from a Tenant

> Removes a user from the supplied tenant.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml delete /users/{user_id}/tenants/{tenant_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /users/{user_id}/tenants/{tenant_id}:
    delete:
      tags:
        - User Tenants
      summary: Remove User from a Tenant
      description: Removes a user from the supplied tenant.
      operationId: users_tenants_remove
      parameters:
        - name: user_id
          in: path
          description: Id of the user to be removed from the supplied tenant.
          required: true
          schema:
            type: string
        - name: tenant_id
          in: path
          description: Id of the tenant the user should be removed from.
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


            await client.users.tenants.removeSingle('tenant_id', { user_id:
            'user_id' });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.users.tenants.remove_single(
                tenant_id="tenant_id",
                user_id="user_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Users.Tenants.RemoveSingle(\n\t\tcontext.TODO(),\n\t\t\"tenant_id\",\n\t\tcourier.UserTenantRemoveSingleParams{\n\t\t\tUserID: \"user_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.users.tenants.TenantRemoveSingleParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TenantRemoveSingleParams params = TenantRemoveSingleParams.builder()
                        .userId("user_id")
                        .tenantId("tenant_id")
                        .build();
                    client.users().tenants().removeSingle(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.users.tenants.remove_single("tenant_id", user_id:
            "user_id")


            puts(result)
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````