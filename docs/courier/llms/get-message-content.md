# Source: https://www.courier.com/docs/api-reference/sent-messages/get-message-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get message content



## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /messages/{message_id}/output
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /messages/{message_id}/output:
    get:
      tags:
        - Sent Messages
      summary: Get message content
      operationId: messages_getContent
      parameters:
        - name: message_id
          in: path
          description: >-
            A unique identifier associated with the message you wish to retrieve
            (results from a send).
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RenderOutputResponse'
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

            const response = await client.messages.content('message_id');

            console.log(response.results);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.messages.content(
                "message_id",
            )
            print(response.results)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Messages.Content(context.TODO(), \"message_id\")\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.Results)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.messages.MessageContentParams;
            import com.courier.models.messages.MessageContentResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    MessageContentResponse response = client.messages().content("message_id");
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.messages.content("message_id")

            puts(response)
components:
  schemas:
    RenderOutputResponse:
      title: RenderOutputResponse
      type: object
      properties:
        results:
          type: array
          items:
            $ref: '#/components/schemas/RenderOutput'
          description: An array of render output of a previously sent message.
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
    RenderOutput:
      title: RenderOutput
      type: object
      properties:
        channel:
          type: string
          description: The channel used for rendering the message.
        channel_id:
          type: string
          description: The ID of channel used for rendering the message.
        content:
          $ref: '#/components/schemas/RenderedMessageContent'
          description: Content details of the rendered message.
      required:
        - channel
        - channel_id
        - content
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
    RenderedMessageContent:
      title: RenderedMessageContent
      type: object
      properties:
        html:
          type: string
          description: The html content of the rendered message.
        title:
          type: string
          description: The title of the rendered message.
        body:
          type: string
          description: The body of the rendered message.
        subject:
          type: string
          description: The subject of the rendered message.
        text:
          type: string
          description: The text of the rendered message.
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/RenderedMessageBlock'
          description: The blocks of the rendered message.
      required:
        - html
        - title
        - body
        - subject
        - text
        - blocks
    RenderedMessageBlock:
      title: RenderedMessageBlock
      type: object
      properties:
        type:
          type: string
          description: The block type of the rendered message block.
        text:
          type: string
          description: The block text of the rendered message block.
      required:
        - type
        - text
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````