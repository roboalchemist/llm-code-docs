# Source: https://www.courier.com/docs/api-reference/tenants/get-users-in-tenant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Users in Tenant



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /tenants/{tenant_id}/users
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /tenants/{tenant_id}/users:
    get:
      tags:
        - Tenants
      summary: Get Users in Tenant
      operationId: tenants_getUsersByTenant
      parameters:
        - name: tenant_id
          in: path
          description: Id of the tenant for user membership.
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
                $ref: '#/components/schemas/ListUsersForTenantResponse'
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

            const response = await client.tenants.listUsers('tenant_id');

            console.log(response.has_more);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.tenants.list_users(
                tenant_id="tenant_id",
            )
            print(response.has_more)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Tenants.ListUsers(\n\t\tcontext.TODO(),\n\t\t\"tenant_id\",\n\t\tcourier.TenantListUsersParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.HasMore)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.tenants.TenantListUsersParams;
            import com.courier.models.tenants.TenantListUsersResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TenantListUsersResponse response = client.tenants().listUsers("tenant_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.tenants.list_users("tenant_id")

            puts(response)
components:
  schemas:
    ListUsersForTenantResponse:
      title: ListUsersForTenantResponse
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
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````