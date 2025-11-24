# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/get-a-domains-configuration.md

# Get a Domain's configuration

> Get a Domain's configuration.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/domains/{domain}/config
paths:
  path: /v6/domains/{domain}/config
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
        projectIdOrName:
          schema:
            - type: string
              required: false
              description: >-
                The project id or name that will be associated with the domain.
                Use this when the domain is not yet associated with a project.
        strict:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: >-
                When true, the response will only include the nameservers
                assigned directly to the specified domain. When false and there
                are no nameservers assigned directly to the specified domain,
                the response will include the nameservers of the domain's parent
                zone.
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
      - label: getDomainConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.GetDomainConfig(ctx, \"example.com\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getDomainConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.getDomainConfig({
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
              configuredBy:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - CNAME
                      - A
                      - http
                      - dns-01
                    description: >-
                      How we see the domain's configuration. - `CNAME`: Domain
                      has a CNAME pointing to Vercel. - `A`: Domain's A record
                      is resolving to Vercel. - `http`: Domain is resolving to
                      Vercel but may be behind a Proxy. - `dns-01`: Domain is
                      not resolving to Vercel but dns-01 challenge is enabled. -
                      `null`: Domain is not resolving to Vercel.
              acceptedChallenges:
                allOf:
                  - items:
                      type: string
                      enum:
                        - dns-01
                        - http-01
                      description: >-
                        Which challenge types the domain can use for issuing
                        certs.
                    type: array
                    description: >-
                      Which challenge types the domain can use for issuing
                      certs.
              recommendedIPv4:
                allOf:
                  - items:
                      properties:
                        rank:
                          type: number
                        value:
                          items:
                            type: string
                          type: array
                      required:
                        - rank
                        - value
                      type: object
                      description: >-
                        Recommended IPv4s for the domain. rank=1 is the
                        preferred value(s) to use. Only using 1 ip value is
                        acceptable.
                    type: array
                    description: >-
                      Recommended IPv4s for the domain. rank=1 is the preferred
                      value(s) to use. Only using 1 ip value is acceptable.
              recommendedCNAME:
                allOf:
                  - items:
                      properties:
                        rank:
                          type: number
                        value:
                          type: string
                      required:
                        - rank
                        - value
                      type: object
                      description: >-
                        Recommended CNAMEs for the domain. rank=1 is the
                        preferred value to use.
                    type: array
                    description: >-
                      Recommended CNAMEs for the domain. rank=1 is the preferred
                      value to use.
              misconfigured:
                allOf:
                  - type: boolean
                    description: >-
                      Whether or not the domain is configured AND we can
                      automatically generate a TLS certificate.
            requiredProperties:
              - configuredBy
              - acceptedChallenges
              - recommendedIPv4
              - recommendedCNAME
              - misconfigured
        examples:
          example:
            value:
              configuredBy: CNAME
              acceptedChallenges:
                - dns-01
              recommendedIPv4:
                - rank: 123
                  value:
                    - <string>
              recommendedCNAME:
                - rank: 123
                  value: <string>
              misconfigured: true
        description: ''
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
  deprecated: false
  type: path
components:
  schemas: {}

````