# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/delete-one-or-more-env-var.md

# Delete one or more Env Var

> Deletes one or many Shared Environment Variables for a given team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/env
paths:
  path: /v1/env
  method: delete
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
              ids:
                allOf:
                  - description: IDs of the Shared Environment Variables to delete
                    minimum: 1
                    maximum: 50
                    type: array
                    items:
                      type: string
                    example:
                      - env_abc123
                      - env_abc124
            requiredProperties:
              - ids
        examples:
          example:
            value:
              ids:
                - env_abc123
                - env_abc124
    codeSamples:
      - label: deleteSharedEnvVariable
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.deleteSharedEnvVariable({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                ids: [
                  "env_abc123",
                  "env_abc124",
                ],
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
              deleted:
                allOf:
                  - items:
                      type: string
                    type: array
              failed:
                allOf:
                  - items:
                      properties:
                        error:
                          properties:
                            code:
                              type: string
                            message:
                              type: string
                            key:
                              type: string
                            envVarId:
                              type: string
                            envVarKey:
                              type: string
                            action:
                              type: string
                            link:
                              type: string
                            value:
                              oneOf:
                                - type: string
                                - items:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                      - development
                                      - preview
                                      - development
                                  type: array
                            gitBranch:
                              type: string
                            target:
                              oneOf:
                                - items:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                      - development
                                      - preview
                                      - development
                                  type: array
                                - type: string
                                  enum:
                                    - production
                                    - preview
                                    - development
                                    - preview
                                    - development
                            project:
                              type: string
                          required:
                            - code
                            - message
                          type: object
                      required:
                        - error
                      type: object
                    type: array
            requiredProperties:
              - deleted
              - failed
        examples:
          example:
            value:
              deleted:
                - <string>
              failed:
                - error:
                    code: <string>
                    message: <string>
                    key: <string>
                    envVarId: <string>
                    envVarKey: <string>
                    action: <string>
                    link: <string>
                    value: <string>
                    gitBranch: <string>
                    target:
                      - production
                    project: <string>
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
  deprecated: false
  type: path
components:
  schemas: {}

````