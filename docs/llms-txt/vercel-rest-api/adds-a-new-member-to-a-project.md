# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projectmembers/adds-a-new-member-to-a-project.md

# Adds a new member to a project.

> Adds a new member to the project.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/members
paths:
  path: /v1/projects/{idOrName}/members
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
              description: The ID or name of the Project.
              example: prj_pavWOn1iLObbXLRiwVvzmPrTWyTf
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
              uid:
                allOf:
                  - &ref_0
                    type: string
                    maxLength: 256
                    example: ndlgr43fadlPyCtREAqxxdyFK
                    description: >-
                      The ID of the team member that should be added to this
                      project.
              username:
                allOf:
                  - &ref_1
                    type: string
                    maxLength: 256
                    example: example
                    description: >-
                      The username of the team member that should be added to
                      this project.
              email:
                allOf:
                  - &ref_2
                    type: string
                    format: email
                    example: entity@example.com
                    description: >-
                      The email of the team member that should be added to this
                      project.
              role:
                allOf:
                  - &ref_3
                    type: string
                    enum:
                      - ADMIN
                      - PROJECT_DEVELOPER
                      - PROJECT_VIEWER
                    example: ADMIN
                    description: The project role of the member that will be added.
            required: true
            requiredProperties:
              - role
              - uid
            additionalProperties: false
          - type: object
            properties:
              uid:
                allOf:
                  - *ref_0
              username:
                allOf:
                  - *ref_1
              email:
                allOf:
                  - *ref_2
              role:
                allOf:
                  - *ref_3
            required: true
            requiredProperties:
              - role
              - username
            additionalProperties: false
          - type: object
            properties:
              uid:
                allOf:
                  - *ref_0
              username:
                allOf:
                  - *ref_1
              email:
                allOf:
                  - *ref_2
              role:
                allOf:
                  - *ref_3
            required: true
            requiredProperties:
              - role
              - email
            additionalProperties: false
        examples:
          example:
            value:
              uid: ndlgr43fadlPyCtREAqxxdyFK
              username: example
              email: entity@example.com
              role: ADMIN
    codeSamples:
      - label: addProjectMember
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.ProjectMembers.AddProjectMember(ctx, \"prj_pavWOn1iLObbXLRiwVvzmPrTWyTf\", nil, nil, vercel.Pointer(operations.CreateAddProjectMemberRequestBodyAddProjectMemberRequestBody1(\n        operations.AddProjectMemberRequestBody1{\n            UID: \"ndlgr43fadlPyCtREAqxxdyFK\",\n            Username: vercel.String(\"example\"),\n            Email: vercel.String(\"entity@example.com\"),\n            Role: operations.RequestBodyRoleAdmin,\n        },\n    )))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: addProjectMember
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projectMembers.addProjectMember({
              idOrName: "prj_pavWOn1iLObbXLRiwVvzmPrTWyTf",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                uid: "ndlgr43fadlPyCtREAqxxdyFK",
                username: "example",
                email: "entity@example.com",
                role: "ADMIN",
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
              id:
                allOf:
                  - type: string
            description: Responds with the project ID on success.
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: <string>
        description: Responds with the project ID on success.
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````