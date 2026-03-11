# Source: https://www.courier.com/docs/api-reference/brands/delete-a-brand.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a brand

> Delete a brand by brand ID.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml delete /brands/{brand_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /brands/{brand_id}:
    delete:
      tags:
        - Brands
      summary: Delete a brand
      description: Delete a brand by brand ID.
      operationId: brands_delete
      parameters:
        - name: brand_id
          in: path
          description: A unique identifier associated with the brand you wish to retrieve.
          required: true
          schema:
            type: string
      responses:
        '204':
          description: ''
        '409':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Conflict'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            await client.brands.delete('brand_id');
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.brands.delete(
                "brand_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Brands.Delete(context.TODO(), \"brand_id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.brands.BrandDeleteParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    client.brands().delete("brand_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            result = courier.brands.delete("brand_id")

            puts(result)
components:
  schemas:
    Conflict:
      title: Conflict
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