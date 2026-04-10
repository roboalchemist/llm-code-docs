# Source: https://dub.co/docs/api-reference/endpoint/update-a-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a domain

> Update a domain for the authenticated workspace.



## OpenAPI

````yaml patch /domains/{slug}
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
  /domains/{slug}:
    patch:
      tags:
        - Domains
      summary: Update a domain
      description: Update a domain for the authenticated workspace.
      operationId: updateDomain
      parameters:
        - in: path
          name: slug
          schema:
            type: string
            description: The domain name.
            example: acme.com
          required: true
          description: The domain name.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                slug:
                  type: string
                  minLength: 1
                  maxLength: 190
                  description: Name of the domain.
                  example: acme.com
                expiredUrl:
                  description: >-
                    Redirect users to a specific URL when any link under this
                    domain has expired.
                  example: https://acme.com/expired
                  nullable: true
                  type: string
                  maxLength: 32000
                notFoundUrl:
                  description: >-
                    Redirect users to a specific URL when a link under this
                    domain doesn't exist.
                  example: https://acme.com/not-found
                  nullable: true
                  type: string
                  maxLength: 32000
                archived:
                  default: false
                  description: >-
                    Whether to archive this domain. `false` will unarchive a
                    previously archived domain.
                  example: false
                  type: boolean
                placeholder:
                  description: >-
                    Provide context to your teammates in the link creation modal
                    by showing them an example of a link to be shortened.
                  example: https://dub.co/help/article/what-is-dub
                  nullable: true
                  type: string
                  maxLength: 100
                logo:
                  description: The logo of the domain.
                  nullable: true
                  anyOf:
                    - type: string
                      pattern: ^data:image\/(png|jpeg|jpg|gif|webp);base64,
                    - type: string
                      format: uri
                    - type: string
                      format: uri
                assetLinks:
                  description: >-
                    assetLinks.json configuration file (for deep link support on
                    Android).
                  nullable: true
                  type: string
                appleAppSiteAssociation:
                  description: >-
                    apple-app-site-association configuration file (for deep link
                    support on iOS).
                  nullable: true
                  type: string
      responses:
        '200':
          description: The domain was updated.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DomainSchema'
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
    DomainSchema:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the domain.
        slug:
          type: string
          description: The domain name.
          example: acme.com
        verified:
          default: false
          description: Whether the domain is verified.
          type: boolean
        primary:
          default: false
          description: Whether the domain is the primary domain for the workspace.
          type: boolean
        archived:
          default: false
          type: boolean
          description: Whether the domain is archived.
        placeholder:
          nullable: true
          description: >-
            Provide context to your teammates in the link creation modal by
            showing them an example of a link to be shortened.
          example: https://dub.co/help/article/what-is-dub
          type: string
        expiredUrl:
          nullable: true
          description: The URL to redirect to when a link under this domain has expired.
          example: https://acme.com/expired
          type: string
        notFoundUrl:
          nullable: true
          description: The URL to redirect to when a link under this domain doesn't exist.
          example: https://acme.com/not-found
          type: string
        logo:
          nullable: true
          description: The logo of the domain.
          type: string
        assetLinks:
          default: null
          description: >-
            assetLinks.json configuration file (for deep link support on
            Android).
          nullable: true
          type: string
        appleAppSiteAssociation:
          default: null
          description: >-
            apple-app-site-association configuration file (for deep link support
            on iOS).
          nullable: true
          type: string
        createdAt:
          description: The date the domain was created.
          type: string
        updatedAt:
          description: The date the domain was last updated.
          type: string
        registeredDomain:
          nullable: true
          description: The registered domain record.
          type: object
          properties:
            id:
              type: string
              description: The ID of the registered domain record.
            autoRenewalDisabledAt:
              nullable: true
              description: The date the domain auto-renew is disabled.
              type: string
            createdAt:
              description: The date the domain was created.
              type: string
            expiresAt:
              description: The date the domain expires.
              type: string
            renewalFee:
              type: number
              description: The fee to renew the domain.
          required:
            - id
            - autoRenewalDisabledAt
            - createdAt
            - expiresAt
            - renewalFee
          additionalProperties: false
      required:
        - id
        - slug
        - verified
        - primary
        - archived
        - placeholder
        - expiredUrl
        - notFoundUrl
        - logo
        - assetLinks
        - appleAppSiteAssociation
        - createdAt
        - updatedAt
        - registeredDomain
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