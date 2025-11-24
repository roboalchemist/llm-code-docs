# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/create-a-custom-environment-for-the-current-project.md

# Create a custom environment for the current project.

> Creates a custom environment for the current project. Cannot be named 'Production' or 'Preview'.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v9/projects/{idOrName}/custom-environments
paths:
  path: /v9/projects/{idOrName}/custom-environments
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
              slug:
                allOf:
                  - description: The slug of the custom environment to create.
                    type: string
                    maxLength: 32
              description:
                allOf:
                  - description: Description of the custom environment. This is optional.
                    type: string
                    maxLength: 256
              branchMatcher:
                allOf:
                  - required:
                      - type
                      - pattern
                    description: >-
                      How we want to determine a matching branch. This is
                      optional.
                    type: object
                    properties:
                      type:
                        description: >-
                          Type of matcher. One of \"equals\", \"startsWith\", or
                          \"endsWith\".
                        enum:
                          - equals
                          - startsWith
                          - endsWith
                      pattern:
                        description: Git branch name or portion thereof.
                        type: string
                        maxLength: 100
              copyEnvVarsFrom:
                allOf:
                  - description: >-
                      Where to copy environment variables from. This is
                      optional.
                    type: string
        examples:
          example:
            value:
              slug: <string>
              description: <string>
              branchMatcher:
                type: equals
                pattern: <string>
              copyEnvVarsFrom: <string>
    codeSamples:
      - label: createCustomEnvironment
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.createCustomEnvironment({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
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
              id:
                allOf:
                  - type: string
                    description: >-
                      Unique identifier for the custom environment (format:
                      env_*)
              slug:
                allOf:
                  - type: string
                    description: URL-friendly name of the environment
              type:
                allOf:
                  - type: string
                    enum:
                      - preview
                      - production
                      - development
                    description: >-
                      The type of environment (production, preview, or
                      development)
              description:
                allOf:
                  - type: string
                    description: Optional description of the environment's purpose
              branchMatcher:
                allOf:
                  - properties:
                      type:
                        type: string
                        enum:
                          - endsWith
                          - startsWith
                          - equals
                        description: The type of matching to perform
                      pattern:
                        type: string
                        description: The pattern to match against branch names
                    required:
                      - type
                      - pattern
                    type: object
                    description: >-
                      Configuration for matching git branches to this
                      environment
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
                      description: List of domains associated with this environment
                    type: array
                    description: List of domains associated with this environment
              currentDeploymentAliases:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: List of aliases for the current deployment
              createdAt:
                allOf:
                  - type: number
                    description: Timestamp when the environment was created
              updatedAt:
                allOf:
                  - type: number
                    description: Timestamp when the environment was last updated
            description: >-
              Internal representation of a custom environment with all required
              properties
            requiredProperties:
              - id
              - slug
              - type
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              slug: <string>
              type: preview
              description: <string>
              branchMatcher:
                type: endsWith
                pattern: <string>
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
              currentDeploymentAliases:
                - <string>
              createdAt: 123
              updatedAt: 123
        description: ''
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
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````