# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/list-deployment-files.md

# List Deployment Files

> Allows to retrieve the file structure of the source code of a deployment by supplying the deployment unique identifier. If the deployment was created with the Vercel CLI or the API directly with the `files` key, it will have a file tree that can be retrievable.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/deployments/{id}/files
paths:
  path: /v6/deployments/{id}/files
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
        id:
          schema:
            - type: string
              required: true
              description: The unique deployment identifier
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
    body: {}
    codeSamples:
      - label: listDeploymentFiles
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.ListDeploymentFiles(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.FileTrees != nil {\n        // handle response\n    }\n}"
      - label: listDeploymentFiles
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.listDeploymentFiles({
              id: "<id>",
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
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/FileTree'
        examples:
          example:
            value:
              - name: my-file.json
                type: file
                uid: 2d4aad419917f15b1146e9e03ddc9bb31747e4d0
                children:
                  - {}
                contentType: application/json
                mode: 123
        description: Retrieved the file tree successfully
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
            description: |-
              File tree not found
              Deployment not found
        examples: {}
        description: |-
          File tree not found
          Deployment not found
  deprecated: false
  type: path
components:
  schemas:
    FileTree:
      properties:
        name:
          type: string
          description: The name of the file tree entry
          example: my-file.json
        type:
          type: string
          enum:
            - directory
            - file
            - symlink
            - lambda
            - middleware
            - invalid
          description: String indicating the type of file tree entry.
          example: file
        uid:
          type: string
          description: The unique identifier of the file (only valid for the `file` type)
          example: 2d4aad419917f15b1146e9e03ddc9bb31747e4d0
        children:
          items:
            $ref: '#/components/schemas/FileTree'
          type: array
          description: >-
            The list of children files of the directory (only valid for the
            `directory` type)
        contentType:
          type: string
          description: The content-type of the file (only valid for the `file` type)
          example: application/json
        mode:
          type: number
          description: The file "mode" indicating file type and permissions.
      required:
        - name
        - type
        - mode
      type: object
      description: A deployment file tree entry

````