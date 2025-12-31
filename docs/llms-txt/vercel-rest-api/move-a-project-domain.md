# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/move-a-project-domain.md

# Move a project domain

> Move one project's domain to another project. Also allows the move of all redirects pointed to that domain in the same project.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/domains/{domain}/move
paths:
  path: /v1/projects/{idOrName}/domains/{domain}/move
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
        idOrName:
          schema:
            - type: string
              required: true
              description: The unique project identifier or the project name
        domain:
          schema:
            - type: string
              required: true
              description: The project domain name
              example: www.example.com
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
              projectId:
                allOf:
                  - description: The unique target project identifier
                    example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
                    oneOf:
                      - type: string
            requiredProperties:
              - projectId
        examples:
          example:
            value:
              projectId: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
    codeSamples:
      - label: moveProjectDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.moveProjectDomain({
              idOrName: "<value>",
              domain: "www.example.com",
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
              name:
                allOf:
                  - type: string
              apexName:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              redirect:
                allOf:
                  - nullable: true
                    type: string
              redirectStatusCode:
                allOf:
                  - nullable: true
                    type: number
                    enum:
                      - 307
                      - 301
                      - 302
                      - 308
              gitBranch:
                allOf:
                  - nullable: true
                    type: string
              customEnvironmentId:
                allOf:
                  - nullable: true
                    type: string
              updatedAt:
                allOf:
                  - type: number
              createdAt:
                allOf:
                  - type: number
              verified:
                allOf:
                  - type: boolean
                    description: >-
                      `true` if the domain is verified for use with the project.
                      If `false` it will not be used as an alias on this project
                      until the challenge in `verification` is completed.
              verification:
                allOf:
                  - items:
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
                        A list of verification challenges, one of which must be
                        completed to verify the domain for use on the project.
                        After the challenge is complete `POST
                        /projects/:idOrName/domains/:domain/verify` to verify
                        the domain. Possible challenges: - If `verification.type
                        = TXT` the `verification.domain` will be checked for a
                        TXT record matching `verification.value`.
                    type: array
                    description: >-
                      A list of verification challenges, one of which must be
                      completed to verify the domain for use on the project.
                      After the challenge is complete `POST
                      /projects/:idOrName/domains/:domain/verify` to verify the
                      domain. Possible challenges: - If `verification.type =
                      TXT` the `verification.domain` will be checked for a TXT
                      record matching `verification.value`.
            requiredProperties:
              - name
              - apexName
              - projectId
              - verified
        examples:
          example:
            value:
              name: <string>
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
        description: The domain was updated successfuly
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
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The project is currently being transferred
        examples: {}
        description: The project is currently being transferred
  deprecated: false
  type: path
components:
  schemas: {}

````