# Source: https://www.courier.com/docs/api-reference/lists/get-all-lists.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all lists

> Returns all of the lists, with the ability to filter based on a pattern.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /lists
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /lists:
    get:
      tags:
        - Lists
      summary: Get all lists
      description: Returns all of the lists, with the ability to filter based on a pattern.
      operationId: lists_list
      parameters:
        - name: cursor
          in: query
          description: A unique identifier that allows for fetching the next page of lists.
          required: false
          schema:
            type: string
            nullable: true
        - name: pattern
          in: query
          description: >-
            "A pattern used to filter the list items returned. Pattern types
            supported: exact match on `list_id` or a pattern of one or more
            pattern parts. you may replace a part with either: `*` to match all
            parts in that position, or `**` to signify a wildcard `endsWith`
            pattern match."
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
                $ref: '#/components/schemas/ListGetAllResponse'
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

            const lists = await client.lists.list();

            console.log(lists.items);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            lists = client.lists.list()
            print(lists.items)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tlists, err := client.Lists.List(context.TODO(), courier.ListListParams{})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", lists.Items)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.lists.ListListParams;
            import com.courier.models.lists.ListListResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    ListListResponse lists = client.lists().list();
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            lists = courier.lists.list

            puts(lists)
components:
  schemas:
    ListGetAllResponse:
      title: ListGetAllResponse
      type: object
      properties:
        paging:
          $ref: '#/components/schemas/Paging'
        items:
          type: array
          items:
            $ref: '#/components/schemas/SubscriptionList'
      required:
        - paging
        - items
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
    SubscriptionList:
      title: SubscriptionList
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        created:
          type: string
          nullable: true
        updated:
          type: string
          nullable: true
      required:
        - id
        - name
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