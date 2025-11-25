# Source: https://dub.co/docs/api-reference/endpoint/retrieve-a-list-of-events.md

# Retrieve a list of events

> Retrieve a paginated list of events for the authenticated workspace.

## OpenAPI

````yaml get /events
paths:
  path: /events
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
              description: >-
                The type of event to retrieve analytics for. Defaults to
                'clicks'.
              default: clicks
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
        page:
          schema:
            - type: number
              default: 1
        limit:
          schema:
            - type: number
              default: 100
        sortOrder:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              description: The sort order. The default is `desc`.
              default: desc
        sortBy:
          schema:
            - type: enum<string>
              enum:
                - timestamp
              description: The field to sort the events by. The default is `timestamp`.
              default: timestamp
        order:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              description: DEPRECATED. Use `sortOrder` instead.
              deprecated: true
              default: desc
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: listEvents
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.events.list(request={
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
      - label: listEvents
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

          $request = new Operations\ListEventsRequest(
              timezone: 'America/New_York',
              city: 'New York',
              device: 'Desktop',
              browser: 'Chrome',
              os: 'Windows',
              referer: 'google.com',
              refererUrl: 'https://dub.co/blog',
              query: 'metadata[\'key\']:\'value\'',
          );

          $response = $sdk->events->list(
              request: $request
          );

          if ($response->responseBodies !== null) {
              // handle response
          }
      - label: listEvents
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Events.List(ctx, operations.ListEventsRequest{\n        Timezone: dubgo.Pointer(\"America/New_York\"),\n        City: dubgo.Pointer(\"New York\"),\n        Device: dubgo.Pointer(\"Desktop\"),\n        Browser: dubgo.Pointer(\"Chrome\"),\n        Os: dubgo.Pointer(\"Windows\"),\n        Referer: dubgo.Pointer(\"google.com\"),\n        RefererURL: dubgo.Pointer(\"https://dub.co/blog\"),\n        Query: dubgo.Pointer(\"metadata['key']:'value'\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: listEvents
        lang: ruby
        source: |-
          require 'dub'

          Models = ::OpenApiSDK::Models
          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          req = Models::Operations::ListEventsRequest.new(
            timezone: 'America/New_York',
            city: 'New York',
            device: 'Desktop',
            browser: 'Chrome',
            os: 'Windows',
            referer: 'google.com',
            referer_url: 'https://dub.co/blog',
            query: 'metadata[\'key\']:\'value\'',
          )

          res = s.events.list(request: req)

          unless res.nil?
            # handle response
          end
      - label: listEvents
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.events.list();

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
                - oneOf:
                    - $ref: '#/components/schemas/ClickEvent'
                    - $ref: '#/components/schemas/LeadEvent'
                    - $ref: '#/components/schemas/SaleEvent'
                  discriminator:
                    propertyName: event
                    mapping:
                      click: '#/components/schemas/ClickEvent'
                      lead: '#/components/schemas/LeadEvent'
                      sale: '#/components/schemas/SaleEvent'
        examples:
          example:
            value:
              - event: click
                timestamp: <string>
                click:
                  id: <string>
                  timestamp: <string>
                  url: <string>
                  country: <string>
                  city: <string>
                  region: <string>
                  continent: <string>
                  device: <string>
                  browser: <string>
                  os: <string>
                  trigger: <string>
                  referer: <string>
                  refererUrl: <string>
                  qr: true
                  ip: <string>
                link:
                  id: <string>
                  domain: <string>
                  key: <string>
                  url: <string>
                  trackConversion: true
                  externalId: <string>
                  tenantId: <string>
                  programId: <string>
                  partnerId: <string>
                  archived: true
                  expiresAt: <string>
                  expiredUrl: <string>
                  password: <string>
                  proxy: true
                  title: <string>
                  description: <string>
                  image: <string>
                  video: <string>
                  rewrite: true
                  doIndex: true
                  ios: <string>
                  android: <string>
                  geo: {}
                  publicStats: true
                  tags:
                    - id: <string>
                      name: <string>
                      color: red
                  folderId: <string>
                  webhookIds:
                    - <string>
                  comments: <string>
                  shortLink: <string>
                  qrCode: <string>
                  utm_source: <string>
                  utm_medium: <string>
                  utm_campaign: <string>
                  utm_term: <string>
                  utm_content: <string>
                  testVariants:
                    - url: https://example.com/variant-1
                      percentage: 50
                    - url: https://example.com/variant-2
                      percentage: 50
                  testStartedAt: <string>
                  testCompletedAt: <string>
                  userId: <string>
                  workspaceId: <string>
                  clicks: 0
                  leads: 0
                  conversions: 0
                  sales: 0
                  saleAmount: 0
                  lastClicked: <string>
                  createdAt: <string>
                  updatedAt: <string>
                  tagId: <string>
                  projectId: <string>
                click_id: <string>
                link_id: <string>
                domain: <string>
                key: <string>
                url: <string>
                continent: <string>
                country: <string>
                city: <string>
                device: <string>
                browser: <string>
                os: <string>
                qr: 123
                ip: <string>
        description: A list of events
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
    LinkTagSchema:
      type: object
      properties:
        id:
          type: string
          description: The unique ID of the tag.
        name:
          type: string
          description: The name of the tag.
        color:
          type: string
          enum:
            - red
            - yellow
            - green
            - blue
            - purple
            - brown
            - pink
          description: The color of the tag.
      required:
        - id
        - name
        - color
      title: LinkTag
    ClickEvent:
      type: object
      properties:
        event:
          type: string
          enum:
            - click
        timestamp:
          type: string
        click:
          type: object
          properties:
            id:
              type: string
            timestamp:
              type: string
            url:
              type: string
            country:
              type: string
            city:
              type: string
            region:
              type: string
            continent:
              type: string
            device:
              type: string
            browser:
              type: string
            os:
              type: string
            trigger:
              type: string
              nullable: true
            referer:
              type: string
            refererUrl:
              type: string
            qr:
              type: boolean
            ip:
              type: string
          required:
            - id
            - timestamp
            - url
            - country
            - city
            - region
            - continent
            - device
            - browser
            - os
            - referer
            - refererUrl
            - qr
            - ip
        link:
          type: object
          properties:
            id:
              type: string
              description: The unique ID of the short link.
            domain:
              type: string
              description: >-
                The domain of the short link. If not provided, the primary
                domain for the workspace will be used (or `dub.sh` if the
                workspace has no domains).
            key:
              type: string
              description: >-
                The short link slug. If not provided, a random 7-character slug
                will be generated.
            url:
              type: string
            trackConversion:
              type: boolean
            externalId:
              type: string
              nullable: true
              description: >-
                The ID of the link in your database. If set, it can be used to
                identify the link in future API requests (must be prefixed with
                'ext_' when passed as a query parameter). This key is unique
                across your workspace.
            tenantId:
              type: string
              nullable: true
              description: >-
                The ID of the tenant that created the link inside your system.
                If set, it can be used to fetch all links for a tenant.
            programId:
              type: string
              nullable: true
              description: The ID of the program the short link is associated with.
            partnerId:
              type: string
              nullable: true
              description: The ID of the partner the short link is associated with.
            archived:
              type: boolean
            expiresAt:
              type: string
            expiredUrl:
              type: string
              nullable: true
            password:
              type: string
              nullable: true
              description: >-
                The password required to access the destination URL of the short
                link.
            proxy:
              type: boolean
            title:
              type: string
              nullable: true
              description: >-
                The title of the short link. Will be used for Custom Link
                Previews if `proxy` is true.
            description:
              type: string
              nullable: true
              description: >-
                The description of the short link. Will be used for Custom Link
                Previews if `proxy` is true.
            image:
              type: string
              nullable: true
              description: >-
                The image of the short link. Will be used for Custom Link
                Previews if `proxy` is true.
            video:
              type: string
              nullable: true
              description: >-
                The custom link preview video (og:video). Will be used for
                Custom Link Previews if `proxy` is true. Learn more:
                https://d.to/og
            rewrite:
              type: boolean
            doIndex:
              type: boolean
            ios:
              type: string
              nullable: true
              description: >-
                The iOS destination URL for the short link for iOS device
                targeting.
            android:
              type: string
              nullable: true
              description: >-
                The Android destination URL for the short link for Android
                device targeting.
            geo:
              type: object
              nullable: true
              additionalProperties:
                type: string
                format: uri
              description: >-
                Geo targeting information for the short link in JSON format
                `{[COUNTRY]: https://example.com }`. See https://d.to/geo for
                more information.
            publicStats:
              type: boolean
            tags:
              type: array
              nullable: true
              items:
                $ref: '#/components/schemas/LinkTagSchema'
              description: The tags assigned to the short link.
            folderId:
              type: string
              nullable: true
              description: The unique ID of the folder assigned to the short link.
            webhookIds:
              type: array
              items:
                type: string
              description: The IDs of the webhooks that the short link is associated with.
            comments:
              type: string
              nullable: true
              description: The comments for the short link.
            shortLink:
              type: string
              format: uri
              description: >-
                The full URL of the short link, including the https protocol
                (e.g. `https://dub.sh/try`).
            qrCode:
              type: string
              format: uri
              description: >-
                The full URL of the QR code for the short link (e.g.
                `https://api.dub.co/qr?url=https://dub.sh/try`).
            utm_source:
              type: string
              nullable: true
              description: The UTM source of the short link.
            utm_medium:
              type: string
              nullable: true
              description: The UTM medium of the short link.
            utm_campaign:
              type: string
              nullable: true
              description: The UTM campaign of the short link.
            utm_term:
              type: string
              nullable: true
              description: The UTM term of the short link.
            utm_content:
              type: string
              nullable: true
              description: The UTM content of the short link.
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
                An array of A/B test URLs and the percentage of traffic to send
                to each URL.
              example:
                - url: https://example.com/variant-1
                  percentage: 50
                - url: https://example.com/variant-2
                  percentage: 50
            testStartedAt:
              type: string
              nullable: true
            testCompletedAt:
              type: string
              nullable: true
            userId:
              type: string
              nullable: true
            workspaceId:
              type: string
              description: The workspace ID of the short link.
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
              description: The number of leads that converted to paying customers.
            sales:
              type: number
              default: 0
              description: >-
                The total number of sales (includes recurring sales) generated
                by the short link.
            saleAmount:
              type: number
              default: 0
              description: >-
                The total dollar value of sales (in cents) generated by the
                short link.
            lastClicked:
              type: string
            createdAt:
              type: string
            updatedAt:
              type: string
            tagId:
              type: string
              nullable: true
              description: >-
                Deprecated: Use `tags` instead. The unique ID of the tag
                assigned to the short link.
              deprecated: true
            projectId:
              type: string
              description: >-
                Deprecated: Use `workspaceId` instead. The project ID of the
                short link.
              deprecated: true
          required:
            - id
            - domain
            - key
            - url
            - trackConversion
            - externalId
            - tenantId
            - programId
            - partnerId
            - archived
            - expiresAt
            - expiredUrl
            - password
            - proxy
            - title
            - description
            - image
            - video
            - rewrite
            - doIndex
            - ios
            - android
            - geo
            - publicStats
            - tags
            - folderId
            - webhookIds
            - comments
            - shortLink
            - qrCode
            - utm_source
            - utm_medium
            - utm_campaign
            - utm_term
            - utm_content
            - testStartedAt
            - testCompletedAt
            - userId
            - workspaceId
            - clicks
            - leads
            - conversions
            - sales
            - saleAmount
            - lastClicked
            - createdAt
            - updatedAt
            - tagId
            - projectId
          title: Link
        click_id:
          type: string
          description: 'Deprecated: Use `click.id` instead.'
          deprecated: true
        link_id:
          type: string
          description: 'Deprecated: Use `link.id` instead.'
          deprecated: true
        domain:
          type: string
          description: 'Deprecated: Use `link.domain` instead.'
          deprecated: true
        key:
          type: string
          description: 'Deprecated: Use `link.key` instead.'
          deprecated: true
        url:
          type: string
          description: 'Deprecated: Use `click.url` instead.'
          deprecated: true
        continent:
          type: string
          description: 'Deprecated: Use `click.continent` instead.'
          deprecated: true
        country:
          type: string
          description: 'Deprecated: Use `click.country` instead.'
          deprecated: true
        city:
          type: string
          description: 'Deprecated: Use `click.city` instead.'
          deprecated: true
        device:
          type: string
          description: 'Deprecated: Use `click.device` instead.'
          deprecated: true
        browser:
          type: string
          description: 'Deprecated: Use `click.browser` instead.'
          deprecated: true
        os:
          type: string
          description: 'Deprecated: Use `click.os` instead.'
          deprecated: true
        qr:
          type: number
          description: 'Deprecated: Use `click.qr` instead.'
          deprecated: true
        ip:
          type: string
          description: 'Deprecated: Use `click.ip` instead.'
          deprecated: true
      required:
        - event
        - timestamp
        - click
        - link
        - click_id
        - link_id
        - domain
        - key
        - url
        - continent
        - country
        - city
        - device
        - browser
        - os
        - qr
        - ip
      title: ClickEvent
    LeadEvent:
      type: object
      properties:
        event:
          type: string
          enum:
            - lead
        timestamp:
          type: string
        eventId:
          type: string
        eventName:
          type: string
        metadata:
          nullable: true
        click:
          type: object
          properties:
            id:
              type: string
            timestamp:
              type: string
            url:
              type: string
            country:
              type: string
            city:
              type: string
            region:
              type: string
            continent:
              type: string
            device:
              type: string
            browser:
              type: string
            os:
              type: string
            trigger:
              type: string
              nullable: true
            referer:
              type: string
            refererUrl:
              type: string
            qr:
              type: boolean
            ip:
              type: string
          required:
            - id
            - timestamp
            - url
            - country
            - city
            - region
            - continent
            - device
            - browser
            - os
            - referer
            - refererUrl
            - qr
            - ip
        link:
          type: object
          properties:
            id:
              type: string
              description: The unique ID of the short link.
            domain:
              type: string
              description: >-
                The domain of the short link. If not provided, the primary
                domain for the workspace will be used (or `dub.sh` if the
                workspace has no domains).
            key:
              type: string
              description: >-
                The short link slug. If not provided, a random 7-character slug
                will be generated.
            url:
              type: string
            trackConversion:
              type: boolean
            externalId:
              type: string
              nullable: true
              description: >-
                The ID of the link in your database. If set, it can be used to
                identify the link in future API requests (must be prefixed with
                'ext_' when passed as a query parameter). This key is unique
                across your workspace.
            tenantId:
              type: string
              nullable: true
              description: >-
                The ID of the tenant that created the link inside your system.
                If set, it can be used to fetch all links for a tenant.
            programId:
              type: string
              nullable: true
              description: The ID of the program the short link is associated with.
            partnerId:
              type: string
              nullable: true
              description: The ID of the partner the short link is associated with.
            archived:
              type: boolean
            expiresAt:
              type: string
            expiredUrl:
              type: string
              nullable: true
            password:
              type: string
              nullable: true
              description: >-
                The password required to access the destination URL of the short
                link.
            proxy:
              type: boolean
            title:
              type: string
              nullable: true
              description: >-
                The title of the short link. Will be used for Custom Link
                Previews if `proxy` is true.
            description:
              type: string
              nullable: true
              description: >-
                The description of the short link. Will be used for Custom Link
                Previews if `proxy` is true.
            image:
              type: string
              nullable: true
              description: >-
                The image of the short link. Will be used for Custom Link
                Previews if `proxy` is true.
            video:
              type: string
              nullable: true
              description: >-
                The custom link preview video (og:video). Will be used for
                Custom Link Previews if `proxy` is true. Learn more:
                https://d.to/og
            rewrite:
              type: boolean
            doIndex:
              type: boolean
            ios:
              type: string
              nullable: true
              description: >-
                The iOS destination URL for the short link for iOS device
                targeting.
            android:
              type: string
              nullable: true
              description: >-
                The Android destination URL for the short link for Android
                device targeting.
            geo:
              type: object
              nullable: true
              additionalProperties:
                type: string
                format: uri
              description: >-
                Geo targeting information for the short link in JSON format
                `{[COUNTRY]: https://example.com }`. See https://d.to/geo for
                more information.
            publicStats:
              type: boolean
            tags:
              type: array
              nullable: true
              items:
                $ref: '#/components/schemas/LinkTagSchema'
              description: The tags assigned to the short link.
            folderId:
              type: string
              nullable: true
              description: The unique ID of the folder assigned to the short link.
            webhookIds:
              type: array
              items:
                type: string
              description: The IDs of the webhooks that the short link is associated with.
            comments:
              type: string
              nullable: true
              description: The comments for the short link.
            shortLink:
              type: string
              format: uri
              description: >-
                The full URL of the short link, including the https protocol
                (e.g. `https://dub.sh/try`).
            qrCode:
              type: string
              format: uri
              description: >-
                The full URL of the QR code for the short link (e.g.
                `https://api.dub.co/qr?url=https://dub.sh/try`).
            utm_source:
              type: string
              nullable: true
              description: The UTM source of the short link.
            utm_medium:
              type: string
              nullable: true
              description: The UTM medium of the short link.
            utm_campaign:
              type: string
              nullable: true
              description: The UTM campaign of the short link.
            utm_term:
              type: string
              nullable: true
              description: The UTM term of the short link.
            utm_content:
              type: string
              nullable: true
              description: The UTM content of the short link.
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
                An array of A/B test URLs and the percentage of traffic to send
                to each URL.
              example:
                - url: https://example.com/variant-1
                  percentage: 50
                - url: https://example.com/variant-2
                  percentage: 50
            testStartedAt:
              type: string
              nullable: true
            testCompletedAt:
              type: string
              nullable: true
            userId:
              type: string
              nullable: true
            workspaceId:
              type: string
              description: The workspace ID of the short link.
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
              description: The number of leads that converted to paying customers.
            sales:
              type: number
              default: 0
              description: >-
                The total number of sales (includes recurring sales) generated
                by the short link.
            saleAmount:
              type: number
              default: 0
              description: >-
                The total dollar value of sales (in cents) generated by the
                short link.
            lastClicked:
              type: string
            createdAt:
              type: string
            updatedAt:
              type: string
            tagId:
              type: string
              nullable: true
              description: >-
                Deprecated: Use `tags` instead. The unique ID of the tag
                assigned to the short link.
              deprecated: true
            projectId:
              type: string
              description: >-
                Deprecated: Use `workspaceId` instead. The project ID of the
                short link.
              deprecated: true
          required:
            - id
            - domain
            - key
            - url
            - trackConversion
            - externalId
            - tenantId
            - programId
            - partnerId
            - archived
            - expiresAt
            - expiredUrl
            - password
            - proxy
            - title
            - description
            - image
            - video
            - rewrite
            - doIndex
            - ios
            - android
            - geo
            - publicStats
            - tags
            - folderId
            - webhookIds
            - comments
            - shortLink
            - qrCode
            - utm_source
            - utm_medium
            - utm_campaign
            - utm_term
            - utm_content
            - testStartedAt
            - testCompletedAt
            - userId
            - workspaceId
            - clicks
            - leads
            - conversions
            - sales
            - saleAmount
            - lastClicked
            - createdAt
            - updatedAt
            - tagId
            - projectId
          title: Link
        customer:
          type: object
          properties:
            id:
              type: string
              description: >-
                The unique ID of the customer. You may use either the customer's
                `id` on Dub (obtained via `/customers` endpoint) or their
                `externalId` (unique ID within your system, prefixed with
                `ext_`, e.g. `ext_123`).
            externalId:
              type: string
              description: Unique identifier for the customer in the client's app.
            name:
              type: string
              description: Name of the customer.
            email:
              type: string
              nullable: true
              description: Email of the customer.
            avatar:
              type: string
              nullable: true
              description: Avatar URL of the customer.
            country:
              type: string
              nullable: true
              description: Country of the customer.
            sales:
              type: number
              nullable: true
              description: Total number of sales for the customer.
            saleAmount:
              type: number
              nullable: true
              description: Total amount of sales for the customer.
            createdAt:
              type: string
              description: The date the customer was created.
          required:
            - id
            - externalId
            - name
            - createdAt
        click_id:
          type: string
          description: 'Deprecated: Use `click.id` instead.'
          deprecated: true
        link_id:
          type: string
          description: 'Deprecated: Use `link.id` instead.'
          deprecated: true
        domain:
          type: string
          description: 'Deprecated: Use `link.domain` instead.'
          deprecated: true
        key:
          type: string
          description: 'Deprecated: Use `link.key` instead.'
          deprecated: true
        url:
          type: string
          description: 'Deprecated: Use `click.url` instead.'
          deprecated: true
        continent:
          type: string
          description: 'Deprecated: Use `click.continent` instead.'
          deprecated: true
        country:
          type: string
          description: 'Deprecated: Use `click.country` instead.'
          deprecated: true
        city:
          type: string
          description: 'Deprecated: Use `click.city` instead.'
          deprecated: true
        device:
          type: string
          description: 'Deprecated: Use `click.device` instead.'
          deprecated: true
        browser:
          type: string
          description: 'Deprecated: Use `click.browser` instead.'
          deprecated: true
        os:
          type: string
          description: 'Deprecated: Use `click.os` instead.'
          deprecated: true
        qr:
          type: number
          description: 'Deprecated: Use `click.qr` instead.'
          deprecated: true
        ip:
          type: string
          description: 'Deprecated: Use `click.ip` instead.'
          deprecated: true
      required:
        - event
        - timestamp
        - eventId
        - eventName
        - click
        - link
        - customer
        - click_id
        - link_id
        - domain
        - key
        - url
        - continent
        - country
        - city
        - device
        - browser
        - os
        - qr
        - ip
      title: LeadEvent
    SaleEvent:
      type: object
      properties:
        event:
          type: string
          enum:
            - sale
        timestamp:
          type: string
        eventId:
          type: string
        eventName:
          type: string
        sale:
          type: object
          properties:
            amount:
              type: integer
              minimum: 0
              description: >-
                The amount of the sale in cents (for all two-decimal
                currencies). If the sale is in a zero-decimal currency, pass the
                full integer value (e.g. `1437` JPY). Learn more:
                https://d.to/currency
            invoiceId:
              type: string
              nullable: true
              default: null
              description: >-
                The invoice ID of the sale. Can be used as a idempotency key –
                only one sale event can be recorded for a given invoice ID.
            paymentProcessor:
              type: string
              enum:
                - stripe
                - shopify
                - polar
                - paddle
                - revenuecat
                - custom
              default: custom
              description: The payment processor via which the sale was made.
          required:
            - amount
            - invoiceId
            - paymentProcessor
        metadata:
          nullable: true
        link:
          type: object
          properties:
            id:
              type: string
              description: The unique ID of the short link.
            domain:
              type: string
              description: >-
                The domain of the short link. If not provided, the primary
                domain for the workspace will be used (or `dub.sh` if the
                workspace has no domains).
            key:
              type: string
              description: >-
                The short link slug. If not provided, a random 7-character slug
                will be generated.
            url:
              type: string
            trackConversion:
              type: boolean
            externalId:
              type: string
              nullable: true
              description: >-
                The ID of the link in your database. If set, it can be used to
                identify the link in future API requests (must be prefixed with
                'ext_' when passed as a query parameter). This key is unique
                across your workspace.
            tenantId:
              type: string
              nullable: true
              description: >-
                The ID of the tenant that created the link inside your system.
                If set, it can be used to fetch all links for a tenant.
            programId:
              type: string
              nullable: true
              description: The ID of the program the short link is associated with.
            partnerId:
              type: string
              nullable: true
              description: The ID of the partner the short link is associated with.
            archived:
              type: boolean
            expiresAt:
              type: string
            expiredUrl:
              type: string
              nullable: true
            password:
              type: string
              nullable: true
              description: >-
                The password required to access the destination URL of the short
                link.
            proxy:
              type: boolean
            title:
              type: string
              nullable: true
              description: >-
                The title of the short link. Will be used for Custom Link
                Previews if `proxy` is true.
            description:
              type: string
              nullable: true
              description: >-
                The description of the short link. Will be used for Custom Link
                Previews if `proxy` is true.
            image:
              type: string
              nullable: true
              description: >-
                The image of the short link. Will be used for Custom Link
                Previews if `proxy` is true.
            video:
              type: string
              nullable: true
              description: >-
                The custom link preview video (og:video). Will be used for
                Custom Link Previews if `proxy` is true. Learn more:
                https://d.to/og
            rewrite:
              type: boolean
            doIndex:
              type: boolean
            ios:
              type: string
              nullable: true
              description: >-
                The iOS destination URL for the short link for iOS device
                targeting.
            android:
              type: string
              nullable: true
              description: >-
                The Android destination URL for the short link for Android
                device targeting.
            geo:
              type: object
              nullable: true
              additionalProperties:
                type: string
                format: uri
              description: >-
                Geo targeting information for the short link in JSON format
                `{[COUNTRY]: https://example.com }`. See https://d.to/geo for
                more information.
            publicStats:
              type: boolean
            tags:
              type: array
              nullable: true
              items:
                $ref: '#/components/schemas/LinkTagSchema'
              description: The tags assigned to the short link.
            folderId:
              type: string
              nullable: true
              description: The unique ID of the folder assigned to the short link.
            webhookIds:
              type: array
              items:
                type: string
              description: The IDs of the webhooks that the short link is associated with.
            comments:
              type: string
              nullable: true
              description: The comments for the short link.
            shortLink:
              type: string
              format: uri
              description: >-
                The full URL of the short link, including the https protocol
                (e.g. `https://dub.sh/try`).
            qrCode:
              type: string
              format: uri
              description: >-
                The full URL of the QR code for the short link (e.g.
                `https://api.dub.co/qr?url=https://dub.sh/try`).
            utm_source:
              type: string
              nullable: true
              description: The UTM source of the short link.
            utm_medium:
              type: string
              nullable: true
              description: The UTM medium of the short link.
            utm_campaign:
              type: string
              nullable: true
              description: The UTM campaign of the short link.
            utm_term:
              type: string
              nullable: true
              description: The UTM term of the short link.
            utm_content:
              type: string
              nullable: true
              description: The UTM content of the short link.
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
                An array of A/B test URLs and the percentage of traffic to send
                to each URL.
              example:
                - url: https://example.com/variant-1
                  percentage: 50
                - url: https://example.com/variant-2
                  percentage: 50
            testStartedAt:
              type: string
              nullable: true
            testCompletedAt:
              type: string
              nullable: true
            userId:
              type: string
              nullable: true
            workspaceId:
              type: string
              description: The workspace ID of the short link.
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
              description: The number of leads that converted to paying customers.
            sales:
              type: number
              default: 0
              description: >-
                The total number of sales (includes recurring sales) generated
                by the short link.
            saleAmount:
              type: number
              default: 0
              description: >-
                The total dollar value of sales (in cents) generated by the
                short link.
            lastClicked:
              type: string
            createdAt:
              type: string
            updatedAt:
              type: string
            tagId:
              type: string
              nullable: true
              description: >-
                Deprecated: Use `tags` instead. The unique ID of the tag
                assigned to the short link.
              deprecated: true
            projectId:
              type: string
              description: >-
                Deprecated: Use `workspaceId` instead. The project ID of the
                short link.
              deprecated: true
          required:
            - id
            - domain
            - key
            - url
            - trackConversion
            - externalId
            - tenantId
            - programId
            - partnerId
            - archived
            - expiresAt
            - expiredUrl
            - password
            - proxy
            - title
            - description
            - image
            - video
            - rewrite
            - doIndex
            - ios
            - android
            - geo
            - publicStats
            - tags
            - folderId
            - webhookIds
            - comments
            - shortLink
            - qrCode
            - utm_source
            - utm_medium
            - utm_campaign
            - utm_term
            - utm_content
            - testStartedAt
            - testCompletedAt
            - userId
            - workspaceId
            - clicks
            - leads
            - conversions
            - sales
            - saleAmount
            - lastClicked
            - createdAt
            - updatedAt
            - tagId
            - projectId
          title: Link
        click:
          type: object
          properties:
            id:
              type: string
            timestamp:
              type: string
            url:
              type: string
            country:
              type: string
            city:
              type: string
            region:
              type: string
            continent:
              type: string
            device:
              type: string
            browser:
              type: string
            os:
              type: string
            trigger:
              type: string
              nullable: true
            referer:
              type: string
            refererUrl:
              type: string
            qr:
              type: boolean
            ip:
              type: string
          required:
            - id
            - timestamp
            - url
            - country
            - city
            - region
            - continent
            - device
            - browser
            - os
            - referer
            - refererUrl
            - qr
            - ip
        customer:
          type: object
          properties:
            id:
              type: string
              description: >-
                The unique ID of the customer. You may use either the customer's
                `id` on Dub (obtained via `/customers` endpoint) or their
                `externalId` (unique ID within your system, prefixed with
                `ext_`, e.g. `ext_123`).
            externalId:
              type: string
              description: Unique identifier for the customer in the client's app.
            name:
              type: string
              description: Name of the customer.
            email:
              type: string
              nullable: true
              description: Email of the customer.
            avatar:
              type: string
              nullable: true
              description: Avatar URL of the customer.
            country:
              type: string
              nullable: true
              description: Country of the customer.
            sales:
              type: number
              nullable: true
              description: Total number of sales for the customer.
            saleAmount:
              type: number
              nullable: true
              description: Total amount of sales for the customer.
            createdAt:
              type: string
              description: The date the customer was created.
          required:
            - id
            - externalId
            - name
            - createdAt
        saleAmount:
          type: number
          description: 'Deprecated: Use `sale.amount` instead.'
          deprecated: true
        invoice_id:
          type: string
          description: 'Deprecated: Use `sale.invoiceId` instead.'
          deprecated: true
        payment_processor:
          type: string
          description: 'Deprecated: Use `sale.paymentProcessor` instead.'
          deprecated: true
        click_id:
          type: string
          description: 'Deprecated: Use `click.id` instead.'
          deprecated: true
        link_id:
          type: string
          description: 'Deprecated: Use `link.id` instead.'
          deprecated: true
        domain:
          type: string
          description: 'Deprecated: Use `link.domain` instead.'
          deprecated: true
        key:
          type: string
          description: 'Deprecated: Use `link.key` instead.'
          deprecated: true
        url:
          type: string
          description: 'Deprecated: Use `click.url` instead.'
          deprecated: true
        continent:
          type: string
          description: 'Deprecated: Use `click.continent` instead.'
          deprecated: true
        country:
          type: string
          description: 'Deprecated: Use `click.country` instead.'
          deprecated: true
        city:
          type: string
          description: 'Deprecated: Use `click.city` instead.'
          deprecated: true
        device:
          type: string
          description: 'Deprecated: Use `click.device` instead.'
          deprecated: true
        browser:
          type: string
          description: 'Deprecated: Use `click.browser` instead.'
          deprecated: true
        os:
          type: string
          description: 'Deprecated: Use `click.os` instead.'
          deprecated: true
        qr:
          type: number
          description: 'Deprecated: Use `click.qr` instead.'
          deprecated: true
        ip:
          type: string
          description: 'Deprecated: Use `click.ip` instead.'
          deprecated: true
      required:
        - event
        - timestamp
        - eventId
        - eventName
        - sale
        - link
        - click
        - customer
        - saleAmount
        - invoice_id
        - payment_processor
        - click_id
        - link_id
        - domain
        - key
        - url
        - continent
        - country
        - city
        - device
        - browser
        - os
        - qr
        - ip
      title: SaleEvent

````