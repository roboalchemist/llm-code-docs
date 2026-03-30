# Source: https://www.courier.com/docs/api-reference/sent-messages/get-message-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get message history

> Fetch the array of events of a message you've previously sent.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /messages/{message_id}/history
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /messages/{message_id}/history:
    get:
      tags:
        - Sent Messages
      summary: Get message history
      description: Fetch the array of events of a message you've previously sent.
      operationId: messages_getHistory
      parameters:
        - name: message_id
          in: path
          description: A unique identifier representing the message ID
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: >-
            A supported Message History type that will filter the events
            returned.
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
                $ref: '#/components/schemas/MessageHistoryResponse'
        '400':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequest'
        '404':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MessageNotFound'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const response = await client.messages.history('message_id');

            console.log(response.results);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.messages.history(
                message_id="message_id",
            )
            print(response.results)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Messages.History(\n\t\tcontext.TODO(),\n\t\t\"message_id\",\n\t\tcourier.MessageHistoryParams{},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.Results)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.messages.MessageHistoryParams;
            import com.courier.models.messages.MessageHistoryResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    MessageHistoryResponse response = client.messages().history("message_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.messages.history("message_id")

            puts(response)
components:
  schemas:
    MessageHistoryResponse:
      title: MessageHistoryResponse
      type: object
      properties:
        results:
          type: array
          items:
            type: object
            additionalProperties: true
      required:
        - results
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
    MessageNotFound:
      title: MessageNotFound
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