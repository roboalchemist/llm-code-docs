# Source: https://dub.co/docs/api-reference/endpoint/create-a-partner.md

# Create or update a partner

> Creates or updates a partner record (upsert behavior). If a partner with the same email already exists, their program enrollment will be updated with the provided tenantId. If no existing partner is found, a new partner will be created using the supplied information.

## OpenAPI

````yaml post /partners
paths:
  path: /partners
  method: post
  servers:
    - url: https://api.dub.co
      description: Production API
  request:
    security:
      - title: token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 100
                    description: >-
                      The partner's full name. If undefined, the partner's email
                      will be used in lieu of their name (e.g. `john@acme.com`)
              email:
                allOf:
                  - type: string
                    format: email
                    minLength: 1
                    maxLength: 190
                    description: >-
                      The partner's email address. Partners will be able to
                      claim their profile by signing up at `partners.dub.co`
                      with this email.
              username:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 100
                    description: >-
                      The partner's unique username in your system (max 100
                      characters). This will be used to create a short link for
                      the partner using your program's default domain. If not
                      provided, Dub will try to generate a username from the
                      partner's name or email.
              image:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The partner's avatar image. If not provided, a default
                      avatar will be used.
              tenantId:
                allOf:
                  - type: string
                    description: >-
                      The partner's unique ID in your system. Useful for
                      retrieving the partner's links and stats later on. If not
                      provided, the partner will be created as a standalone
                      partner.
              groupId:
                allOf:
                  - type: string
                    description: >-
                      The group ID to add the partner to. If not provided, the
                      partner will be added to the default group.
              country:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The partner's country of residence. Must be passed as a
                      2-letter ISO 3166-1 country code. See https://d.to/geo for
                      more information.
              description:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 5000
                    description: >-
                      A brief description of the partner and their background.
                      Max 5,000 characters.
              linkProps:
                allOf:
                  - type: object
                    properties:
                      keyLength:
                        type: number
                        minimum: 3
                        maximum: 190
                        description: >-
                          The length of the short link slug. Defaults to 7 if
                          not provided. When used with `prefix`, the total
                          length of the key will be `prefix.length + keyLength`.
                      externalId:
                        type: string
                        nullable: true
                        minLength: 1
                        maxLength: 255
                        description: >-
                          The ID of the link in your database. If set, it can be
                          used to identify the link in future API requests (must
                          be prefixed with 'ext_' when passed as a query
                          parameter). This key is unique across your workspace.
                        example: '123456'
                      tenantId:
                        type: string
                        nullable: true
                        maxLength: 255
                        description: >-
                          The ID of the tenant that created the link inside your
                          system. If set, it can be used to fetch all links for
                          a tenant.
                      prefix:
                        type: string
                        description: >-
                          The prefix of the short link slug for
                          randomly-generated keys (e.g. if prefix is `/c/`,
                          generated keys will be in the `/c/:key` format). Will
                          be ignored if `key` is provided.
                      archived:
                        type: boolean
                        description: >-
                          Whether the short link is archived. Defaults to
                          `false` if not provided.
                      tagIds:
                        anyOf:
                          - type: string
                          - type: array
                            items:
                              type: string
                        description: The unique IDs of the tags assigned to the short link.
                        example:
                          - clux0rgak00011...
                      tagNames:
                        anyOf:
                          - type: string
                          - type: array
                            items:
                              type: string
                        description: >-
                          The unique name of the tags assigned to the short link
                          (case insensitive).
                      folderId:
                        type: string
                        nullable: true
                        description: >-
                          The unique ID existing folder to assign the short link
                          to.
                      comments:
                        type: string
                        nullable: true
                        description: The comments for the short link.
                      expiresAt:
                        type: string
                        nullable: true
                        description: The date and time when the short link will expire at.
                      expiredUrl:
                        type: string
                        nullable: true
                        maxLength: 32000
                        description: >-
                          The URL to redirect to when the short link has
                          expired.
                      password:
                        type: string
                        nullable: true
                        description: >-
                          The password required to access the destination URL of
                          the short link.
                      proxy:
                        type: boolean
                        description: >-
                          Whether the short link uses Custom Link Previews
                          feature. Defaults to `false` if not provided.
                      title:
                        type: string
                        nullable: true
                        description: >-
                          The custom link preview title (og:title). Will be used
                          for Custom Link Previews if `proxy` is true. Learn
                          more: https://d.to/og
                      description:
                        type: string
                        nullable: true
                        description: >-
                          The custom link preview description (og:description).
                          Will be used for Custom Link Previews if `proxy` is
                          true. Learn more: https://d.to/og
                      image:
                        type: string
                        nullable: true
                        description: >-
                          The custom link preview image (og:image). Will be used
                          for Custom Link Previews if `proxy` is true. Learn
                          more: https://d.to/og
                      video:
                        type: string
                        nullable: true
                        description: >-
                          The custom link preview video (og:video). Will be used
                          for Custom Link Previews if `proxy` is true. Learn
                          more: https://d.to/og
                      rewrite:
                        type: boolean
                        description: >-
                          Whether the short link uses link cloaking. Defaults to
                          `false` if not provided.
                      ios:
                        type: string
                        nullable: true
                        maxLength: 32000
                        description: >-
                          The iOS destination URL for the short link for iOS
                          device targeting.
                      android:
                        type: string
                        nullable: true
                        maxLength: 32000
                        description: >-
                          The Android destination URL for the short link for
                          Android device targeting.
                      doIndex:
                        type: boolean
                        description: >-
                          Allow search engines to index your short link.
                          Defaults to `false` if not provided. Learn more:
                          https://d.to/noindex
                      utm_source:
                        type: string
                        nullable: true
                        description: >-
                          The UTM source of the short link. If set, this will
                          populate or override the UTM source in the destination
                          URL.
                      utm_medium:
                        type: string
                        nullable: true
                        description: >-
                          The UTM medium of the short link. If set, this will
                          populate or override the UTM medium in the destination
                          URL.
                      utm_campaign:
                        type: string
                        nullable: true
                        description: >-
                          The UTM campaign of the short link. If set, this will
                          populate or override the UTM campaign in the
                          destination URL.
                      utm_term:
                        type: string
                        nullable: true
                        description: >-
                          The UTM term of the short link. If set, this will
                          populate or override the UTM term in the destination
                          URL.
                      utm_content:
                        type: string
                        nullable: true
                        description: >-
                          The UTM content of the short link. If set, this will
                          populate or override the UTM content in the
                          destination URL.
                      ref:
                        type: string
                        nullable: true
                        description: >-
                          The referral tag of the short link. If set, this will
                          populate or override the `ref` query parameter in the
                          destination URL.
                      testVariants:
                        type: array
                        nullable: true
                        items:
                          type: object
                          properties:
                            url:
                              type: string
                            percentage:
                              type: number
                              minimum: 10
                              maximum: 90
                          required:
                            - url
                            - percentage
                        minItems: 2
                        maxItems: 4
                        description: >-
                          An array of A/B test URLs and the percentage of
                          traffic to send to each URL.
                        example:
                          - url: https://example.com/variant-1
                            percentage: 50
                          - url: https://example.com/variant-2
                            percentage: 50
                      testStartedAt:
                        type: string
                        nullable: true
                        description: The date and time when the tests started.
                      testCompletedAt:
                        type: string
                        nullable: true
                        description: >-
                          The date and time when the tests were or will be
                          completed.
                    description: >-
                      Additional properties that you can pass to the partner's
                      short link. Will be used to override the default link
                      properties for this partner.
            requiredProperties:
              - email
        examples:
          example:
            value:
              name: <string>
              email: jsmith@example.com
              username: <string>
              image: <string>
              tenantId: <string>
              groupId: <string>
              country: <string>
              description: <string>
              linkProps:
                keyLength: 96.5
                externalId: '123456'
                tenantId: <string>
                prefix: <string>
                archived: true
                tagIds:
                  - clux0rgak00011...
                tagNames: <string>
                folderId: <string>
                comments: <string>
                expiresAt: <string>
                expiredUrl: <string>
                password: <string>
                proxy: true
                title: <string>
                description: <string>
                image: <string>
                video: <string>
                rewrite: true
                ios: <string>
                android: <string>
                doIndex: true
                utm_source: <string>
                utm_medium: <string>
                utm_campaign: <string>
                utm_term: <string>
                utm_content: <string>
                ref: <string>
                testVariants:
                  - url: https://example.com/variant-1
                    percentage: 50
                  - url: https://example.com/variant-2
                    percentage: 50
                testStartedAt: <string>
                testCompletedAt: <string>
    codeSamples:
      - label: createPartner
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.partners.create(request={
                  "email": "Summer50@yahoo.com",
                  "link_props": {
                      "external_id": "123456",
                      "tag_ids": [
                          "clux0rgak00011...",
                      ],
                      "test_variants": [
                          {
                              "url": "https://example.com/variant-1",
                              "percentage": 50,
                          },
                          {
                              "url": "https://example.com/variant-2",
                              "percentage": 50,
                          },
                      ],
                  },
              })

              assert res is not None

              # Handle response
              print(res)
      - label: createPartner
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Dub;
          use Dub\Models\Operations;

          $sdk = Dub\Dub::builder()
              ->setSecurity(
                  'DUB_API_KEY'
              )
              ->build();

          $request = new Operations\CreatePartnerRequestBody(
              email: 'Summer50@yahoo.com',
              linkProps: new Operations\LinkProps(
                  externalId: '123456',
                  tagIds: [
                      'clux0rgak00011...',
                  ],
                  testVariants: [
                      new Operations\CreatePartnerTestVariants(
                          url: 'https://example.com/variant-1',
                          percentage: 50,
                      ),
                      new Operations\CreatePartnerTestVariants(
                          url: 'https://example.com/variant-2',
                          percentage: 50,
                      ),
                  ],
              ),
          );

          $response = $sdk->partners->create(
              request: $request
          );

          if ($response->object !== null) {
              // handle response
          }
      - label: createPartner
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Partners.Create(ctx, &operations.CreatePartnerRequestBody{\n        Email: \"Summer50@yahoo.com\",\n        LinkProps: &operations.LinkProps{\n            ExternalID: dubgo.Pointer(\"123456\"),\n            TagIds: dubgo.Pointer(operations.CreateCreatePartnerTagIdsArrayOfStr(\n                []string{\n                    \"clux0rgak00011...\",\n                },\n            )),\n            TestVariants: []operations.CreatePartnerTestVariants{\n                operations.CreatePartnerTestVariants{\n                    URL: \"https://example.com/variant-1\",\n                    Percentage: 50,\n                },\n                operations.CreatePartnerTestVariants{\n                    URL: \"https://example.com/variant-2\",\n                    Percentage: 50,\n                },\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: createPartner
        lang: ruby
        source: |-
          require 'dub'

          Models = ::OpenApiSDK::Models
          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          req = Models::Operations::CreatePartnerRequestBody.new(
            email: 'Summer50@yahoo.com',
            link_props: Models::Operations::LinkProps.new(
              external_id: '123456',
              tag_ids: [
                'clux0rgak00011...',
              ],
              test_variants: [
                Models::Operations::CreatePartnerTestVariants.new(
                  url: 'https://example.com/variant-1',
                  percentage: 50.0,
                ),
                Models::Operations::CreatePartnerTestVariants.new(
                  url: 'https://example.com/variant-2',
                  percentage: 50.0,
                ),
              ],
            ),
          )

          res = s.partners.create(request: req)

          unless res.nil?
            # handle response
          end
      - label: createPartner
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.partners.create();

            console.log(result);
          }

          run();
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The partner's unique ID on Dub.
              name:
                allOf:
                  - type: string
                    maxLength: 190
                    description: The partner's full legal name.
              companyName:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 190
                    description: >-
                      If the partner profile type is a company, this is the
                      partner's legal company name.
              email:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 190
                    description: >-
                      The partner's email address. Should be a unique value
                      across Dub.
              image:
                allOf:
                  - type: string
                    nullable: true
                    description: The partner's avatar image.
              description:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 5000
                    description: A brief description of the partner and their background.
              country:
                allOf:
                  - type: string
                    nullable: true
                    description: The partner's country (required for tax purposes).
              paypalEmail:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The partner's PayPal email (for receiving payouts via
                      PayPal).
              stripeConnectId:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The partner's Stripe Connect ID (for receiving payouts via
                      Stripe).
              payoutsEnabledAt:
                allOf:
                  - type: string
                    nullable: true
                    description: The date when the partner enabled payouts.
              programId:
                allOf:
                  - type: string
                    description: The program's unique ID on Dub.
              groupId:
                allOf:
                  - type: string
                    nullable: true
                    description: The partner's group ID on Dub.
              partnerId:
                allOf:
                  - type: string
                    description: The partner's unique ID on Dub.
              tenantId:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The partner's unique ID within your database. Can be
                      useful for associating the partner with a user in your
                      database and retrieving/update their data in the future.
              createdAt:
                allOf:
                  - type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - pending
                      - approved
                      - rejected
                      - invited
                      - declined
                      - deactivated
                      - banned
                      - archived
                    description: The status of the partner's enrollment in the program.
              links:
                allOf:
                  - type: array
                    nullable: true
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: The unique ID of the short link.
                        domain:
                          type: string
                          description: >-
                            The domain of the short link. If not provided, the
                            primary domain for the workspace will be used (or
                            `dub.sh` if the workspace has no domains).
                        key:
                          type: string
                          description: >-
                            The short link slug. If not provided, a random
                            7-character slug will be generated.
                        shortLink:
                          type: string
                          format: uri
                          description: >-
                            The full URL of the short link, including the https
                            protocol (e.g. `https://dub.sh/try`).
                        url:
                          type: string
                          format: uri
                          description: The destination URL of the short link.
                        clicks:
                          type: number
                          default: 0
                          description: The number of clicks on the short link.
                        leads:
                          type: number
                          default: 0
                          description: The number of leads the short link has generated.
                        conversions:
                          type: number
                          default: 0
                          description: >-
                            The number of leads that converted to paying
                            customers.
                        sales:
                          type: number
                          default: 0
                          description: >-
                            The total number of sales (includes recurring sales)
                            generated by the short link.
                        saleAmount:
                          type: number
                          default: 0
                          description: >-
                            The total dollar value of sales (in cents) generated
                            by the short link.
                      required:
                        - id
                        - domain
                        - key
                        - shortLink
                        - url
                        - clicks
                        - leads
                        - conversions
                        - sales
                        - saleAmount
                      title: Link
                    description: The partner's referral links in this program.
              totalCommissions:
                allOf:
                  - type: number
                    default: 0
                    description: >-
                      The total commissions paid to the partner for their
                      referrals
              clickRewardId:
                allOf:
                  - type: string
                    nullable: true
              leadRewardId:
                allOf:
                  - type: string
                    nullable: true
              saleRewardId:
                allOf:
                  - type: string
                    nullable: true
              discountId:
                allOf:
                  - type: string
                    nullable: true
              applicationId:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      If the partner submitted an application to join the
                      program, this is the ID of the application.
              bannedAt:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      If the partner was banned from the program, this is the
                      date of the ban.
              bannedReason:
                allOf:
                  - type: string
                    nullable: true
                    enum:
                      - tos_violation
                      - inappropriate_content
                      - fake_traffic
                      - fraud
                      - spam
                      - brand_abuse
                      - null
                    description: >-
                      If the partner was banned from the program, this is the
                      reason for the ban.
              totalClicks:
                allOf:
                  - type: number
                    default: 0
                    description: The total number of clicks on the partner's links
              totalLeads:
                allOf:
                  - type: number
                    default: 0
                    description: The total number of leads generated by the partner's links
              totalConversions:
                allOf:
                  - type: number
                    default: 0
                    description: >-
                      The total number of leads that converted to paying
                      customers
              totalSales:
                allOf:
                  - type: number
                    default: 0
                    description: >-
                      The total number of sales generated by the partner's links
                      (includes recurring sales)
              totalSaleAmount:
                allOf:
                  - type: number
                    default: 0
                    description: >-
                      The total amount of sales (in cents) generated by the
                      partner's links
              netRevenue:
                allOf:
                  - type: number
                    default: 0
                    description: The total net revenue generated by the partner
              website:
                allOf:
                  - type: string
                    nullable: true
                    description: The partner's website URL (including the https protocol).
              youtube:
                allOf:
                  - type: string
                    nullable: true
                    description: The partner's YouTube channel username (e.g. `johndoe`).
              twitter:
                allOf:
                  - type: string
                    nullable: true
                    description: The partner's Twitter username (e.g. `johndoe`).
              linkedin:
                allOf:
                  - type: string
                    nullable: true
                    description: The partner's LinkedIn username (e.g. `johndoe`).
              instagram:
                allOf:
                  - type: string
                    nullable: true
                    description: The partner's Instagram username (e.g. `johndoe`).
              tiktok:
                allOf:
                  - type: string
                    nullable: true
                    description: The partner's TikTok username (e.g. `johndoe`).
            requiredProperties:
              - id
              - name
              - companyName
              - email
              - image
              - country
              - paypalEmail
              - stripeConnectId
              - payoutsEnabledAt
              - programId
              - partnerId
              - tenantId
              - createdAt
              - status
              - links
              - totalCommissions
              - totalClicks
              - totalLeads
              - totalConversions
              - totalSales
              - totalSaleAmount
              - netRevenue
        examples:
          example:
            value:
              id: <string>
              name: <string>
              companyName: <string>
              email: <string>
              image: <string>
              description: <string>
              country: <string>
              paypalEmail: <string>
              stripeConnectId: <string>
              payoutsEnabledAt: <string>
              programId: <string>
              groupId: <string>
              partnerId: <string>
              tenantId: <string>
              createdAt: <string>
              status: pending
              links:
                - id: <string>
                  domain: <string>
                  key: <string>
                  shortLink: <string>
                  url: <string>
                  clicks: 0
                  leads: 0
                  conversions: 0
                  sales: 0
                  saleAmount: 0
              totalCommissions: 0
              clickRewardId: <string>
              leadRewardId: <string>
              saleRewardId: <string>
              discountId: <string>
              applicationId: <string>
              bannedAt: <string>
              bannedReason: tos_violation
              totalClicks: 0
              totalLeads: 0
              totalConversions: 0
              totalSales: 0
              totalSaleAmount: 0
              netRevenue: 0
              website: <string>
              youtube: <string>
              twitter: <string>
              linkedin: <string>
              instagram: <string>
              tiktok: <string>
        description: The created or updated partner
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - bad_request
                        description: A short code indicating the error code returned.
                        example: bad_request
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#bad-request
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: bad_request
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#bad-request
        description: >-
          The server cannot or will not process the request due to something
          that is perceived to be a client error (e.g., malformed request
          syntax, invalid request message framing, or deceptive request
          routing).
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - unauthorized
                        description: A short code indicating the error code returned.
                        example: unauthorized
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#unauthorized
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: unauthorized
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#unauthorized
        description: >-
          Although the HTTP standard specifies "unauthorized", semantically this
          response means "unauthenticated". That is, the client must
          authenticate itself to get the requested response.
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - forbidden
                        description: A short code indicating the error code returned.
                        example: forbidden
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#forbidden
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: forbidden
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#forbidden
        description: >-
          The client does not have access rights to the content; that is, it is
          unauthorized, so the server is refusing to give the requested
          resource. Unlike 401 Unauthorized, the client's identity is known to
          the server.
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - not_found
                        description: A short code indicating the error code returned.
                        example: not_found
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#not-found
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: not_found
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#not-found
        description: The server cannot find the requested resource.
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - conflict
                        description: A short code indicating the error code returned.
                        example: conflict
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#conflict
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: conflict
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#conflict
        description: >-
          This response is sent when a request conflicts with the current state
          of the server.
    '410':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - invite_expired
                        description: A short code indicating the error code returned.
                        example: invite_expired
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#invite-expired
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: invite_expired
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#invite-expired
        description: >-
          This response is sent when the requested content has been permanently
          deleted from server, with no forwarding address.
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - unprocessable_entity
                        description: A short code indicating the error code returned.
                        example: unprocessable_entity
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#unprocessable-entity
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: unprocessable_entity
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#unprocessable-entity
        description: >-
          The request was well-formed but was unable to be followed due to
          semantic errors.
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - rate_limit_exceeded
                        description: A short code indicating the error code returned.
                        example: rate_limit_exceeded
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#rate-limit_exceeded
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: rate_limit_exceeded
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#rate-limit_exceeded
        description: >-
          The user has sent too many requests in a given amount of time ("rate
          limiting")
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - internal_server_error
                        description: A short code indicating the error code returned.
                        example: internal_server_error
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#internal-server_error
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: internal_server_error
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#internal-server_error
        description: The server has encountered a situation it does not know how to handle.
  deprecated: false
  type: path
components:
  schemas: {}

````