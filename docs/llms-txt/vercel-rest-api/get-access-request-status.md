# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/get-access-request-status.md

# Get access request status

> Check the status of a join request. It'll respond with a 404 if the request has been declined. If no `userId` path segment was provided, this endpoint will instead return the status of the authenticated user.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/teams/{teamId}/request/{userId}
paths:
  path: /v1/teams/{teamId}/request/{userId}
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
        userId:
          schema:
            - type: string
              required: true
              description: The unique user identifier
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getTeamAccessRequest
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.GetTeamAccessRequest(ctx, \"<id>\", \"<id>\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getTeamAccessRequest
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.getTeamAccessRequest({
              userId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
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
                    description: The slug of the team.
                    example: my-team
              teamName:
                allOf:
                  - type: string
                    description: The name of the team.
                    example: My Team
              confirmed:
                allOf:
                  - type: boolean
                    description: >-
                      Current status of the membership. Will be `true` if
                      confirmed, if pending it'll be `false`.
                    example: false
              joinedFrom:
                allOf:
                  - properties:
                      origin:
                        type: string
                        enum:
                          - link
                          - mail
                          - import
                          - teams
                          - github
                          - gitlab
                          - bitbucket
                          - saml
                          - dsync
                          - feedback
                          - organization-teams
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
                    description: >-
                      A map that describes the origin from where the user
                      joined.
              accessRequestedAt:
                allOf:
                  - type: number
                    description: >-
                      Timestamp in milliseconds when the user requested access
                      to the team.
                    example: 1588720733602
              github:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                    description: Map of the connected GitHub account.
              gitlab:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                    description: Map of the connected GitLab account.
              bitbucket:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                    description: Map of the connected Bitbucket account.
            requiredProperties:
              - teamSlug
              - teamName
              - confirmed
              - joinedFrom
              - accessRequestedAt
              - github
              - gitlab
              - bitbucket
        examples:
          example:
            value:
              teamSlug: my-team
              teamName: My Team
              confirmed: false
              joinedFrom:
                origin: link
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
              accessRequestedAt: 1588720733602
              github:
                login: <string>
              gitlab:
                login: <string>
              bitbucket:
                login: <string>
        description: Successfully
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              One of the provided values in the request query is invalid.

              User is already a confirmed member of the team and did not request
              access. Only visible when the authenticated user does have access
              to the team.
        examples: {}
        description: >-
          One of the provided values in the request query is invalid.

          User is already a confirmed member of the team and did not request
          access. Only visible when the authenticated user does have access to
          the team.
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
            description: |-
              The provided user doesn't have a membership.
              Team was not found.
        examples: {}
        description: |-
          The provided user doesn't have a membership.
          Team was not found.
  deprecated: false
  type: path
components:
  schemas: {}

````