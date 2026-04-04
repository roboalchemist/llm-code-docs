# Source: https://www.courier.com/docs/api-reference/brands/list-brands.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List brands

> Get the list of brands.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /brands
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
    get:
      tags:
        - Brands
      summary: List brands
      description: Get the list of brands.
      operationId: brands_list
      parameters:
        - name: cursor
          in: query
          description: A unique identifier that allows for fetching the next set of brands.
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
                $ref: '#/components/schemas/BrandsResponse'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const brands = await client.brands.list();

            console.log(brands.paging);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            brands = client.brands.list()
            print(brands.paging)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tbrands, err := client.Brands.List(context.TODO(), courier.BrandListParams{})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", brands.Paging)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.brands.BrandListParams;
            import com.courier.models.brands.BrandListResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    BrandListResponse brands = client.brands().list();
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            brands = courier.brands.list

            puts(brands)
components:
  schemas:
    BrandsResponse:
      title: BrandsResponse
      type: object
      properties:
        paging:
          $ref: '#/components/schemas/Paging'
        results:
          type: array
          items:
            $ref: '#/components/schemas/Brand'
      required:
        - paging
        - results
    Paging:
      title: Paging
      type: object
      properties:
        cursor:
          type: string
          nullable: true
        more:
          type: boolean
      required:
        - more
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