# Source: https://www.courier.com/docs/api-reference/lists/restore-a-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Restore a list

> Restore a previously deleted list.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /lists/{list_id}/restore
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /lists/{list_id}/restore:
    put:
      tags:
        - Lists
      summary: Restore a list
      description: Restore a previously deleted list.
      operationId: lists_restore
      parameters:
        - name: list_id
          in: path
          description: A unique identifier representing the list you wish to retrieve.
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties: {}
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

            await client.lists.restore('list_id');
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            client.lists.restore(
                "list_id",
            )
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\terr := client.Lists.Restore(\n\t\tcontext.TODO(),\n\t\t\"list_id\",\n\t\tcourier.ListRestoreParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.core.JsonValue;
            import com.courier.models.lists.ListRestoreParams;
            import java.util.Map;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ListRestoreParams params = ListRestoreParams.builder()
                        .listId("list_id")
                        .body(JsonValue.from(<String, Object>Map.of()))
                        .build();
                    client.lists().restore(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            result = courier.lists.restore("list_id")

            puts(result)
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````