# Source: https://www.courier.com/docs/api-reference/translations/update-translations-by-locale.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update translations by locale

> Update a translation



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /translations/{domain}/{locale}
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
    put:
      tags:
        - Translations
      summary: Update translations by locale
      description: Update a translation
      operationId: translations_update
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
      requestBody:
        description: .po file translation content
        required: true
        content:
          application/json:
            schema:
              type: string
      responses:
        '204':
          description: ''
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


            await client.translations.update('locale', { domain: 'domain', body:
            'body' });
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.translations.update(
                locale="locale",
                domain="domain",
                body="body",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Translations.Update(\n\t\tcontext.TODO(),\n\t\t\"locale\",\n\t\tcourier.TranslationUpdateParams{\n\t\t\tDomain: \"domain\",\n\t\t\tBody:   \"body\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.translations.TranslationUpdateParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TranslationUpdateParams params = TranslationUpdateParams.builder()
                        .domain("domain")
                        .locale("locale")
                        .body("body")
                        .build();
                    client.translations().update(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            result = courier.translations.update("locale", domain: "domain",
            body: "body")


            puts(result)
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