# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/retrieve-project-domains-by-project-by-id-or-name.md

# Retrieve project domains by project by id or name

> Retrieve the domains associated with a given project by passing either the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/domains
paths:
  path: /v9/projects/{idOrName}/domains
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
        idOrName:
          schema:
            - type: string
              required: true
              description: The unique project identifier or the project name
      query:
        production:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: Filters only production domains when set to `true`.
              default: 'false'
        target:
          schema:
            - type: enum<string>
              enum:
                - production
                - preview
              required: false
              description: >-
                Filters on the target of the domain. Can be either
                \"production\", \"preview\"
        customEnvironmentId:
          schema:
            - type: string
              required: false
              description: The unique custom environment identifier within the project
              example: env_123abc4567
        gitBranch:
          schema:
            - type: string
              required: false
              description: Filters domains based on specific branch.
        redirects:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: >-
                Excludes redirect project domains when \"false\". Includes
                redirect project domains when \"true\" (default).
              default: 'true'
        redirect:
          schema:
            - type: string
              required: false
              description: Filters domains based on their redirect target.
              example: example.com
        verified:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: Filters domains based on their verification status.
        limit:
          schema:
            - type: number
              required: false
              description: Maximum number of domains to list from a request (max 100).
              example: 20
        since:
          schema:
            - type: number
              required: false
              description: Get domains created after this JavaScript timestamp.
              example: 1609499532000
        until:
          schema:
            - type: number
              required: false
              description: Get domains created before this JavaScript timestamp.
              example: 1612264332000
        order:
          schema:
            - type: enum<string>
              enum:
                - ASC
                - DESC
              required: false
              description: Domains sort order by createdAt
              default: DESC
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
      - label: getProjectDomains
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.getProjectDomains({
              idOrName: "<value>",
              customEnvironmentId: "env_123abc4567",
              redirect: "example.com",
              limit: 20,
              since: 1609499532000,
              until: 1612264332000,
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
          - type: object
            properties:
              domains:
                allOf:
                  - items:
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
                            - 307
                            - 301
                            - 302
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
                          description: >-
                            `true` if the domain is verified for use with the
                            project. If `false` it will not be used as an alias
                            on this project until the challenge in
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
                              - type
                              - domain
                              - value
                              - reason
                            type: object
                            description: >-
                              A list of verification challenges, one of which
                              must be completed to verify the domain for use on
                              the project. After the challenge is complete `POST
                              /projects/:idOrName/domains/:domain/verify` to
                              verify the domain. Possible challenges: - If
                              `verification.type = TXT` the
                              `verification.domain` will be checked for a TXT
                              record matching `verification.value`.
                          type: array
                          description: >-
                            A list of verification challenges, one of which must
                            be completed to verify the domain for use on the
                            project. After the challenge is complete `POST
                            /projects/:idOrName/domains/:domain/verify` to
                            verify the domain. Possible challenges: - If
                            `verification.type = TXT` the `verification.domain`
                            will be checked for a TXT record matching
                            `verification.value`.
                      required:
                        - name
                        - apexName
                        - projectId
                        - verified
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
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
            requiredProperties:
              - domains
              - pagination
          - type: object
            properties:
              domains:
                allOf:
                  - items:
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
                            - 307
                            - 301
                            - 302
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
                          description: >-
                            `true` if the domain is verified for use with the
                            project. If `false` it will not be used as an alias
                            on this project until the challenge in
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
                              - type
                              - domain
                              - value
                              - reason
                            type: object
                            description: >-
                              A list of verification challenges, one of which
                              must be completed to verify the domain for use on
                              the project. After the challenge is complete `POST
                              /projects/:idOrName/domains/:domain/verify` to
                              verify the domain. Possible challenges: - If
                              `verification.type = TXT` the
                              `verification.domain` will be checked for a TXT
                              record matching `verification.value`.
                          type: array
                          description: >-
                            A list of verification challenges, one of which must
                            be completed to verify the domain for use on the
                            project. After the challenge is complete `POST
                            /projects/:idOrName/domains/:domain/verify` to
                            verify the domain. Possible challenges: - If
                            `verification.type = TXT` the `verification.domain`
                            will be checked for a TXT record matching
                            `verification.value`.
                      required:
                        - name
                        - apexName
                        - projectId
                        - verified
                      type: object
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            requiredProperties:
              - domains
              - pagination
        examples:
          example:
            value:
              domains:
                - name: <string>
                  apexName: <string>
                  projectId: <string>
                  redirect: <string>
                  redirectStatusCode: 307
                  gitBranch: <string>
                  customEnvironmentId: <string>
                  updatedAt: 123
                  createdAt: 123
                  verified: true
                  verification:
                    - type: <string>
                      domain: <string>
                      value: <string>
                      reason: <string>
              pagination:
                count: 123
                next: 123
                prev: 123
        description: Successful response retrieving a list of domains
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