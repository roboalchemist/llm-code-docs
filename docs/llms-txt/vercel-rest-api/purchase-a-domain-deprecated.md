# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/purchase-a-domain-deprecated.md

# Purchase a domain (deprecated)

> This endpoint is deprecated and replaced with the endpoint [Buy a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain). Purchases the specified domain.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v5/domains/buy
paths:
  path: /v5/domains/buy
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
              name:
                allOf:
                  - description: The domain name to purchase.
                    type: string
                    example: example.com
              expectedPrice:
                allOf:
                  - description: The price you expect to be charged for the purchase.
                    type: number
                    example: 10
              renew:
                allOf:
                  - description: >-
                      Indicates whether the domain should be automatically
                      renewed.
                    type: boolean
                    example: true
              country:
                allOf:
                  - description: The country of the domain registrant
                    type: string
                    example: US
              orgName:
                allOf:
                  - description: The company name of the domain registrant
                    type: string
                    example: Acme Inc.
              firstName:
                allOf:
                  - description: The first name of the domain registrant
                    type: string
                    example: Jane
              lastName:
                allOf:
                  - description: The last name of the domain registrant
                    type: string
                    example: Doe
              address1:
                allOf:
                  - description: The street address of the domain registrant
                    type: string
                    example: 340 S Lemon Ave Suite 4133
              city:
                allOf:
                  - description: The city of the domain registrant
                    type: string
                    example: San Francisco
              state:
                allOf:
                  - description: The state of the domain registrant
                    type: string
                    example: CA
              postalCode:
                allOf:
                  - description: The postal code of the domain registrant
                    type: string
                    example: '91789'
              phone:
                allOf:
                  - description: The phone number of the domain registrant
                    type: string
                    example: '+1.4158551452'
              email:
                allOf:
                  - description: The email of the domain registrant
                    type: string
                    example: jane.doe@someplace.com
            required: true
            requiredProperties:
              - name
              - country
              - firstName
              - lastName
              - address1
              - city
              - state
              - postalCode
              - phone
              - email
            additionalProperties: false
        examples:
          example:
            value:
              name: example.com
              expectedPrice: 10
              renew: true
              country: US
              orgName: Acme Inc.
              firstName: Jane
              lastName: Doe
              address1: 340 S Lemon Ave Suite 4133
              city: San Francisco
              state: CA
              postalCode: '91789'
              phone: '+1.4158551452'
              email: jane.doe@someplace.com
    codeSamples:
      - label: buyDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.BuyDomain(ctx, nil, nil, &operations.BuyDomainRequestBody{\n        Name: \"example.com\",\n        ExpectedPrice: vercel.Float64(10),\n        Renew: vercel.Bool(true),\n        Country: \"US\",\n        OrgName: vercel.String(\"Acme Inc.\"),\n        FirstName: \"Jane\",\n        LastName: \"Doe\",\n        Address1: \"340 S Lemon Ave Suite 4133\",\n        City: \"San Francisco\",\n        State: \"CA\",\n        PostalCode: \"91789\",\n        Phone: \"+1.4158551452\",\n        Email: \"jane.doe@someplace.com\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.TwoHundredAndOneApplicationJSONObject != nil {\n        // handle response\n    }\n}"
      - label: buyDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.buyDomain({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "example.com",
                expectedPrice: 10,
                renew: true,
                country: "US",
                orgName: "Acme Inc.",
                firstName: "Jane",
                lastName: "Doe",
                address1: "340 S Lemon Ave Suite 4133",
                city: "San Francisco",
                state: "CA",
                postalCode: "91789",
                phone: "+1.4158551452",
                email: "jane.doe@someplace.com",
              },
            });

            console.log(result);
          }

          run();
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              domain:
                allOf:
                  - properties:
                      uid:
                        type: string
                      ns:
                        items:
                          type: string
                        type: array
                      verified:
                        type: boolean
                      created:
                        type: number
                      pending:
                        type: boolean
                    required:
                      - uid
                      - ns
                      - verified
                      - created
                      - pending
                    type: object
            requiredProperties:
              - domain
        examples:
          example:
            value:
              domain:
                uid: <string>
                ns:
                  - <string>
                verified: true
                created: 123
                pending: true
        description: ''
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              domain:
                allOf:
                  - properties:
                      uid:
                        type: string
                      ns:
                        items:
                          type: string
                        type: array
                      verified:
                        type: boolean
                      created:
                        type: number
                      pending:
                        type: boolean
                    required:
                      - uid
                      - ns
                      - verified
                      - created
                      - pending
                    type: object
            requiredProperties:
              - domain
        examples:
          example:
            value:
              domain:
                uid: <string>
                ns:
                  - <string>
                verified: true
                created: 123
                pending: true
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
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '409': {}
    '429': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````