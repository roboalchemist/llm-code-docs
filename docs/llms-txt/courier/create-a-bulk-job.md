# Source: https://www.courier.com/docs/api-reference/bulk/create-a-bulk-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a bulk job

> Creates a new bulk job for sending messages to multiple recipients.

**Required**: `message.event` (event ID or notification ID)

**Optional (V2 format)**: `message.template` (notification ID) or `message.content` (Elemental content) 
can be provided to override the notification associated with the event.




## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /bulk
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /bulk:
    post:
      tags:
        - Bulk
      summary: Create a bulk job
      description: >
        Creates a new bulk job for sending messages to multiple recipients.


        **Required**: `message.event` (event ID or notification ID)


        **Optional (V2 format)**: `message.template` (notification ID) or
        `message.content` (Elemental content) 

        can be provided to override the notification associated with the event.
      operationId: bulk_createJob
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  $ref: '#/components/schemas/InboundBulkMessage'
              required:
                - message
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BulkCreateJobResponse'
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
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const response = await client.bulk.createJob({ message: { event:
            'event' } });


            console.log(response.jobId);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.bulk.create_job(
                message={
                    "event": "event"
                },
            )
            print(response.job_id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Bulk.NewJob(context.TODO(), courier.BulkNewJobParams{\n\t\tMessage: courier.InboundBulkMessageParam{\n\t\t\tEvent: \"event\",\n\t\t},\n\t})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.JobID)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.bulk.BulkCreateJobParams;
            import com.courier.models.bulk.BulkCreateJobResponse;
            import com.courier.models.bulk.InboundBulkMessage;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    BulkCreateJobParams params = BulkCreateJobParams.builder()
                        .message(InboundBulkMessage.builder()
                            .event("event")
                            .build())
                        .build();
                    BulkCreateJobResponse response = client.bulk().createJob(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.bulk.create_job(message: {event: "event"})

            puts(response)
components:
  schemas:
    InboundBulkMessage:
      title: InboundBulkMessage
      type: object
      description: >
        Bulk message definition. Supports two formats:

        - V1 format: Requires `event` field (event ID or notification ID)

        - V2 format: Optionally use `template` (notification ID) or `content`
        (Elemental content) in addition to `event`
      properties:
        brand:
          type: string
          nullable: true
        data:
          type: object
          additionalProperties: true
          nullable: true
        event:
          type: string
          description: >
            Event ID or Notification ID (required). Can be either a 

            Notification ID (e.g., "FRH3QXM9E34W4RKP7MRC8NZ1T8V8") or a custom
            Event ID 

            (e.g., "welcome-email") mapped to a notification.
        template:
          type: string
          nullable: true
          description: >
            Notification ID or template ID (optional, for V2 format). When
            provided, 

            this will be used instead of the notification associated with the
            `event` field.
        content:
          $ref: '#/components/schemas/Content'
          nullable: true
          description: >
            Elemental content (optional, for V2 format). When provided, this
            will be used 

            instead of the notification associated with the `event` field.
        locale:
          type: object
          additionalProperties:
            type: object
            additionalProperties: true
          nullable: true
        override:
          type: object
          additionalProperties: true
          nullable: true
      required:
        - event
    BulkCreateJobResponse:
      title: BulkCreateJobResponse
      type: object
      properties:
        jobId:
          type: string
      required:
        - jobId
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
    Content:
      title: Content
      oneOf:
        - $ref: '#/components/schemas/ElementalContentSugar'
        - $ref: '#/components/schemas/ElementalContent'
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
    ElementalContentSugar:
      title: ElementalContentSugar
      type: object
      description: >-
        Syntactic sugar to provide a fast shorthand for Courier Elemental
        Blocks.
      properties:
        title:
          type: string
          description: Title/subject displayed by supported channels.
        body:
          type: string
          description: The text content displayed in the notification.
      required:
        - title
        - body
    ElementalContent:
      title: ElementalContent
      type: object
      properties:
        version:
          type: string
          description: For example, "2022-01-01"
        elements:
          type: array
          items:
            $ref: '#/components/schemas/ElementalNode'
      required:
        - version
        - elements
    ElementalNode:
      title: ElementalNode
      oneOf:
        - type: object
          allOf:
            - type: object
              properties:
                type:
                  type: string
                  enum:
                    - text
            - $ref: '#/components/schemas/ElementalTextNode'
          required:
            - type
        - type: object
          allOf:
            - type: object
              properties:
                type:
                  type: string
                  enum:
                    - meta
            - $ref: '#/components/schemas/ElementalMetaNode'
          required:
            - type
        - type: object
          allOf:
            - type: object
              properties:
                type:
                  type: string
                  enum:
                    - channel
            - $ref: '#/components/schemas/ElementalChannelNode'
          required:
            - type
            - channel
        - type: object
          allOf:
            - type: object
              properties:
                type:
                  type: string
                  enum:
                    - image
            - $ref: '#/components/schemas/ElementalImageNode'
          required:
            - type
        - type: object
          allOf:
            - type: object
              properties:
                type:
                  type: string
                  enum:
                    - action
            - $ref: '#/components/schemas/ElementalActionNode'
          required:
            - type
        - type: object
          allOf:
            - type: object
              properties:
                type:
                  type: string
                  enum:
                    - divider
            - $ref: '#/components/schemas/ElementalDividerNode'
          required:
            - type
        - type: object
          allOf:
            - type: object
              properties:
                type:
                  type: string
                  enum:
                    - quote
            - $ref: '#/components/schemas/ElementalQuoteNode'
          required:
            - type
    ElementalTextNode:
      title: ElementalTextNode
      type: object
      description: Represents a body of text to be rendered inside of the notification.
      properties:
        content:
          type: string
          description: |-
            The text content displayed in the notification. Either this
            field must be specified, or the elements field
        align:
          $ref: '#/components/schemas/TextAlign'
          description: Text alignment.
        text_style:
          $ref: '#/components/schemas/TextStyle'
          nullable: true
          description: Allows the text to be rendered as a heading level.
        color:
          type: string
          nullable: true
          description: Specifies the color of text. Can be any valid css color value
        bold:
          type: string
          nullable: true
          description: Apply bold to the text
        italic:
          type: string
          nullable: true
          description: Apply italics to the text
        strikethrough:
          type: string
          nullable: true
          description: Apply a strike through the text
        underline:
          type: string
          nullable: true
          description: Apply an underline to the text
        locales:
          $ref: '#/components/schemas/Locales'
          nullable: true
          description: >-
            Region specific content. See [locales
            docs](https://www.courier.com/docs/platform/content/elemental/locales/)
            for more details.
        format:
          type: string
          enum:
            - markdown
          nullable: true
      required:
        - content
        - align
      allOf:
        - $ref: '#/components/schemas/ElementalBaseNode'
    ElementalMetaNode:
      title: ElementalMetaNode
      type: object
      description: >-
        The meta element contains information describing the notification that
        may 

        be used by a particular channel or provider. One important field is the
        title 

        field which will be used as the title for channels that support it.
      properties:
        title:
          type: string
          nullable: true
          description: >-
            The title to be displayed by supported channels. For example, the
            email subject.
      allOf:
        - $ref: '#/components/schemas/ElementalBaseNode'
    ElementalChannelNode:
      title: ElementalChannelNode
      type: object
      description: >-
        The channel element allows a notification to be customized based on
        which channel it is sent through. 

        For example, you may want to display a detailed message when the
        notification is sent through email, 

        and a more concise message in a push notification. Channel elements are
        only valid as top-level 

        elements; you cannot nest channel elements. If there is a channel
        element specified at the top-level 

        of the document, all sibling elements must be channel elements.

        Note: As an alternative, most elements support a `channel` property.
        Which allows you to selectively 

        display an individual element on a per channel basis. See the 

        [control flow
        docs](https://www.courier.com/docs/platform/content/elemental/control-flow/)
        for more details.
      properties:
        channel:
          type: string
          example: email
          description: >-
            The channel the contents of this element should be applied to. Can
            be `email`,

            `push`, `direct_message`, `sms` or a provider such as slack
        raw:
          type: object
          additionalProperties: true
          nullable: true
          description: >-
            Raw data to apply to the channel. If `elements` has not been
            specified, `raw` is required.
      allOf:
        - $ref: '#/components/schemas/ElementalBaseNode'
    ElementalImageNode:
      title: ElementalImageNode
      type: object
      description: Used to embed an image into the notification.
      properties:
        src:
          type: string
          description: The source of the image.
        href:
          type: string
          nullable: true
          description: A URL to link to when the image is clicked.
        align:
          $ref: '#/components/schemas/IAlignment'
          nullable: true
          description: The alignment of the image.
        altText:
          type: string
          nullable: true
          description: Alternate text for the image.
        width:
          type: string
          nullable: true
          description: CSS width properties to apply to the image. For example, 50px
      required:
        - src
      allOf:
        - $ref: '#/components/schemas/ElementalBaseNode'
    ElementalActionNode:
      title: ElementalActionNode
      type: object
      description: Allows the user to execute an action. Can be a button or a link.
      properties:
        content:
          type: string
          description: The text content of the action shown to the user.
        href:
          type: string
          description: The target URL of the action.
        action_id:
          type: string
          nullable: true
          description: A unique id used to identify the action when it is executed.
        align:
          nullable: true
          description: The alignment of the action button. Defaults to "center".
          allOf:
            - $ref: '#/components/schemas/IAlignment'
        background_color:
          type: string
          nullable: true
          description: The background color of the action button.
        style:
          nullable: true
          description: Defaults to `button`.
          allOf:
            - $ref: '#/components/schemas/IActionButtonStyle'
        locales:
          description: >-
            Region specific content. See [locales
            docs](https://www.courier.com/docs/platform/content/elemental/locales/)
            for more details.
          allOf:
            - $ref: '#/components/schemas/Locales'
      required:
        - content
        - href
        - locales
      allOf:
        - $ref: '#/components/schemas/ElementalBaseNode'
    ElementalDividerNode:
      title: ElementalDividerNode
      type: object
      description: Renders a dividing line between elements.
      properties:
        color:
          type: string
          nullable: true
          description: The CSS color to render the line with. For example, `#fff`
      allOf:
        - $ref: '#/components/schemas/ElementalBaseNode'
    ElementalQuoteNode:
      title: ElementalQuoteNode
      type: object
      description: Renders a quote block.
      properties:
        content:
          type: string
          description: The text value of the quote.
        align:
          $ref: '#/components/schemas/IAlignment'
          nullable: true
          description: Alignment of the quote.
        borderColor:
          type: string
          nullable: true
          description: CSS border color property. For example, `#fff`
        text_style:
          $ref: '#/components/schemas/TextStyle'
        locales:
          $ref: '#/components/schemas/Locales'
          description: >-
            Region specific content. See [locales
            docs](https://www.courier.com/docs/platform/content/elemental/locales/)
            for more details.
      required:
        - content
        - text_style
        - locales
      allOf:
        - $ref: '#/components/schemas/ElementalBaseNode'
    TextAlign:
      title: TextAlign
      type: string
      enum:
        - left
        - center
        - right
    TextStyle:
      title: TextStyle
      type: string
      enum:
        - text
        - h1
        - h2
        - subtext
    Locales:
      title: Locales
      type: object
      additionalProperties:
        $ref: '#/components/schemas/Locale'
      nullable: true
    ElementalBaseNode:
      title: ElementalBaseNode
      type: object
      properties:
        channels:
          type: array
          items:
            type: string
          nullable: true
        ref:
          type: string
          nullable: true
        if:
          type: string
          nullable: true
        loop:
          type: string
          nullable: true
    IAlignment:
      title: IAlignment
      type: string
      enum:
        - center
        - left
        - right
        - full
    IActionButtonStyle:
      title: IActionButtonStyle
      type: string
      enum:
        - button
        - link
    Locale:
      title: Locale
      type: object
      properties:
        content:
          type: string
      required:
        - content
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````