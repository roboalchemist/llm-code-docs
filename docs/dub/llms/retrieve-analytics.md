# Source: https://dub.co/docs/api-reference/endpoint/retrieve-analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve analytics

> Retrieve analytics for a link, a domain, or the authenticated workspace. The response type depends on the `event` and `type` query parameters.

<Note>
  Analytics endpoints require a [Pro plan](https://dub.co/pricing) subscription
  or higher.
</Note>


## OpenAPI

````yaml get /analytics
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
  /analytics:
    get:
      tags:
        - Analytics
      summary: Retrieve analytics for a link, a domain, or the authenticated workspace.
      description: >-
        Retrieve analytics for a link, a domain, or the authenticated workspace.
        The response type depends on the `event` and `type` query parameters.
      operationId: retrieveAnalytics
      parameters:
        - in: query
          name: event
          schema:
            default: clicks
            description: The type of event to retrieve analytics for. Defaults to `clicks`.
            example: leads
            type: string
            enum:
              - clicks
              - leads
              - sales
              - composite
          description: The type of event to retrieve analytics for. Defaults to `clicks`.
        - in: query
          name: groupBy
          schema:
            default: count
            description: >-
              The parameter to group the analytics data points by. Defaults to
              `count` if undefined.
            type: string
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
              - top_base_urls
              - top_partners
              - top_groups
              - utm_sources
              - utm_mediums
              - utm_campaigns
              - utm_terms
              - utm_contents
          description: >-
            The parameter to group the analytics data points by. Defaults to
            `count` if undefined.
        - in: query
          name: domain
          schema:
            description: The domain to filter analytics for.
            type: string
          description: The domain to filter analytics for.
        - in: query
          name: key
          schema:
            description: >-
              The slug of the short link to retrieve analytics for. Must be used
              along with the corresponding `domain` of the short link to fetch
              analytics for a specific short link.
            type: string
          description: >-
            The slug of the short link to retrieve analytics for. Must be used
            along with the corresponding `domain` of the short link to fetch
            analytics for a specific short link.
        - in: query
          name: linkId
          schema:
            description: The unique ID of the short link on Dub to retrieve analytics for.
            type: string
          description: The unique ID of the short link on Dub to retrieve analytics for.
        - in: query
          name: externalId
          schema:
            description: >-
              The ID of the link in the your database. Must be prefixed with
              'ext_' when passed as a query parameter.
            type: string
          description: >-
            The ID of the link in the your database. Must be prefixed with
            'ext_' when passed as a query parameter.
        - in: query
          name: tenantId
          schema:
            description: The ID of the tenant that created the link inside your system.
            type: string
          description: The ID of the tenant that created the link inside your system.
        - in: query
          name: programId
          schema:
            description: The ID of the program to retrieve analytics for.
            type: string
          description: The ID of the program to retrieve analytics for.
        - in: query
          name: partnerId
          schema:
            description: The ID of the partner to retrieve analytics for.
            type: string
          description: The ID of the partner to retrieve analytics for.
        - in: query
          name: customerId
          schema:
            description: The ID of the customer to retrieve analytics for.
            type: string
          description: The ID of the customer to retrieve analytics for.
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
          name: country
          schema:
            description: >-
              The country to retrieve analytics for. Must be passed as a
              2-letter ISO 3166-1 country code. See https://d.to/geo for more
              information.
            type: string
          description: >-
            The country to retrieve analytics for. Must be passed as a 2-letter
            ISO 3166-1 country code. See https://d.to/geo for more information.
        - in: query
          name: city
          schema:
            description: The city to retrieve analytics for.
            example: New York
            type: string
          description: The city to retrieve analytics for.
        - in: query
          name: region
          schema:
            description: The ISO 3166-2 region code to retrieve analytics for.
            type: string
          description: The ISO 3166-2 region code to retrieve analytics for.
        - in: query
          name: continent
          schema:
            description: The continent to retrieve analytics for.
            type: string
            enum:
              - AF
              - AN
              - AS
              - EU
              - NA
              - OC
              - SA
          description: The continent to retrieve analytics for.
        - in: query
          name: device
          schema:
            description: The device to retrieve analytics for.
            example: Desktop
            type: string
          description: The device to retrieve analytics for.
        - in: query
          name: browser
          schema:
            description: The browser to retrieve analytics for.
            example: Chrome
            type: string
          description: The browser to retrieve analytics for.
        - in: query
          name: os
          schema:
            description: The OS to retrieve analytics for.
            example: Windows
            type: string
          description: The OS to retrieve analytics for.
        - in: query
          name: trigger
          schema:
            description: >-
              The trigger to retrieve analytics for. If undefined, returns all
              trigger types.
            type: string
            enum:
              - qr
              - link
              - pageview
              - deeplink
          description: >-
            The trigger to retrieve analytics for. If undefined, returns all
            trigger types.
        - in: query
          name: referer
          schema:
            description: The referer hostname to retrieve analytics for.
            example: google.com
            type: string
          description: The referer hostname to retrieve analytics for.
        - in: query
          name: refererUrl
          schema:
            description: The full referer URL to retrieve analytics for.
            example: https://dub.co/blog
            type: string
          description: The full referer URL to retrieve analytics for.
        - in: query
          name: url
          schema:
            description: The URL to retrieve analytics for.
            type: string
          description: The URL to retrieve analytics for.
        - in: query
          name: tagIds
          schema:
            description: The tag IDs to retrieve analytics for.
            anyOf:
              - type: string
              - type: array
                items:
                  type: string
          description: The tag IDs to retrieve analytics for.
        - in: query
          name: folderId
          schema:
            description: >-
              The folder ID to retrieve analytics for. If not provided, return
              analytics for unsorted links.
            type: string
          description: >-
            The folder ID to retrieve analytics for. If not provided, return
            analytics for unsorted links.
        - in: query
          name: groupId
          schema:
            description: The group ID to retrieve analytics for.
            type: string
          description: The group ID to retrieve analytics for.
        - in: query
          name: root
          schema:
            description: >-
              Filter for root domains. If true, filter for domains only. If
              false, filter for links only. If undefined, return both.
            type: boolean
          description: >-
            Filter for root domains. If true, filter for domains only. If false,
            filter for links only. If undefined, return both.
        - in: query
          name: saleType
          schema:
            description: >-
              Filter sales by type: 'new' for first-time purchases, 'recurring'
              for repeat purchases. If undefined, returns both.
            type: string
            enum:
              - new
              - recurring
          description: >-
            Filter sales by type: 'new' for first-time purchases, 'recurring'
            for repeat purchases. If undefined, returns both.
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
          name: tagId
          schema:
            description: >-
              Deprecated: Use `tagIds` instead. The tag ID to retrieve analytics
              for.
            deprecated: true
            type: string
          description: >-
            Deprecated: Use `tagIds` instead. The tag ID to retrieve analytics
            for.
        - in: query
          name: qr
          schema:
            description: >-
              Deprecated: Use the `trigger` field instead. Filter for QR code
              scans. If true, filter for QR codes only. If false, filter for
              links only. If undefined, return both.
            deprecated: true
            type: boolean
          description: >-
            Deprecated: Use the `trigger` field instead. Filter for QR code
            scans. If true, filter for QR codes only. If false, filter for links
            only. If undefined, return both.
        - in: query
          name: utm_source
          schema:
            description: The UTM source of the short link.
            nullable: true
            type: string
            maxLength: 190
          description: The UTM source of the short link.
        - in: query
          name: utm_medium
          schema:
            description: The UTM medium of the short link.
            nullable: true
            type: string
            maxLength: 190
          description: The UTM medium of the short link.
        - in: query
          name: utm_campaign
          schema:
            description: The UTM campaign of the short link.
            nullable: true
            type: string
            maxLength: 190
          description: The UTM campaign of the short link.
        - in: query
          name: utm_term
          schema:
            description: The UTM term of the short link.
            nullable: true
            type: string
            maxLength: 190
          description: The UTM term of the short link.
        - in: query
          name: utm_content
          schema:
            description: The UTM content of the short link.
            nullable: true
            type: string
            maxLength: 190
          description: The UTM content of the short link.
        - in: query
          name: ref
          schema:
            description: The ref of the short link.
            nullable: true
            type: string
            maxLength: 190
          description: The ref of the short link.
      responses:
        '200':
          description: Analytics data
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/AnalyticsCount'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsTimeseries'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsContinents'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsCountries'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsRegions'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsCities'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsDevices'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsBrowsers'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsOS'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsTriggers'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsReferers'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsRefererUrls'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsTopLinks'
                  - type: array
                    items:
                      $ref: '#/components/schemas/AnalyticsTopUrls'
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
    AnalyticsCount:
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
      required:
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
    AnalyticsTimeseries:
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
      required:
        - start
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
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
          default: 0
          type: number
          description: The number of clicks from this continent
        leads:
          default: 0
          type: number
          description: The number of leads from this continent
        sales:
          default: 0
          type: number
          description: The number of sales from this continent
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this continent, in cents
      required:
        - continent
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
    AnalyticsCountries:
      type: object
      properties:
        country:
          type: string
          description: >-
            The 2-letter ISO 3166-1 country code of the country. Learn more:
            https://d.to/geo
        region:
          default: '*'
          type: string
          enum:
            - '*'
        city:
          default: '*'
          type: string
          enum:
            - '*'
        clicks:
          default: 0
          type: number
          description: The number of clicks from this country
        leads:
          default: 0
          type: number
          description: The number of leads from this country
        sales:
          default: 0
          type: number
          description: The number of sales from this country
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this country, in cents
      required:
        - country
        - region
        - city
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
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
          default: '*'
          type: string
          enum:
            - '*'
        clicks:
          default: 0
          type: number
          description: The number of clicks from this region
        leads:
          default: 0
          type: number
          description: The number of leads from this region
        sales:
          default: 0
          type: number
          description: The number of sales from this region
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this region, in cents
      required:
        - country
        - region
        - city
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
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
          default: 0
          type: number
          description: The number of clicks from this city
        leads:
          default: 0
          type: number
          description: The number of leads from this city
        sales:
          default: 0
          type: number
          description: The number of sales from this city
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this city, in cents
      required:
        - country
        - region
        - city
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
    AnalyticsDevices:
      type: object
      properties:
        device:
          type: string
          description: The name of the device
        clicks:
          default: 0
          type: number
          description: The number of clicks from this device
        leads:
          default: 0
          type: number
          description: The number of leads from this device
        sales:
          default: 0
          type: number
          description: The number of sales from this device
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this device, in cents
      required:
        - device
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
    AnalyticsBrowsers:
      type: object
      properties:
        browser:
          type: string
          description: The name of the browser
        clicks:
          default: 0
          type: number
          description: The number of clicks from this browser
        leads:
          default: 0
          type: number
          description: The number of leads from this browser
        sales:
          default: 0
          type: number
          description: The number of sales from this browser
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this browser, in cents
      required:
        - browser
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
    AnalyticsOS:
      type: object
      properties:
        os:
          type: string
          description: The name of the OS
        clicks:
          default: 0
          type: number
          description: The number of clicks from this OS
        leads:
          default: 0
          type: number
          description: The number of leads from this OS
        sales:
          default: 0
          type: number
          description: The number of sales from this OS
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this OS, in cents
      required:
        - os
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
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
          default: 0
          type: number
          description: The number of clicks from this trigger method
        leads:
          default: 0
          type: number
          description: The number of leads from this trigger method
        sales:
          default: 0
          type: number
          description: The number of sales from this trigger method
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this trigger method, in cents
      required:
        - trigger
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
    AnalyticsReferers:
      type: object
      properties:
        referer:
          type: string
          description: The name of the referer. If unknown, this will be `(direct)`
        clicks:
          default: 0
          type: number
          description: The number of clicks from this referer
        leads:
          default: 0
          type: number
          description: The number of leads from this referer
        sales:
          default: 0
          type: number
          description: The number of sales from this referer
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this referer, in cents
      required:
        - referer
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
    AnalyticsRefererUrls:
      type: object
      properties:
        refererUrl:
          type: string
          description: The full URL of the referer. If unknown, this will be `(direct)`
        clicks:
          default: 0
          type: number
          description: The number of clicks from this referer to this URL
        leads:
          default: 0
          type: number
          description: The number of leads from this referer to this URL
        sales:
          default: 0
          type: number
          description: The number of sales from this referer to this URL
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this referer to this URL, in cents
      required:
        - refererUrl
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
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
      additionalProperties: false
    AnalyticsTopUrls:
      type: object
      properties:
        url:
          type: string
          description: The full destination URL (including query parameters)
        clicks:
          default: 0
          type: number
          description: The number of clicks from this URL
        leads:
          default: 0
          type: number
          description: The number of leads from this URL
        sales:
          default: 0
          type: number
          description: The number of sales from this URL
        saleAmount:
          default: 0
          type: number
          description: The total amount of sales from this URL, in cents
      required:
        - url
        - clicks
        - leads
        - sales
        - saleAmount
      additionalProperties: false
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