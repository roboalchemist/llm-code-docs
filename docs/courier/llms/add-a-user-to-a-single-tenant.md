# Source: https://www.courier.com/docs/api-reference/user-tenants/add-a-user-to-a-single-tenant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a User to a Single Tenant

> This endpoint is used to add a single tenant.

A custom profile can also be supplied with the tenant. 
This profile will be merged with the user's main profile 
when sending to the user with that tenant.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /users/{user_id}/tenants/{tenant_id}
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
    put:
      tags:
        - User Tenants
      summary: Add a User to a Single Tenant
      description: |-
        This endpoint is used to add a single tenant.

        A custom profile can also be supplied with the tenant. 
        This profile will be merged with the user's main profile 
        when sending to the user with that tenant.
      operationId: users_tenants_add
      parameters:
        - name: user_id
          in: path
          description: Id of the user to be added to the supplied tenant.
          required: true
          schema:
            type: string
        - name: tenant_id
          in: path
          description: Id of the tenant the user should be added to.
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
                profile:
                  type: object
                  additionalProperties: true
                  nullable: true
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


            await client.users.tenants.addSingle('tenant_id', { user_id:
            'user_id' });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.users.tenants.add_single(
                tenant_id="tenant_id",
                user_id="user_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Users.Tenants.AddSingle(\n\t\tcontext.TODO(),\n\t\t\"tenant_id\",\n\t\tcourier.UserTenantAddSingleParams{\n\t\t\tUserID: \"user_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.users.tenants.TenantAddSingleParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TenantAddSingleParams params = TenantAddSingleParams.builder()
                        .userId("user_id")
                        .tenantId("tenant_id")
                        .build();
                    client.users().tenants().addSingle(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.users.tenants.add_single("tenant_id", user_id:
            "user_id")


            puts(result)
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````