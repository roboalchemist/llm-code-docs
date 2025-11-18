# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/update-an-existing-dns-record.md

# Update an existing DNS record

> Updates an existing DNS record for a domain name.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/domains/records/{recordId}
paths:
  path: /v1/domains/records/{recordId}
  method: patch
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
        recordId:
          schema:
            - type: string
              required: true
              description: The id of the DNS record
              example: rec_2qn7pzrx89yxy34vezpd31y9
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
              name:
                allOf:
                  - type: string
                    description: The name of the DNS record
                    example: example-1
                    nullable: true
              value:
                allOf:
                  - type: string
                    description: The value of the DNS record
                    example: google.com
                    nullable: true
              type:
                allOf:
                  - enum:
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
                    type: string
                    description: The type of the DNS record
                    example: A
                    maxLength: 255
                    nullable: true
              ttl:
                allOf:
                  - type: integer
                    description: The Time to live (TTL) value of the DNS record
                    example: '60'
                    minimum: 60
                    maximum: 2147483647
                    nullable: true
              mxPriority:
                allOf:
                  - type: integer
                    description: The MX priority value of the DNS record
                    nullable: true
              srv:
                allOf:
                  - additionalProperties: false
                    required:
                      - target
                      - weight
                      - port
                      - priority
                    properties:
                      target:
                        type: string
                        description: ''
                        example: example2.com.
                        maxLength: 255
                        nullable: true
                      weight:
                        description: ''
                        type: integer
                        nullable: true
                      port:
                        description: ''
                        type: integer
                        nullable: true
                      priority:
                        description: ''
                        type: integer
                        nullable: true
                    type: object
                    nullable: true
              https:
                allOf:
                  - additionalProperties: false
                    required:
                      - priority
                      - target
                    properties:
                      priority:
                        description: ''
                        type: integer
                        nullable: true
                      target:
                        type: string
                        description: ''
                        example: example2.com.
                        maxLength: 255
                        nullable: true
                      params:
                        description: ''
                        type: string
                        nullable: true
                    type: object
                    nullable: true
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              name: example-1
              value: google.com
              type: A
              ttl: '60'
              mxPriority: 123
              srv:
                target: example2.com.
                weight: 123
                port: 123
                priority: 123
              https:
                priority: 123
                target: example2.com.
                params: <string>
              comment: used to verify ownership of domain
    codeSamples:
      - label: updateRecord
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.DNS.UpdateRecord(ctx, \"rec_2qn7pzrx89yxy34vezpd31y9\", nil, nil, &operations.UpdateRecordRequestBody{\n        Name: vercel.String(\"example-1\"),\n        Value: vercel.String(\"google.com\"),\n        Type: operations.UpdateRecordTypeA.ToPointer(),\n        TTL: vercel.Int64(60),\n        Srv: &operations.Srv{\n            Target: vercel.String(\"example2.com.\"),\n            Weight: vercel.Int64(97604),\n            Port: vercel.Int64(570172),\n            Priority: vercel.Int64(199524),\n        },\n        HTTPS: &operations.HTTPS{\n            Priority: vercel.Int64(35000),\n            Target: vercel.String(\"example2.com.\"),\n        },\n        Comment: vercel.String(\"used to verify ownership of domain\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateRecord
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.dns.updateRecord({
              recordId: "rec_2qn7pzrx89yxy34vezpd31y9",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "example-1",
                value: "google.com",
                type: "A",
                ttl: 60,
                srv: null,
                https: null,
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
              createdAt:
                allOf:
                  - nullable: true
                    type: number
              creator:
                allOf:
                  - type: string
              domain:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              recordType:
                allOf:
                  - type: string
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
              ttl:
                allOf:
                  - type: number
              type:
                allOf:
                  - type: string
                    enum:
                      - record
                      - record-sys
              value:
                allOf:
                  - type: string
              comment:
                allOf:
                  - type: string
            requiredProperties:
              - creator
              - domain
              - id
              - name
              - recordType
              - type
              - value
        examples:
          example:
            value:
              createdAt: 123
              creator: <string>
              domain: <string>
              id: <string>
              name: <string>
              recordType: A
              ttl: 123
              type: record
              value: <string>
              comment: <string>
        description: ''
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