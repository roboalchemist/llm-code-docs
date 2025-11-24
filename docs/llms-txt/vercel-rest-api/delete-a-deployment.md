# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/delete-a-deployment.md

# Delete a Deployment

> This API allows you to delete a deployment, either by supplying its `id` in the URL or the `url` of the deployment as a query parameter. You can obtain the ID, for example, by listing all deployments.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v13/deployments/{id}
paths:
  path: /v13/deployments/{id}
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The ID of the deployment to be deleted
              example: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
      query:
        url:
          schema:
            - type: string
              required: false
              description: >-
                A Deployment or Alias URL. In case it is passed, the ID will be
                ignored
              example: https://files-orcin-xi.vercel.app/
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
      - label: deleteDeployment
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.DeleteDeployment(ctx, \"dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd\", vercel.String(\"https://files-orcin-xi.vercel.app/\"), nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: deleteDeployment
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.deleteDeployment({
              id: "dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd",
              url: "https://files-orcin-xi.vercel.app/",
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
              uid:
                allOf:
                  - type: string
                    description: The removed deployment ID.
                    example: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
              state:
                allOf:
                  - type: string
                    enum:
                      - DELETED
                    description: A constant with the final state of the deployment.
            requiredProperties:
              - uid
              - state
        examples:
          example:
            value:
              uid: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
              state: DELETED
        description: The deployment was successfully deleted
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The deployment was not found
        examples: {}
        description: The deployment was not found
  deprecated: false
  type: path
components:
  schemas: {}

````