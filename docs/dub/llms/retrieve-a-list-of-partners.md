# Source: https://dub.co/docs/api-reference/endpoint/retrieve-a-list-of-partners.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all partners

> List all partners for a partner program.

<Note>
  Partners endpoints require an [Advanced plan](https://dub.co/pricing)
  subscription or higher.
</Note>


## OpenAPI

````yaml get /partners
openapi: 3.0.3
info:
  title: Dub API
  description: >-
    Dub is the modern link attribution platform for short links, conversion
    tracking, and affiliate programs.
  version: 0.0.1
  contact:
    name: Dub Support
    email: support@dub.co
    url: https://dub.co/api
  license:
    name: AGPL-3.0 license
    url: https://github.com/dubinc/dub/blob/main/LICENSE.md
servers:
  - url: https://api.dub.co
    description: Production API
security: []
paths:
  /partners:
    get:
      tags:
        - Partners
      summary: List all partners
      description: List all partners for a partner program.
      operationId: listPartners
      parameters:
        - in: query
          name: status
          schema:
            description: A filter on the list based on the partner's `status` field.
            example: approved
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
          description: A filter on the list based on the partner's `status` field.
        - in: query
          name: country
          schema:
            description: A filter on the list based on the partner's `country` field.
            example: US
            type: string
          description: A filter on the list based on the partner's `country` field.
        - in: query
          name: sortBy
          schema:
            default: totalSaleAmount
            description: >-
              The field to sort the partners by. The default is
              `totalSaleAmount`.
            example: totalSaleAmount
            type: string
            enum:
              - createdAt
              - totalClicks
              - totalLeads
              - totalConversions
              - totalSaleAmount
              - totalCommissions
              - netRevenue
              - earningsPerClick
              - averageLifetimeValue
              - clickToLeadRate
              - clickToConversionRate
              - leadToConversionRate
              - returnOnAdSpend
          description: The field to sort the partners by. The default is `totalSaleAmount`.
        - in: query
          name: sortOrder
          schema:
            default: desc
            description: The sort order. The default is `desc`.
            example: desc
            type: string
            enum:
              - asc
              - desc
          description: The sort order. The default is `desc`.
        - in: query
          name: email
          schema:
            description: >-
              Filter the partner list based on the partner's `email`. The value
              must be a string. Takes precedence over `search`.
            example: panic@thedis.co
            type: string
          description: >-
            Filter the partner list based on the partner's `email`. The value
            must be a string. Takes precedence over `search`.
        - in: query
          name: tenantId
          schema:
            description: >-
              Filter the partner list based on the partner's `tenantId`. The
              value must be a string. Takes precedence over `email` and
              `search`.
            example: 1K0NM7HCN944PEMZ3CQPH43H8
            type: string
          description: >-
            Filter the partner list based on the partner's `tenantId`. The value
            must be a string. Takes precedence over `email` and `search`.
        - in: query
          name: search
          schema:
            description: A search query to filter partners by ID, name, email, or link.
            example: john
            type: string
          description: A search query to filter partners by ID, name, email, or link.
        - in: query
          name: page
          schema:
            default: 1
            description: The page number for pagination.
            example: 1
            type: number
            minimum: 0
            exclusiveMinimum: true
          description: The page number for pagination.
        - in: query
          name: pageSize
          schema:
            default: 100
            description: The number of items per page.
            example: 50
            type: number
            minimum: 0
            exclusiveMinimum: true
            maximum: 100
          description: The number of items per page.
      responses:
        '200':
          description: The list of partners.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: The partner's unique ID on Dub.
                    name:
                      type: string
                      maxLength: 190
                      description: The partner's full legal name.
                    companyName:
                      nullable: true
                      description: >-
                        If the partner profile type is a company, this is the
                        partner's legal company name.
                      type: string
                      maxLength: 190
                    email:
                      nullable: true
                      description: >-
                        The partner's email address. Should be a unique value
                        across Dub.
                      type: string
                      maxLength: 190
                    image:
                      nullable: true
                      description: The partner's avatar image.
                      type: string
                    description:
                      description: A brief description of the partner and their background.
                      nullable: true
                      type: string
                      maxLength: 5000
                    country:
                      nullable: true
                      description: The partner's country (required for tax purposes).
                      type: string
                    paypalEmail:
                      nullable: true
                      description: >-
                        The partner's PayPal email (for receiving payouts via
                        PayPal).
                      type: string
                    stripeConnectId:
                      nullable: true
                      description: >-
                        The partner's Stripe Connect ID (for receiving payouts
                        via Stripe).
                      type: string
                    payoutsEnabledAt:
                      nullable: true
                      description: The date when the partner enabled payouts.
                      type: string
                    trustedAt:
                      nullable: true
                      description: >-
                        The date when the partner received the trusted badge in
                        the partner network.
                      type: string
                    programId:
                      type: string
                      description: The program's unique ID on Dub.
                    groupId:
                      description: The partner's group ID on Dub.
                      nullable: true
                      type: string
                    partnerId:
                      type: string
                      description: The partner's unique ID on Dub.
                    tenantId:
                      nullable: true
                      description: >-
                        The partner's unique ID within your database. Can be
                        useful for associating the partner with a user in your
                        database and retrieving/update their data in the future.
                      type: string
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
                      nullable: true
                      description: The partner's referral links in this program.
                      type: array
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
                            default: 0
                            description: The number of clicks on the short link.
                            type: number
                          leads:
                            default: 0
                            description: The number of leads the short link has generated.
                            type: number
                          conversions:
                            default: 0
                            description: >-
                              The number of leads that converted to paying
                              customers.
                            type: number
                          sales:
                            default: 0
                            description: >-
                              The total number of sales (includes recurring
                              sales) generated by the short link.
                            type: number
                          saleAmount:
                            default: 0
                            description: >-
                              The total dollar value of sales (in cents)
                              generated by the short link.
                            type: number
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
                        additionalProperties: false
                    totalCommissions:
                      default: 0
                      description: >-
                        The total commissions paid to the partner for their
                        referrals
                      type: number
                    clickRewardId:
                      nullable: true
                      type: string
                    leadRewardId:
                      nullable: true
                      type: string
                    saleRewardId:
                      nullable: true
                      type: string
                    discountId:
                      nullable: true
                      type: string
                    applicationId:
                      description: >-
                        If the partner submitted an application to join the
                        program, this is the ID of the application.
                      nullable: true
                      type: string
                    bannedAt:
                      description: >-
                        If the partner was banned from the program, this is the
                        date of the ban.
                      nullable: true
                      type: string
                    bannedReason:
                      description: >-
                        If the partner was banned from the program, this is the
                        reason for the ban.
                      nullable: true
                      type: string
                      enum:
                        - tos_violation
                        - inappropriate_content
                        - fake_traffic
                        - fraud
                        - spam
                        - brand_abuse
                    totalClicks:
                      default: 0
                      description: The total number of clicks on the partner's links
                      type: number
                    totalLeads:
                      default: 0
                      description: >-
                        The total number of leads generated by the partner's
                        links
                      type: number
                    totalConversions:
                      default: 0
                      description: >-
                        The total number of leads that converted to paying
                        customers
                      type: number
                    totalSales:
                      default: 0
                      description: >-
                        The total number of sales generated by the partner's
                        links (includes recurring sales)
                      type: number
                    totalSaleAmount:
                      default: 0
                      description: Total revenue generated by the partner's links
                      type: number
                    netRevenue:
                      default: 0
                      description: >-
                        Net revenue after commissions (`Total Revenue - Total
                        Commissions`)
                      type: number
                    earningsPerClick:
                      description: >-
                        Earnings Per Click (EPC) (`Total Revenue ÷ Total
                        Clicks`)
                      nullable: true
                      type: number
                    averageLifetimeValue:
                      description: >-
                        Average lifetime value for each paying customer (`Total
                        Revenue ÷ Total Conversions`)
                      nullable: true
                      type: number
                    clickToLeadRate:
                      description: >-
                        Percentage of clicks that become leads (`Total Leads ÷
                        Total Clicks`)
                      nullable: true
                      type: number
                    clickToConversionRate:
                      description: >-
                        Percentage of clicks that convert to paying customers
                        (`Total Conversions ÷ Total Clicks`)
                      nullable: true
                      type: number
                    leadToConversionRate:
                      description: >-
                        Percentage of leads that convert to paying customers
                        (`Total Conversions ÷ Total Leads`)
                      nullable: true
                      type: number
                    returnOnAdSpend:
                      description: >-
                        Return On Ad Spend (ROAS) (`Total Revenue ÷ Total
                        Commissions`)
                      nullable: true
                      type: number
                    website:
                      description: >-
                        The partner's website URL (including the https
                        protocol).
                      nullable: true
                      type: string
                    youtube:
                      description: The partner's YouTube channel username (e.g. `johndoe`).
                      nullable: true
                      type: string
                    twitter:
                      description: The partner's Twitter username (e.g. `johndoe`).
                      nullable: true
                      type: string
                    linkedin:
                      description: The partner's LinkedIn username (e.g. `johndoe`).
                      nullable: true
                      type: string
                    instagram:
                      description: The partner's Instagram username (e.g. `johndoe`).
                      nullable: true
                      type: string
                    tiktok:
                      description: The partner's TikTok username (e.g. `johndoe`).
                      nullable: true
                      type: string
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
                    - trustedAt
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
                  additionalProperties: false
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '403':
          $ref: '#/components/responses/403'
        '404':
          $ref: '#/components/responses/404'
        '409':
          $ref: '#/components/responses/409'
        '410':
          $ref: '#/components/responses/410'
        '422':
          $ref: '#/components/responses/422'
        '429':
          $ref: '#/components/responses/429'
        '500':
          $ref: '#/components/responses/500'
      security:
        - token: []
