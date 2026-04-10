# Source: https://dub.co/docs/api-reference/endpoint/track-sale.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Track a sale

> Track a sale for a short link.

<Note>
  Conversions endpoints require a [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>


## OpenAPI

````yaml post /track/sale
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
  /track/sale:
    post:
      tags:
        - Track
      summary: Track a sale
      description: Track a sale for a short link.
      operationId: trackSale
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                customerExternalId:
                  type: string
                  minLength: 1
                  maxLength: 100
                  description: >-
                    The unique ID of the customer in your system. Will be used
                    to identify and attribute all future events to this
                    customer.
                amount:
                  type: integer
                  minimum: 0
                  maximum: 9007199254740991
                  description: >-
                    The amount of the sale in cents (for all two-decimal
                    currencies). If the sale is in a zero-decimal currency, pass
                    the full integer value (e.g. `1437` JPY). Learn more:
                    https://d.to/currency
                currency:
                  description: >-
                    The currency of the sale. Accepts ISO 4217 currency codes.
                    Sales will be automatically converted and stored as USD at
                    the latest exchange rates. Learn more: https://d.to/currency
                  default: usd
                  type: string
                eventName:
                  default: Purchase
                  description: >-
                    The name of the sale event. Recommended format: `Invoice
                    paid` or `Subscription created`.
                  example: Invoice paid
                  type: string
                  maxLength: 255
                paymentProcessor:
                  default: custom
                  description: The payment processor via which the sale was made.
                  type: string
                  enum:
                    - stripe
                    - shopify
                    - polar
                    - paddle
                    - revenuecat
                    - custom
                invoiceId:
                  default: null
                  description: >-
                    The invoice ID of the sale. Can be used as a idempotency key
                    – only one sale event can be recorded for a given invoice
                    ID.
                  nullable: true
                  type: string
                metadata:
                  default: null
                  description: >-
                    Additional metadata to be stored with the sale event. Max
                    10,000 characters when stringified.
                  nullable: true
                  type: object
                  additionalProperties: {}
                leadEventName:
                  default: null
                  description: >-
                    The name of the lead event that occurred before the sale
                    (case-sensitive). This is used to associate the sale event
                    with a particular lead event (instead of the latest lead
                    event for a link-customer combination, which is the default
                    behavior). For direct sale tracking, this field can also be
                    used to specify the lead event name.
                  example: Cloned template 1481267
                  nullable: true
                  type: string
                clickId:
                  description: >-
                    [For direct sale tracking]: The unique ID of the click that
                    the sale conversion event is attributed to. You can read
                    this value from `dub_id` cookie.
                  nullable: true
                  type: string
                customerName:
                  default: null
                  description: >-
                    [For direct sale tracking]: The name of the customer. If not
                    passed, a random name will be generated (e.g. “Big Red
                    Caribou”).
                  nullable: true
                  type: string
                  maxLength: 100
                customerEmail:
                  default: null
                  description: >-
                    [For direct sale tracking]: The email address of the
                    customer.
                  nullable: true
                  type: string
                  maxLength: 100
                  format: email
                  pattern: >-
                    ^(?!\.)(?!.*\.\.)([A-Za-z0-9_'+\-\.]*)[A-Za-z0-9_+-]@([A-Za-z0-9][A-Za-z0-9\-]*\.)+[A-Za-z]{2,}$
                customerAvatar:
                  default: null
                  description: '[For direct sale tracking]: The avatar URL of the customer.'
                  nullable: true
                  type: string
              required:
                - customerExternalId
                - amount
      responses:
        '200':
          description: A sale was tracked.
          content:
            application/json:
              schema:
                type: object
                properties:
                  eventName:
                    type: string
                  customer:
                    nullable: true
                    type: object
                    properties:
                      id:
                        type: string
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
                      - id
                      - name
                      - email
                      - avatar
                      - externalId
                    additionalProperties: false
                  sale:
                    nullable: true
                    type: object
                    properties:
                      amount:
                        type: number
                      currency:
                        type: string
                      paymentProcessor:
                        type: string
                      invoiceId:
                        nullable: true
                        type: string
                      metadata:
                        nullable: true
                        type: object
                        additionalProperties: {}
                    required:
                      - amount
                      - currency
                      - paymentProcessor
                      - invoiceId
                      - metadata
                    additionalProperties: false
                required:
                  - eventName
                  - customer
                  - sale
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