# Source: https://docs.zapier.com/powered-by-zapier/api-reference/zap-templates/get-zap-templates.md

# Get Zap Templates

> List popular Zap Templates using your app. See our List Zap Templates guide to get started.

## OpenAPI

````yaml https://api.zapier.com/schema get /v1/zap-templates
paths:
  path: /v1/zap-templates
  method: get
  servers:
    - url: https://api.zapier.com
  request:
    security:
      - title: ClientIDAuthentication
        parameters:
          query:
            ClientIDAuthentication:
              type: apiKey
              description: >-
                See our authentication documentation for how to find your Client
                ID
          header: {}
          cookie: {}
    parameters:
      path: {}
      query:
        apps:
          schema:
            - type: string
              description: >-
                A comma separated list of Zapier Apps to match Zap templates
                against. Note:

                - Your app will always be one of the apps in the template

                - The list will return Zap Templates with all the provided apps,
                not a subset
        limit:
          schema:
            - type: number
              description: '(Max: 100) Limit the number of Zap templates returned.'
              default: 5
        offset:
          schema:
            - type: number
              description: >-
                The number of Zap templates to skip before beginning to return
                the Zap templates. The default value is 0, which is the offset
                of the first item.
              default: 0
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/ZapTemplate'
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
                      advertisers pay to display brief advertisements, service
                      offerings, product listings, video content, and generate
                      mobile application installs within the Google ad network
                      to web users.
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
                      Slack is a platform for team communication: everything in
                      one place, instantly searchable, available wherever you
                      go. Offering instant messaging, document sharing and
                      knowledge search for modern teams.
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
                  A new Google Ads campaign can mean the start of your next
                  marketing push, but it can also mean the start of a ton of new
                  sales and service workflows. Zapier gives you a head start on
                  those projects by automatically posting a new message in Slack
                  to a specific channel you choose. Give your teams the heads up
                  they need before your new clients come rolling in!
                description_raw: >-
                  A new Google Ads campaign can mean the start of your next
                  marketing push, but it can also mean the start of a ton of new
                  sales and service workflows. Zapier gives you a head start on
                  those projects by automatically posting a new message in Slack
                  to a specific channel you choose. Give your teams the heads up
                  they need before your new clients come rolling in!
                url: >-
                  https://zapier.com/apps/google-ads/integrations/slack/51652/send-messages-to-slack-channels-whenever-new-google-ads-campaigns-launch?utm_medium=partner_api
                description: >
                  <p>A new Google Ads campaign can mean the start of your next
                  marketing push, but it can also mean the start of a ton of new
                  sales and service workflows. Zapier gives you a head start on
                  those projects by automatically posting a new message in Slack
                  to a specific channel you choose. Give your teams the heads up
                  they need before your new clients come rolling in!</p>
                create_url: https://api.zapier.com/v1/embed/google-ads/create/51652
                type: guided_zap
        description: ''
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Missing client_id in query parameters
        examples: {}
        description: Missing client_id in query parameters
    '403':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 403 Response
    '409':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 409 Response
    '429':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 429 Response
    '503':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 503 Response
  deprecated: false
  type: path
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
    ZapTemplateStatusEnum:
      enum:
        - draft
        - published
      type: string
      description: |-
        * `draft` - draft
        * `published` - published
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

````