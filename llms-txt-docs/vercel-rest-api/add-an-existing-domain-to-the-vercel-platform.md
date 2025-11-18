# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/add-an-existing-domain-to-the-vercel-platform.md

# Add an existing domain to the Vercel platform

> This endpoint is used for adding a new apex domain name with Vercel for the authenticating user. Note: This endpoint is no longer used for initiating domain transfers from external registrars to Vercel. For this, please use the endpoint [Transfer-in a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/transfer-in-a-domain).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v7/domains
paths:
  path: /v7/domains
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
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
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              method:
                allOf:
                  - &ref_0
                    description: >-
                      The domain operation to perform. It can be either `add` or
                      `move-in`.
                    type: string
                    example: add
                  - description: The domain operation to perform.
                    type: string
                    example: add
              name:
                allOf:
                  - description: The domain name you want to add.
                    type: string
                    example: example.com
              cdnEnabled:
                allOf:
                  - description: >-
                      Whether the domain has the Vercel Edge Network enabled or
                      not.
                    type: boolean
                    example: true
              zone:
                allOf:
                  - type: boolean
            description: add
            requiredProperties:
              - name
            additionalProperties: false
          - type: object
            properties:
              method:
                allOf:
                  - *ref_0
                  - description: The domain operation to perform.
                    type: string
                    example: move-in
              name:
                allOf:
                  - description: The domain name you want to add.
                    type: string
                    example: example.com
              token:
                allOf:
                  - description: The move-in token from Move Requested email.
                    type: string
                    example: fdhfr820ad#@FAdlj$$
            description: move-in
            requiredProperties:
              - method
              - name
            additionalProperties: false
          - type: object
            properties:
              method:
                allOf:
                  - *ref_0
                  - description: The domain operation to perform.
                    type: string
                    example: transfer-in
              name:
                allOf:
                  - description: The domain name you want to add.
                    type: string
                    example: example.com
              authCode:
                allOf:
                  - description: The authorization code assigned to the domain.
                    type: string
                    example: fdhfr820ad#@FAdlj$$
              expectedPrice:
                allOf:
                  - description: >-
                      The price you expect to be charged for the required 1 year
                      renewal.
                    type: number
                    example: 8
            description: transfer-in
            deprecated: true
            requiredProperties:
              - method
              - name
            additionalProperties: false
        examples:
          example:
            value:
              name: example.com
              cdnEnabled: true
              zone: true
              method: add
    codeSamples:
      - label: createOrTransferDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.createOrTransferDomain({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "example.com",
                method: "add",
                token: "fdhfr820ad#@FAdlj$$",
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              domain:
                allOf:
                  - properties:
                      verified:
                        type: boolean
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
                          id:
                            type: string
                        required:
                          - username
                          - email
                          - id
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
                      orderedAt:
                        type: number
                        description: >-
                          Timestamp in milliseconds at which the domain was
                          ordered.
                        example: 1613602938882
                      renew:
                        type: boolean
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
                      teamId:
                        nullable: true
                        type: string
                    required:
                      - verified
                      - nameservers
                      - intendedNameservers
                      - creator
                      - name
                      - boughtAt
                      - createdAt
                      - expiresAt
                      - id
                      - serviceType
                      - userId
                      - teamId
                    type: object
            requiredProperties:
              - domain
        examples:
          example:
            value:
              domain:
                verified: true
                nameservers:
                  - ns1.nameserver.net
                  - ns2.nameserver.net
                intendedNameservers:
                  - ns1.vercel-dns.com
                  - ns2.vercel-dns.com
                customNameservers:
                  - ns1.nameserver.net
                  - ns2.nameserver.net
                creator:
                  id: ZspSRT4ljIEEmMHgoDwKWDei
                  username: vercel_user
                  email: demo@example.com
                registrar: new
                name: example.com
                boughtAt: 1613602938882
                createdAt: 1613602938882
                expiresAt: 1613602938882
                id: EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1
                orderedAt: 1613602938882
                renew: true
                serviceType: zeit.world
                transferredAt: 1613602938882
                transferStartedAt: 1613602938882
                userId: <string>
                teamId: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '402':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The account was soft-blocked for an unhandled reason.
              The account is missing a payment so payment method must be updated
        examples: {}
        description: |-
          The account was soft-blocked for an unhandled reason.
          The account is missing a payment so payment method must be updated
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The domain is not allowed to be used
        examples: {}
        description: The domain is not allowed to be used
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````