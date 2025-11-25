# Source: https://dub.co/docs/api-reference/endpoint/retrieve-a-list-of-partners.md

# List all partners

> List all partners for a partner program.

## OpenAPI

````yaml get /partners
paths:
  path: /partners
  method: get
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
      query:
        status:
          schema:
            - type: enum<string>
              enum:
                - pending
                - approved
                - rejected
                - invited
                - declined
                - deactivated
                - banned
                - archived
              description: A filter on the list based on the partner's `status` field.
              example: approved
        country:
          schema:
            - type: string
              description: A filter on the list based on the partner's `country` field.
              example: US
        sortBy:
          schema:
            - type: enum<string>
              enum:
                - createdAt
                - totalClicks
                - totalLeads
                - totalConversions
                - totalSaleAmount
                - totalCommissions
              description: >-
                The field to sort the partners by. The default is
                `totalSaleAmount`.
              default: totalSaleAmount
              example: totalSaleAmount
        sortOrder:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              description: The sort order. The default is `desc`.
              default: desc
              example: desc
        email:
          schema:
            - type: string
              description: >-
                Filter the partner list based on the partner's `email`. The
                value must be a string. Takes precedence over `search`.
              example: panic@thedis.co
        tenantId:
          schema:
            - type: string
              description: >-
                Filter the partner list based on the partner's `tenantId`. The
                value must be a string. Takes precedence over `email` and
                `search`.
              example: 1K0NM7HCN944PEMZ3CQPH43H8
        search:
          schema:
            - type: string
              description: A search query to filter partners by ID, name, email, or link.
              example: john
        page:
          schema:
            - type: number
              description: The page number for pagination.
              minimum: 0
              exclusiveMinimum: true
              default: 1
              example: 1
        pageSize:
          schema:
            - type: number
              description: The number of items per page.
              maximum: 100
              minimum: 0
              exclusiveMinimum: true
              default: 100
              example: 50
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: listPartners
        lang: python
        source: |-
          from dub import Dub
          from dub.models import operations


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.partners.list(request={
                  "status": operations.ListPartnersQueryParamStatus.APPROVED,
                  "country": "US",
                  "email": "panic@thedis.co",
                  "tenant_id": "1K0NM7HCN944PEMZ3CQPH43H8",
                  "search": "john",
                  "page_size": 50,
              })

              assert res is not None

              # Handle response
              print(res)
      - label: listPartners
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

          $request = new Operations\ListPartnersRequest(
              status: Operations\ListPartnersQueryParamStatus::Approved,
              country: 'US',
              email: 'panic@thedis.co',
              tenantId: '1K0NM7HCN944PEMZ3CQPH43H8',
              search: 'john',
              pageSize: 50,
          );

          $response = $sdk->partners->list(
              request: $request
          );

          if ($response->responseBodies !== null) {
              // handle response
          }
      - label: listPartners
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Partners.List(ctx, operations.ListPartnersRequest{\n        Status: operations.ListPartnersQueryParamStatusApproved.ToPointer(),\n        Country: dubgo.Pointer(\"US\"),\n        Email: dubgo.Pointer(\"panic@thedis.co\"),\n        TenantID: dubgo.Pointer(\"1K0NM7HCN944PEMZ3CQPH43H8\"),\n        Search: dubgo.Pointer(\"john\"),\n        PageSize: dubgo.Pointer[float64](50),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: listPartners
        lang: ruby
        source: |-
          require 'dub'

          Models = ::OpenApiSDK::Models
          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          req = Models::Operations::ListPartnersRequest.new(
            status: Models::Operations::ListPartnersQueryParamStatus::APPROVED,
            country: 'US',
            email: 'panic@thedis.co',
            tenant_id: '1K0NM7HCN944PEMZ3CQPH43H8',
            search: 'john',
            page_size: 50.0,
          )

          res = s.partners.list(request: req)

          unless res.nil?
            # handle response
          end
      - label: listPartners
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.partners.list();

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - type: object
                  properties:
                    id:
                      type: string
                      description: The partner's unique ID on Dub.
                    name:
                      type: string
                      maxLength: 190
                      description: The partner's full legal name.
                    companyName:
                      type: string
                      nullable: true
                      maxLength: 190
                      description: >-
                        If the partner profile type is a company, this is the
                        partner's legal company name.
                    email:
                      type: string
                      nullable: true
                      maxLength: 190
                      description: >-
                        The partner's email address. Should be a unique value
                        across Dub.
                    image:
                      type: string
                      nullable: true
                      description: The partner's avatar image.
                    description:
                      type: string
                      nullable: true
                      maxLength: 5000
                      description: A brief description of the partner and their background.
                    country:
                      type: string
                      nullable: true
                      description: The partner's country (required for tax purposes).
                    paypalEmail:
                      type: string
                      nullable: true
                      description: >-
                        The partner's PayPal email (for receiving payouts via
                        PayPal).
                    stripeConnectId:
                      type: string
                      nullable: true
                      description: >-
                        The partner's Stripe Connect ID (for receiving payouts
                        via Stripe).
                    payoutsEnabledAt:
                      type: string
                      nullable: true
                      description: The date when the partner enabled payouts.
                    programId:
                      type: string
                      description: The program's unique ID on Dub.
                    groupId:
                      type: string
                      nullable: true
                      description: The partner's group ID on Dub.
                    partnerId:
                      type: string
                      description: The partner's unique ID on Dub.
                    tenantId:
                      type: string
                      nullable: true
                      description: >-
                        The partner's unique ID within your database. Can be
                        useful for associating the partner with a user in your
                        database and retrieving/update their data in the future.
                    createdAt:
                      type: string
                    status:
                      type: string
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
                      type: array
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
                              The full URL of the short link, including the
                              https protocol (e.g. `https://dub.sh/try`).
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
                              The total number of sales (includes recurring
                              sales) generated by the short link.
                          saleAmount:
                            type: number
                            default: 0
                            description: >-
                              The total dollar value of sales (in cents)
                              generated by the short link.
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
                      type: number
                      default: 0
                      description: >-
                        The total commissions paid to the partner for their
                        referrals
                    clickRewardId:
                      type: string
                      nullable: true
                    leadRewardId:
                      type: string
                      nullable: true
                    saleRewardId:
                      type: string
                      nullable: true
                    discountId:
                      type: string
                      nullable: true
                    applicationId:
                      type: string
                      nullable: true
                      description: >-
                        If the partner submitted an application to join the
                        program, this is the ID of the application.
                    bannedAt:
                      type: string
                      nullable: true
                      description: >-
                        If the partner was banned from the program, this is the
                        date of the ban.
                    bannedReason:
                      type: string
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
                      type: number
                      default: 0
                      description: The total number of clicks on the partner's links
                    totalLeads:
                      type: number
                      default: 0
                      description: >-
                        The total number of leads generated by the partner's
                        links
                    totalConversions:
                      type: number
                      default: 0
                      description: >-
                        The total number of leads that converted to paying
                        customers
                    totalSales:
                      type: number
                      default: 0
                      description: >-
                        The total number of sales generated by the partner's
                        links (includes recurring sales)
                    totalSaleAmount:
                      type: number
                      default: 0
                      description: >-
                        The total amount of sales (in cents) generated by the
                        partner's links
                    netRevenue:
                      type: number
                      default: 0
                      description: The total net revenue generated by the partner
                    website:
                      type: string
                      nullable: true
                      description: >-
                        The partner's website URL (including the https
                        protocol).
                    youtube:
                      type: string
                      nullable: true
                      description: The partner's YouTube channel username (e.g. `johndoe`).
                    twitter:
                      type: string
                      nullable: true
                      description: The partner's Twitter username (e.g. `johndoe`).
                    linkedin:
                      type: string
                      nullable: true
                      description: The partner's LinkedIn username (e.g. `johndoe`).
                    instagram:
                      type: string
                      nullable: true
                      description: The partner's Instagram username (e.g. `johndoe`).
                    tiktok:
                      type: string
                      nullable: true
                      description: The partner's TikTok username (e.g. `johndoe`).
                  required:
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
              - id: <string>
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
        description: The list of partners.
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