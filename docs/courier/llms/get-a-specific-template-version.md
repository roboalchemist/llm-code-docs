# Source: https://www.courier.com/docs/api-reference/courier-create/get-a-specific-template-version.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a Specific Template Version

> Fetches a specific version of a tenant template.

Supports the following version formats:
- `latest` - The most recent version of the template
- `published` - The currently published version
- `v{version}` - A specific version (e.g., "v1", "v2", "v1.0.0")




## OpenAPI

````yaml openapi-specs/openapi.documented.yml get /tenants/{tenant_id}/templates/{template_id}/versions/{version}
openapi: 3.0.1
info:
  title: Courier
  version: 0.0.1
servers:
  - url: https://api.courier.com
    description: Production
security: []
paths:
  /tenants/{tenant_id}/templates/{template_id}/versions/{version}:
    get:
      tags:
        - Courier Create
      summary: Get a Specific Template Version
      description: |
        Fetches a specific version of a tenant template.

        Supports the following version formats:
        - `latest` - The most recent version of the template
        - `published` - The currently published version
        - `v{version}` - A specific version (e.g., "v1", "v2", "v1.0.0")
      operationId: tenants_getTemplateVersion
      parameters:
        - name: tenant_id
          in: path
          description: Id of the tenant for which to retrieve the template.
          required: true
          schema:
            type: string
        - name: template_id
          in: path
          description: Id of the template to be retrieved.
          required: true
          schema:
            type: string
        - name: version
          in: path
          description: >-
            Version of the template to retrieve. Accepts "latest", "published",
            or a specific version string (e.g., "v1", "v2").
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTemplateByTenantResponse'
        '400':
          description: Bad request - invalid version format
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequest'
        '404':
          description: Template, version, or tenant not found
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


            const baseTemplateTenantAssociation = await
            client.tenants.templates.versions.retrieve('version', {
              tenant_id: 'tenant_id',
              template_id: 'template_id',
            });


            console.log(baseTemplateTenantAssociation.id);
        - lang: Python
          source: >-
            import os

            from courier import Courier


            client = Courier(
                api_key=os.environ.get("COURIER_API_KEY"),  # This is the default and can be omitted
            )

            base_template_tenant_association =
            client.tenants.templates.versions.retrieve(
                version="version",
                tenant_id="tenant_id",
                template_id="template_id",
            )

            print(base_template_tenant_association.id)
        - lang: Go
          source: "package main\n\nimport (\n\t\"context\"\n\t\"fmt\"\n\n\t\"github.com/trycourier/courier-go\"\n\t\"github.com/trycourier/courier-go/option\"\n)\n\nfunc main() {\n\tclient := courier.NewClient(\n\t\toption.WithAPIKey(\"My API Key\"),\n\t)\n\tbaseTemplateTenantAssociation, err := client.Tenants.Templates.Versions.Get(\n\t\tcontext.TODO(),\n\t\t\"version\",\n\t\tcourier.TenantTemplateVersionGetParams{\n\t\t\tTenantID:   \"tenant_id\",\n\t\t\tTemplateID: \"template_id\",\n\t\t},\n\t)\n\tif err != nil {\n\t\tpanic(err.Error())\n\t}\n\tfmt.Printf(\"%+v\\n\", baseTemplateTenantAssociation.ID)\n}\n"
        - lang: Java
          source: >-
            package com.courier.example;


            import com.courier.client.CourierClient;

            import com.courier.client.okhttp.CourierOkHttpClient;

            import com.courier.models.tenants.BaseTemplateTenantAssociation;

            import
            com.courier.models.tenants.templates.versions.VersionRetrieveParams;


            public final class Main {
                private Main() {}

                public static void main(String[] args) {
                    CourierClient client = CourierOkHttpClient.fromEnv();

                    VersionRetrieveParams params = VersionRetrieveParams.builder()
                        .tenantId("tenant_id")
                        .templateId("template_id")
                        .version("version")
                        .build();
                    BaseTemplateTenantAssociation baseTemplateTenantAssociation = client.tenants().templates().versions().retrieve(params);
                }
            }
        - lang: Ruby
          source: >-
            require "courier"


            courier = Courier::Client.new(api_key: "My API Key")


            base_template_tenant_association =
            courier.tenants.templates.versions.retrieve("version", tenant_id:
            "tenant_id", template_id: "template_id")


            puts(base_template_tenant_association)
components:
  schemas:
    GetTemplateByTenantResponse:
      title: GetTemplateByTenantResponse
      type: object
      properties: {}
      allOf:
        - $ref: '#/components/schemas/SingleTemplateTenantAssociation'
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
    SingleTemplateTenantAssociation:
      title: SingleTemplateTenantAssociation
      type: object
      properties:
        data:
          $ref: '#/components/schemas/TenantTemplateData'
      required:
        - data
      allOf:
        - $ref: '#/components/schemas/BaseTemplateTenantAssociation'
    BaseError:
      title: BaseError
      type: object
      properties:
        message:
          type: string
          description: A message describing the error that occurred.
      required:
        - message
    TenantTemplateData:
      title: TenantTemplateData
      type: object
      description: >-
        The template's data containing it's routing configs and Elemental
        content
      properties:
        routing:
          $ref: '#/components/schemas/MessageRouting'
        content:
          $ref: '#/components/schemas/ElementalContent'
      required:
        - routing
        - content
    BaseTemplateTenantAssociation:
      title: BaseTemplateTenantAssociation
      type: object
      properties:
        id:
          type: string
          description: The template's id
        created_at:
          type: string
          description: The timestamp at which the template was created
        updated_at:
          type: string
          description: The timestamp at which the template was last updated
        published_at:
          type: string
          description: The timestamp at which the template was published
        version:
          type: string
          description: The version of the template
      required:
        - id
        - created_at
        - updated_at
        - published_at
        - version
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