# Source: https://www.courier.com/docs/api-reference/sent-messages/archive-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Archive message



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /requests/{request_id}/archive
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /requests/{request_id}/archive:
    put:
      tags:
        - Sent Messages
      summary: Archive message
      operationId: messages_archive
      parameters:
        - name: request_id
          in: path
          description: A unique identifier representing the request ID
          required: true
          schema:
            type: string
      responses:
        '204':
          description: ''
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            await client.requests.archive('request_id');
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.requests.archive(
                "request_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Requests.Archive(context.TODO(), \"request_id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.requests.RequestArchiveParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    client.requests().archive("request_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            result = courier.requests.archive("request_id")

            puts(result)
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````