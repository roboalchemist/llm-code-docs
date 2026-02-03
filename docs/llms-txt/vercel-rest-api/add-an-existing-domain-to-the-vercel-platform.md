# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/add-an-existing-domain-to-the-vercel-platform.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Add an existing domain to the Vercel platform

> This endpoint is used for adding a new apex domain name with Vercel for the authenticating user. Note: This endpoint is no longer used for initiating domain transfers from external registrars to Vercel. For this, please use the endpoint [Transfer-in a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/transfer-in-a-domain).



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v7/domains
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v7/domains:
    post:
      tags:
        - domains
      summary: Add an existing domain to the Vercel platform
      description: >-
        This endpoint is used for adding a new apex domain name with Vercel for
        the authenticating user. Note: This endpoint is no longer used for
        initiating domain transfers from external registrars to Vercel. For
        this, please use the endpoint [Transfer-in a
        domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/transfer-in-a-domain).
      operationId: createOrTransferDomain
      parameters:
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      requestBody:
        content:
          application/json:
            schema:
              properties:
                method:
                  description: >-
                    The domain operation to perform. It can be either `add` or
                    `move-in`.
                  type: string
                  example: add
              oneOf:
                - additionalProperties: false
                  type: object
                  description: add
                  required:
                    - name
                  properties:
                    name:
                      description: The domain name you want to add.
                      type: string
                      example: example.com
                    cdnEnabled:
                      description: >-
                        Whether the domain has the Vercel Edge Network enabled
                        or not.
                      type: boolean
                      example: true
                    zone:
                      type: boolean
                    method:
                      description: The domain operation to perform.
                      type: string
                      example: add
                - additionalProperties: false
                  type: object
                  description: move-in
                  required:
                    - method
                    - name
                  properties:
                    name:
                      description: The domain name you want to add.
                      type: string
                      example: example.com
                    method:
                      description: The domain operation to perform.
                      type: string
                      example: move-in
                    token:
                      description: The move-in token from Move Requested email.
                      type: string
                      example: fdhfr820ad#@FAdlj$$
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  domain:
                    properties:
                      verified:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: If the domain has the ownership verified.
                        example: true
                      nameservers:
                        items:
                          type: string
                        type: array
                        description: A list of the current nameservers of the domain.
                        example:
                          - ns1.nameserver.net
                          - ns2.nameserver.net
                      intendedNameservers:
                        items:
                          type: string
                        type: array
                        description: >-
                          A list of the intended nameservers for the domain to
                          point to Vercel DNS.
                        example:
                          - ns1.vercel-dns.com
                          - ns2.vercel-dns.com
                      customNameservers:
                        items:
                          type: string
                        type: array
                        description: >-
                          A list of custom nameservers for the domain to point
                          to. Only applies to domains purchased with Vercel.
                        example:
                          - ns1.nameserver.net
                          - ns2.nameserver.net
                      creator:
                        properties:
                          username:
                            type: string
                          email:
                            type: string
                          customerId:
                            nullable: true
                            type: string
                          isDomainReseller:
                            type: boolean
                            enum:
                              - false
                              - true
                          id:
                            type: string
                        required:
                          - email
                          - id
                          - username
                        type: object
                        description: >-
                          An object containing information of the domain
                          creator, including the user's id, username, and email.
                        example:
                          id: ZspSRT4ljIEEmMHgoDwKWDei
                          username: vercel_user
                          email: demo@example.com
                      registrar:
                        type: string
                        enum:
                          - new
                        description: >-
                          Whether or not the domain is registered with Name.com.
                          If set to `true`, the domain is registered with
                          Name.com.
                      name:
                        type: string
                        description: The domain name.
                        example: example.com
                      teamId:
                        nullable: true
                        type: string
                      boughtAt:
                        nullable: true
                        type: number
                        description: >-
                          If it was purchased through Vercel, the timestamp in
                          milliseconds when it was purchased.
                        example: 1613602938882
                      createdAt:
                        type: number
                        description: >-
                          Timestamp in milliseconds when the domain was created
                          in the registry.
                        example: 1613602938882
                      expiresAt:
                        nullable: true
                        type: number
                        description: >-
                          Timestamp in milliseconds at which the domain is set
                          to expire. `null` if not bought with Vercel.
                        example: 1613602938882
                      id:
                        type: string
                        description: The unique identifier of the domain.
                        example: EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1
                      renew:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          Indicates whether the domain is set to automatically
                          renew.
                        example: true
                      serviceType:
                        type: string
                        enum:
                          - zeit.world
                          - external
                          - na
                        description: >-
                          The type of service the domain is handled by.
                          `external` if the DNS is externally handled,
                          `zeit.world` if handled with Vercel, or `na` if the
                          service is not available.
                        example: zeit.world
                      transferredAt:
                        nullable: true
                        type: number
                        description: >-
                          Timestamp in milliseconds at which the domain was
                          successfully transferred into Vercel. `null` if the
                          transfer is still processing or was never transferred
                          in.
                        example: 1613602938882
                      transferStartedAt:
                        type: number
                        description: >-
                          If transferred into Vercel, timestamp in milliseconds
                          when the domain transfer was initiated.
                        example: 1613602938882
                      userId:
                        type: string
                    required:
                      - boughtAt
                      - createdAt
                      - creator
                      - expiresAt
                      - id
                      - intendedNameservers
                      - name
                      - nameservers
                      - serviceType
                      - teamId
                      - userId
                      - verified
                    type: object
                required:
                  - domain
                type: object
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '409':
          description: The domain is not allowed to be used
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````