# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/list-existing-dns-records.md

# List existing DNS records

> Retrieves a list of DNS records created for a domain name. By default it returns 20 records if no limit is provided. The rest can be retrieved using the pagination options.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/domains/{domain}/records
paths:
  path: /v4/domains/{domain}/records
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
        limit:
          schema:
            - type: string
              required: false
              description: Maximum number of records to list from a request.
              example: 20
        since:
          schema:
            - type: string
              required: false
              description: Get records created after this JavaScript timestamp.
              example: 1609499532000
        until:
          schema:
            - type: string
              required: false
              description: Get records created before this JavaScript timestamp.
              example: 1612264332000
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
      - label: getRecords
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.DNS.GetRecords(ctx, operations.GetRecordsRequest{\n        Domain: \"example.com\",\n        Limit: vercel.String(\"20\"),\n        Since: vercel.String(\"1609499532000\"),\n        Until: vercel.String(\"1612264332000\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getRecords
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.dns.getRecords({
              domain: "example.com",
              limit: "20",
              since: "1609499532000",
              until: "1612264332000",
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
          - type: string
          - type: object
            properties:
              records:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        slug:
                          type: string
                        name:
                          type: string
                        type:
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
                        value:
                          type: string
                        mxPriority:
                          type: number
                        priority:
                          type: number
                        creator:
                          type: string
                        created:
                          nullable: true
                          type: number
                        updated:
                          nullable: true
                          type: number
                        createdAt:
                          nullable: true
                          type: number
                        updatedAt:
                          nullable: true
                          type: number
                        ttl:
                          type: number
                        comment:
                          type: string
                      required:
                        - id
                        - slug
                        - name
                        - type
                        - value
                        - creator
                        - created
                        - updated
                        - createdAt
                        - updatedAt
                      type: object
                    type: array
            requiredProperties:
              - records
          - type: object
            properties:
              records:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        slug:
                          type: string
                        name:
                          type: string
                        type:
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
                        value:
                          type: string
                        mxPriority:
                          type: number
                        priority:
                          type: number
                        creator:
                          type: string
                        created:
                          nullable: true
                          type: number
                        updated:
                          nullable: true
                          type: number
                        createdAt:
                          nullable: true
                          type: number
                        updatedAt:
                          nullable: true
                          type: number
                        ttl:
                          type: number
                        comment:
                          type: string
                      required:
                        - id
                        - slug
                        - name
                        - type
                        - value
                        - creator
                        - created
                        - updated
                        - createdAt
                        - updatedAt
                      type: object
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            description: Successful response retrieving a list of paginated DNS records.
            requiredProperties:
              - records
              - pagination
        examples:
          example:
            value: <string>
        description: Successful response retrieving a list of paginated DNS records.
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
  schemas:
    Pagination:
      properties:
        count:
          type: number
          description: Amount of items in the current page.
          example: 20
        next:
          nullable: true
          type: number
          description: Timestamp that must be used to request the next page.
          example: 1540095775951
        prev:
          nullable: true
          type: number
          description: Timestamp that must be used to request the previous page.
          example: 1540095775951
      required:
        - count
        - next
        - prev
      type: object
      description: >-
        This object contains information related to the pagination of the
        current request, including the necessary parameters to get the next or
        previous page of data.

````