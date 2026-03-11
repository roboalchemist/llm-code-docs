# Source: https://www.courier.com/docs/api-reference/user-tenants/add-a-user-to-multiple-tenants.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a User to Multiple Tenants

> This endpoint is used to add a user to
multiple tenants in one call.
A custom profile can also be supplied for each tenant. 
This profile will be merged with the user's main 
profile when sending to the user with that tenant.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /users/{user_id}/tenants
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
    put:
      tags:
        - User Tenants
      summary: Add a User to Multiple Tenants
      description: |-
        This endpoint is used to add a user to
        multiple tenants in one call.
        A custom profile can also be supplied for each tenant. 
        This profile will be merged with the user's main 
        profile when sending to the user with that tenant.
      operationId: users_tenants_addMultiple
      parameters:
        - name: user_id
          in: path
          description: The user's ID. This can be any uniquely identifiable string.
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
                tenants:
                  type: array
                  items:
                    $ref: '#/components/schemas/UserTenantAssociation'
              required:
                - tenants
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


            await client.users.tenants.addMultiple('user_id', { tenants: [{
            tenant_id: 'tenant_id' }] });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.users.tenants.add_multiple(
                user_id="user_id",
                tenants=[{
                    "tenant_id": "tenant_id"
                }],
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Users.Tenants.AddMultiple(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.UserTenantAddMultipleParams{\n\t\t\tTenants: []courier.TenantAssociationParam{{\n\t\t\t\tTenantID: \"tenant_id\",\n\t\t\t}},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.tenants.TenantAssociation;
            import com.courier.models.users.tenants.TenantAddMultipleParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TenantAddMultipleParams params = TenantAddMultipleParams.builder()
                        .userId("user_id")
                        .addTenant(TenantAssociation.builder()
                            .tenantId("tenant_id")
                            .build())
                        .build();
                    client.users().tenants().addMultiple(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.users.tenants.add_multiple("user_id", tenants:
            [{tenant_id: "tenant_id"}])


            puts(result)
components:
  schemas:
    UserTenantAssociation:
      title: UserTenantAssociation
      type: object
      properties:
        user_id:
          type: string
          nullable: true
          description: User ID for the association between tenant and user
        type:
          type: string
          enum:
            - user
          nullable: true
        tenant_id:
          type: string
          description: Tenant ID for the association between tenant and user
        profile:
          type: object
          additionalProperties: true
          nullable: true
          description: >-
            Additional metadata to be applied to a user profile when used in a
            tenant context
      required:
        - tenant_id
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````