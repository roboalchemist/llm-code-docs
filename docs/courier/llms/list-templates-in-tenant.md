# Source: https://www.courier.com/docs/api-reference/courier-create/list-templates-in-tenant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Templates in Tenant



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /tenants/{tenant_id}/templates
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /tenants/{tenant_id}/templates:
    get:
      tags:
        - Courier Create
      summary: List Templates in Tenant
      operationId: tenants_getTemplateListByTenant
      parameters:
        - name: tenant_id
          in: path
          description: Id of the tenant for which to retrieve the templates.
          required: true
          schema:
            type: string
        - name: limit
          in: query
          description: >-
            The number of templates to return (defaults to 20, maximum value of
            100)
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
                $ref: '#/components/schemas/ListTemplatesByTenantResponse'
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

            const templates = await client.tenants.templates.list('tenant_id');

            console.log(templates.has_more);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            templates = client.tenants.templates.list(
                tenant_id="tenant_id",
            )
            print(templates.has_more)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\ttemplates, err := client.Tenants.Templates.List(\n\t\tcontext.TODO(),\n\t\t\"tenant_id\",\n\t\tcourier.TenantTemplateListParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", templates.HasMore)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.tenants.templates.TemplateListParams;
            import com.courier.models.tenants.templates.TemplateListResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TemplateListResponse templates = client.tenants().templates().list("tenant_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            templates = courier.tenants.templates.list("tenant_id")

            puts(templates)
components:
  schemas:
    ListTemplatesByTenantResponse:
      title: ListTemplatesByTenantResponse
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/ListTemplateTenantAssociation'
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
    ListTemplateTenantAssociation:
      title: ListTemplateTenantAssociation
      type: object
      properties:
        data:
          $ref: '#/components/schemas/TenantTemplateDataNoContent'
      required:
        - data
      allOf:
        - $ref: '#/components/schemas/BaseTemplateTenantAssociation'
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
    TenantTemplateDataNoContent:
      title: TenantTemplateDataNoContent
      type: object
      description: The template's data containing it's routing configs
      properties:
        routing:
          $ref: '#/components/schemas/MessageRouting'
      required:
        - routing
    BaseTemplateTenantAssociation:
      title: BaseTemplateTenantAssociation
      type: object
      properties:
        id:
          type: string
          description: The template's id
        created_at:
          type: string
          description: The timestamp at which the template was created
        updated_at:
          type: string
          description: The timestamp at which the template was last updated
        published_at:
          type: string
          description: The timestamp at which the template was published
        version:
          type: string
          description: The version of the template
      required:
        - id
        - created_at
        - updated_at
        - published_at
        - version
    MessageRouting:
      title: MessageRouting
      type: object
      properties:
        method:
          $ref: '#/components/schemas/MessageRoutingMethod'
        channels:
          type: array
          items:
            $ref: '#/components/schemas/MessageRoutingChannel'
      required:
        - method
        - channels
    MessageRoutingMethod:
      title: MessageRoutingMethod
      type: string
      enum:
        - all
        - single
    MessageRoutingChannel:
      title: MessageRoutingChannel
      oneOf:
        - type: string
        - $ref: '#/components/schemas/MessageRouting'
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````