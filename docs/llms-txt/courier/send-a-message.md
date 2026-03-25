# Source: https://www.courier.com/docs/api-reference/send/send-a-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send a message

> Send a message to one or more recipients.



## OpenAPI

````yaml openapi-specs/openapi.documented.yml post /send
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /send:
    post:
      tags:
        - Send
      summary: Send a message
      description: Send a message to one or more recipients.
      operationId: send
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  $ref: '#/components/schemas/Message'
                  description: Defines the message to be delivered
              required:
                - message
            examples:
              Example1:
                summary: Send message with UserRecipient
                description: Default example using UserRecipient type
                value:
                  message:
                    to:
                      user_id: user_id
                    template: template_id
                    data:
                      foo: bar
              Example2:
                value:
                  message:
                    to:
                      email: user@example.com
                    template: template_id
                    data:
                      foo: bar
              Example3:
                value:
                  message:
                    to:
                      phone_number: '+1234567890'
                    template: template_id
                    data:
                      foo: bar
              Example4:
                value:
                  message:
                    to:
                      list_id: example_list
                    template: template_id
                    data:
                      foo: bar
              Example5:
                value:
                  message:
                    to:
                      user_id: example_user
                    content:
                      title: Hello {name}
                      body: How are you?
                    data:
                      name: Ben
                    routing:
                      method: single
                      channels:
                        - email
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SendMessageResponse'
              examples:
                Example1:
                  value:
                    requestId: 1-65f240a0-47a6a120c8374de9bcf9f22a
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: |-
            import Courier from '@trycourier/courier';

            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });

            const response = await client.send.message({
              message: {
                to: { user_id: 'user_id' },
                template: 'template_id',
                data: { foo: 'bar' },
              },
            });

            console.log(response.requestId);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            response = client.send.message(
                message={
                    "to": {
                        "user_id": "user_id"
                    },
                    "template": "template_id",
                    "data": {
                        "foo": "bar"
                    },
                },
            )
            print(response.request_id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n\t\"github.com/trycourier/courier-go/shared\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tresponse, err := client.Send.Message(context.TODO(), courier.SendMessageParams{\n\t\tMessage: courier.SendMessageParamsMessage{\n\t\t\tTo: courier.SendMessageParamsMessageToUnion{\n\t\t\t\tOfUserRecipient: &shared.UserRecipientParam{\n\t\t\t\t\tUserID: courier.String(\"user_id\"),\n\t\t\t\t},\n\t\t\t},\n\t\t\tTemplate: courier.String(\"template_id\"),\n\t\t\tData: map[string]any{\n\t\t\t\t\"foo\": \"bar\",\n\t\t\t},\n\t\t},\n\t})\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", response.RequestID)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.send.SendMessageParams;
            import com.courier.models.send.SendMessageResponse;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    SendMessageParams params = SendMessageParams.builder()
                        .message(SendMessageParams.Message.builder().build())
                        .build();
                    SendMessageResponse response = client.send().message(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            response = courier.send_.message(message: {})

            puts(response)
components:
  schemas:
    Message:
      title: Message
      oneOf:
        - $ref: '#/components/schemas/ContentMessage'
    SendMessageResponse:
      title: SendMessageResponse
      type: object
      properties:
        requestId:
          type: string
          description: >-
            A successful call to `POST /send` returns a `202` status code along
            with a `requestId` in the response body.

            For single-recipient requests, the `requestId` is the derived
            message_id. For multiple recipients, Courier assigns a unique
            message_id to each derived message.
          example: 1-65f240a0-47a6a120c8374de9bcf9f22c
      required:
        - requestId
    ContentMessage:
      title: ContentMessage
      type: object
      description: >-
        The message property has the following primary top-level properties.
        They define the destination and content of the message.
      properties:
        content:
          $ref: '#/components/schemas/Content'
          description: >-
            Describes content that will work for email, inbox, push, chat, or
            any channel id.
      allOf:
        - $ref: '#/components/schemas/BaseMessage'
        - $ref: '#/components/schemas/BaseMessageSendTo'
    Content:
      title: Content
      oneOf:
        - $ref: '#/components/schemas/ElementalContentSugar'
        - $ref: '#/components/schemas/ElementalContent'
    BaseMessage:
      title: BaseMessage
      type: object
      properties:
        template:
          type: string
          nullable: true
        data:
          $ref: '#/components/schemas/MessageData'
          nullable: true
        brand_id:
          type: string
          nullable: true
        channels:
          $ref: '#/components/schemas/MessageChannels'
          nullable: true
          description: >-
            Define run-time configuration for channels. Valid ChannelId's:
            email, sms, push, inbox, direct_message, banner, webhook.
        context:
          $ref: '#/components/schemas/MessageContext'
          nullable: true
        metadata:
          $ref: '#/components/schemas/MessageMetadata'
          nullable: true
        preferences:
          $ref: '#/components/schemas/MessagePreferences'
          nullable: true
        providers:
          $ref: '#/components/schemas/MessageProviders'
          nullable: true
        routing:
          $ref: '#/components/schemas/Routing'
          nullable: true
        timeout:
          $ref: '#/components/schemas/Timeout'
          nullable: true
        delay:
          $ref: '#/components/schemas/Delay'
          nullable: true
        expiry:
          $ref: '#/components/schemas/Expiry'
          nullable: true
    BaseMessageSendTo:
      title: BaseMessageSendTo
      type: object
      properties:
        to:
          $ref: '#/components/schemas/MessageRecipient'
          nullable: true
          description: The recipient or a list of recipients of the message
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
    MessageData:
      title: MessageData
      type: object
      additionalProperties: true
    MessageChannels:
      title: MessageChannels
      type: object
      additionalProperties:
        $ref: '#/components/schemas/Channel'
    MessageContext:
      title: MessageContext
      type: object
      properties:
        tenant_id:
          type: string
          nullable: true
          description: Tenant id used to load brand/default preferences/context.
    MessageMetadata:
      title: MessageMetadata
      type: object
      properties:
        event:
          type: string
          nullable: true
        tags:
          type: array
          items:
            type: string
          nullable: true
        utm:
          $ref: '#/components/schemas/UTM'
          nullable: true
        trace_id:
          type: string
          nullable: true
    MessagePreferences:
      title: MessagePreferences
      type: object
      properties:
        subscription_topic_id:
          type: string
          description: The subscription topic to apply to the message.
      required:
        - subscription_topic_id
    MessageProviders:
      title: MessageProviders
      type: object
      additionalProperties:
        $ref: '#/components/schemas/MessageProvidersType'
    Routing:
      title: Routing
      type: object
      description: >-
        Customize which channels/providers Courier may deliver the message
        through.
      properties:
        method:
          $ref: '#/components/schemas/RoutingMethod'
        channels:
          type: array
          items:
            $ref: '#/components/schemas/MessageRoutingChannel'
          description: A list of channels or providers (or nested routing rules).
      required:
        - method
        - channels
    Timeout:
      title: Timeout
      type: object
      properties:
        provider:
          type: object
          additionalProperties:
            type: integer
          nullable: true
        channel:
          type: object
          additionalProperties:
            type: integer
          nullable: true
        message:
          type: integer
          nullable: true
        escalation:
          type: integer
          nullable: true
        criteria:
          $ref: '#/components/schemas/Criteria'
          nullable: true
    Delay:
      title: Delay
      type: object
      properties:
        duration:
          type: integer
          nullable: true
          description: The duration of the delay in milliseconds.
        until:
          type: string
          nullable: true
          description: ISO 8601 timestamp or opening_hours-like format.
        timezone:
          type: string
          nullable: true
          description: >-
            IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Used
            when resolving opening hours expressions. Takes precedence over user
            profile timezone settings.
    Expiry:
      title: Expiry
      type: object
      properties:
        expires_at:
          type: string
          nullable: true
          description: Epoch or ISO8601 timestamp with timezone.
        expires_in:
          $ref: '#/components/schemas/ExpiresInType'
          description: Duration in ms or ISO8601 duration (e.g. P1DT4H).
      required:
        - expires_in
    MessageRecipient:
      title: MessageRecipient
      description: >-
        The recipient of a message. Can be a single recipient or an array of
        recipients.
      oneOf:
        - $ref: '#/components/schemas/Recipient'
        - type: array
          items:
            $ref: '#/components/schemas/Recipient'
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
    Channel:
      title: Channel
      type: object
      properties:
        brand_id:
          type: string
          nullable: true
          description: Brand id used for rendering.
        providers:
          type: array
          items:
            type: string
          nullable: true
          description: Providers enabled for this channel.
        routing_method:
          $ref: '#/components/schemas/RoutingMethod'
          nullable: true
          description: Defaults to `single`.
        if:
          type: string
          nullable: true
          description: JS conditional with access to data/profile.
        timeouts:
          $ref: '#/components/schemas/Timeouts'
          nullable: true
        override:
          type: object
          additionalProperties: true
          nullable: true
          description: Channel specific overrides.
        metadata:
          $ref: '#/components/schemas/ChannelMetadata'
          nullable: true
    UTM:
      title: UTM
      type: object
      properties:
        source:
          type: string
          nullable: true
        medium:
          type: string
          nullable: true
        campaign:
          type: string
          nullable: true
        term:
          type: string
          nullable: true
        content:
          type: string
          nullable: true
    MessageProvidersType:
      title: MessageProvidersType
      type: object
      properties:
        override:
          type: object
          additionalProperties: true
          nullable: true
          description: Provider-specific overrides.
        if:
          type: string
          nullable: true
          description: JS conditional with access to data/profile.
        timeouts:
          type: integer
          nullable: true
        metadata:
          $ref: '#/components/schemas/Metadata'
          nullable: true
    RoutingMethod:
      title: RoutingMethod
      type: string
      enum:
        - all
        - single
    MessageRoutingChannel:
      title: MessageRoutingChannel
      oneOf:
        - type: string
        - $ref: '#/components/schemas/MessageRouting'
    Criteria:
      title: Criteria
      type: string
      enum:
        - no-escalation
        - delivered
        - viewed
        - engaged
    ExpiresInType:
      title: ExpiresInType
      oneOf:
        - type: string
        - type: integer
    Recipient:
      title: Recipient
      description: >-
        A single recipient of the message. Choose one of the following types
        based on how you want to identify the recipient: - **User**: Send to a
        specific user by user_id, email, or phone number - **Audience**: Send to
        all users in an audience - **List**: Send to all users in a list -
        **List Pattern**: Send to users in lists matching a pattern - **Slack**:
        Send via Slack (channel, email, or user_id) - **MS Teams**: Send via
        Microsoft Teams - **PagerDuty**: Send via PagerDuty - **Webhook**: Send
        via webhook
      oneOf:
        - $ref: '#/components/schemas/UserRecipient'
        - $ref: '#/components/schemas/AudienceRecipient'
        - $ref: '#/components/schemas/ListRecipient'
        - $ref: '#/components/schemas/ListPatternRecipient'
        - $ref: '#/components/schemas/SlackRecipient'
        - $ref: '#/components/schemas/MsTeamsRecipient'
        - $ref: '#/components/schemas/PagerdutyRecipient'
        - $ref: '#/components/schemas/WebhookRecipient'
      discriminator:
        propertyName: _type
        mapping:
          user:
            $ref: '#/components/schemas/UserRecipient'
          audience:
            $ref: '#/components/schemas/AudienceRecipient'
          list:
            $ref: '#/components/schemas/ListRecipient'
          list_pattern:
            $ref: '#/components/schemas/ListPatternRecipient'
          slack:
            $ref: '#/components/schemas/SlackRecipient'
          ms_teams:
            $ref: '#/components/schemas/MsTeamsRecipient'
          pagerduty:
            $ref: '#/components/schemas/PagerdutyRecipient'
          webhook:
            $ref: '#/components/schemas/WebhookRecipient'
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
    Timeouts:
      title: Timeouts
      type: object
      properties:
        provider:
          type: integer
          nullable: true
        channel:
          type: integer
          nullable: true
    ChannelMetadata:
      title: ChannelMetadata
      type: object
      properties:
        utm:
          $ref: '#/components/schemas/UTM'
          nullable: true
    Metadata:
      title: Metadata
      type: object
      properties:
        utm:
          $ref: '#/components/schemas/UTM'
          nullable: true
    MessageRouting:
      title: MessageRouting
      type: object
      properties:
        method:
          $ref: '#/components/schemas/MessageRoutingMethod'
        channels:
          type: array
          items:
            $ref: '#/components/schemas/MessageRoutingChannel'
      required:
        - method
        - channels
    UserRecipient:
      title: User Recipient
      description: Send to a specific user by user_id, email, phone_number, or list_id
      type: object
      properties:
        user_id:
          type: string
          nullable: true
          description: >-
            The user's unique identifier. Typically, this will match the user id
            of a user in your system.
        account_id:
          type: string
          nullable: true
          description: Deprecated - Use `tenant_id` instead.
        context:
          $ref: '#/components/schemas/MessageContext'
          nullable: true
          description: Context such as tenant_id to send the notification with.
        data:
          $ref: '#/components/schemas/MessageData'
          nullable: true
        email:
          type: string
          nullable: true
          description: The user's email address.
        locale:
          type: string
          nullable: true
          description: The user's preferred ISO 639-1 language code.
        phone_number:
          type: string
          nullable: true
          description: The user's phone number.
        list_id:
          type: string
          nullable: true
          description: The id of the list to send the message to.
        preferences:
          $ref: '#/components/schemas/ProfilePreferences'
          nullable: true
        tenant_id:
          type: string
          nullable: true
          description: The id of the tenant the user is associated with.
      allOf:
        - $ref: '#/components/schemas/UserRecipientType'
    AudienceRecipient:
      title: Audience Recipient
      description: Send to all users in an audience
      type: object
      properties:
        audience_id:
          type: string
          description: >-
            A unique identifier associated with an Audience. A message will be
            sent to each user in the audience.
        data:
          $ref: '#/components/schemas/MessageData'
          nullable: true
        filters:
          type: array
          items:
            $ref: '#/components/schemas/AudienceFilter'
          nullable: true
      required:
        - audience_id
    ListRecipient:
      title: List Recipient
      description: Send to all users in a specific list
      type: object
      properties:
        list_id:
          type: string
          nullable: true
        data:
          $ref: '#/components/schemas/MessageData'
          nullable: true
        filters:
          type: array
          items:
            $ref: '#/components/schemas/ListFilter'
          nullable: true
    ListPatternRecipient:
      title: List Pattern Recipient
      description: Send to users in lists matching a pattern
      type: object
      properties:
        list_pattern:
          type: string
          nullable: true
        data:
          $ref: '#/components/schemas/MessageData'
          nullable: true
    SlackRecipient:
      title: Slack Recipient
      description: Send via Slack (channel, email, or user_id)
      type: object
      properties:
        slack:
          $ref: '#/components/schemas/Slack'
      required:
        - slack
    MsTeamsRecipient:
      title: MS Teams Recipient
      description: Send via Microsoft Teams
      type: object
      properties:
        ms_teams:
          $ref: '#/components/schemas/MsTeams'
      required:
        - ms_teams
    PagerdutyRecipient:
      title: PagerDuty Recipient
      description: Send via PagerDuty
      type: object
      properties:
        pagerduty:
          $ref: '#/components/schemas/Pagerduty'
      required:
        - pagerduty
    WebhookRecipient:
      title: Webhook Recipient
      description: Send via webhook
      type: object
      properties:
        webhook:
          $ref: '#/components/schemas/WebhookProfile'
      required:
        - webhook
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
    MessageRoutingMethod:
      title: MessageRoutingMethod
      type: string
      enum:
        - all
        - single
    ProfilePreferences:
      title: ProfilePreferences
      type: object
      properties:
        categories:
          $ref: '#/components/schemas/Preferences'
          nullable: true
        notifications:
          $ref: '#/components/schemas/Preferences'
        templateId:
          type: string
          nullable: true
      required:
        - notifications
    UserRecipientType:
      title: UserRecipientType
      type: object
      properties: {}
    AudienceFilter:
      title: AudienceFilter
      type: object
      properties:
        operator:
          type: string
          enum:
            - MEMBER_OF
          description: Send to users only if they are member of the account
        path:
          type: string
          enum:
            - account_id
        value:
          type: string
      required:
        - operator
        - path
        - value
    ListFilter:
      title: ListFilter
      type: object
      properties:
        operator:
          type: string
          enum:
            - MEMBER_OF
          description: Send to users only if they are member of the account
        path:
          type: string
          enum:
            - account_id
        value:
          type: string
      required:
        - operator
        - path
        - value
    Slack:
      title: Slack
      oneOf:
        - $ref: '#/components/schemas/SendToSlackChannel'
        - $ref: '#/components/schemas/SendToSlackEmail'
        - $ref: '#/components/schemas/SendToSlackUserId'
    MsTeams:
      title: MsTeams
      oneOf:
        - $ref: '#/components/schemas/SendToMsTeamsUserId'
        - $ref: '#/components/schemas/SendToMsTeamsEmail'
        - $ref: '#/components/schemas/SendToMsTeamsChannelId'
        - $ref: '#/components/schemas/SendToMsTeamsConversationId'
        - $ref: '#/components/schemas/SendToMsTeamsChannelName'
    Pagerduty:
      title: Pagerduty
      type: object
      properties:
        routing_key:
          type: string
          nullable: true
        event_action:
          type: string
          nullable: true
        severity:
          type: string
          nullable: true
        source:
          type: string
          nullable: true
    WebhookProfile:
      title: WebhookProfile
      type: object
      properties:
        url:
          type: string
          description: The URL to send the webhook request to.
        method:
          $ref: '#/components/schemas/WebhookMethod'
          nullable: true
          description: >-
            The HTTP method to use for the webhook request. Defaults to POST if
            not specified.
        headers:
          type: object
          additionalProperties:
            type: string
          nullable: true
          description: Custom headers to include in the webhook request.
        authentication:
          $ref: '#/components/schemas/WebhookAuthentication'
          nullable: true
          description: Authentication configuration for the webhook request.
        profile:
          $ref: '#/components/schemas/WebhookProfileType'
          nullable: true
          description: >-
            Specifies what profile information is included in the request
            payload. Defaults to 'limited' if not specified.
      required:
        - url
    Locale:
      title: Locale
      type: object
      properties:
        content:
          type: string
      required:
        - content
    Preferences:
      title: Preferences
      type: object
      additionalProperties:
        $ref: '#/components/schemas/Preference'
    SendToSlackChannel:
      title: SendToSlackChannel
      type: object
      properties:
        access_token:
          type: string
        channel:
          type: string
      required:
        - access_token
        - channel
    SendToSlackEmail:
      title: SendToSlackEmail
      type: object
      properties:
        access_token:
          type: string
        email:
          type: string
      required:
        - access_token
        - email
    SendToSlackUserId:
      title: SendToSlackUserId
      type: object
      properties:
        access_token:
          type: string
        user_id:
          type: string
      required:
        - access_token
        - user_id
    SendToMsTeamsUserId:
      title: SendToMsTeamsUserId
      type: object
      properties:
        tenant_id:
          type: string
        service_url:
          type: string
        user_id:
          type: string
      required:
        - tenant_id
        - service_url
        - user_id
    SendToMsTeamsEmail:
      title: SendToMsTeamsEmail
      type: object
      properties:
        tenant_id:
          type: string
        service_url:
          type: string
        email:
          type: string
      required:
        - tenant_id
        - service_url
        - email
    SendToMsTeamsChannelId:
      title: SendToMsTeamsChannelId
      type: object
      properties:
        tenant_id:
          type: string
        service_url:
          type: string
        channel_id:
          type: string
      required:
        - tenant_id
        - service_url
        - channel_id
    SendToMsTeamsConversationId:
      title: SendToMsTeamsConversationId
      type: object
      properties:
        tenant_id:
          type: string
        service_url:
          type: string
        conversation_id:
          type: string
      required:
        - tenant_id
        - service_url
        - conversation_id
    SendToMsTeamsChannelName:
      title: SendToMsTeamsChannelName
      type: object
      properties:
        tenant_id:
          type: string
        service_url:
          type: string
        channel_name:
          type: string
        team_id:
          type: string
      required:
        - tenant_id
        - service_url
        - channel_name
        - team_id
    WebhookMethod:
      title: WebhookMethod
      type: string
      enum:
        - POST
        - PUT
    WebhookAuthentication:
      title: WebhookAuthentication
      type: object
      properties:
        mode:
          $ref: '#/components/schemas/WebhookAuthMode'
          description: The authentication mode to use. Defaults to 'none' if not specified.
        username:
          type: string
          nullable: true
          description: Username for basic authentication.
        password:
          type: string
          nullable: true
          description: Password for basic authentication.
        token:
          type: string
          nullable: true
          description: Token for bearer authentication.
      required:
        - mode
    WebhookProfileType:
      title: WebhookProfileType
      type: string
      enum:
        - limited
        - expanded
    Preference:
      title: Preference
      type: object
      properties:
        status:
          $ref: '#/components/schemas/PreferenceStatus'
        rules:
          type: array
          items:
            $ref: '#/components/schemas/Rule'
          nullable: true
        channel_preferences:
          type: array
          items:
            $ref: '#/components/schemas/ChannelPreference'
          nullable: true
        source:
          $ref: '#/components/schemas/ChannelSource'
          nullable: true
      required:
        - status
    WebhookAuthMode:
      title: WebhookAuthMode
      type: string
      enum:
        - none
        - basic
        - bearer
    PreferenceStatus:
      title: PreferenceStatus
      type: string
      enum:
        - OPTED_IN
        - OPTED_OUT
        - REQUIRED
    Rule:
      title: Rule
      type: object
      properties:
        start:
          type: string
          nullable: true
        until:
          type: string
      required:
        - until
    ChannelPreference:
      title: ChannelPreference
      type: object
      properties:
        channel:
          $ref: '#/components/schemas/ChannelClassification'
      required:
        - channel
    ChannelSource:
      title: ChannelSource
      type: string
      enum:
        - subscription
        - list
        - recipient
    ChannelClassification:
      title: ChannelClassification
      type: string
      enum:
        - direct_message
        - email
        - push
        - sms
        - webhook
        - inbox
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````