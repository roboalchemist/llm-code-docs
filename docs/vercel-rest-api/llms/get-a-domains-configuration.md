# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/get-a-domains-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a Domain's configuration

> Get a Domain's configuration.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/domains/{domain}/config
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
  /v6/domains/{domain}/config:
    get:
      tags:
        - domains
      summary: Get a Domain's configuration
      description: Get a Domain's configuration.
      operationId: getDomainConfig
      parameters:
        - name: domain
          description: The name of the domain.
          in: path
          required: true
          schema:
            description: The name of the domain.
            type: string
            example: example.com
        - name: projectIdOrName
          description: >-
            The project id or name that will be associated with the domain. Use
            this when the domain is not yet associated with a project.
          in: query
          required: false
          schema:
            description: >-
              The project id or name that will be associated with the domain.
              Use this when the domain is not yet associated with a project.
            type: string
        - name: strict
          description: >-
            When true, the response will only include the nameservers assigned
            directly to the specified domain. When false and there are no
            nameservers assigned directly to the specified domain, the response
            will include the nameservers of the domain's parent zone.
          in: query
          required: false
          schema:
            enum:
              - 'true'
              - 'false'
            description: >-
              When true, the response will only include the nameservers assigned
              directly to the specified domain. When false and there are no
              nameservers assigned directly to the specified domain, the
              response will include the nameservers of the domain's parent zone.
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
          description: ''
          content:
            application/json:
              schema:
                properties:
                  configuredBy:
                    nullable: true
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
                    items:
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
                    items:
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
                    items:
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
                    type: boolean
                    enum:
                      - false
                      - true
                    description: >-
                      Whether or not the domain is configured AND we can
                      automatically generate a TLS certificate.
                required:
                  - acceptedChallenges
                  - configuredBy
                  - misconfigured
                  - recommendedCNAME
                  - recommendedIPv4
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````