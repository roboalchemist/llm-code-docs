# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/list-existing-dns-records.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List existing DNS records

> Retrieves a list of DNS records created for a domain name. By default it returns 20 records if no limit is provided. The rest can be retrieved using the pagination options.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/domains/{domain}/records
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
  /v4/domains/{domain}/records:
    get:
      tags:
        - dns
      summary: List existing DNS records
      description: >-
        Retrieves a list of DNS records created for a domain name. By default it
        returns 20 records if no limit is provided. The rest can be retrieved
        using the pagination options.
      operationId: getRecords
      parameters:
        - name: domain
          in: path
          required: true
          schema:
            type: string
            example: example.com
        - name: limit
          description: Maximum number of records to list from a request.
          in: query
          required: false
          schema:
            description: Maximum number of records to list from a request.
            type: string
            example: 20
        - name: since
          description: Get records created after this JavaScript timestamp.
          in: query
          required: false
          schema:
            description: Get records created after this JavaScript timestamp.
            type: string
            example: 1609499532000
        - name: until
          description: Get records created before this JavaScript timestamp.
          in: query
          required: false
          schema:
            description: Get records created before this JavaScript timestamp.
            type: string
            example: 1612264332000
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
      responses:
        '200':
          description: Successful response retrieving a list of paginated DNS records.
          content:
            application/json:
              schema:
                oneOf:
                  - type: string
                  - properties:
                      records:
                        items:
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
                            - created
                            - createdAt
                            - creator
                            - id
                            - name
                            - slug
                            - type
                            - updated
                            - updatedAt
                            - value
                          type: object
                        type: array
                    required:
                      - records
                    type: object
                  - properties:
                      records:
                        items:
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
                            - created
                            - createdAt
                            - creator
                            - id
                            - name
                            - slug
                            - type
                            - updated
                            - updatedAt
                            - value
                          type: object
                        type: array
                      pagination:
                        $ref: '#/components/schemas/Pagination'
                    required:
                      - pagination
                      - records
                    type: object
                    description: >-
                      Successful response retrieving a list of paginated DNS
                      records.
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
      security:
        - bearerToken: []
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
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````