# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/get-domain-transfer-info-deprecated.md

# Get domain transfer info (deprecated)

> This endpoint is deprecated and replaced with the endpoint [Get a domain's transfer status](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domains-transfer-status). Fetch domain transfer availability or transfer status if a transfer is in progress.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/domains/{domain}/registry
paths:
  path: /v1/domains/{domain}/registry
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
      - label: getDomainTransfer
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.GetDomainTransfer(ctx, \"example.com\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getDomainTransfer
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.getDomainTransfer({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              domain: "example.com",
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
              reason:
                allOf:
                  - type: string
              status:
                allOf:
                  - type: string
              transferable:
                allOf:
                  - type: boolean
              transferPolicy:
                allOf:
                  - type: string
                    enum:
                      - charge-and-renew
            requiredProperties:
              - reason
              - status
              - transferable
              - transferPolicy
          - type: object
            properties:
              transferable:
                allOf:
                  - type: boolean
                    description: Whether or not the domain is transferable
              transferPolicy:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - charge-and-renew
                      - no-charge-no-change
                      - no-change
                      - new-term
                      - not-supported
                    description: >-
                      The domain's transfer policy (depends on TLD
                      requirements). `charge-and-renew`: transfer will charge
                      for renewal and will renew the existing domain's
                      registration. `no-charge-no-change`: transfer will have no
                      change to registration period and does not require charge.
                      `no-change`: transfer charge is required, but no change in
                      registration period. `new-term`: transfer charge is
                      required and a new registry term is set based on the
                      transfer date. `not-supported`: transfers are not
                      supported for this domain or TLD. `null`: This TLD is not
                      supported by Vercel's Registrar.
              reason:
                allOf:
                  - type: string
                    description: Description associated with transferable state.
              status:
                allOf:
                  - type: string
                    enum:
                      - completed
                      - undef
                      - pending_owner
                      - pending_admin
                      - pending_registry
                      - cancelled
                      - unknown
                    description: >-
                      The current state of an ongoing transfer. `pending_owner`:
                      Awaiting approval by domain's admin contact (every
                      transfer begins with this status). If approval is not
                      given within five days, the transfer is cancelled.
                      `pending_admin`: Waiting for approval by Vercel Registrar
                      admin. `pending_registry`: Awaiting registry approval (the
                      transfer completes after 7 days unless it is declined by
                      the current registrar). `completed`: The transfer
                      completed successfully. `cancelled`: The transfer was
                      cancelled. `undef`: No transfer exists for this domain.
                      `unknown`: This TLD is not supported by Vercel's
                      Registrar.
            requiredProperties:
              - transferable
              - transferPolicy
              - reason
              - status
        examples:
          example:
            value:
              reason: <string>
              status: <string>
              transferable: true
              transferPolicy: charge-and-renew
        description: ''
    '400': {}
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````