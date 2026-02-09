# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/get-information-for-a-single-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Information for a Single Domain

> Get information for a single domain in an account or team.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/domains/{domain}
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
  /v5/domains/{domain}:
    get:
      tags:
        - domains
      summary: Get Information for a Single Domain
      description: Get information for a single domain in an account or team.
      operationId: getDomain
      parameters:
        - name: domain
          description: The name of the domain.
          in: path
          required: true
          schema:
            description: The name of the domain.
            type: string
            example: example.com
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
      responses:
        '200':
          description: >-
            Successful response retrieving an information for a specific
            domains.
          content:
            application/json:
              schema:
                properties:
                  domain:
                    properties:
                      suffix:
                        type: boolean
                        enum:
                          - false
                          - true
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
                      - suffix
                      - teamId
                      - userId
                      - verified
                    type: object
                required:
                  - domain
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````