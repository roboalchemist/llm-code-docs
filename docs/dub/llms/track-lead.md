# Source: https://dub.co/docs/api-reference/endpoint/track-lead.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Track a lead

> Track a lead for a short link.

<Note>
  Conversions endpoints require a [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>

### Deduplication behavior

Lead events are automatically deduplicated to prevent duplicate tracking:

* Events are deduplicated based on the combination of `customerExternalId` (the user ID of the referred customer within your database) and `eventName`
* If you send multiple lead events with the same customer ID and event name, only the first event will be tracked
* Subsequent duplicate events will return `null` and won't be tracked


## OpenAPI

````yaml post /track/lead
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
  /track/lead:
    post:
      tags:
        - Track
      summary: Track a lead
      description: Track a lead for a short link.
      operationId: trackLead
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                clickId:
                  type: string
                  description: >-
                    The unique ID of the click that the lead conversion event is
                    attributed to. You can read this value from `dub_id` cookie.
                    [For deferred lead tracking]: If an empty string is
                    provided, Dub will try to find an existing customer with the
                    provided `customerExternalId` and use the `clickId` from the
                    customer if found.
                eventName:
                  type: string
                  minLength: 1
                  maxLength: 255
                  description: >-
                    The name of the lead event to track. Can also be used as a
                    unique identifier to associate a given lead event for a
                    customer for a subsequent sale event (via the
                    `leadEventName` prop in `/track/sale`).
                  example: Sign up
                customerExternalId:
                  type: string
                  minLength: 1
                  maxLength: 100
                  description: >-
                    The unique ID of the customer in your system. Will be used
                    to identify and attribute all future events to this
                    customer.
                customerName:
                  default: null
                  description: >-
                    The name of the customer. If not passed, a random name will
                    be generated (e.g. “Big Red Caribou”).
                  nullable: true
                  type: string
                  maxLength: 100
                customerEmail:
                  default: null
                  description: The email address of the customer.
                  nullable: true
                  type: string
                  maxLength: 100
                  format: email
                  pattern: >-
                    ^(?!\.)(?!.*\.\.)([A-Za-z0-9_'+\-\.]*)[A-Za-z0-9_+-]@([A-Za-z0-9][A-Za-z0-9\-]*\.)+[A-Za-z]{2,}$
                customerAvatar:
                  default: null
                  description: The avatar URL of the customer.
                  nullable: true
                  type: string
                mode:
                  default: async
                  description: >-
                    The mode to use for tracking the lead event. `async` will
                    not block the request; `wait` will block the request until
                    the lead event is fully recorded in Dub; `deferred` will
                    defer the lead event creation to a subsequent request.
                  type: string
                  enum:
                    - async
                    - wait
                    - deferred
                eventQuantity:
                  description: >-
                    The numerical value associated with this lead event (e.g.,
                    number of provisioned seats in a free trial). If defined as
                    N, the lead event will be tracked N times.
                  nullable: true
                  type: number
                metadata:
                  default: null
                  description: >-
                    Additional metadata to be stored with the lead event. Max
                    10,000 characters.
                  nullable: true
                  type: object
                  additionalProperties: {}
              required:
                - clickId
                - eventName
                - customerExternalId
      responses:
        '200':
          description: A lead was tracked.
          content:
            application/json:
              schema:
                type: object
                properties:
                  click:
                    type: object
                    properties:
                      id:
                        type: string
                    required:
                      - id
                    additionalProperties: false
                  link:
                    nullable: true
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
                      partnerId:
                        nullable: true
                        description: >-
                          The ID of the partner the short link is associated
                          with.
                        type: string
                      programId:
                        nullable: true
                        description: >-
                          The ID of the program the short link is associated
                          with.
                        type: string
                      tenantId:
                        nullable: true
                        description: >-
                          The ID of the tenant that created the link inside your
                          system. If set, it can be used to fetch all links for
                          a tenant.
                        type: string
                      externalId:
                        nullable: true
                        description: >-
                          The ID of the link in your database. If set, it can be
                          used to identify the link in future API requests (must
                          be prefixed with 'ext_' when passed as a query
                          parameter). This key is unique across your workspace.
                        type: string
                    required:
                      - id
                      - domain
                      - key
                      - shortLink
                      - url
                      - partnerId
                      - programId
                      - tenantId
                      - externalId
                    additionalProperties: false
                  customer:
                    type: object
                    properties:
                      name:
                        nullable: true
                        type: string
                      email:
                        nullable: true
                        type: string
                      avatar:
                        nullable: true
                        type: string
                      externalId:
                        nullable: true
                        type: string
                    required:
                      - name
                      - email
                      - avatar
                      - externalId
                    additionalProperties: false
                required:
                  - click
                  - link
                  - customer
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