# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/retrieve-project-domains-by-project-by-id-or-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve project domains by project by id or name

> Retrieve the domains associated with a given project by passing either the project `id` or `name` in the URL.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/domains
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
  /v9/projects/{idOrName}/domains:
    get:
      tags:
        - projects
      summary: Retrieve project domains by project by id or name
      description: >-
        Retrieve the domains associated with a given project by passing either
        the project `id` or `name` in the URL.
      operationId: getProjectDomains
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
            oneOf:
              - type: string
        - name: production
          description: Filters only production domains when set to `true`.
          in: query
          required: false
          schema:
            default: 'false'
            description: Filters only production domains when set to `true`.
            enum:
              - 'true'
              - 'false'
        - name: target
          description: >-
            Filters on the target of the domain. Can be either \"production\",
            \"preview\"
          in: query
          required: false
          schema:
            description: >-
              Filters on the target of the domain. Can be either \"production\",
              \"preview\"
            enum:
              - production
              - preview
            type: string
        - name: customEnvironmentId
          description: The unique custom environment identifier within the project
          in: query
          required: false
          schema:
            description: The unique custom environment identifier within the project
            type: string
            example: env_123abc4567
        - name: gitBranch
          description: Filters domains based on specific branch.
          in: query
          required: false
          schema:
            description: Filters domains based on specific branch.
            type: string
        - name: redirects
          description: >-
            Excludes redirect project domains when \"false\". Includes redirect
            project domains when \"true\" (default).
          in: query
          required: false
          schema:
            default: 'true'
            description: >-
              Excludes redirect project domains when \"false\". Includes
              redirect project domains when \"true\" (default).
            enum:
              - 'true'
              - 'false'
        - name: redirect
          description: Filters domains based on their redirect target.
          in: query
          required: false
          schema:
            description: Filters domains based on their redirect target.
            type: string
            example: example.com
        - name: verified
          description: Filters domains based on their verification status.
          in: query
          required: false
          schema:
            description: Filters domains based on their verification status.
            enum:
              - 'true'
              - 'false'
        - name: limit
          description: Maximum number of domains to list from a request (max 100).
          in: query
          required: false
          schema:
            description: Maximum number of domains to list from a request (max 100).
            type: number
            example: 20
        - name: since
          description: Get domains created after this JavaScript timestamp.
          in: query
          required: false
          schema:
            description: Get domains created after this JavaScript timestamp.
            type: number
            example: 1609499532000
        - name: until
          description: Get domains created before this JavaScript timestamp.
          in: query
          required: false
          schema:
            description: Get domains created before this JavaScript timestamp.
            type: number
            example: 1612264332000
        - name: order
          description: Domains sort order by createdAt
          in: query
          required: false
          schema:
            default: DESC
            description: Domains sort order by createdAt
            enum:
              - ASC
              - DESC
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
          description: Successful response retrieving a list of domains
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
                      domains:
                        items:
                          properties:
                            name:
                              type: string
                            apexName:
                              type: string
                            projectId:
                              type: string
                            redirect:
                              nullable: true
                              type: string
                            redirectStatusCode:
                              nullable: true
                              type: number
                              enum:
                                - 301
                                - 302
                                - 307
                                - 308
                            gitBranch:
                              nullable: true
                              type: string
                            customEnvironmentId:
                              nullable: true
                              type: string
                            updatedAt:
                              type: number
                            createdAt:
                              type: number
                            verified:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                `true` if the domain is verified for use with
                                the project. If `false` it will not be used as
                                an alias on this project until the challenge in
                                `verification` is completed.
                            verification:
                              items:
                                properties:
                                  type:
                                    type: string
                                  domain:
                                    type: string
                                  value:
                                    type: string
                                  reason:
                                    type: string
                                required:
                                  - domain
                                  - reason
                                  - type
                                  - value
                                type: object
                                description: >-
                                  A list of verification challenges, one of
                                  which must be completed to verify the domain
                                  for use on the project. After the challenge is
                                  complete `POST
                                  /projects/:idOrName/domains/:domain/verify` to
                                  verify the domain. Possible challenges: - If
                                  `verification.type = TXT` the
                                  `verification.domain` will be checked for a
                                  TXT record matching `verification.value`.
                              type: array
                              description: >-
                                A list of verification challenges, one of which
                                must be completed to verify the domain for use
                                on the project. After the challenge is complete
                                `POST
                                /projects/:idOrName/domains/:domain/verify` to
                                verify the domain. Possible challenges: - If
                                `verification.type = TXT` the
                                `verification.domain` will be checked for a TXT
                                record matching `verification.value`.
                          required:
                            - apexName
                            - name
                            - projectId
                            - verified
                          type: object
                        type: array
                      pagination:
                        properties:
                          count:
                            type: number
                          next:
                            nullable: true
                            type: number
                          prev:
                            nullable: true
                            type: number
                        required:
                          - count
                          - next
                          - prev
                        type: object
                    required:
                      - domains
                      - pagination
                    type: object
                  - properties:
                      domains:
                        items:
                          properties:
                            name:
                              type: string
                            apexName:
                              type: string
                            projectId:
                              type: string
                            redirect:
                              nullable: true
                              type: string
                            redirectStatusCode:
                              nullable: true
                              type: number
                              enum:
                                - 301
                                - 302
                                - 307
                                - 308
                            gitBranch:
                              nullable: true
                              type: string
                            customEnvironmentId:
                              nullable: true
                              type: string
                            updatedAt:
                              type: number
                            createdAt:
                              type: number
                            verified:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                `true` if the domain is verified for use with
                                the project. If `false` it will not be used as
                                an alias on this project until the challenge in
                                `verification` is completed.
                            verification:
                              items:
                                properties:
                                  type:
                                    type: string
                                  domain:
                                    type: string
                                  value:
                                    type: string
                                  reason:
                                    type: string
                                required:
                                  - domain
                                  - reason
                                  - type
                                  - value
                                type: object
                                description: >-
                                  A list of verification challenges, one of
                                  which must be completed to verify the domain
                                  for use on the project. After the challenge is
                                  complete `POST
                                  /projects/:idOrName/domains/:domain/verify` to
                                  verify the domain. Possible challenges: - If
                                  `verification.type = TXT` the
                                  `verification.domain` will be checked for a
                                  TXT record matching `verification.value`.
                              type: array
                              description: >-
                                A list of verification challenges, one of which
                                must be completed to verify the domain for use
                                on the project. After the challenge is complete
                                `POST
                                /projects/:idOrName/domains/:domain/verify` to
                                verify the domain. Possible challenges: - If
                                `verification.type = TXT` the
                                `verification.domain` will be checked for a TXT
                                record matching `verification.value`.
                          required:
                            - apexName
                            - name
                            - projectId
                            - verified
                          type: object
                        type: array
                      pagination:
                        $ref: '#/components/schemas/Pagination'
                    required:
                      - domains
                      - pagination
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