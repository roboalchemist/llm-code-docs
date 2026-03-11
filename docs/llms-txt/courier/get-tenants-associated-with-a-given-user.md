# Source: https://www.courier.com/docs/api-reference/user-tenants/get-tenants-associated-with-a-given-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get tenants associated with a given user

> Returns a paginated list of user tenant associations.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /users/{user_id}/tenants
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
    get:
      tags:
        - User Tenants
      summary: Get tenants associated with a given user
      description: Returns a paginated list of user tenant associations.
      operationId: users_tenants_list
      parameters:
        - name: user_id
          in: path
          description: Id of the user to retrieve all associated tenants for.
          required: true
          schema:
            type: string
        - name: limit
          in: query
          description: |-
            The number of accounts to return 
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
                $ref: '#/components/schemas/UsersListTenantsForUserResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const tenants = await client.users.tenants.list('user_id');

            console.log(tenants.has_more);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            tenants = client.users.tenants.list(
                user_id="user_id",
            )
            print(tenants.has_more)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\ttenants, err := client.Users.Tenants.List(\n\t\tcontext.TODO(),\n\t\t\"user_id\",\n\t\tcourier.UserTenantListParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", tenants.HasMore)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.users.tenants.TenantListParams;
            import com.courier.models.users.tenants.TenantListResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TenantListResponse tenants = client.users().tenants().list("user_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            tenants = courier.users.tenants.list("user_id")

            puts(tenants)
components:
  schemas:
    UsersListTenantsForUserResponse:
      title: UsersListTenantsForUserResponse
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/UserTenantAssociation'
          nullable: true
        has_more:
          type: boolean
          description: Set to true when there are more pages that can be retrieved.
        url:
          type: string
          description: A url that may be used to generate these results.
        next_url:
          type: string
          nullable: true
          description: |-
            A url that may be used to generate fetch the next set of results. 
            Defined only when `has_more` is set to true
        cursor:
          type: string
          nullable: true
          description: |-
            A pointer to the next page of results. Defined 
            only when `has_more` is set to true
        type:
          type: string
          enum:
            - list
          description: Always set to `list`. Represents the type of this object.
      required:
        - has_more
        - url
        - type
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