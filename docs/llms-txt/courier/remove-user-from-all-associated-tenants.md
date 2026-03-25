# Source: https://www.courier.com/docs/api-reference/user-tenants/remove-user-from-all-associated-tenants.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove User From All Associated Tenants

> Removes a user from any tenants they may have been associated with.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml delete /users/{user_id}/tenants
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /users/{user_id}/tenants:
    delete:
      tags:
        - User Tenants
      summary: Remove User From All Associated Tenants
      description: Removes a user from any tenants they may have been associated with.
      operationId: users_tenants_removeAll
      parameters:
        - name: user_id
          in: path
          description: Id of the user to be removed from the supplied tenant.
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
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            await client.users.tenants.removeAll('user_id');
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.users.tenants.remove_all(
                "user_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Users.Tenants.RemoveAll(context.TODO(), \"user_id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.users.tenants.TenantRemoveAllParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    client.users().tenants().removeAll("user_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            result = courier.users.tenants.remove_all("user_id")

            puts(result)
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````