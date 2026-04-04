# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/create-a-dns-record.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a DNS record

> Creates a DNS record for a domain.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/domains/{domain}/records
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
  /v2/domains/{domain}/records:
    post:
      tags:
        - dns
      summary: Create a DNS record
      description: Creates a DNS record for a domain.
      operationId: createRecord
      parameters:
        - name: domain
          description: The domain used to create the DNS record.
          in: path
          required: true
          schema:
            description: The domain used to create the DNS record.
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
      requestBody:
        content:
          application/json:
            schema:
              required:
                - type
              properties:
                type:
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
              anyOf:
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - value
                    - name
                  properties:
                    name:
                      description: A subdomain name or an empty string for the root domain.
                      type: string
                      example: subdomain
                    type:
                      description: Must be of type `A`.
                      type: string
                      enum:
                        - A
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    value:
                      description: The record value must be a valid IPv4 address.
                      type: string
                      format: ipv4
                      example: 192.0.2.42
                    comment:
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - value
                    - name
                  properties:
                    name:
                      description: A subdomain name or an empty string for the root domain.
                      type: string
                      example: subdomain
                    type:
                      description: Must be of type `AAAA`.
                      type: string
                      enum:
                        - AAAA
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    value:
                      description: An AAAA record pointing to an IPv6 address.
                      type: string
                      format: ipv6
                      example: 2001:DB8::42
                    comment:
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - value
                    - name
                  properties:
                    name:
                      description: A subdomain name or an empty string for the root domain.
                      type: string
                      example: subdomain
                    type:
                      description: Must be of type `ALIAS`.
                      type: string
                      enum:
                        - ALIAS
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    value:
                      description: >-
                        An ALIAS virtual record pointing to a hostname resolved
                        to an A record on server side.
                      type: string
                      example: cname.vercel-dns.com
                    comment:
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - value
                    - name
                  properties:
                    name:
                      description: A subdomain name or an empty string for the root domain.
                      type: string
                      example: subdomain
                    type:
                      description: Must be of type `CAA`.
                      type: string
                      enum:
                        - CAA
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    value:
                      description: >-
                        A CAA record to specify which Certificate Authorities
                        (CAs) are allowed to issue certificates for the domain.
                      type: string
                      example: 0 issue \"letsencrypt.org\"
                    comment:
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - name
                  properties:
                    name:
                      description: A subdomain name or an empty string for the root domain.
                      type: string
                      example: subdomain
                    type:
                      description: Must be of type `CNAME`.
                      type: string
                      enum:
                        - CNAME
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    value:
                      description: A CNAME record mapping to another domain name.
                      type: string
                      example: cname.vercel-dns.com
                    comment:
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - value
                    - name
                    - mxPriority
                  properties:
                    name:
                      description: A subdomain name or an empty string for the root domain.
                      type: string
                      example: subdomain
                    type:
                      description: Must be of type `MX`.
                      type: string
                      enum:
                        - MX
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    value:
                      description: >-
                        An MX record specifying the mail server responsible for
                        accepting messages on behalf of the domain name.
                      type: string
                      example: 10 mail.example.com.
                    mxPriority:
                      type: number
                      minimum: 0
                      maximum: 65535
                      example: 10
                    comment:
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - name
                    - srv
                  properties:
                    type:
                      description: Must be of type `SRV`.
                      type: string
                      enum:
                        - SRV
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    srv:
                      type: object
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
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - value
                    - name
                  properties:
                    type:
                      description: Must be of type `TXT`.
                      type: string
                      enum:
                        - TXT
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    value:
                      description: A TXT record containing arbitrary text.
                      type: string
                      example: hello
                    comment:
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - name
                  properties:
                    name:
                      description: A subdomain name.
                      type: string
                      example: subdomain
                    type:
                      description: Must be of type `NS`.
                      type: string
                      enum:
                        - NS
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    value:
                      description: An NS domain value.
                      type: string
                      example: ns1.example.com
                    comment:
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
                - type: object
                  additionalProperties: false
                  required:
                    - type
                    - name
                    - https
                  properties:
                    type:
                      description: Must be of type `HTTPS`.
                      type: string
                      enum:
                        - HTTPS
                    ttl:
                      description: >-
                        The TTL value. Must be a number between 60 and
                        2147483647. Default value is 60.
                      type: number
                      minimum: 60
                      maximum: 2147483647
                      example: 60
                    https:
                      type: object
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
                      type: string
                      description: A comment to add context on what this DNS record is for
                      example: used to verify ownership of domain
                      maxLength: 500
        required: true
      responses:
        '200':
          description: Successful response showing the uid of the newly created DNS record.
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
                      uid:
                        type: string
                      updated:
                        type: number
                    required:
                      - uid
                      - updated
                    type: object
                  - properties:
                      uid:
                        type: string
                        description: The id of the newly created DNS record
                        example: rec_V0fra8eEgQwEpFhYG2vTzC3K
                    required:
                      - uid
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