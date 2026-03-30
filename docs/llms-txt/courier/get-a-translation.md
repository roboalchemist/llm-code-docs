# Source: https://www.courier.com/docs/api-reference/translations/get-a-translation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a translation

> Get translations by locale



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /translations/{domain}/{locale}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /translations/{domain}/{locale}:
    get:
      tags:
        - Translations
      summary: Get a translation
      description: Get translations by locale
      operationId: translations_get
      parameters:
        - name: domain
          in: path
          description: >-
            The domain you want to retrieve translations for. Only `default` is
            supported at the moment
          required: true
          schema:
            type: string
        - name: locale
          in: path
          description: The locale you want to retrieve the translations for
          required: true
          schema:
            type: string
      responses:
        '200':
          description: .po file translation content
          content:
            application/json:
              schema:
                type: string
        '404':
          description: ''
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


            const translation = await client.translations.retrieve('locale', {
            domain: 'domain' });


            console.log(translation);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            translation = client.translations.retrieve(
                locale="locale",
                domain="domain",
            )
            print(translation)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\ttranslation, err := client.Translations.Get(\n\t\tcontext.TODO(),\n\t\t\"locale\",\n\t\tcourier.TranslationGetParams{\n\t\t\tDomain: \"domain\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", translation)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.translations.TranslationRetrieveParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TranslationRetrieveParams params = TranslationRetrieveParams.builder()
                        .domain("domain")
                        .locale("locale")
                        .build();
                    String translation = client.translations().retrieve(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            translation = courier.translations.retrieve("locale", domain:
            "domain")


            puts(translation)
components:
  schemas:
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