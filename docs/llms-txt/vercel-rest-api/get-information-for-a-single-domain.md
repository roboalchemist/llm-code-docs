# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/get-information-for-a-single-domain.md

# Get Information for a Single Domain

> Get information for a single domain in an account or team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/domains/{domain}
paths:
  path: /v5/domains/{domain}
  method: get
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
      path:
        domain:
          schema:
            - type: string
              required: true
              description: The name of the domain.
              example: example.com
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
    body: {}
    codeSamples:
      - label: getDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.GetDomain(ctx, \"example.com\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.getDomain({
              domain: "example.com",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
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
                      suffix:
                        type: boolean
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
                      name:
                        type: string
                        description: The domain name.
                        example: example.com
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
                    required:
                      - suffix
                      - verified
                      - nameservers
                      - intendedNameservers
                      - creator
                      - teamId
                      - boughtAt
                      - name
                      - createdAt
                      - expiresAt
                      - id
                      - serviceType
                      - userId
                    type: object
            requiredProperties:
              - domain
        examples:
          example:
            value:
              domain:
                suffix: true
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
                teamId: <string>
                boughtAt: 1613602938882
                name: example.com
                createdAt: 1613602938882
                expiresAt: 1613602938882
                id: EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1
                orderedAt: 1613602938882
                renew: true
                serviceType: zeit.world
                transferredAt: 1613602938882
                transferStartedAt: 1613602938882
                userId: <string>
        description: Successful response retrieving an information for a specific domains.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````