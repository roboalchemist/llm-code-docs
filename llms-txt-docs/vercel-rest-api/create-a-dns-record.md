# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/create-a-dns-record.md

# Create a DNS record

> Creates a DNS record for a domain.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/domains/{domain}/records
paths:
  path: /v2/domains/{domain}/records
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
      path:
        domain:
          schema:
            - type: string
              required: true
              description: The domain used to create the DNS record.
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              type:
                allOf:
                  - &ref_0
                    description: >-
                      The type of record, it could be one of the valid DNS
                      records.
                    type: string
                    enum:
                      - A
                      - AAAA
                      - ALIAS
                      - CAA
                      - CNAME
                      - HTTPS
                      - MX
                      - SRV
                      - TXT
                      - NS
                  - description: Must be of type `A`.
                    type: string
                    enum:
                      - A
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: The record value must be a valid IPv4 address.
                    type: string
                    format: ipv4
                    example: 192.0.2.42
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `AAAA`.
                    type: string
                    enum:
                      - AAAA
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: An AAAA record pointing to an IPv6 address.
                    type: string
                    format: ipv6
                    example: 2001:DB8::42
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `ALIAS`.
                    type: string
                    enum:
                      - ALIAS
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: >-
                      An ALIAS virtual record pointing to a hostname resolved to
                      an A record on server side.
                    type: string
                    example: cname.vercel-dns.com
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `CAA`.
                    type: string
                    enum:
                      - CAA
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: >-
                      A CAA record to specify which Certificate Authorities
                      (CAs) are allowed to issue certificates for the domain.
                    type: string
                    example: 0 issue \"letsencrypt.org\"
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `CNAME`.
                    type: string
                    enum:
                      - CNAME
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: A CNAME record mapping to another domain name.
                    type: string
                    example: cname.vercel-dns.com
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `MX`.
                    type: string
                    enum:
                      - MX
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: >-
                      An MX record specifying the mail server responsible for
                      accepting messages on behalf of the domain name.
                    type: string
                    example: 10 mail.example.com.
              mxPriority:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 65535
                    example: 10
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
              - mxPriority
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `SRV`.
                    type: string
                    enum:
                      - SRV
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              srv:
                allOf:
                  - type: object
                    additionalProperties: false
                    required:
                      - weight
                      - port
                      - priority
                      - target
                    properties:
                      priority:
                        anyOf:
                          - type: number
                            minimum: 0
                            maximum: 65535
                            example: 10
                        nullable: true
                      weight:
                        anyOf:
                          - type: number
                            minimum: 0
                            maximum: 65535
                            example: 10
                        nullable: true
                      port:
                        anyOf:
                          - type: number
                            minimum: 0
                            maximum: 65535
                            example: 5000
                        nullable: true
                      target:
                        type: string
                        example: host.example.com
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - name
              - srv
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `TXT`.
                    type: string
                    enum:
                      - TXT
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: A TXT record containing arbitrary text.
                    type: string
                    example: hello
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `NS`.
                    type: string
                    enum:
                      - NS
              name:
                allOf:
                  - description: A subdomain name.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: An NS domain value.
                    type: string
                    example: ns1.example.com
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `HTTPS`.
                    type: string
                    enum:
                      - HTTPS
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              https:
                allOf:
                  - type: object
                    additionalProperties: false
                    required:
                      - priority
                      - target
                    properties:
                      priority:
                        anyOf:
                          - type: number
                            minimum: 0
                            maximum: 65535
                            example: 10
                        nullable: true
                      target:
                        type: string
                        example: host.example.com
                      params:
                        type: string
                        example: alpn=h2,h3
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - name
              - https
            additionalProperties: false
        examples:
          example:
            value:
              name: subdomain
              type: A
              ttl: 60
              value: 192.0.2.42
              comment: used to verify ownership of domain
    codeSamples:
      - label: createRecord
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.DNS.CreateRecord(ctx, \"example.com\", nil, nil, vercel.Pointer(operations.CreateCreateRecordRequestBodyTen(\n        operations.Ten{\n            Type: operations.CreateRecordRequestBodyDNSRequest10TypeCname,\n            TTL: vercel.Float64(60),\n            HTTPS: operations.RequestBodyHTTPS{\n                Priority: vercel.Float64(10),\n                Target: \"host.example.com\",\n                Params: vercel.String(\"alpn=h2,h3\"),\n            },\n            Comment: vercel.String(\"used to verify ownership of domain\"),\n        },\n    )))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: createRecord
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.dns.createRecord({
              domain: "example.com",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                type: "NS",
                ttl: 60,
                srv: {
                  priority: 10,
                  weight: 10,
                  port: 5000,
                  target: "host.example.com",
                },
                comment: "used to verify ownership of domain",
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
              uid:
                allOf:
                  - type: string
              updated:
                allOf:
                  - type: number
            requiredProperties:
              - uid
              - updated
          - type: object
            properties:
              uid:
                allOf:
                  - type: string
                    description: The id of the newly created DNS record
                    example: rec_V0fra8eEgQwEpFhYG2vTzC3K
            requiredProperties:
              - uid
        examples:
          example:
            value:
              uid: <string>
              updated: 123
        description: Successful response showing the uid of the newly created DNS record.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````