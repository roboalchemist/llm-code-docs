# Source: https://dub.co/docs/api-reference/endpoint/retrieve-analytics.md

# Retrieve analytics

> Retrieve analytics for a link, a domain, or the authenticated workspace. The response type depends on the `event` and `type` query parameters.

## OpenAPI

````yaml get /analytics
paths:
  path: /analytics
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
        event:
          schema:
            - type: enum<string>
              enum:
                - clicks
                - leads
                - sales
                - composite
              description: >-
                The type of event to retrieve analytics for. Defaults to
                `clicks`.
              default: clicks
        groupBy:
          schema:
            - type: enum<string>
              enum:
                - count
                - timeseries
                - continents
                - regions
                - countries
                - cities
                - devices
                - browsers
                - os
                - trigger
                - triggers
                - referers
                - referer_urls
                - top_folders
                - top_link_tags
                - top_domains
                - top_links
                - top_urls
                - top_partners
                - utm_sources
                - utm_mediums
                - utm_campaigns
                - utm_terms
                - utm_contents
              description: >-
                The parameter to group the analytics data points by. Defaults to
                `count` if undefined.
              default: count
        domain:
          schema:
            - type: string
              description: The domain to filter analytics for.
        key:
          schema:
            - type: string
              description: >-
                The slug of the short link to retrieve analytics for. Must be
                used along with the corresponding `domain` of the short link to
                fetch analytics for a specific short link.
        linkId:
          schema:
            - type: string
              description: >-
                The unique ID of the short link on Dub to retrieve analytics
                for.
        externalId:
          schema:
            - type: string
              description: >-
                The ID of the link in the your database. Must be prefixed with
                'ext_' when passed as a query parameter.
        tenantId:
          schema:
            - type: string
              description: The ID of the tenant that created the link inside your system.
        programId:
          schema:
            - type: string
              description: The ID of the program to retrieve analytics for.
        partnerId:
          schema:
            - type: string
              description: The ID of the partner to retrieve analytics for.
        customerId:
          schema:
            - type: string
              description: The ID of the customer to retrieve analytics for.
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
        country:
          schema:
            - type: string
              description: >-
                The country to retrieve analytics for. Must be passed as a
                2-letter ISO 3166-1 country code. See https://d.to/geo for more
                information.
        city:
          schema:
            - type: string
              description: The city to retrieve analytics for.
              example: New York
        region:
          schema:
            - type: string
              description: The ISO 3166-2 region code to retrieve analytics for.
        continent:
          schema:
            - type: enum<string>
              enum:
                - AF
                - AN
                - AS
                - EU
                - NA
                - OC
                - SA
              description: The continent to retrieve analytics for.
        device:
          schema:
            - type: string
              description: The device to retrieve analytics for.
              example: Desktop
        browser:
          schema:
            - type: string
              description: The browser to retrieve analytics for.
              example: Chrome
        os:
          schema:
            - type: string
              description: The OS to retrieve analytics for.
              example: Windows
        trigger:
          schema:
            - type: enum<string>
              enum:
                - qr
                - link
                - pageview
                - deeplink
              description: >-
                The trigger to retrieve analytics for. If undefined, returns all
                trigger types.
        referer:
          schema:
            - type: string
              description: The referer to retrieve analytics for.
              example: google.com
        refererUrl:
          schema:
            - type: string
              description: The full referer URL to retrieve analytics for.
              example: https://dub.co/blog
        url:
          schema:
            - type: string
              description: The URL to retrieve analytics for.
        tagIds:
          schema:
            - type: string
              description: The tag IDs to retrieve analytics for.
            - type: array
              items:
                allOf:
                  - type: string
              description: The tag IDs to retrieve analytics for.
        folderId:
          schema:
            - type: string
              description: >-
                The folder ID to retrieve analytics for. If not provided, return
                analytics for unsorted links.
        root:
          schema:
            - type: boolean
              description: >-
                Filter for root domains. If true, filter for domains only. If
                false, filter for links only. If undefined, return both.
        saleType:
          schema:
            - type: enum<string>
              enum:
                - new
                - recurring
              description: >-
                Filter sales by type: 'new' for first-time purchases,
                'recurring' for repeat purchases. If undefined, returns both.
        query:
          schema:
            - type: string
              description: >-
                Search the events by a custom metadata value. Only available for
                lead and sale events.
              maxLength: 10000
              example: metadata['key']:'value'
        tagId:
          schema:
            - type: string
              description: >-
                Deprecated: Use `tagIds` instead. The tag ID to retrieve
                analytics for.
              deprecated: true
        qr:
          schema:
            - type: boolean
              description: >-
                Deprecated: Use the `trigger` field instead. Filter for QR code
                scans. If true, filter for QR codes only. If false, filter for
                links only. If undefined, return both.
              deprecated: true
        utm_source:
          schema:
            - type: string
              description: The UTM source of the short link.
              maxLength: 190
            - type: 'null'
              description: The UTM source of the short link.
        utm_medium:
          schema:
            - type: string
              description: The UTM medium of the short link.
              maxLength: 190
            - type: 'null'
              description: The UTM medium of the short link.
        utm_campaign:
          schema:
            - type: string
              description: The UTM campaign of the short link.
              maxLength: 190
            - type: 'null'
              description: The UTM campaign of the short link.
        utm_term:
          schema:
            - type: string
              description: The UTM term of the short link.
              maxLength: 190
            - type: 'null'
              description: The UTM term of the short link.
        utm_content:
          schema:
            - type: string
              description: The UTM content of the short link.
              maxLength: 190
            - type: 'null'
              description: The UTM content of the short link.
        ref:
          schema:
            - type: string
              description: The ref of the short link.
              maxLength: 190
            - type: 'null'
              description: The ref of the short link.
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: retrieveAnalytics
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.analytics.retrieve(request={
                  "timezone": "America/New_York",
                  "city": "New York",
                  "device": "Desktop",
                  "browser": "Chrome",
                  "os": "Windows",
                  "referer": "google.com",
                  "referer_url": "https://dub.co/blog",
                  "query": "metadata['key']:'value'",
              })

              assert res is not None

              # Handle response
              print(res)
      - label: retrieveAnalytics
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

          $request = new Operations\RetrieveAnalyticsRequest(
              timezone: 'America/New_York',
              city: 'New York',
              device: 'Desktop',
              browser: 'Chrome',
              os: 'Windows',
              referer: 'google.com',
              refererUrl: 'https://dub.co/blog',
              query: 'metadata[\'key\']:\'value\'',
          );

          $response = $sdk->analytics->retrieve(
              request: $request
          );

          if ($response->oneOf !== null) {
              // handle response
          }
      - label: retrieveAnalytics
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Analytics.Retrieve(ctx, operations.RetrieveAnalyticsRequest{\n        Timezone: dubgo.Pointer(\"America/New_York\"),\n        City: dubgo.Pointer(\"New York\"),\n        Device: dubgo.Pointer(\"Desktop\"),\n        Browser: dubgo.Pointer(\"Chrome\"),\n        Os: dubgo.Pointer(\"Windows\"),\n        Referer: dubgo.Pointer(\"google.com\"),\n        RefererURL: dubgo.Pointer(\"https://dub.co/blog\"),\n        Query: dubgo.Pointer(\"metadata['key']:'value'\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: retrieveAnalytics
        lang: ruby
        source: |-
          require 'dub'

          Models = ::OpenApiSDK::Models
          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          req = Models::Operations::RetrieveAnalyticsRequest.new(
            timezone: 'America/New_York',
            city: 'New York',
            device: 'Desktop',
            browser: 'Chrome',
            os: 'Windows',
            referer: 'google.com',
            referer_url: 'https://dub.co/blog',
            query: 'metadata[\'key\']:\'value\'',
          )

          res = s.analytics.retrieve(request: req)

          unless res.nil?
            # handle response
          end
      - label: retrieveAnalytics
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.analytics.retrieve();

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
            title: AnalyticsCount
            refIdentifier: '#/components/schemas/AnalyticsCount'
            requiredProperties:
              - clicks
              - leads
              - sales
              - saleAmount
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsTimeseries'
            title: AnalyticsTimeseries
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsContinents'
            title: AnalyticsContinents
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsCountries'
            title: AnalyticsCountries
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsRegions'
            title: AnalyticsRegions
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsCities'
            title: AnalyticsCities
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsDevices'
            title: AnalyticsDevices
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsBrowsers'
            title: AnalyticsBrowsers
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsOS'
            title: AnalyticsOS
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsTriggers'
            title: AnalyticsTriggers
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsReferers'
            title: AnalyticsReferers
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsRefererUrls'
            title: AnalyticsRefererUrls
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsTopLinks'
            title: AnalyticsTopLinks
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/AnalyticsTopUrls'
            title: AnalyticsTopUrls
        examples:
          example:
            value:
              clicks: 0
              leads: 0
              sales: 0
              saleAmount: 0
        description: Analytics data
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
    AnalyticsTimeseries:
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
      required:
        - start
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsContinents:
      type: object
      properties:
        continent:
          type: string
          enum:
            - AF
            - AN
            - AS
            - EU
            - NA
            - OC
            - SA
          description: >-
            The 2-letter ISO 3166-1 code representing the continent associated
            with the location of the user.
        clicks:
          type: number
          description: The number of clicks from this continent
          default: 0
        leads:
          type: number
          description: The number of leads from this continent
          default: 0
        sales:
          type: number
          description: The number of sales from this continent
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this continent, in cents
          default: 0
      required:
        - continent
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsCountries:
      type: object
      properties:
        country:
          type: string
          description: >-
            The 2-letter ISO 3166-1 country code of the country. Learn more:
            https://d.to/geo
        region:
          type: string
          enum:
            - '*'
          default: '*'
        city:
          type: string
          enum:
            - '*'
          default: '*'
        clicks:
          type: number
          description: The number of clicks from this country
          default: 0
        leads:
          type: number
          description: The number of leads from this country
          default: 0
        sales:
          type: number
          description: The number of sales from this country
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this country, in cents
          default: 0
      required:
        - country
        - region
        - city
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsRegions:
      type: object
      properties:
        country:
          type: string
          description: >-
            The 2-letter ISO 3166-1 country code of the country. Learn more:
            https://d.to/geo
        region:
          type: string
          description: The 2-letter ISO 3166-2 region code of the region.
        city:
          type: string
          enum:
            - '*'
          default: '*'
        clicks:
          type: number
          description: The number of clicks from this region
          default: 0
        leads:
          type: number
          description: The number of leads from this region
          default: 0
        sales:
          type: number
          description: The number of sales from this region
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this region, in cents
          default: 0
      required:
        - country
        - region
        - city
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsCities:
      type: object
      properties:
        country:
          type: string
          description: >-
            The 2-letter ISO 3166-1 country code of the country where this city
            is located. Learn more: https://d.to/geo
        region:
          type: string
          description: >-
            The 2-letter ISO 3166-2 region code representing the region
            associated with the location of the user.
        city:
          type: string
          description: The name of the city
        clicks:
          type: number
          description: The number of clicks from this city
          default: 0
        leads:
          type: number
          description: The number of leads from this city
          default: 0
        sales:
          type: number
          description: The number of sales from this city
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this city, in cents
          default: 0
      required:
        - country
        - region
        - city
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsDevices:
      type: object
      properties:
        device:
          type: string
          description: The name of the device
        clicks:
          type: number
          description: The number of clicks from this device
          default: 0
        leads:
          type: number
          description: The number of leads from this device
          default: 0
        sales:
          type: number
          description: The number of sales from this device
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this device, in cents
          default: 0
      required:
        - device
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsBrowsers:
      type: object
      properties:
        browser:
          type: string
          description: The name of the browser
        clicks:
          type: number
          description: The number of clicks from this browser
          default: 0
        leads:
          type: number
          description: The number of leads from this browser
          default: 0
        sales:
          type: number
          description: The number of sales from this browser
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this browser, in cents
          default: 0
      required:
        - browser
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsOS:
      type: object
      properties:
        os:
          type: string
          description: The name of the OS
        clicks:
          type: number
          description: The number of clicks from this OS
          default: 0
        leads:
          type: number
          description: The number of leads from this OS
          default: 0
        sales:
          type: number
          description: The number of sales from this OS
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this OS, in cents
          default: 0
      required:
        - os
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsTriggers:
      type: object
      properties:
        trigger:
          type: string
          enum:
            - qr
            - link
            - pageview
            - deeplink
          description: 'The type of trigger method: link click or QR scan'
        clicks:
          type: number
          description: The number of clicks from this trigger method
          default: 0
        leads:
          type: number
          description: The number of leads from this trigger method
          default: 0
        sales:
          type: number
          description: The number of sales from this trigger method
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this trigger method, in cents
          default: 0
      required:
        - trigger
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsReferers:
      type: object
      properties:
        referer:
          type: string
          description: The name of the referer. If unknown, this will be `(direct)`
        clicks:
          type: number
          description: The number of clicks from this referer
          default: 0
        leads:
          type: number
          description: The number of leads from this referer
          default: 0
        sales:
          type: number
          description: The number of sales from this referer
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this referer, in cents
          default: 0
      required:
        - referer
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsRefererUrls:
      type: object
      properties:
        refererUrl:
          type: string
          description: The full URL of the referer. If unknown, this will be `(direct)`
        clicks:
          type: number
          description: The number of clicks from this referer to this URL
          default: 0
        leads:
          type: number
          description: The number of leads from this referer to this URL
          default: 0
        sales:
          type: number
          description: The number of sales from this referer to this URL
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this referer to this URL, in cents
          default: 0
      required:
        - refererUrl
        - clicks
        - leads
        - sales
        - saleAmount
    AnalyticsTopLinks:
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
    AnalyticsTopUrls:
      type: object
      properties:
        url:
          type: string
          description: The destination URL
        clicks:
          type: number
          description: The number of clicks from this URL
          default: 0
        leads:
          type: number
          description: The number of leads from this URL
          default: 0
        sales:
          type: number
          description: The number of sales from this URL
          default: 0
        saleAmount:
          type: number
          description: The total amount of sales from this URL, in cents
          default: 0
      required:
        - url
        - clicks
        - leads
        - sales
        - saleAmount

````