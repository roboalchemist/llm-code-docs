# Source: https://polar.sh/docs/api-reference/oauth2/connect/authorize.md

# Authorize

## OpenAPI

````yaml get /v1/oauth2/authorize
paths:
  path: /v1/oauth2/authorize
  method: get
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: access token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                You can generate an **Organization Access Token** from your
                organization's settings.
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Oauth2.Authorize(ctx)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseOauth2Authorize != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.oauth2.authorize()

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar({
            accessToken: process.env["POLAR_ACCESS_TOKEN"] ?? "",
          });

          async function run() {
            const result = await polar.oauth2.authorize();

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();



          $response = $sdk->oauth2->authorize(

          );

          if ($response->responseOauth2Authorize !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              client:
                allOf:
                  - $ref: '#/components/schemas/OAuth2ClientPublic'
              sub_type:
                allOf:
                  - type: string
                    const: user
                    title: Sub Type
              sub:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AuthorizeUser'
                      - type: 'null'
              scopes:
                allOf:
                  - items:
                      $ref: '#/components/schemas/Scope'
                    type: array
                    title: Scopes
            title: AuthorizeResponseUser
            refIdentifier: '#/components/schemas/AuthorizeResponseUser'
            requiredProperties:
              - client
              - sub_type
              - sub
              - scopes
          - type: object
            properties:
              client:
                allOf:
                  - $ref: '#/components/schemas/OAuth2ClientPublic'
              sub_type:
                allOf:
                  - type: string
                    const: organization
                    title: Sub Type
              sub:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AuthorizeOrganization'
                      - type: 'null'
              scopes:
                allOf:
                  - items:
                      $ref: '#/components/schemas/Scope'
                    type: array
                    title: Scopes
              organizations:
                allOf:
                  - items:
                      $ref: '#/components/schemas/AuthorizeOrganization'
                    type: array
                    title: Organizations
            title: AuthorizeResponseOrganization
            refIdentifier: '#/components/schemas/AuthorizeResponseOrganization'
            requiredProperties:
              - client
              - sub_type
              - sub
              - scopes
              - organizations
        examples:
          example:
            value:
              client:
                created_at: '2023-11-07T05:31:56Z'
                modified_at: '2023-11-07T05:31:56Z'
                client_id: <string>
                client_name: <string>
                client_uri: <string>
                logo_uri: <string>
                tos_uri: <string>
                policy_uri: <string>
              sub_type: <string>
              sub:
                id: <string>
                email: jsmith@example.com
                avatar_url: <string>
              scopes:
                - openid
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas:
    AuthorizeOrganization:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
        slug:
          type: string
          title: Slug
        avatar_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Avatar Url
      type: object
      required:
        - id
        - slug
        - avatar_url
      title: AuthorizeOrganization
    AuthorizeUser:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
        email:
          type: string
          format: email
          title: Email
        avatar_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Avatar Url
      type: object
      required:
        - id
        - email
        - avatar_url
      title: AuthorizeUser
    OAuth2ClientPublic:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        client_id:
          type: string
          title: Client Id
        client_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Client Name
        client_uri:
          anyOf:
            - type: string
            - type: 'null'
          title: Client Uri
        logo_uri:
          anyOf:
            - type: string
            - type: 'null'
          title: Logo Uri
        tos_uri:
          anyOf:
            - type: string
            - type: 'null'
          title: Tos Uri
        policy_uri:
          anyOf:
            - type: string
            - type: 'null'
          title: Policy Uri
      type: object
      required:
        - created_at
        - modified_at
        - client_id
        - client_name
        - client_uri
        - logo_uri
        - tos_uri
        - policy_uri
      title: OAuth2ClientPublic
    Scope:
      type: string
      enum:
        - openid
        - profile
        - email
        - user:read
        - web:read
        - web:write
        - organizations:read
        - organizations:write
        - custom_fields:read
        - custom_fields:write
        - discounts:read
        - discounts:write
        - checkout_links:read
        - checkout_links:write
        - checkouts:read
        - checkouts:write
        - transactions:read
        - transactions:write
        - payouts:read
        - payouts:write
        - products:read
        - products:write
        - benefits:read
        - benefits:write
        - events:read
        - events:write
        - meters:read
        - meters:write
        - files:read
        - files:write
        - subscriptions:read
        - subscriptions:write
        - customers:read
        - customers:write
        - customer_meters:read
        - customer_sessions:write
        - customer_seats:read
        - customer_seats:write
        - orders:read
        - orders:write
        - refunds:read
        - refunds:write
        - payments:read
        - metrics:read
        - webhooks:read
        - webhooks:write
        - external_organizations:read
        - license_keys:read
        - license_keys:write
        - repositories:read
        - repositories:write
        - issues:read
        - issues:write
        - customer_portal:read
        - customer_portal:write
        - notifications:read
        - notifications:write
        - notification_recipients:read
        - notification_recipients:write
      title: Scope
      enumNames:
        benefits:read: Read benefits
        benefits:write: Create or modify benefits
        checkout_links:read: Read checkout links
        checkout_links:write: Create or modify checkout links
        checkouts:read: Read checkout sessions
        checkouts:write: Create or modify checkout sessions
        custom_fields:read: Read custom fields
        custom_fields:write: Create or modify custom fields
        customer_meters:read: Read customer meters
        customer_portal:read: Read your orders, subscriptions and benefits
        customer_portal:write: Create or modify your orders, subscriptions and benefits
        customer_seats:read: Read customer seats
        customer_seats:write: Create or modify customer seats
        customer_sessions:write: Create or modify customer sessions
        customers:read: Read customers
        customers:write: Create or modify customers
        discounts:read: Read discounts
        discounts:write: Create or modify discounts
        email: Read your email address
        events:read: Read events
        events:write: Create events
        external_organizations:read: Read external organizations
        files:read: Read file uploads
        files:write: Create or modify file uploads
        license_keys:read: Read license keys
        license_keys:write: Modify license keys
        meters:read: Read meters
        meters:write: Create or modify meters
        metrics:read: Read metrics
        notification_recipients:read: Read notification recipients
        notification_recipients:write: Create or modify notification recipients
        notifications:read: Read notifications
        notifications:write: Mark notifications as read
        openid: OpenID
        orders:read: Read orders made on your organizations
        orders:write: Modify orders made on your organizations
        organizations:read: Read your organizations
        organizations:write: Create or modify organizations
        payments:read: Read payments made on your organizations
        payouts:read: Read payouts
        payouts:write: Create or modify payouts
        products:read: Read products
        products:write: Create or modify products
        profile: Read your profile
        refunds:read: Read refunds made on your organizations
        refunds:write: Create or modify refunds
        subscriptions:read: Read subscriptions made on your organizations
        subscriptions:write: Create or modify subscriptions made on your organizations
        transactions:read: Read transactions
        transactions:write: Create or modify transactions
        user:read: User Read
        web:read: Web Read Access
        web:write: Web Write Access
        webhooks:read: Read webhooks
        webhooks:write: Create or modify webhooks

````