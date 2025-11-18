# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/request-access-to-a-team.md

# Request access to a team

> Request access to a team as a member. An owner has to approve the request. Only 10 users can request access to a team at the same time.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/request
paths:
  path: /v1/teams/{teamId}/request
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
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              joinedFrom:
                allOf:
                  - type: object
                    additionalProperties: false
                    required:
                      - origin
                    properties:
                      origin:
                        type: string
                        enum:
                          - import
                          - teams
                          - github
                          - gitlab
                          - bitbucket
                          - feedback
                          - organization-teams
                        description: The origin of the request.
                        example: github
                      commitId:
                        type: string
                        description: The commit sha if the origin is a git provider.
                        example: f498d25d8bd654b578716203be73084b31130cd7
                      repoId:
                        type: string
                        description: The ID of the repository for the given Git provider.
                        example: '67753070'
                      repoPath:
                        type: string
                        description: The path to the repository for the given Git provider.
                        example: jane-doe/example
                      gitUserId:
                        description: >-
                          The ID of the Git account of the user who requests
                          access.
                        example: 103053343
                        oneOf:
                          - type: string
                          - type: number
                      gitUserLogin:
                        type: string
                        description: >-
                          The login name for the Git account of the user who
                          requests access.
                        example: jane-doe
            required: true
            requiredProperties:
              - joinedFrom
            additionalProperties: false
        examples:
          example:
            value:
              joinedFrom:
                origin: github
                commitId: f498d25d8bd654b578716203be73084b31130cd7
                repoId: '67753070'
                repoPath: jane-doe/example
                gitUserId: 103053343
                gitUserLogin: jane-doe
    codeSamples:
      - label: requestAccessToTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.RequestAccessToTeam(ctx, \"<id>\", &operations.RequestAccessToTeamRequestBody{\n        JoinedFrom: operations.JoinedFrom{\n            Origin: operations.OriginGithub,\n            CommitID: vercel.String(\"f498d25d8bd654b578716203be73084b31130cd7\"),\n            RepoID: vercel.String(\"67753070\"),\n            RepoPath: vercel.String(\"jane-doe/example\"),\n            GitUserID: vercel.Pointer(operations.CreateGitUserIDNumber(\n                103053343,\n            )),\n            GitUserLogin: vercel.String(\"jane-doe\"),\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: requestAccessToTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.requestAccessToTeam({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                joinedFrom: {
                  origin: "github",
                  commitId: "f498d25d8bd654b578716203be73084b31130cd7",
                  repoId: "67753070",
                  repoPath: "jane-doe/example",
                  gitUserId: 103053343,
                  gitUserLogin: "jane-doe",
                },
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
              teamSlug:
                allOf:
                  - type: string
              teamName:
                allOf:
                  - type: string
              confirmed:
                allOf:
                  - type: boolean
              joinedFrom:
                allOf:
                  - properties:
                      origin:
                        type: string
                        enum:
                          - import
                          - teams
                          - github
                          - gitlab
                          - bitbucket
                          - feedback
                          - organization-teams
                          - link
                          - mail
                          - saml
                          - dsync
                      commitId:
                        type: string
                      repoId:
                        type: string
                      repoPath:
                        type: string
                      gitUserId:
                        oneOf:
                          - type: string
                          - type: number
                      gitUserLogin:
                        type: string
                      ssoUserId:
                        type: string
                      ssoConnectedAt:
                        type: number
                      idpUserId:
                        type: string
                      dsyncUserId:
                        type: string
                      dsyncConnectedAt:
                        type: number
                    required:
                      - origin
                    type: object
              accessRequestedAt:
                allOf:
                  - type: number
              github:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
              gitlab:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
              bitbucket:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
            requiredProperties:
              - teamSlug
              - teamName
              - github
              - gitlab
              - bitbucket
        examples:
          example:
            value:
              teamSlug: <string>
              teamName: <string>
              confirmed: true
              joinedFrom:
                origin: import
                commitId: <string>
                repoId: <string>
                repoPath: <string>
                gitUserId: <string>
                gitUserLogin: <string>
                ssoUserId: <string>
                ssoConnectedAt: 123
                idpUserId: <string>
                dsyncUserId: <string>
                dsyncConnectedAt: 123
              accessRequestedAt: 123
              github:
                login: <string>
              gitlab:
                login: <string>
              bitbucket:
                login: <string>
        description: Successfuly requested access to the team.
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
    '401': {}
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
            description: The team was not found.
        examples: {}
        description: The team was not found.
    '503': {}
  deprecated: false
  type: path
components:
  schemas: {}

````