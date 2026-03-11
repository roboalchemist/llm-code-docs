# Source: https://www.courier.com/docs/api-reference/courier-create/publish-a-tenant-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Publish a Tenant Template

> Publishes a specific version of a notification template for a tenant.

The template must already exist in the tenant's notification map.
If no version is specified, defaults to publishing the "latest" version.




## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /tenants/{tenant_id}/templates/{template_id}/publish
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /tenants/{tenant_id}/templates/{template_id}/publish:
    post:
      tags:
        - Courier Create
      summary: Publish a Tenant Template
      description: |
        Publishes a specific version of a notification template for a tenant.

        The template must already exist in the tenant's notification map.
        If no version is specified, defaults to publishing the "latest" version.
      operationId: tenants_publishTemplate
      parameters:
        - name: tenant_id
          in: path
          description: Id of the tenant that owns the template.
          required: true
          schema:
            type: string
        - name: template_id
          in: path
          description: Id of the template to be published.
          required: true
          schema:
            type: string
      requestBody:
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PostTenantTemplatePublishRequest'
      responses:
        '200':
          description: Template published successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PostTenantTemplatePublishResponse'
        '400':
          description: Bad request - validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequest'
        '404':
          description: Template or tenant not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFound'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const postTenantTemplatePublishResponse = await
            client.tenants.templates.publish('template_id', {
              tenant_id: 'tenant_id',
            });


            console.log(postTenantTemplatePublishResponse.id);
        - lang: Python
          source: >-
            import os

            from courier import Courier


            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )

            post_tenant_template_publish_response =
            client.tenants.templates.publish(
                template_id="template_id",
                tenant_id="tenant_id",
            )

            print(post_tenant_template_publish_response.id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tpostTenantTemplatePublishResponse, err := client.Tenants.Templates.Publish(\n\t\tcontext.TODO(),\n\t\t\"template_id\",\n\t\tcourier.TenantTemplatePublishParams{\n\t\t\tTenantID: \"tenant_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", postTenantTemplatePublishResponse.ID)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.tenants.PostTenantTemplatePublishResponse;
            import com.courier.models.tenants.templates.TemplatePublishParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TemplatePublishParams params = TemplatePublishParams.builder()
                        .tenantId("tenant_id")
                        .templateId("template_id")
                        .build();
                    PostTenantTemplatePublishResponse postTenantTemplatePublishResponse = client.tenants().templates().publish(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            post_tenant_template_publish_response =
            courier.tenants.templates.publish("template_id", tenant_id:
            "tenant_id")


            puts(post_tenant_template_publish_response)
components:
  schemas:
    PostTenantTemplatePublishRequest:
      title: PostTenantTemplatePublishRequest
      type: object
      description: Request body for publishing a tenant template version
      properties:
        version:
          type: string
          default: latest
          description: >-
            The version of the template to publish (e.g., "v1", "v2", "latest").
            If not provided, defaults to "latest".
    PostTenantTemplatePublishResponse:
      title: PostTenantTemplatePublishResponse
      type: object
      description: Response from publishing a tenant template
      properties:
        id:
          type: string
          description: The template ID
        version:
          type: string
          description: The published version of the template
        published_at:
          type: string
          description: The timestamp when the template was published
      required:
        - id
        - version
        - published_at
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
    NotFound:
      title: NotFound
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