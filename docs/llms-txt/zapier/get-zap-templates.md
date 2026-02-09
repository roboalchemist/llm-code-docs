# Source: https://docs.zapier.com/powered-by-zapier/api-reference/zap-templates/get-zap-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Zap Templates

> List popular Zap Templates using your app. See our List Zap Templates guide to get started.

This API is [rate limited](/powered-by-zapier/api-reference/rate-limiting).


## OpenAPI

````yaml https://api.zapier.com/schema get /v1/zap-templates
openapi: 3.1.0
info:
  title: Partner API
  version: 2024.11.0
  description: >

    ## Introduction


    The Partner API is the best tool for complete style control over a user's
    Zapier experience within your app.

    Essentially, it lets you customize how you present Zapier within your
    product without sacrificing your app's look,

    feel, and flow.


    Think of it as a native Zapier integration, helping you showcase your best
    Zapier-powered workflows where it's most

    helpful to your users (within the flow of your tool). You can customize
    styling, streamline Zap set-up for users,

    expose relevant Zap information, and more!


    With the Partner API, you can:


    - Get a list of all the apps available in Zapier's app directory so you can
    power your app directory and show your

    users all the integration possibilities with your Zapier integration.

    - Have complete style control over how you present Zap templates in your
    product. The Partner API gives you access

    to the raw Zap Template data so you can give your users access to your Zap
    template with your product's style, look

    and feel.

    - Get access to all your Zap templates and give your users the ability to
    search to quickly find the one they need.

    - Streamline Zap setup by pre-filling fields on behalf of your users.

    - Show users the Zaps they have set up from right within your product
    keeping them on your site longer and giving them

    complete confidence in their Zapier integration.

    - Embed our Zapier Editor to allow your users to create new Zaps and modify
    existing ones, without needing to leave

    your product.


    ## Authentication


    There are two ways to authenticate with the Partner API.


    1. Your application's `client_id` which you will receive once you are
    approved for access to the API

    (Client ID Authentication)

    2. A user's access token (Access Token Authentication).


    Which authentication method you should use depends on which endpoint(s) you
    are using.

    Review each endpoint's documentation to understand which parameters are
    required.


    > Note: while we do generate a `client_secret`, the type of grant we use
    (implicit) doesn't

    need it so it's not something we provide.'


    ## Learn more


    See the [Workflow API
    documentation](https://docs.zapier.com/partner-solutions/workflow-api/intro)
    for more information.
  contact:
    name: Zapier
    url: https://developer.zapier.com/contact
servers:
  - url: https://api.zapier.com
security: []
tags:
  - name: Accounts
    description: Refers to resources interacting with 'Accounts' associated resources
  - name: Actions
    description: Refers to resources interacting with 'Actions' associated resources
  - name: Apps
    description: Refers to resources interacting with 'Apps' associated resources
  - name: Authentications
    description: >-
      Refers to resources interacting with 'Authentications' associated
      resources
  - name: Categories
    description: Refers to resources interacting with 'Categories' associated resources
  - name: Experimental
    description: Refers to resources interacting with 'Experimental' associated resources
  - name: Inputs
    description: Refers to resources interacting with 'Inputs' associated resources
  - name: Outputs
    description: Refers to resources interacting with 'Outputs' associated resources
  - name: Zaps
    description: Refers to resources interacting with 'Zaps' associated resources
  - name: Zap Templates
    description: Refers to resources interacting with 'Zap Templates' associated resources
paths:
  /v1/zap-templates:
    get:
      tags:
        - Zap Templates
      summary: Get Zap Templates
      description: >-
        List popular Zap Templates using your app. See our List Zap Templates
        guide to get started.
      operationId: v1_zap_templates_list
      parameters:
        - in: query
          name: apps
          schema:
            type: string
          description: >-
            A comma separated list of Zapier Apps to match Zap templates
            against. Note:

            - Your app will always be one of the apps in the template

            - The list will return Zap Templates with all the provided apps, not
            a subset
          example: mailchimp
        - in: query
          name: limit
          schema:
            type: number
            default: 5
          description: '(Max: 100) Limit the number of Zap templates returned.'
        - in: query
          name: offset
          schema:
            type: number
            default: 0
          description: >-
            The number of Zap templates to skip before beginning to return the
            Zap templates. The default value is 0, which is the offset of the
            first item.
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ZapTemplate'
              examples:
                /v1/zap-templates:
                  value:
                    - id: 51652
                      steps:
                        - id: 1
                          uuid: b9df4eff-f311-44f9-ac54-2901f952c6ac
                          title: Google Ads
                          slug: google-ads
                          description: >-
                            Google Ads (formerly Google AdWords) is an online
                            advertising platform developed by Google, where
                            advertisers pay to display brief advertisements,
                            service offerings, product listings, video content,
                            and generate mobile application installs within the
                            Google ad network to web users.
                          image: >-
                            https://zapier-images.imgix.net/storage/services/4058ec8b47ad751cbd39bd686cf4eab7.png?auto=format%2Ccompress&ixlib=python-3.0.0&q=50
                          hex_color: 4285F4
                          images:
                            url_16x16: >-
                              https://zapier-images.imgix.net/storage/services/4058ec8b47ad751cbd39bd686cf4eab7.png?auto=format%2Ccompress&fit=crop&h=16&ixlib=python-3.0.0&q=50&w=16
                            url_32x32: >-
                              https://zapier-images.imgix.net/storage/services/4058ec8b47ad751cbd39bd686cf4eab7.png?auto=format%2Ccompress&fit=crop&h=32&ixlib=python-3.0.0&q=50&w=32
                            url_64x64: >-
                              https://zapier-images.imgix.net/storage/services/4058ec8b47ad751cbd39bd686cf4eab7.png?auto=format%2Ccompress&fit=crop&h=64&ixlib=python-3.0.0&q=50&w=64
                            url_128x128: >-
                              https://zapier-images.imgix.net/storage/services/4058ec8b47ad751cbd39bd686cf4eab7.png?auto=format%2Ccompress&fit=crop&h=128&ixlib=python-3.0.0&q=50&w=128
                          api: GoogleAdsCLIAPI@3.0.0
                          url: >-
                            https://zapier.com/apps/google-ads/integrations?utm_medium=partner_api
                          label: New Campaign
                        - id: 2
                          uuid: ca83afc5-ee9a-470d-b577-e7f8fd555b67
                          title: Slack
                          slug: slack
                          description: >-
                            Slack is a platform for team communication:
                            everything in one place, instantly searchable,
                            available wherever you go. Offering instant
                            messaging, document sharing and knowledge search for
                            modern teams.
                          image: >-
                            https://zapier-images.imgix.net/storage/services/6cf3f5a461feadfba7abc93c4c395b33_2.png?auto=format%2Ccompress&ixlib=python-3.0.0&q=50
                          hex_color: 510f4d
                          images:
                            url_16x16: >-
                              https://zapier-images.imgix.net/storage/services/6cf3f5a461feadfba7abc93c4c395b33_2.png?auto=format%2Ccompress&fit=crop&h=16&ixlib=python-3.0.0&q=50&w=16
                            url_32x32: >-
                              https://zapier-images.imgix.net/storage/services/6cf3f5a461feadfba7abc93c4c395b33_2.png?auto=format%2Ccompress&fit=crop&h=32&ixlib=python-3.0.0&q=50&w=32
                            url_64x64: >-
                              https://zapier-images.imgix.net/storage/services/6cf3f5a461feadfba7abc93c4c395b33_2.png?auto=format%2Ccompress&fit=crop&h=64&ixlib=python-3.0.0&q=50&w=64
                            url_128x128: >-
                              https://zapier-images.imgix.net/storage/services/6cf3f5a461feadfba7abc93c4c395b33_2.png?auto=format%2Ccompress&fit=crop&h=128&ixlib=python-3.0.0&q=50&w=128
                          api: SlackAPI
                          url: >-
                            https://zapier.com/apps/slack/integrations?utm_medium=partner_api
                          label: Send Channel Message
                      title: >-
                        Send messages to Slack channels whenever new Google Ads
                        campaigns launch
                      slug: >-
                        send-messages-to-slack-channels-whenever-new-google-ads-campaigns-launch
                      status: published
                      description_plain: >
                        A new Google Ads campaign can mean the start of your
                        next marketing push, but it can also mean the start of a
                        ton of new sales and service workflows. Zapier gives you
                        a head start on those projects by automatically posting
                        a new message in Slack to a specific channel you choose.
                        Give your teams the heads up they need before your new
                        clients come rolling in!
                      description_raw: >-
                        A new Google Ads campaign can mean the start of your
                        next marketing push, but it can also mean the start of a
                        ton of new sales and service workflows. Zapier gives you
                        a head start on those projects by automatically posting
                        a new message in Slack to a specific channel you choose.
                        Give your teams the heads up they need before your new
                        clients come rolling in!
                      url: >-
                        https://zapier.com/apps/google-ads/integrations/slack/51652/send-messages-to-slack-channels-whenever-new-google-ads-campaigns-launch?utm_medium=partner_api
                      description: >
                        <p>A new Google Ads campaign can mean the start of your
                        next marketing push, but it can also mean the start of a
                        ton of new sales and service workflows. Zapier gives you
                        a head start on those projects by automatically posting
                        a new message in Slack to a specific channel you choose.
                        Give your teams the heads up they need before your new
                        clients come rolling in!</p>
                      create_url: https://api.zapier.com/v1/embed/google-ads/create/51652
                      type: guided_zap
          description: ''
        '401':
          description: Missing client_id in query parameters
        '403':
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 403 Response
        '409':
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 409 Response
        '429':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 429 Response
        '503':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 503 Response
        '504':
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 504 Response
      security:
        - ClientIDAuthentication: []
components:
  schemas:
    ZapTemplate:
      type: object
      description: A Zap Template.
      properties:
        id:
          type: integer
          description: The numeric identifier of this Zap Template
        steps:
          type: array
          items:
            $ref: '#/components/schemas/ZapTemplateStep'
          readOnly: true
          description: The steps this Zap Template are composed of
        title:
          type: string
          description: The title of this Zap Template
        slug:
          type: string
          description: The shortened slug for this Zap Template
          pattern: ^[-a-zA-Z0-9_]+$
        status:
          allOf:
            - $ref: '#/components/schemas/ZapTemplateStatusEnum'
          description: |-
            The status of this Zap Template

            * `draft` - draft
            * `published` - published
        description_plain:
          type: string
          readOnly: true
          description: The plain (rendered) description for this Zap Template
        description_raw:
          type: string
          description: >-
            The raw description for this Zap Template. May include styling
            syntax intended to be rendered
        url:
          type: string
          format: uri
          readOnly: true
          description: The URL for this Zap Template
        description:
          type: string
          description: >-
            The HTML description for this Zap Template. Intended to be rendered
            in a browser
        create_url:
          type: string
          format: uri
          readOnly: true
          description: The URL to access to create a Zap from this Zap Template
        type:
          type: string
          readOnly: true
          default: guided_zap
          description: The type of this Zap Template
      required:
        - create_url
        - description
        - description_plain
        - description_raw
        - id
        - slug
        - status
        - steps
        - title
        - type
        - url
    ZapTemplateStep:
      type: object
      description: One step in a Zap Template.
      properties:
        id:
          type:
            - integer
            - 'null'
          readOnly: true
          description: The numeric identifier of this step, if specified
        uuid:
          type: string
          format: uuid
          description: UUID identifier of this step
        title:
          type: string
          description: The name of this step
        slug:
          type: string
          description: The shortened slug for this step
          pattern: ^[-a-zA-Z0-9_]+$
        description:
          type: string
          description: The description of this step
        image:
          type: string
          description: The image URL for this step
        hex_color:
          type: string
          description: The primary (hex) color for this step
        images:
          allOf:
            - $ref: '#/components/schemas/ZapTemplateStepImages'
          description: The images (at various sizes) for this step
        api:
          type: string
          readOnly: true
          description: The API used in this step
        url:
          type: string
          format: uri
          readOnly: true
          description: The URL for this step
        label:
          type:
            - string
            - 'null'
          readOnly: true
          description: The label for this step
      required:
        - api
        - description
        - hex_color
        - id
        - image
        - images
        - label
        - slug
        - title
        - url
        - uuid
    ZapTemplateStatusEnum:
      enum:
        - draft
        - published
      type: string
      description: |-
        * `draft` - draft
        * `published` - published
    ZapTemplateStepImages:
      type: object
      description: Images for a Zap Template at various sizes
      properties:
        url_16x16:
          type: string
          description: URL to 16x16 image for Zap Template
        url_32x32:
          type: string
          description: URL to 32x32 image for Zap Template
        url_64x64:
          type: string
          description: URL to 64x64 image for Zap Template
        url_128x128:
          type: string
          description: URL to 128x128 image for Zap Template
      required:
        - url_128x128
        - url_16x16
        - url_32x32
        - url_64x64
  securitySchemes:
    ClientIDAuthentication:
      type: apiKey
      in: query
      name: client_id
      description: See our authentication documentation for how to find your Client ID
      x-zapier-auth-scheme-exempt: true

````