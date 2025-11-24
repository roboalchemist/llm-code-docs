# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/assign-an-alias.md

# Assign an Alias

> Creates a new alias for the deployment with the given deployment ID. The authenticated user or team must own this deployment. If the desired alias is already assigned to another deployment, then it will be removed from the old deployment and assigned to the new one.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/deployments/{id}/aliases
paths:
  path: /v2/deployments/{id}/aliases
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
        id:
          schema:
            - type: string
              required: true
              description: The ID of the deployment the aliases should be listed for
              example: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
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
              alias:
                allOf:
                  - description: >-
                      The alias we want to assign to the deployment defined in
                      the URL
                    example: my-alias.vercel.app
                    type: string
              redirect:
                allOf:
                  - description: >-
                      The redirect property will take precedence over the
                      deployment id from the URL and consists of a hostname
                      (like test.com) to which the alias should redirect using
                      status code 307
                    example: null
                    type: string
                    nullable: true
            required: true
        examples:
          example:
            value:
              alias: my-alias.vercel.app
              redirect: null
    codeSamples:
      - label: assignAlias
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Aliases.AssignAlias(ctx, \"<id>\", nil, nil, &operations.AssignAliasRequestBody{\n        Alias: vercel.String(\"my-alias.vercel.app\"),\n        Redirect: nil,\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: assignAlias
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.assignAlias({
              id: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                alias: "my-alias.vercel.app",
                redirect: null,
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
              uid:
                allOf:
                  - type: string
                    description: The unique identifier of the alias
                    example: 2WjyKQmM8ZnGcJsPWMrHRHrE
              alias:
                allOf:
                  - type: string
                    description: The assigned alias name
                    example: my-alias.vercel.app
              created:
                allOf:
                  - type: string
                    format: date-time
                    description: The date when the alias was created
                    example: '2017-04-26T23:00:34.232Z'
              oldDeploymentId:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the previously aliased
                      deployment, only received when the alias was used before
                    example: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
            requiredProperties:
              - uid
              - alias
              - created
        examples:
          example:
            value:
              uid: 2WjyKQmM8ZnGcJsPWMrHRHrE
              alias: my-alias.vercel.app
              created: '2017-04-26T23:00:34.232Z'
              oldDeploymentId: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
        description: The alias was successfully assigned to the deployment
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              The cert for the provided alias is not ready
              The deployment is not READY and can not be aliased
              The supplied alias is invalid
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          The cert for the provided alias is not ready
          The deployment is not READY and can not be aliased
          The supplied alias is invalid
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
              If no .vercel.app alias exists then we fail (nothing to mirror)
        examples: {}
        description: |-
          You do not have permission to access this resource.
          If no .vercel.app alias exists then we fail (nothing to mirror)
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The domain used for the alias was not found
              The deployment was not found
        examples: {}
        description: |-
          The domain used for the alias was not found
          The deployment was not found
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The provided alias is already assigned to the given deployment
              The domain is not allowed to be used
        examples: {}
        description: |-
          The provided alias is already assigned to the given deployment
          The domain is not allowed to be used
  deprecated: false
  type: path
components:
  schemas: {}

````