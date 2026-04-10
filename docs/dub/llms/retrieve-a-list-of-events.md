# Source: https://dub.co/docs/api-reference/endpoint/retrieve-a-list-of-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a list of events

> Retrieve a paginated list of events for the authenticated workspace.

<Note>
  Events endpoints require a [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>


## OpenAPI

````yaml get /events
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
  /events:
    get:
      tags:
        - Events
      summary: Retrieve a list of events
      description: Retrieve a paginated list of events for the authenticated workspace.
      operationId: listEvents
      parameters:
        - in: query
          name: event
          schema:
            default: clicks
            description: The type of event to retrieve analytics for. Defaults to 'clicks'.
            type: string
            enum:
              - clicks
              - leads
              - sales
          description: The type of event to retrieve analytics for. Defaults to 'clicks'.
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
        - in: query
          name: page
          schema:
            default: 1
            type: number
        - in: query
          name: limit
          schema:
            default: 100
            type: number
            maximum: 1000
        - in: query
          name: sortOrder
          schema:
            default: desc
            description: The sort order. The default is `desc`.
            type: string
            enum:
              - asc
              - desc
          description: The sort order. The default is `desc`.
        - in: query
          name: sortBy
          schema:
            default: timestamp
            description: The field to sort the events by. The default is `timestamp`.
            type: string
            enum:
              - timestamp
          description: The field to sort the events by. The default is `timestamp`.
        - in: query
          name: order
          schema:
            description: DEPRECATED. Use `sortOrder` instead.
            deprecated: true
            default: desc
            type: string
            enum:
              - asc
              - desc
          description: DEPRECATED. Use `sortOrder` instead.
      responses:
        '200':
          description: A list of events
          content:
            application/json:
              schema:
                type: array
                items:
                  oneOf:
                    - type: object
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
                              nullable: true
                              type: string
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
                          additionalProperties: false
                        link:
                          type: object
                          properties:
                            id:
                              type: string
                              description: The unique ID of the short link.
                            domain:
                              type: string
                              description: >-
                                The domain of the short link. If not provided,
                                the primary domain for the workspace will be
                                used (or `dub.sh` if the workspace has no
                                domains).
                            key:
                              type: string
                              description: >-
                                The short link slug. If not provided, a random
                                7-character slug will be generated.
                            url:
                              type: string
                            trackConversion:
                              type: boolean
                            externalId:
                              nullable: true
                              description: >-
                                The ID of the link in your database. If set, it
                                can be used to identify the link in future API
                                requests (must be prefixed with 'ext_' when
                                passed as a query parameter). This key is unique
                                across your workspace.
                              type: string
                            tenantId:
                              nullable: true
                              description: >-
                                The ID of the tenant that created the link
                                inside your system. If set, it can be used to
                                fetch all links for a tenant.
                              type: string
                            programId:
                              nullable: true
                              description: >-
                                The ID of the program the short link is
                                associated with.
                              type: string
                            partnerId:
                              nullable: true
                              description: >-
                                The ID of the partner the short link is
                                associated with.
                              type: string
                            archived:
                              type: boolean
                            expiresAt:
                              type: string
                            expiredUrl:
                              nullable: true
                              type: string
                            disabledAt:
                              type: string
                            password:
                              nullable: true
                              description: >-
                                The password required to access the destination
                                URL of the short link.
                              type: string
                            proxy:
                              type: boolean
                            title:
                              nullable: true
                              description: >-
                                The title of the short link. Will be used for
                                Custom Link Previews if `proxy` is true.
                              type: string
                            description:
                              nullable: true
                              description: >-
                                The description of the short link. Will be used
                                for Custom Link Previews if `proxy` is true.
                              type: string
                            image:
                              nullable: true
                              description: >-
                                The image of the short link. Will be used for
                                Custom Link Previews if `proxy` is true.
                              type: string
                            video:
                              nullable: true
                              description: >-
                                The custom link preview video (og:video). Will
                                be used for Custom Link Previews if `proxy` is
                                true. Learn more: https://d.to/og
                              type: string
                            rewrite:
                              type: boolean
                            doIndex:
                              type: boolean
                            ios:
                              nullable: true
                              description: >-
                                The iOS destination URL for the short link for
                                iOS device targeting.
                              type: string
                            android:
                              nullable: true
                              description: >-
                                The Android destination URL for the short link
                                for Android device targeting.
                              type: string
                            geo:
                              nullable: true
                              description: >-
                                Geo targeting information for the short link in
                                JSON format `{[COUNTRY]: https://example.com }`.
                                See https://d.to/geo for more information.
                              type: object
                              additionalProperties:
                                type: string
                                format: uri
                            publicStats:
                              type: boolean
                            tags:
                              nullable: true
                              description: The tags assigned to the short link.
                              type: array
                              items:
                                $ref: '#/components/schemas/LinkTagSchemaOutput'
                            folderId:
                              nullable: true
                              description: >-
                                The unique ID of the folder assigned to the
                                short link.
                              type: string
                            webhookIds:
                              type: array
                              items:
                                type: string
                              description: >-
                                The IDs of the webhooks that the short link is
                                associated with.
                            comments:
                              nullable: true
                              description: The comments for the short link.
                              type: string
                            shortLink:
                              type: string
                              format: uri
                              description: >-
                                The full URL of the short link, including the
                                https protocol (e.g. `https://dub.sh/try`).
                            qrCode:
                              type: string
                              format: uri
                              description: >-
                                The full URL of the QR code for the short link
                                (e.g.
                                `https://api.dub.co/qr?url=https://dub.sh/try`).
                            utm_source:
                              nullable: true
                              description: The UTM source of the short link.
                              type: string
                            utm_medium:
                              nullable: true
                              description: The UTM medium of the short link.
                              type: string
                            utm_campaign:
                              nullable: true
                              description: The UTM campaign of the short link.
                              type: string
                            utm_term:
                              nullable: true
                              description: The UTM term of the short link.
                              type: string
                            utm_content:
                              nullable: true
                              description: The UTM content of the short link.
                              type: string
                            testVariants:
                              nullable: true
                              minItems: 2
                              maxItems: 4
                              type: array
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
                                additionalProperties: false
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
                            testCompletedAt:
                              type: string
                            userId:
                              nullable: true
                              type: string
                            workspaceId:
                              type: string
                              description: The workspace ID of the short link.
                            clicks:
                              default: 0
                              description: The number of clicks on the short link.
                              type: number
                            leads:
                              default: 0
                              description: >-
                                The number of leads the short link has
                                generated.
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
                            lastClicked:
                              type: string
                            createdAt:
                              type: string
                            updatedAt:
                              type: string
                            tagId:
                              nullable: true
                              description: >-
                                Deprecated: Use `tags` instead. The unique ID of
                                the tag assigned to the short link.
                              deprecated: true
                              type: string
                            projectId:
                              type: string
                              description: >-
                                Deprecated: Use `workspaceId` instead. The
                                project ID of the short link.
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
                            - disabledAt
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
                          additionalProperties: false
                        click_id:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.id` instead.'
                        link_id:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `link.id` instead.'
                        domain:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `link.domain` instead.'
                        key:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `link.key` instead.'
                        url:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.url` instead.'
                        continent:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.continent` instead.'
                        country:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.country` instead.'
                        city:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.city` instead.'
                        device:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.device` instead.'
                        browser:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.browser` instead.'
                        os:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.os` instead.'
                        qr:
                          type: number
                          deprecated: true
                          description: 'Deprecated: Use `click.qr` instead.'
                        ip:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.ip` instead.'
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
                      additionalProperties: false
                      title: ClickEvent
                    - type: object
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
                              nullable: true
                              type: string
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
                          additionalProperties: false
                        link:
                          type: object
                          properties:
                            id:
                              type: string
                              description: The unique ID of the short link.
                            domain:
                              type: string
                              description: >-
                                The domain of the short link. If not provided,
                                the primary domain for the workspace will be
                                used (or `dub.sh` if the workspace has no
                                domains).
                            key:
                              type: string
                              description: >-
                                The short link slug. If not provided, a random
                                7-character slug will be generated.
                            url:
                              type: string
                            trackConversion:
                              type: boolean
                            externalId:
                              nullable: true
                              description: >-
                                The ID of the link in your database. If set, it
                                can be used to identify the link in future API
                                requests (must be prefixed with 'ext_' when
                                passed as a query parameter). This key is unique
                                across your workspace.
                              type: string
                            tenantId:
                              nullable: true
                              description: >-
                                The ID of the tenant that created the link
                                inside your system. If set, it can be used to
                                fetch all links for a tenant.
                              type: string
                            programId:
                              nullable: true
                              description: >-
                                The ID of the program the short link is
                                associated with.
                              type: string
                            partnerId:
                              nullable: true
                              description: >-
                                The ID of the partner the short link is
                                associated with.
                              type: string
                            archived:
                              type: boolean
                            expiresAt:
                              type: string
                            expiredUrl:
                              nullable: true
                              type: string
                            disabledAt:
                              type: string
                            password:
                              nullable: true
                              description: >-
                                The password required to access the destination
                                URL of the short link.
                              type: string
                            proxy:
                              type: boolean
                            title:
                              nullable: true
                              description: >-
                                The title of the short link. Will be used for
                                Custom Link Previews if `proxy` is true.
                              type: string
                            description:
                              nullable: true
                              description: >-
                                The description of the short link. Will be used
                                for Custom Link Previews if `proxy` is true.
                              type: string
                            image:
                              nullable: true
                              description: >-
                                The image of the short link. Will be used for
                                Custom Link Previews if `proxy` is true.
                              type: string
                            video:
                              nullable: true
                              description: >-
                                The custom link preview video (og:video). Will
                                be used for Custom Link Previews if `proxy` is
                                true. Learn more: https://d.to/og
                              type: string
                            rewrite:
                              type: boolean
                            doIndex:
                              type: boolean
                            ios:
                              nullable: true
                              description: >-
                                The iOS destination URL for the short link for
                                iOS device targeting.
                              type: string
                            android:
                              nullable: true
                              description: >-
                                The Android destination URL for the short link
                                for Android device targeting.
                              type: string
                            geo:
                              nullable: true
                              description: >-
                                Geo targeting information for the short link in
                                JSON format `{[COUNTRY]: https://example.com }`.
                                See https://d.to/geo for more information.
                              type: object
                              additionalProperties:
                                type: string
                                format: uri
                            publicStats:
                              type: boolean
                            tags:
                              nullable: true
                              description: The tags assigned to the short link.
                              type: array
                              items:
                                $ref: '#/components/schemas/LinkTagSchemaOutput'
                            folderId:
                              nullable: true
                              description: >-
                                The unique ID of the folder assigned to the
                                short link.
                              type: string
                            webhookIds:
                              type: array
                              items:
                                type: string
                              description: >-
                                The IDs of the webhooks that the short link is
                                associated with.
                            comments:
                              nullable: true
                              description: The comments for the short link.
                              type: string
                            shortLink:
                              type: string
                              format: uri
                              description: >-
                                The full URL of the short link, including the
                                https protocol (e.g. `https://dub.sh/try`).
                            qrCode:
                              type: string
                              format: uri
                              description: >-
                                The full URL of the QR code for the short link
                                (e.g.
                                `https://api.dub.co/qr?url=https://dub.sh/try`).
                            utm_source:
                              nullable: true
                              description: The UTM source of the short link.
                              type: string
                            utm_medium:
                              nullable: true
                              description: The UTM medium of the short link.
                              type: string
                            utm_campaign:
                              nullable: true
                              description: The UTM campaign of the short link.
                              type: string
                            utm_term:
                              nullable: true
                              description: The UTM term of the short link.
                              type: string
                            utm_content:
                              nullable: true
                              description: The UTM content of the short link.
                              type: string
                            testVariants:
                              nullable: true
                              minItems: 2
                              maxItems: 4
                              type: array
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
                                additionalProperties: false
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
                            testCompletedAt:
                              type: string
                            userId:
                              nullable: true
                              type: string
                            workspaceId:
                              type: string
                              description: The workspace ID of the short link.
                            clicks:
                              default: 0
                              description: The number of clicks on the short link.
                              type: number
                            leads:
                              default: 0
                              description: >-
                                The number of leads the short link has
                                generated.
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
                            lastClicked:
                              type: string
                            createdAt:
                              type: string
                            updatedAt:
                              type: string
                            tagId:
                              nullable: true
                              description: >-
                                Deprecated: Use `tags` instead. The unique ID of
                                the tag assigned to the short link.
                              deprecated: true
                              type: string
                            projectId:
                              type: string
                              description: >-
                                Deprecated: Use `workspaceId` instead. The
                                project ID of the short link.
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
                            - disabledAt
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
                          additionalProperties: false
                        customer:
                          type: object
                          properties:
                            id:
                              type: string
                              description: >-
                                The unique ID of the customer. You may use
                                either the customer's `id` on Dub (obtained via
                                `/customers` endpoint) or their `externalId`
                                (unique ID within your system, prefixed with
                                `ext_`, e.g. `ext_123`).
                            externalId:
                              type: string
                              description: >-
                                Unique identifier for the customer in the
                                client's app.
                            name:
                              type: string
                              description: Name of the customer.
                            email:
                              description: Email of the customer.
                              nullable: true
                              type: string
                            avatar:
                              description: Avatar URL of the customer.
                              nullable: true
                              type: string
                            country:
                              description: Country of the customer.
                              nullable: true
                              type: string
                            sales:
                              description: Total number of sales for the customer.
                              nullable: true
                              type: number
                            saleAmount:
                              description: Total amount of sales for the customer.
                              nullable: true
                              type: number
                            createdAt:
                              description: The date the customer was created.
                              type: string
                          required:
                            - id
                            - externalId
                            - name
                            - createdAt
                          additionalProperties: false
                        click_id:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.id` instead.'
                        link_id:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `link.id` instead.'
                        domain:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `link.domain` instead.'
                        key:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `link.key` instead.'
                        url:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.url` instead.'
                        continent:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.continent` instead.'
                        country:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.country` instead.'
                        city:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.city` instead.'
                        device:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.device` instead.'
                        browser:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.browser` instead.'
                        os:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.os` instead.'
                        qr:
                          type: number
                          deprecated: true
                          description: 'Deprecated: Use `click.qr` instead.'
                        ip:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.ip` instead.'
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
                      additionalProperties: false
                      title: LeadEvent
                    - type: object
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
                              maximum: 9007199254740991
                              description: >-
                                The amount of the sale in cents (for all
                                two-decimal currencies). If the sale is in a
                                zero-decimal currency, pass the full integer
                                value (e.g. `1437` JPY). Learn more:
                                https://d.to/currency
                            invoiceId:
                              default: null
                              description: >-
                                The invoice ID of the sale. Can be used as a
                                idempotency key – only one sale event can be
                                recorded for a given invoice ID.
                              nullable: true
                              type: string
                            paymentProcessor:
                              default: custom
                              description: >-
                                The payment processor via which the sale was
                                made.
                              type: string
                              enum:
                                - stripe
                                - shopify
                                - polar
                                - paddle
                                - revenuecat
                                - custom
                          required:
                            - amount
                            - invoiceId
                            - paymentProcessor
                          additionalProperties: false
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
                                The domain of the short link. If not provided,
                                the primary domain for the workspace will be
                                used (or `dub.sh` if the workspace has no
                                domains).
                            key:
                              type: string
                              description: >-
                                The short link slug. If not provided, a random
                                7-character slug will be generated.
                            url:
                              type: string
                            trackConversion:
                              type: boolean
                            externalId:
                              nullable: true
                              description: >-
                                The ID of the link in your database. If set, it
                                can be used to identify the link in future API
                                requests (must be prefixed with 'ext_' when
                                passed as a query parameter). This key is unique
                                across your workspace.
                              type: string
                            tenantId:
                              nullable: true
                              description: >-
                                The ID of the tenant that created the link
                                inside your system. If set, it can be used to
                                fetch all links for a tenant.
                              type: string
                            programId:
                              nullable: true
                              description: >-
                                The ID of the program the short link is
                                associated with.
                              type: string
                            partnerId:
                              nullable: true
                              description: >-
                                The ID of the partner the short link is
                                associated with.
                              type: string
                            archived:
                              type: boolean
                            expiresAt:
                              type: string
                            expiredUrl:
                              nullable: true
                              type: string
                            disabledAt:
                              type: string
                            password:
                              nullable: true
                              description: >-
                                The password required to access the destination
                                URL of the short link.
                              type: string
                            proxy:
                              type: boolean
                            title:
                              nullable: true
                              description: >-
                                The title of the short link. Will be used for
                                Custom Link Previews if `proxy` is true.
                              type: string
                            description:
                              nullable: true
                              description: >-
                                The description of the short link. Will be used
                                for Custom Link Previews if `proxy` is true.
                              type: string
                            image:
                              nullable: true
                              description: >-
                                The image of the short link. Will be used for
                                Custom Link Previews if `proxy` is true.
                              type: string
                            video:
                              nullable: true
                              description: >-
                                The custom link preview video (og:video). Will
                                be used for Custom Link Previews if `proxy` is
                                true. Learn more: https://d.to/og
                              type: string
                            rewrite:
                              type: boolean
                            doIndex:
                              type: boolean
                            ios:
                              nullable: true
                              description: >-
                                The iOS destination URL for the short link for
                                iOS device targeting.
                              type: string
                            android:
                              nullable: true
                              description: >-
                                The Android destination URL for the short link
                                for Android device targeting.
                              type: string
                            geo:
                              nullable: true
                              description: >-
                                Geo targeting information for the short link in
                                JSON format `{[COUNTRY]: https://example.com }`.
                                See https://d.to/geo for more information.
                              type: object
                              additionalProperties:
                                type: string
                                format: uri
                            publicStats:
                              type: boolean
                            tags:
                              nullable: true
                              description: The tags assigned to the short link.
                              type: array
                              items:
                                $ref: '#/components/schemas/LinkTagSchemaOutput'
                            folderId:
                              nullable: true
                              description: >-
                                The unique ID of the folder assigned to the
                                short link.
                              type: string
                            webhookIds:
                              type: array
                              items:
                                type: string
                              description: >-
                                The IDs of the webhooks that the short link is
                                associated with.
                            comments:
                              nullable: true
                              description: The comments for the short link.
                              type: string
                            shortLink:
                              type: string
                              format: uri
                              description: >-
                                The full URL of the short link, including the
                                https protocol (e.g. `https://dub.sh/try`).
                            qrCode:
                              type: string
                              format: uri
                              description: >-
                                The full URL of the QR code for the short link
                                (e.g.
                                `https://api.dub.co/qr?url=https://dub.sh/try`).
                            utm_source:
                              nullable: true
                              description: The UTM source of the short link.
                              type: string
                            utm_medium:
                              nullable: true
                              description: The UTM medium of the short link.
                              type: string
                            utm_campaign:
                              nullable: true
                              description: The UTM campaign of the short link.
                              type: string
                            utm_term:
                              nullable: true
                              description: The UTM term of the short link.
                              type: string
                            utm_content:
                              nullable: true
                              description: The UTM content of the short link.
                              type: string
                            testVariants:
                              nullable: true
                              minItems: 2
                              maxItems: 4
                              type: array
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
                                additionalProperties: false
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
                            testCompletedAt:
                              type: string
                            userId:
                              nullable: true
                              type: string
                            workspaceId:
                              type: string
                              description: The workspace ID of the short link.
                            clicks:
                              default: 0
                              description: The number of clicks on the short link.
                              type: number
                            leads:
                              default: 0
                              description: >-
                                The number of leads the short link has
                                generated.
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
                            lastClicked:
                              type: string
                            createdAt:
                              type: string
                            updatedAt:
                              type: string
                            tagId:
                              nullable: true
                              description: >-
                                Deprecated: Use `tags` instead. The unique ID of
                                the tag assigned to the short link.
                              deprecated: true
                              type: string
                            projectId:
                              type: string
                              description: >-
                                Deprecated: Use `workspaceId` instead. The
                                project ID of the short link.
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
                            - disabledAt
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
                          additionalProperties: false
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
                              nullable: true
                              type: string
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
                          additionalProperties: false
                        customer:
                          type: object
                          properties:
                            id:
                              type: string
                              description: >-
                                The unique ID of the customer. You may use
                                either the customer's `id` on Dub (obtained via
                                `/customers` endpoint) or their `externalId`
                                (unique ID within your system, prefixed with
                                `ext_`, e.g. `ext_123`).
                            externalId:
                              type: string
                              description: >-
                                Unique identifier for the customer in the
                                client's app.
                            name:
                              type: string
                              description: Name of the customer.
                            email:
                              description: Email of the customer.
                              nullable: true
                              type: string
                            avatar:
                              description: Avatar URL of the customer.
                              nullable: true
                              type: string
                            country:
                              description: Country of the customer.
                              nullable: true
                              type: string
                            sales:
                              description: Total number of sales for the customer.
                              nullable: true
                              type: number
                            saleAmount:
                              description: Total amount of sales for the customer.
                              nullable: true
                              type: number
                            createdAt:
                              description: The date the customer was created.
                              type: string
                          required:
                            - id
                            - externalId
                            - name
                            - createdAt
                          additionalProperties: false
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
                          deprecated: true
                          description: 'Deprecated: Use `click.id` instead.'
                        link_id:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `link.id` instead.'
                        domain:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `link.domain` instead.'
                        key:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `link.key` instead.'
                        url:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.url` instead.'
                        continent:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.continent` instead.'
                        country:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.country` instead.'
                        city:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.city` instead.'
                        device:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.device` instead.'
                        browser:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.browser` instead.'
                        os:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.os` instead.'
                        qr:
                          type: number
                          deprecated: true
                          description: 'Deprecated: Use `click.qr` instead.'
                        ip:
                          type: string
                          deprecated: true
                          description: 'Deprecated: Use `click.ip` instead.'
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
                      additionalProperties: false
                      title: SaleEvent
                  type: object
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
    LinkTagSchemaOutput:
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
      additionalProperties: false
      title: LinkTag
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