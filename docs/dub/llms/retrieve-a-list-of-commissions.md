# Source: https://dub.co/docs/api-reference/endpoint/retrieve-a-list-of-commissions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all commissions

> Retrieve a list of commissions for a program.

<Note>
  Commissions endpoints require an [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>


## OpenAPI

````yaml get /commissions
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
  /commissions:
    get:
      tags:
        - Commissions
      summary: Get commissions for a program.
      description: Retrieve a list of commissions for a program.
      operationId: listCommissions
      parameters:
        - in: query
          name: type
          schema:
            type: string
            enum:
              - click
              - lead
              - sale
              - custom
        - in: query
          name: customerId
          schema:
            description: Filter the list of commissions by the associated customer.
            type: string
          description: Filter the list of commissions by the associated customer.
        - in: query
          name: payoutId
          schema:
            description: Filter the list of commissions by the associated payout.
            type: string
          description: Filter the list of commissions by the associated payout.
        - in: query
          name: partnerId
          schema:
            description: >-
              Filter the list of commissions by the associated partner. When
              specified, takes precedence over `tenantId`.
            type: string
          description: >-
            Filter the list of commissions by the associated partner. When
            specified, takes precedence over `tenantId`.
        - in: query
          name: tenantId
          schema:
            description: >-
              Filter the list of commissions by the associated partner's
              `tenantId` (their unique ID within your database).
            type: string
          description: >-
            Filter the list of commissions by the associated partner's
            `tenantId` (their unique ID within your database).
        - in: query
          name: groupId
          schema:
            description: Filter the list of commissions by the associated partner group.
            type: string
          description: Filter the list of commissions by the associated partner group.
        - in: query
          name: invoiceId
          schema:
            description: >-
              Filter the list of commissions by the associated invoice. Since
              invoiceId is unique on a per-program basis, this will only return
              one commission per invoice.
            type: string
          description: >-
            Filter the list of commissions by the associated invoice. Since
            invoiceId is unique on a per-program basis, this will only return
            one commission per invoice.
        - in: query
          name: status
          schema:
            description: Filter the list of commissions by their corresponding status.
            type: string
            enum:
              - pending
              - processed
              - paid
              - refunded
              - duplicate
              - fraud
              - canceled
          description: Filter the list of commissions by their corresponding status.
        - in: query
          name: sortBy
          schema:
            default: createdAt
            description: The field to sort the list of commissions by.
            type: string
            enum:
              - createdAt
              - amount
          description: The field to sort the list of commissions by.
        - in: query
          name: sortOrder
          schema:
            default: desc
            description: The sort order for the list of commissions.
            type: string
            enum:
              - asc
              - desc
          description: The sort order for the list of commissions.
        - in: query
          name: interval
          schema:
            default: all
            description: The interval to retrieve commissions for.
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
          description: The interval to retrieve commissions for.
        - in: query
          name: start
          schema:
            description: The start date of the date range to filter the commissions by.
            type: string
          description: The start date of the date range to filter the commissions by.
        - in: query
          name: end
          schema:
            description: The end date of the date range to filter the commissions by.
            type: string
          description: The end date of the date range to filter the commissions by.
        - in: query
          name: timezone
          schema:
            type: string
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
          description: The list of commissions.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: The commission's unique ID on Dub.
                      example: cm_1JVR7XRCSR0EDBAF39FZ4PMYE
                    type:
                      type: string
                      enum:
                        - click
                        - lead
                        - sale
                        - custom
                    amount:
                      type: number
                    earnings:
                      type: number
                    currency:
                      type: string
                    status:
                      type: string
                      enum:
                        - pending
                        - processed
                        - paid
                        - refunded
                        - duplicate
                        - fraud
                        - canceled
                    invoiceId:
                      nullable: true
                      type: string
                    description:
                      nullable: true
                      type: string
                    quantity:
                      type: number
                    userId:
                      description: The user who created the manual commission.
                      nullable: true
                      type: string
                    createdAt:
                      type: string
                    updatedAt:
                      type: string
                    partner:
                      type: object
                      properties:
                        id:
                          type: string
                          description: The partner's unique ID on Dub.
                        name:
                          type: string
                          maxLength: 190
                          description: The partner's full legal name.
                        email:
                          nullable: true
                          description: >-
                            The partner's email address. Should be a unique
                            value across Dub.
                          type: string
                          maxLength: 190
                        image:
                          nullable: true
                          description: The partner's avatar image.
                          type: string
                        payoutsEnabledAt:
                          nullable: true
                          description: The date when the partner enabled payouts.
                          type: string
                        country:
                          nullable: true
                          description: The partner's country (required for tax purposes).
                          type: string
                        groupId:
                          description: The partner's group ID on Dub.
                          nullable: true
                          type: string
                      required:
                        - id
                        - name
                        - email
                        - image
                        - payoutsEnabledAt
                        - country
                      additionalProperties: false
                    customer:
                      nullable: true
                      type: object
                      properties:
                        id:
                          type: string
                          description: >-
                            The unique ID of the customer. You may use either
                            the customer's `id` on Dub (obtained via
                            `/customers` endpoint) or their `externalId` (unique
                            ID within your system, prefixed with `ext_`, e.g.
                            `ext_123`).
                        externalId:
                          type: string
                          description: >-
                            Unique identifier for the customer in the client's
                            app.
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
                  required:
                    - id
                    - amount
                    - earnings
                    - currency
                    - status
                    - invoiceId
                    - description
                    - quantity
                    - createdAt
                    - updatedAt
                    - partner
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