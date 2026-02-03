# Source: https://dub.co/docs/api-reference/endpoint/retrieve-partner-analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve analytics for a partner

> Retrieve analytics for a partner within a program. The response type vary based on the `groupBy` query parameter.

<Note>
  Partners endpoints require an [Advanced plan](https://dub.co/pricing)
  subscription or higher.
</Note>


## OpenAPI

````yaml get /partners/analytics
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
  /partners/analytics:
    get:
      tags:
        - Partners
      summary: Retrieve analytics for a partner
      description: >-
        Retrieve analytics for a partner within a program. The response type
        vary based on the `groupBy` query parameter.
      operationId: retrievePartnerAnalytics
      parameters:
        - in: query
          name: partnerId
          schema:
            description: >-
              The ID of the partner to create a link for. Will take precedence
              over `tenantId` if provided.
            nullable: true
            type: string
          description: >-
            The ID of the partner to create a link for. Will take precedence
            over `tenantId` if provided.
        - in: query
          name: tenantId
          schema:
            description: >-
              The ID of the partner in your system. If both `partnerId` and
              `tenantId` are not provided, an error will be thrown.
            nullable: true
            type: string
          description: >-
            The ID of the partner in your system. If both `partnerId` and
            `tenantId` are not provided, an error will be thrown.
        - in: query
          name: interval
          schema:
            description: >-
              The interval to retrieve analytics for. If undefined, defaults to
              24h.
            type: string
            enum:
              - 24h
              - 7d
              - 30d
              - 90d
              - 1y
              - mtd
              - qtd
              - ytd
              - all
          description: >-
            The interval to retrieve analytics for. If undefined, defaults to
            24h.
        - in: query
          name: start
          schema:
            description: >-
              The start date and time when to retrieve analytics from. If set,
              takes precedence over `interval`.
            type: string
          description: >-
            The start date and time when to retrieve analytics from. If set,
            takes precedence over `interval`.
        - in: query
          name: end
          schema:
            description: >-
              The end date and time when to retrieve analytics from. If not
              provided, defaults to the current date. If set along with `start`,
              takes precedence over `interval`.
            type: string
          description: >-
            The end date and time when to retrieve analytics from. If not
            provided, defaults to the current date. If set along with `start`,
            takes precedence over `interval`.
        - in: query
          name: timezone
          schema:
            description: >-
              The IANA time zone code for aligning timeseries granularity (e.g.
              America/New_York). Defaults to UTC.
            example: America/New_York
            default: UTC
            type: string
          description: >-
            The IANA time zone code for aligning timeseries granularity (e.g.
            America/New_York). Defaults to UTC.
        - in: query
          name: query
          schema:
            description: >-
              Search the events by a custom metadata value. Only available for
              lead and sale events.
            example: metadata['key']:'value'
            type: string
            maxLength: 10000
          description: >-
            Search the events by a custom metadata value. Only available for
            lead and sale events.
        - in: query
          name: groupBy
          schema:
            default: count
            description: >-
              The parameter to group the analytics data points by. Defaults to
              `count` if undefined.
            type: string
            enum:
              - top_links
              - timeseries
              - count
          description: >-
            The parameter to group the analytics data points by. Defaults to
            `count` if undefined.
      responses:
        '200':
          description: Partner analytics data
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/PartnerAnalyticsCount'
                  - type: array
                    items:
                      $ref: '#/components/schemas/PartnerAnalyticsTimeseries'
                  - type: array
                    items:
                      $ref: '#/components/schemas/PartnerAnalyticsTopLinks'
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
  schemas:
    PartnerAnalyticsCount:
      type: object
      properties:
        clicks:
          default: 0
          type: number
          description: The total number of clicks
        leads:
          default: 0
          type: number
          description: The total number of leads
        sales:
          default: 0
          type: number
          description: The total number of sales
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales, in cents
        earnings:
          default: 0
          type: number
      required:
        - clicks
        - leads
        - sales
        - saleAmount
        - earnings
      additionalProperties: false
      title: PartnerAnalyticsCount
    PartnerAnalyticsTimeseries:
      type: object
      properties:
        start:
          type: string
          description: The starting timestamp of the interval
        clicks:
          default: 0
          type: number
          description: The number of clicks in the interval
        leads:
          default: 0
          type: number
          description: The number of leads in the interval
        sales:
          default: 0
          type: number
          description: The number of sales in the interval
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales in the interval, in cents
        earnings:
          default: 0
          type: number
      required:
        - start
        - clicks
        - leads
        - sales
        - saleAmount
        - earnings
      additionalProperties: false
      title: PartnerAnalyticsTimeseries
    PartnerAnalyticsTopLinks:
      type: object
      properties:
        link:
          type: string
          description: The unique ID of the short link
          deprecated: true
        id:
          type: string
          description: The unique ID of the short link
        domain:
          type: string
          description: The domain of the short link
        key:
          type: string
          description: The key of the short link
        shortLink:
          type: string
          description: The short link URL
        url:
          type: string
          description: The destination URL of the short link
        comments:
          description: The comments of the short link
          nullable: true
          type: string
        title:
          description: The custom link preview title (og:title)
          nullable: true
          type: string
        createdAt:
          type: string
          description: The creation timestamp of the short link
        clicks:
          default: 0
          type: number
          description: The number of clicks from this link
        leads:
          default: 0
          type: number
          description: The number of leads from this link
        sales:
          default: 0
          type: number
          description: The number of sales from this link
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this link, in cents
        earnings:
          default: 0
          type: number
      required:
        - link
        - id
        - domain
        - key
        - shortLink
        - url
        - createdAt
        - clicks
        - leads
        - sales
        - saleAmount
        - earnings
      additionalProperties: false
      title: PartnerAnalyticsTopLinks
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