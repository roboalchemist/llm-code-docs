# Source: https://dub.co/docs/api-reference/endpoint/bulk-update-links.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk update links

> Bulk update up to 100 links with the same data for the authenticated workspace.

This endpoint lets you update up to 100 links **with the same data**.

Some potential use cases:

* Tagging multiple links at once
* Setting the same expiration date for multiple links
* Updating UTM parameters for multiple links

<Warning>
  You cannot update the domain or key of a link with this endpoint. Also,
  [webhook events](/concepts/webhooks/introduction) will not be triggered when
  using this endpoint.
</Warning>


## OpenAPI

````yaml patch /links/bulk
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
  /links/bulk:
    patch:
      tags:
        - Links
      summary: Bulk update links
      description: >-
        Bulk update up to 100 links with the same data for the authenticated
        workspace.
      operationId: bulkUpdateLinks
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                linkIds:
                  default: []
                  maxItems: 100
                  type: array
                  items:
                    type: string
                  description: >-
                    The IDs of the links to update. Takes precedence over
                    `externalIds`.
                externalIds:
                  default: []
                  maxItems: 100
                  type: array
                  items:
                    type: string
                  description: >-
                    The external IDs of the links to update as stored in your
                    database.
                data:
                  type: object
                  properties:
                    url:
                      description: The destination URL of the short link.
                      example: https://google.com
                      maxLength: 32000
                      type: string
                    tenantId:
                      description: >-
                        The ID of the tenant that created the link inside your
                        system. If set, it can be used to fetch all links for a
                        tenant.
                      nullable: true
                      type: string
                      maxLength: 255
                    programId:
                      nullable: true
                      description: The ID of the program the short link is associated with.
                      type: string
                    partnerId:
                      nullable: true
                      description: The ID of the partner the short link is associated with.
                      type: string
                    trackConversion:
                      description: >-
                        Whether to track conversions for the short link.
                        Defaults to `false` if not provided.
                      type: boolean
                    archived:
                      description: >-
                        Whether the short link is archived. Defaults to `false`
                        if not provided.
                      type: boolean
                    tagIds:
                      description: The unique IDs of the tags assigned to the short link.
                      example:
                        - clux0rgak00011...
                      anyOf:
                        - type: string
                        - type: array
                          items:
                            type: string
                    tagNames:
                      description: >-
                        The unique name of the tags assigned to the short link
                        (case insensitive).
                      anyOf:
                        - type: string
                        - type: array
                          items:
                            type: string
                    folderId:
                      description: >-
                        The unique ID existing folder to assign the short link
                        to.
                      nullable: true
                      type: string
                    comments:
                      nullable: true
                      description: The comments for the short link.
                      type: string
                    expiresAt:
                      description: The date and time when the short link will expire at.
                      nullable: true
                      type: string
                    expiredUrl:
                      description: The URL to redirect to when the short link has expired.
                      maxLength: 32000
                      nullable: true
                      type: string
                    password:
                      nullable: true
                      description: >-
                        The password required to access the destination URL of
                        the short link.
                      type: string
                    proxy:
                      description: >-
                        Whether the short link uses Custom Link Previews
                        feature. Defaults to `false` if not provided.
                      type: boolean
                    title:
                      description: >-
                        The custom link preview title (og:title). Will be used
                        for Custom Link Previews if `proxy` is true. Learn more:
                        https://d.to/og
                      nullable: true
                      type: string
                    description:
                      description: >-
                        The custom link preview description (og:description).
                        Will be used for Custom Link Previews if `proxy` is
                        true. Learn more: https://d.to/og
                      nullable: true
                      type: string
                    image:
                      description: >-
                        The custom link preview image (og:image). Will be used
                        for Custom Link Previews if `proxy` is true. Learn more:
                        https://d.to/og
                      nullable: true
                      type: string
                    video:
                      nullable: true
                      description: >-
                        The custom link preview video (og:video). Will be used
                        for Custom Link Previews if `proxy` is true. Learn more:
                        https://d.to/og
                      type: string
                    rewrite:
                      description: >-
                        Whether the short link uses link cloaking. Defaults to
                        `false` if not provided.
                      type: boolean
                    ios:
                      description: >-
                        The iOS destination URL for the short link for iOS
                        device targeting.
                      nullable: true
                      type: string
                      maxLength: 32000
                    android:
                      description: >-
                        The Android destination URL for the short link for
                        Android device targeting.
                      nullable: true
                      type: string
                      maxLength: 32000
                    geo:
                      $ref: '#/components/schemas/linkGeoTargeting'
                    doIndex:
                      description: >-
                        Allow search engines to index your short link. Defaults
                        to `false` if not provided. Learn more:
                        https://d.to/noindex
                      type: boolean
                    utm_source:
                      description: >-
                        The UTM source of the short link. If set, this will
                        populate or override the UTM source in the destination
                        URL.
                      nullable: true
                      type: string
                    utm_medium:
                      description: >-
                        The UTM medium of the short link. If set, this will
                        populate or override the UTM medium in the destination
                        URL.
                      nullable: true
                      type: string
                    utm_campaign:
                      description: >-
                        The UTM campaign of the short link. If set, this will
                        populate or override the UTM campaign in the destination
                        URL.
                      nullable: true
                      type: string
                    utm_term:
                      description: >-
                        The UTM term of the short link. If set, this will
                        populate or override the UTM term in the destination
                        URL.
                      nullable: true
                      type: string
                    utm_content:
                      description: >-
                        The UTM content of the short link. If set, this will
                        populate or override the UTM content in the destination
                        URL.
                      nullable: true
                      type: string
                    ref:
                      description: >-
                        The referral tag of the short link. If set, this will
                        populate or override the `ref` query parameter in the
                        destination URL.
                      nullable: true
                      type: string
                    webhookIds:
                      description: >-
                        An array of webhook IDs to trigger when the link is
                        clicked. These webhooks will receive click event data.
                      nullable: true
                      type: array
                      items:
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
                      description: >-
                        An array of A/B test URLs and the percentage of traffic
                        to send to each URL.
                      example:
                        - url: https://example.com/variant-1
                          percentage: 50
                        - url: https://example.com/variant-2
                          percentage: 50
                    testStartedAt:
                      description: The date and time when the tests started.
                      nullable: true
                      type: string
                    testCompletedAt:
                      description: >-
                        The date and time when the tests were or will be
                        completed.
                      nullable: true
                      type: string
                    publicStats:
                      description: >-
                        Deprecated: Use `dashboard` instead. Whether the short
                        link's stats are publicly accessible. Defaults to
                        `false` if not provided.
                      deprecated: true
                      type: boolean
                    tagId:
                      description: >-
                        Deprecated: Use `tagIds` instead. The unique ID of the
                        tag assigned to the short link.
                      deprecated: true
                      nullable: true
                      type: string
              required:
                - data
      responses:
        '200':
          description: The updated links
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/LinkSchema'
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
    linkGeoTargeting:
      description: >-
        Geo targeting information for the short link in JSON format `{[COUNTRY]:
        https://example.com }`. See https://d.to/geo for more information.
      nullable: true
      type: object
      additionalProperties:
        type: string
        maxLength: 32000
    LinkSchema:
      type: object
      properties:
        id:
          type: string
          description: The unique ID of the short link.
        domain:
          type: string
          description: >-
            The domain of the short link. If not provided, the primary domain
            for the workspace will be used (or `dub.sh` if the workspace has no
            domains).
        key:
          type: string
          description: >-
            The short link slug. If not provided, a random 7-character slug will
            be generated.
        url:
          type: string
          format: uri
          description: The destination URL of the short link.
        trackConversion:
          default: false
          description: Whether to track conversions for the short link.
          type: boolean
        externalId:
          nullable: true
          description: >-
            The ID of the link in your database. If set, it can be used to
            identify the link in future API requests (must be prefixed with
            'ext_' when passed as a query parameter). This key is unique across
            your workspace.
          type: string
        tenantId:
          nullable: true
          description: >-
            The ID of the tenant that created the link inside your system. If
            set, it can be used to fetch all links for a tenant.
          type: string
        programId:
          nullable: true
          description: The ID of the program the short link is associated with.
          type: string
        partnerId:
          nullable: true
          description: The ID of the partner the short link is associated with.
          type: string
        archived:
          default: false
          description: Whether the short link is archived.
          type: boolean
        expiresAt:
          nullable: true
          description: >-
            The date and time when the short link will expire in ISO-8601
            format.
          type: string
        expiredUrl:
          nullable: true
          description: The URL to redirect to when the short link has expired.
          type: string
          format: uri
        disabledAt:
          nullable: true
          description: >-
            The date and time when the short link was disabled. When a short
            link is disabled, it will redirect to its domain's not found URL,
            and its stats will be excluded from your overall stats.
          type: string
        password:
          nullable: true
          description: >-
            The password required to access the destination URL of the short
            link.
          type: string
        proxy:
          default: false
          description: Whether the short link uses Custom Link Previews feature.
          type: boolean
        title:
          nullable: true
          description: >-
            The title of the short link. Will be used for Custom Link Previews
            if `proxy` is true.
          type: string
        description:
          nullable: true
          description: >-
            The description of the short link. Will be used for Custom Link
            Previews if `proxy` is true.
          type: string
        image:
          nullable: true
          description: >-
            The image of the short link. Will be used for Custom Link Previews
            if `proxy` is true.
          type: string
        video:
          nullable: true
          description: >-
            The custom link preview video (og:video). Will be used for Custom
            Link Previews if `proxy` is true. Learn more: https://d.to/og
          type: string
        rewrite:
          default: false
          description: Whether the short link uses link cloaking.
          type: boolean
        doIndex:
          default: false
          description: Whether to allow search engines to index the short link.
          type: boolean
        ios:
          nullable: true
          description: The iOS destination URL for the short link for iOS device targeting.
          type: string
        android:
          nullable: true
          description: >-
            The Android destination URL for the short link for Android device
            targeting.
          type: string
        geo:
          nullable: true
          description: >-
            Geo targeting information for the short link in JSON format
            `{[COUNTRY]: https://example.com }`. See https://d.to/geo for more
            information.
          type: object
          additionalProperties:
            type: string
            format: uri
        publicStats:
          default: false
          description: Whether the short link's stats are publicly accessible.
          type: boolean
        tags:
          nullable: true
          description: The tags assigned to the short link.
          type: array
          items:
            $ref: '#/components/schemas/LinkTagSchemaOutput'
        folderId:
          nullable: true
          description: The unique ID of the folder assigned to the short link.
          type: string
        webhookIds:
          type: array
          items:
            type: string
          description: The IDs of the webhooks that the short link is associated with.
        comments:
          nullable: true
          description: The comments for the short link.
          type: string
        shortLink:
          type: string
          format: uri
          description: >-
            The full URL of the short link, including the https protocol (e.g.
            `https://dub.sh/try`).
        qrCode:
          type: string
          format: uri
          description: >-
            The full URL of the QR code for the short link (e.g.
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
            An array of A/B test URLs and the percentage of traffic to send to
            each URL.
          example:
            - url: https://example.com/variant-1
              percentage: 50
            - url: https://example.com/variant-2
              percentage: 50
        testStartedAt:
          description: The date and time when the tests started.
          nullable: true
          type: string
        testCompletedAt:
          description: The date and time when the tests were or will be completed.
          nullable: true
          type: string
        userId:
          nullable: true
          description: The user ID of the creator of the short link.
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
          description: The number of leads the short link has generated.
          type: number
        conversions:
          default: 0
          description: The number of leads that converted to paying customers.
          type: number
        sales:
          default: 0
          description: >-
            The total number of sales (includes recurring sales) generated by
            the short link.
          type: number
        saleAmount:
          default: 0
          description: >-
            The total dollar value of sales (in cents) generated by the short
            link.
          type: number
        lastClicked:
          nullable: true
          description: The date and time when the short link was last clicked.
          type: string
        createdAt:
          type: string
          description: The date and time when the short link was created.
        updatedAt:
          type: string
          description: The date and time when the short link was last updated.
        tagId:
          nullable: true
          description: >-
            Deprecated: Use `tags` instead. The unique ID of the tag assigned to
            the short link.
          deprecated: true
          type: string
        projectId:
          type: string
          description: >-
            Deprecated: Use `workspaceId` instead. The project ID of the short
            link.
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
      title: Link
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