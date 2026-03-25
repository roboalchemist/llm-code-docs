# Source: https://www.courier.com/docs/api-reference/brands/create-a-new-brand.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new brand



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /brands
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /brands:
    post:
      tags:
        - Brands
      summary: Create a new brand
      operationId: brands_create
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BrandParameters'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Brand'
        '400':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequest'
        '402':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentRequired'
        '409':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AlreadyExists'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const brand = await client.brands.create({ name: 'name' });

            console.log(brand.id);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            brand = client.brands.create(
                name="name",
            )
            print(brand.id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tbrand, err := client.Brands.New(context.TODO(), courier.BrandNewParams{\n\t\tName: \"name\",\n\t})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", brand.ID)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.brands.Brand;
            import com.courier.models.brands.BrandCreateParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    BrandCreateParams params = BrandCreateParams.builder()
                        .name("name")
                        .build();
                    Brand brand = client.brands().create(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            brand = courier.brands.create(name: "name")

            puts(brand)
components:
  schemas:
    BrandParameters:
      title: BrandParameters
      type: object
      properties:
        id:
          type: string
          nullable: true
        name:
          type: string
        settings:
          $ref: '#/components/schemas/BrandSettings'
          nullable: true
        snippets:
          $ref: '#/components/schemas/BrandSnippets'
          nullable: true
      required:
        - name
    Brand:
      title: Brand
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        published:
          type: integer
          format: int64
          nullable: true
        created:
          type: integer
          format: int64
        updated:
          type: integer
          format: int64
        settings:
          $ref: '#/components/schemas/BrandSettings'
          nullable: true
        snippets:
          $ref: '#/components/schemas/BrandSnippets'
          nullable: true
        version:
          type: string
          nullable: true
      required:
        - id
        - name
        - created
        - updated
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
    PaymentRequired:
      title: PaymentRequired
      type: object
      properties:
        type:
          type: string
          enum:
            - authorization_error
      required:
        - type
      allOf:
        - $ref: '#/components/schemas/BaseError'
    AlreadyExists:
      title: AlreadyExists
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
    BrandSettings:
      title: BrandSettings
      type: object
      properties:
        colors:
          $ref: '#/components/schemas/BrandColors'
          nullable: true
        email:
          $ref: '#/components/schemas/BrandSettingsEmail'
          nullable: true
        inapp:
          $ref: '#/components/schemas/BrandSettingsInApp'
          nullable: true
    BrandSnippets:
      title: BrandSnippets
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/BrandSnippet'
          nullable: true
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
    BrandColors:
      title: BrandColors
      type: object
      properties:
        primary:
          type: string
        secondary:
          type: string
      additionalProperties:
        type: string
    BrandSettingsEmail:
      title: BrandSettingsEmail
      type: object
      properties:
        templateOverride:
          $ref: '#/components/schemas/BrandTemplateOverride'
          nullable: true
        head:
          $ref: '#/components/schemas/EmailHead'
          nullable: true
        footer:
          $ref: '#/components/schemas/EmailFooter'
          nullable: true
        header:
          $ref: '#/components/schemas/EmailHeader'
          nullable: true
    BrandSettingsInApp:
      title: BrandSettingsInApp
      type: object
      properties:
        borderRadius:
          type: string
          nullable: true
        disableMessageIcon:
          type: boolean
          nullable: true
        fontFamily:
          type: string
          nullable: true
        placement:
          $ref: '#/components/schemas/InAppPlacement'
          nullable: true
        widgetBackground:
          $ref: '#/components/schemas/WidgetBackground'
        colors:
          $ref: '#/components/schemas/BrandColors'
        icons:
          $ref: '#/components/schemas/Icons'
      required:
        - widgetBackground
        - colors
        - icons
    BrandSnippet:
      title: BrandSnippet
      type: object
      properties:
        name:
          type: string
        value:
          type: string
      required:
        - name
        - value
    BrandTemplateOverride:
      title: BrandTemplateOverride
      type: object
      properties:
        mjml:
          $ref: '#/components/schemas/BrandTemplate'
        footerBackgroundColor:
          type: string
          nullable: true
        footerFullWidth:
          type: boolean
          nullable: true
      required:
        - mjml
      allOf:
        - $ref: '#/components/schemas/BrandTemplate'
    EmailHead:
      title: EmailHead
      type: object
      properties:
        inheritDefault:
          type: boolean
        content:
          type: string
          nullable: true
      required:
        - inheritDefault
    EmailFooter:
      title: EmailFooter
      type: object
      properties:
        content:
          type: string
          nullable: true
        inheritDefault:
          type: boolean
          nullable: true
    EmailHeader:
      title: EmailHeader
      type: object
      properties:
        inheritDefault:
          type: boolean
          nullable: true
        barColor:
          type: string
          nullable: true
        logo:
          $ref: '#/components/schemas/Logo'
      required:
        - logo
    InAppPlacement:
      title: InAppPlacement
      type: string
      enum:
        - top
        - bottom
        - left
        - right
    WidgetBackground:
      title: WidgetBackground
      type: object
      properties:
        topColor:
          type: string
          nullable: true
        bottomColor:
          type: string
          nullable: true
    Icons:
      title: Icons
      type: object
      properties:
        bell:
          type: string
          nullable: true
        message:
          type: string
          nullable: true
    BrandTemplate:
      title: BrandTemplate
      type: object
      properties:
        backgroundColor:
          type: string
          nullable: true
        blocksBackgroundColor:
          type: string
          nullable: true
        enabled:
          type: boolean
        footer:
          type: string
          nullable: true
        head:
          type: string
          nullable: true
        header:
          type: string
          nullable: true
        width:
          type: string
          nullable: true
      required:
        - enabled
    Logo:
      title: Logo
      type: object
      properties:
        href:
          type: string
          nullable: true
        image:
          type: string
          nullable: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````