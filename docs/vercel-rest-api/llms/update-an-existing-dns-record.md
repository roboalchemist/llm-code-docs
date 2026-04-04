# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/update-an-existing-dns-record.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an existing DNS record

> Updates an existing DNS record for a domain name.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/domains/records/{recordId}
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
  /v1/domains/records/{recordId}:
    patch:
      tags:
        - dns
      summary: Update an existing DNS record
      description: Updates an existing DNS record for a domain name.
      operationId: updateRecord
      parameters:
        - name: recordId
          description: The id of the DNS record
          in: path
          required: true
          schema:
            description: The id of the DNS record
            example: rec_2qn7pzrx89yxy34vezpd31y9
            type: string
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
              additionalProperties: false
              properties:
                name:
                  type: string
                  description: The name of the DNS record
                  example: example-1
                  nullable: true
                value:
                  type: string
                  description: The value of the DNS record
                  example: google.com
                  nullable: true
                type:
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
                  type: string
                  description: The type of the DNS record
                  example: A
                  maxLength: 255
                  nullable: true
                ttl:
                  type: integer
                  description: The Time to live (TTL) value of the DNS record
                  example: '60'
                  minimum: 60
                  maximum: 2147483647
                  nullable: true
                mxPriority:
                  type: integer
                  description: The MX priority value of the DNS record
                  nullable: true
                srv:
                  additionalProperties: false
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
                  additionalProperties: false
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
                  type: string
                  description: A comment to add context on what this DNS record is for
                  example: used to verify ownership of domain
                  maxLength: 500
              type: object
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                  name:
                    type: string
                  type:
                    type: string
                    enum:
                      - record
                      - record-sys
                  value:
                    type: string
                  creator:
                    type: string
                  domain:
                    type: string
                  ttl:
                    type: number
                  comment:
                    type: string
                  recordType:
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
                  createdAt:
                    nullable: true
                    type: number
                required:
                  - creator
                  - domain
                  - id
                  - name
                  - recordType
                  - type
                  - value
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
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