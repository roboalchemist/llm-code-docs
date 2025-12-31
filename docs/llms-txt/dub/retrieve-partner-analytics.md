# Source: https://dub.co/docs/api-reference/endpoint/retrieve-partner-analytics.md

# Retrieve analytics for a partner

> Retrieve analytics for a partner within a program. The response type vary based on the `groupBy` query parameter.

## OpenAPI

````yaml get /partners/analytics
paths:
  path: /partners/analytics
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
        partnerId:
          schema:
            - type: string
              description: The ID of the partner to retrieve analytics for.
        tenantId:
          schema:
            - type: string
              description: The ID of the tenant that created the link inside your system.
        interval:
          schema:
            - type: enum<string>
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
                The interval to retrieve analytics for. If undefined, defaults
                to 24h.
        start:
          schema:
            - type: string
              description: >-
                The start date and time when to retrieve analytics from. If set,
                takes precedence over `interval`.
        end:
          schema:
            - type: string
              description: >-
                The end date and time when to retrieve analytics from. If not
                provided, defaults to the current date. If set along with
                `start`, takes precedence over `interval`.
        timezone:
          schema:
            - type: string
              description: >-
                The IANA time zone code for aligning timeseries granularity
                (e.g. America/New_York). Defaults to UTC.
              default: UTC
              example: America/New_York
        query:
          schema:
            - type: string
              description: >-
                Search the events by a custom metadata value. Only available for
                lead and sale events.
              maxLength: 10000
              example: metadata['key']:'value'
        groupBy:
          schema:
            - type: enum<string>
              enum:
                - top_links
                - timeseries
                - count
              description: >-
                The parameter to group the analytics data points by. Defaults to
                `count` if undefined.
              default: count
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: retrievePartnerAnalytics
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.partners.analytics(request={
                  "timezone": "America/New_York",
                  "query": "metadata['key']:'value'",
              })

              assert res is not None

              # Handle response
              print(res)
      - label: retrievePartnerAnalytics
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

          $request = new Operations\RetrievePartnerAnalyticsRequest(
              timezone: 'America/New_York',
              query: 'metadata[\'key\']:\'value\'',
          );

          $response = $sdk->partners->analytics(
              request: $request
          );

          if ($response->oneOf !== null) {
              // handle response
          }
      - label: retrievePartnerAnalytics
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Partners.Analytics(ctx, operations.RetrievePartnerAnalyticsRequest{\n        Timezone: dubgo.Pointer(\"America/New_York\"),\n        Query: dubgo.Pointer(\"metadata['key']:'value'\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: retrievePartnerAnalytics
        lang: ruby
        source: |-
          require 'dub'

          Models = ::OpenApiSDK::Models
          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          req = Models::Operations::RetrievePartnerAnalyticsRequest.new(
            timezone: 'America/New_York',
            query: 'metadata[\'key\']:\'value\'',
          )

          res = s.partners.analytics(request: req)

          unless res.nil?
            # handle response
          end
      - label: retrievePartnerAnalytics
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.partners.analytics();

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              clicks:
                allOf:
                  - type: number
                    description: The total number of clicks
                    default: 0
              leads:
                allOf:
                  - type: number
                    description: The total number of leads
                    default: 0
              sales:
                allOf:
                  - type: number
                    description: The total number of sales
                    default: 0
              saleAmount:
                allOf:
                  - type: number
                    description: The total amount of sales, in cents
                    default: 0
              earnings:
                allOf:
                  - type: number
                    default: 0
            title: PartnerAnalyticsCount
            refIdentifier: '#/components/schemas/PartnerAnalyticsCount'
            requiredProperties:
              - clicks
              - leads
              - sales
              - saleAmount
              - earnings
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/PartnerAnalyticsTimeseries'
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/PartnerAnalyticsTopLinks'
        examples:
          example:
            value:
              clicks: 0
              leads: 0
              sales: 0
              saleAmount: 0
              earnings: 0
        description: Partner analytics data
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
  schemas:
    PartnerAnalyticsTimeseries:
      type: object
      properties:
        start:
          type: string
          description: The starting timestamp of the interval
        clicks:
          type: number
          description: The number of clicks in the interval
          default: 0
        leads:
          type: number
          description: The number of leads in the interval
          default: 0
        sales:
          type: number
          description: The number of sales in the interval
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales in the interval, in cents
          default: 0
        earnings:
          type: number
          default: 0
      required:
        - start
        - clicks
        - leads
        - sales
        - saleAmount
        - earnings
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
          type: string
          nullable: true
          description: The comments of the short link
        title:
          type: string
          nullable: true
          description: The custom link preview title (og:title)
        createdAt:
          type: string
          description: The creation timestamp of the short link
        clicks:
          type: number
          description: The number of clicks from this link
          default: 0
        leads:
          type: number
          description: The number of leads from this link
          default: 0
        sales:
          type: number
          description: The number of sales from this link
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this link, in cents
          default: 0
        earnings:
          type: number
          default: 0
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
      title: PartnerAnalyticsTopLinks

````