components:
  responses:
    '400':
      description: >-
        The server cannot or will not process the request due to something that
        is perceived to be a client error (e.g., malformed request syntax,
        invalid request message framing, or deceptive request routing).
      content:
        application/json:
          schema:
            x-speakeasy-name-override: BadRequest
            type: object
            properties:
              error:
                type: object
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
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#bad-request
                required:
                  - code
                  - message
            required:
              - error
    '401':
      description: >-
        Although the HTTP standard specifies "unauthorized", semantically this
        response means "unauthenticated". That is, the client must authenticate
        itself to get the requested response.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: Unauthorized
            type: object
            properties:
              error:
                type: object
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
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#unauthorized
                required:
                  - code
                  - message
            required:
              - error
    '403':
      description: >-
        The client does not have access rights to the content; that is, it is
        unauthorized, so the server is refusing to give the requested resource.
        Unlike 401 Unauthorized, the client's identity is known to the server.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: Forbidden
            type: object
            properties:
              error:
                type: object
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
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#forbidden
                required:
                  - code
                  - message
            required:
              - error
    '404':
      description: The server cannot find the requested resource.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: NotFound
            type: object
            properties:
              error:
                type: object
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
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#not-found
                required:
                  - code
                  - message
            required:
              - error
    '409':
      description: >-
        This response is sent when a request conflicts with the current state of
        the server.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: Conflict
            type: object
            properties:
              error:
                type: object
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
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#conflict
                required:
                  - code
                  - message
            required:
              - error
    '410':
      description: >-
        This response is sent when the requested content has been permanently
        deleted from server, with no forwarding address.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: InviteExpired
            type: object
            properties:
              error:
                type: object
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
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#invite-expired
                required:
                  - code
                  - message
            required:
              - error
    '422':
      description: >-
        The request was well-formed but was unable to be followed due to
        semantic errors.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: UnprocessableEntity
            type: object
            properties:
              error:
                type: object
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
                      A link to our documentation with more details about this
                      error code
                    example: >-
                      https://dub.co/docs/api-reference/errors#unprocessable-entity
                required:
                  - code
                  - message
            required:
              - error
    '429':
      description: >-
        The user has sent too many requests in a given amount of time ("rate
        limiting")
      content:
        application/json:
          schema:
            x-speakeasy-name-override: RateLimitExceeded
            type: object
            properties:
              error:
                type: object
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
                      A link to our documentation with more details about this
                      error code
                    example: >-
                      https://dub.co/docs/api-reference/errors#rate-limit_exceeded
                required:
                  - code
                  - message
            required:
              - error
    '500':
      description: The server has encountered a situation it does not know how to handle.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: InternalServerError
            type: object
            properties:
              error:
                type: object
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
                      A link to our documentation with more details about this
                      error code
                    example: >-
                      https://dub.co/docs/api-reference/errors#internal-server_error
                required:
                  - code
                  - message
            required:
              - error
  securitySchemes:
    token:
      type: http
      description: Default authentication mechanism
      scheme: bearer
      x-speakeasy-example: DUB_API_KEY

````