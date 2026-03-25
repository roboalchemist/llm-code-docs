# Source: https://www.courier.com/docs/api-reference/courier-create/create-or-update-a-tenant-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create or Update a Tenant Template

> Creates or updates a notification template for a tenant.

If the template already exists for the tenant, it will be updated (200).
Otherwise, a new template is created (201).

Optionally publishes the template immediately if the `published` flag is set to true.




## OpenAPI

````yaml openapi-specs/openapi.documented.yml put /tenants/{tenant_id}/templates/{template_id}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /tenants/{tenant_id}/templates/{template_id}:
    put:
      tags:
        - Courier Create
      summary: Create or Update a Tenant Template
      description: >
        Creates or updates a notification template for a tenant.


        If the template already exists for the tenant, it will be updated (200).

        Otherwise, a new template is created (201).


        Optionally publishes the template immediately if the `published` flag is
        set to true.
      operationId: tenants_replaceTemplate
      parameters:
        - name: tenant_id
          in: path
          description: Id of the tenant for which to create or update the template.
          required: true
          schema:
            type: string
        - name: template_id
          in: path
          description: Id of the template to be created or updated.
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PutTenantTemplateRequest'
      responses:
        '200':
          description: Template updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PutTenantTemplateResponse'
        '201':
          description: Template created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PutTenantTemplateResponse'
        '400':
          description: Bad request - validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequest'
        '404':
          description: Tenant not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFound'
        '413':
          description: Payload too large - template size exceeds maximum allowed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayloadTooLarge'
      security:
        - BearerAuth: []
      x-codeSamples:
        - lang: JavaScript
          source: >-
            import Courier from '@trycourier/courier';


            const client = new Courier({
              apiKey: process.env['COURIER_API_KEY'], // This is the default and can be omitted
            });


            const putTenantTemplateResponse = await
            client.tenants.templates.replace('template_id', {
              tenant_id: 'tenant_id',
              template: { content: { elements: [{}], version: 'version' } },
            });


            console.log(putTenantTemplateResponse.id);
        - lang: Python
          source: |-
            import os
            from courier import Courier

            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )
            put_tenant_template_response = client.tenants.templates.replace(
                template_id="template_id",
                tenant_id="tenant_id",
                template={
                    "content": {
                        "elements": [{}],
                        "version": "version",
                    }
                },
            )
            print(put_tenant_template_response.id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n\t\"github.com/trycourier/courier-go/shared\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tputTenantTemplateResponse, err := client.Tenants.Templates.Replace(\n\t\tcontext.TODO(),\n\t\t\"template_id\",\n\t\tcourier.TenantTemplateReplaceParams{\n\t\t\tTenantID: \"tenant_id\",\n\t\t\tPutTenantTemplateRequest: courier.PutTenantTemplateRequestParam{\n\t\t\t\tTemplate: courier.TenantTemplateInputParam{\n\t\t\t\t\tContent: shared.ElementalContentParam{\n\t\t\t\t\t\tElements: []shared.ElementalNodeUnionParam{{\n\t\t\t\t\t\t\tOfElementalTextNodeWithType: &shared.ElementalTextNodeWithTypeParam{\n\t\t\t\t\t\t\t\tElementalBaseNodeParam: shared.ElementalBaseNodeParam{},\n\t\t\t\t\t\t\t},\n\t\t\t\t\t\t}},\n\t\t\t\t\t\tVersion: \"version\",\n\t\t\t\t\t},\n\t\t\t\t},\n\t\t\t},\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", putTenantTemplateResponse.ID)\n}\n"
        - lang: Java
          source: |-
            package com.courier.example;

            import com.courier.client.CourierClient;
            import com.courier.client.okhttp.CourierOkHttpClient;
            import com.courier.models.ElementalContent;
            import com.courier.models.ElementalTextNodeWithType;
            import com.courier.models.tenants.PutTenantTemplateRequest;
            import com.courier.models.tenants.PutTenantTemplateResponse;
            import com.courier.models.tenants.TenantTemplateInput;
            import com.courier.models.tenants.templates.TemplateReplaceParams;

            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    TemplateReplaceParams params = TemplateReplaceParams.builder()
                        .tenantId("tenant_id")
                        .templateId("template_id")
                        .putTenantTemplateRequest(PutTenantTemplateRequest.builder()
                            .template(TenantTemplateInput.builder()
                                .content(ElementalContent.builder()
                                    .addElement(ElementalTextNodeWithType.builder().build())
                                    .version("version")
                                    .build())
                                .build())
                            .build())
                        .build();
                    PutTenantTemplateResponse putTenantTemplateResponse = client.tenants().templates().replace(params);
                }
            }
        - lang: Ruby
          source: |-
            require "courier"

            courier = Courier::Client.new(api_key: "My API Key")

            put_tenant_template_response = courier.tenants.templates.replace(
              "template_id",
              tenant_id: "tenant_id",
              template: {content: {elements: [{}], version: "version"}}
            )

            puts(put_tenant_template_response)
components:
  schemas:
    PutTenantTemplateRequest:
      title: PutTenantTemplateRequest
      type: object
      description: Request body for creating or updating a tenant notification template
      properties:
        published:
          type: boolean
          default: false
          description: >-
            Whether to publish the template immediately after saving. When true,
            the template becomes the active/published version. When false
            (default), the template is saved as a draft.
        template:
          $ref: '#/components/schemas/TenantTemplateInput'
      required:
        - template
    PutTenantTemplateResponse:
      title: PutTenantTemplateResponse
      type: object
      description: Response from creating or updating a tenant notification template
      properties:
        id:
          type: string
          description: The template ID
        version:
          type: string
          description: The version of the saved template
        published_at:
          type: string
          nullable: true
          description: >-
            The timestamp when the template was published. Only present if the
            template was published as part of this request.
      required:
        - id
        - version
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
    PayloadTooLarge:
      title: PayloadTooLarge
      type: object
      description: Error returned when the request payload exceeds the maximum allowed size
      properties:
        type:
          type: string
          enum:
            - invalid_request_error
      required:
        - type
      allOf:
        - $ref: '#/components/schemas/BaseError'
    TenantTemplateInput:
      title: TenantTemplateInput
      type: object
      description: >-
        Template configuration for creating or updating a tenant notification
        template
      properties:
        channels:
          $ref: '#/components/schemas/MessageChannels'
          description: Channel-specific delivery configuration (email, SMS, push, etc.)
        content:
          $ref: '#/components/schemas/ElementalContent'
          description: >-
            Template content configuration including blocks, elements, and
            message structure
        providers:
          $ref: '#/components/schemas/MessageProviders'
          description: >-
            Provider-specific delivery configuration for routing to specific
            email/SMS providers
        routing:
          $ref: '#/components/schemas/MessageRouting'
          description: Message routing configuration for multi-channel delivery strategies
      required:
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
    MessageChannels:
      title: MessageChannels
      type: object
      additionalProperties:
        $ref: '#/components/schemas/Channel'
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
    MessageProviders:
      title: MessageProviders
      type: object
      additionalProperties:
        $ref: '#/components/schemas/MessageProvidersType'
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
    MessageRoutingMethod:
      title: MessageRoutingMethod
      type: string
      enum:
        - all
        - single
    MessageRoutingChannel:
      title: MessageRoutingChannel
      oneOf:
        - type: string
        - $ref: '#/components/schemas/MessageRouting'
    RoutingMethod:
      title: RoutingMethod
      type: string
      enum:
        - all
        - single
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
    Metadata:
      title: Metadata
      type: object
      properties:
        utm:
          $ref: '#/components/schemas/UTM'
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