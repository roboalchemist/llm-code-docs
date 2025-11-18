# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/add-a-domain-to-a-project.md

# Add a domain to a project

> Add a domain to the project by passing its domain name and by specifying the project by either passing the project `id` or `name` in the URL. If the domain is not yet verified to be used on this project, the request will return `verified = false`, and the domain will need to be verified according to the `verification` challenge via `POST /projects/:idOrName/domains/:domain/verify`. If the domain already exists on the project, the request will fail with a `400` status code.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v10/projects/{idOrName}/domains
paths:
  path: /v10/projects/{idOrName}/domains
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
                  - description: The project domain name
                    example: www.example.com
                    type: string
              gitBranch:
                allOf:
                  - description: Git branch to link the project domain
                    example: null
                    maxLength: 250
                    type: string
                    nullable: true
              customEnvironmentId:
                allOf:
                  - description: >-
                      The unique custom environment identifier within the
                      project
                    type: string
              redirect:
                allOf:
                  - description: Target destination domain for redirect
                    example: foobar.com
                    type: string
                    nullable: true
              redirectStatusCode:
                allOf:
                  - description: Status code for domain redirect
                    example: 307
                    type: integer
                    enum:
                      - null
                      - 301
                      - 302
                      - 307
                      - 308
                    nullable: true
            required: true
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: www.example.com
              gitBranch: null
              customEnvironmentId: <string>
              redirect: foobar.com
              redirectStatusCode: 307
    codeSamples:
      - label: addProjectDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.AddProjectDomain(ctx, \"<value>\", nil, nil, &operations.AddProjectDomainRequestBody{\n        Name: \"www.example.com\",\n        GitBranch: nil,\n        Redirect: vercel.String(\"foobar.com\"),\n        RedirectStatusCode: operations.AddProjectDomainRedirectStatusCodeThreeHundredAndSeven.ToPointer(),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: addProjectDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.addProjectDomain({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "www.example.com",
                gitBranch: null,
                redirect: "foobar.com",
                redirectStatusCode: 307,
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
        description: The domain was successfully added to the project
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              One of the provided values in the request body is invalid.

              One of the provided values in the request query is invalid.

              The domain is not valid

              You can't set both a git branch and a redirect for the domain

              The domain can not be added because the latest production
              deployment for the project was not successful

              The domain redirect is not valid

              A domain cannot redirect to itself

              You can not set the production branch as a branch for your domain
        examples: {}
        description: >-
          One of the provided values in the request body is invalid.

          One of the provided values in the request query is invalid.

          The domain is not valid

          You can't set both a git branch and a redirect for the domain

          The domain can not be added because the latest production deployment
          for the project was not successful

          The domain redirect is not valid

          A domain cannot redirect to itself

          You can not set the production branch as a branch for your domain
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
            description: |-
              You do not have permission to access this resource.
              You don't have access to the domain you are adding
        examples: {}
        description: |-
          You do not have permission to access this resource.
          You don't have access to the domain you are adding
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The domain is already assigned to another Vercel project

              Cannot create project domain since owner already has `domain` on
              their account, but it's not verified yet.

              Cannot create project domain since owner already has `domain` on
              their account, and it's verified.

              The domain is not allowed to be used

              The project is currently being transferred
        examples: {}
        description: >-
          The domain is already assigned to another Vercel project

          Cannot create project domain since owner already has `domain` on their
          account, but it's not verified yet.

          Cannot create project domain since owner already has `domain` on their
          account, and it's verified.

          The domain is not allowed to be used

          The project is currently being transferred
  deprecated: false
  type: path
components:
  schemas: {}

````