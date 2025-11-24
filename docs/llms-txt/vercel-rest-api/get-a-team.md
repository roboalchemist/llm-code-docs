# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/get-a-team.md

# Get a Team

> Get information for the Team specified by the `teamId` parameter.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/teams/{teamId}
paths:
  path: /v2/teams/{teamId}
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
        teamId:
          schema:
            - type: string
              required: true
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query:
        slug:
          schema:
            - type: string
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.GetTeam(ctx, \"<id>\", nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Team != nil {\n        // handle response\n    }\n}"
      - label: getTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.getTeam({
              slug: "my-team-url-slug",
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
              connect:
                allOf:
                  - properties:
                      enabled:
                        type: boolean
                    type: object
              creatorId:
                allOf:
                  - type: string
                    description: The ID of the user who created the Team.
                    example: R6efeCJQ2HKXywuasPDc0fOWB
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      Timestamp (in milliseconds) of when the Team was last
                      updated.
                    example: 1611796915677
              emailDomain:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      Hostname that'll be matched with emails on sign-up to
                      automatically join the Team.
                    example: example.com
              saml:
                allOf:
                  - properties:
                      connection:
                        properties:
                          type:
                            type: string
                            description: The Identity Provider "type", for example Okta.
                            example: OktaSAML
                          status:
                            type: string
                            description: Current status of the connection.
                            example: linked
                          state:
                            type: string
                            description: Current state of the connection.
                            example: active
                          connectedAt:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the
                              configuration was connected.
                            example: 1611796915677
                          lastReceivedWebhookEvent:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the last
                              webhook event was received from WorkOS.
                            example: 1611796915677
                        required:
                          - type
                          - status
                          - state
                          - connectedAt
                        type: object
                        description: Information for the SAML Single Sign-On configuration.
                      directory:
                        properties:
                          type:
                            type: string
                            description: The Identity Provider "type", for example Okta.
                            example: OktaSAML
                          state:
                            type: string
                            description: Current state of the connection.
                            example: active
                          connectedAt:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the
                              configuration was connected.
                            example: 1611796915677
                          lastReceivedWebhookEvent:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the last
                              webhook event was received from WorkOS.
                            example: 1611796915677
                        required:
                          - type
                          - state
                          - connectedAt
                        type: object
                        description: Information for the Directory Sync configuration.
                      enforced:
                        type: boolean
                        description: >-
                          When `true`, interactions with the Team **must** be
                          done with an authentication token that has been
                          authenticated with the Team's SAML Single Sign-On
                          provider.
                      defaultRedirectUri:
                        type: string
                        enum:
                          - vercel.com
                          - v0.dev
                          - v0.app
                        description: >-
                          The default redirect URI to use after successful SAML
                          authentication.
                      roles:
                        additionalProperties:
                          oneOf:
                            - properties:
                                accessGroupId:
                                  type: string
                              required:
                                - accessGroupId
                              type: object
                              description: >-
                                When "Directory Sync" is configured, this object
                                contains a mapping of which Directory Group (by
                                ID) should be assigned to which Vercel Team
                                "role".
                            - type: string
                              enum:
                                - OWNER
                                - MEMBER
                                - DEVELOPER
                                - SECURITY
                                - BILLING
                                - VIEWER
                                - VIEWER_FOR_PLUS
                                - CONTRIBUTOR
                        type: object
                        description: >-
                          When "Directory Sync" is configured, this object
                          contains a mapping of which Directory Group (by ID)
                          should be assigned to which Vercel Team "role".
                    required:
                      - enforced
                    type: object
                    description: >-
                      When "Single Sign-On (SAML)" is configured, this object
                      contains information regarding the configuration of the
                      Identity Provider (IdP).
              inviteCode:
                allOf:
                  - type: string
                    description: >-
                      Code that can be used to join this Team. Only visible to
                      Team owners.
                    example: hasihf9e89
              description:
                allOf:
                  - nullable: true
                    type: string
                    description: A short description of the Team.
                    example: >-
                      Our mission is to make cloud computing accessible to
                      everyone.
              defaultRoles:
                allOf:
                  - properties:
                      teamRoles:
                        items:
                          type: string
                          enum:
                            - OWNER
                            - MEMBER
                            - DEVELOPER
                            - SECURITY
                            - BILLING
                            - VIEWER
                            - VIEWER_FOR_PLUS
                            - CONTRIBUTOR
                        type: array
                      teamPermissions:
                        items:
                          type: string
                          enum:
                            - IntegrationManager
                            - CreateProject
                            - FullProductionDeployment
                            - UsageViewer
                            - EnvVariableManager
                            - EnvironmentManager
                            - V0Builder
                            - V0Chatter
                            - V0Viewer
                        type: array
                    type: object
                    description: Default roles for the team.
              stagingPrefix:
                allOf:
                  - type: string
                    description: The prefix that is prepended to automatic aliases.
              resourceConfig:
                allOf:
                  - properties:
                      concurrentBuilds:
                        type: number
                        description: >-
                          The total amount of concurrent builds that can be
                          used.
                      elasticConcurrencyEnabled:
                        type: boolean
                        description: >-
                          Whether every build for this team / user has elastic
                          concurrency enabled automatically.
                      edgeConfigSize:
                        type: number
                        description: >-
                          The maximum size in kilobytes of an Edge Config. Only
                          specified if a custom limit is set.
                      edgeConfigs:
                        type: number
                        description: >-
                          The maximum number of edge configs an account can
                          create.
                      kvDatabases:
                        type: number
                        description: >-
                          The maximum number of kv databases an account can
                          create.
                      blobStores:
                        type: number
                        description: >-
                          The maximum number of blob stores an account can
                          create.
                      postgresDatabases:
                        type: number
                        description: >-
                          The maximum number of postgres databases an account
                          can create.
                      buildEntitlements:
                        properties:
                          enhancedBuilds:
                            type: boolean
                        type: object
                    type: object
              previewDeploymentSuffix:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The hostname that is current set as preview deployment
                      suffix.
                    example: example.dev
              platform:
                allOf:
                  - type: boolean
                    description: Whether the team is a platform team.
                    example: true
              disableHardAutoBlocks:
                allOf:
                  - oneOf:
                      - type: number
                      - type: boolean
              remoteCaching:
                allOf:
                  - properties:
                      enabled:
                        type: boolean
                    type: object
                    description: Is remote caching enabled for this team
              defaultDeploymentProtection:
                allOf:
                  - properties:
                      passwordProtection:
                        properties:
                          deploymentType:
                            type: string
                        required:
                          - deploymentType
                        type: object
                      ssoProtection:
                        properties:
                          deploymentType:
                            type: string
                        required:
                          - deploymentType
                        type: object
                    type: object
                    description: Default deployment protection for this team
              defaultExpirationSettings:
                allOf:
                  - properties:
                      expirationDays:
                        type: number
                        description: >-
                          Number of days to keep non-production deployments
                          (mostly preview deployments) before soft deletion.
                      expirationDaysProduction:
                        type: number
                        description: >-
                          Number of days to keep production deployments before
                          soft deletion.
                      expirationDaysCanceled:
                        type: number
                        description: >-
                          Number of days to keep canceled deployments before
                          soft deletion.
                      expirationDaysErrored:
                        type: number
                        description: >-
                          Number of days to keep errored deployments before soft
                          deletion.
                      deploymentsToKeep:
                        type: number
                        description: >-
                          Minimum number of production deployments to keep for
                          this project, even if they are over the production
                          expiration limit.
                    type: object
                    description: Default deployment expiration settings for this team
              enablePreviewFeedback:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - default
                      - 'on'
                      - 'off'
                      - on-force
                      - off-force
                      - default-force
                    description: Whether toolbar is enabled on preview deployments
              enableProductionFeedback:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - default
                      - 'on'
                      - 'off'
                      - on-force
                      - off-force
                      - default-force
                    description: Whether toolbar is enabled on production deployments
              sensitiveEnvironmentVariablePolicy:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - default
                      - 'on'
                      - 'off'
                    description: Sensitive environment variable policy for this team
              hideIpAddresses:
                allOf:
                  - nullable: true
                    type: boolean
                    description: >-
                      Indicates if IP addresses should be accessible in
                      observability (o11y) tooling
              hideIpAddressesInLogDrains:
                allOf:
                  - nullable: true
                    type: boolean
                    description: >-
                      Indicates if IP addresses should be accessible in log
                      drains
              ipBuckets:
                allOf:
                  - items:
                      properties:
                        bucket:
                          type: string
                        supportUntil:
                          type: number
                      required:
                        - bucket
                      type: object
                    type: array
              id:
                allOf:
                  - type: string
                    description: The Team's unique identifier.
                    example: team_nllPyCtREAqxxdyFKbbMDlxd
              slug:
                allOf:
                  - type: string
                    description: >-
                      The Team's slug, which is unique across the Vercel
                      platform.
                    example: my-team
              name:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      Name associated with the Team account, or `null` if none
                      has been provided.
                    example: My Team
              avatar:
                allOf:
                  - nullable: true
                    type: string
                    description: The ID of the file used as avatar for this Team.
                    example: 6eb07268bcfadd309905ffb1579354084c24655c
              membership:
                allOf:
                  - properties:
                      uid:
                        type: string
                      entitlements:
                        items:
                          properties:
                            entitlement:
                              type: string
                          required:
                            - entitlement
                          type: object
                        type: array
                      teamId:
                        type: string
                      confirmed:
                        type: boolean
                      accessRequestedAt:
                        type: number
                      role:
                        type: string
                        enum:
                          - OWNER
                          - MEMBER
                          - DEVELOPER
                          - SECURITY
                          - BILLING
                          - VIEWER
                          - VIEWER_FOR_PLUS
                          - CONTRIBUTOR
                      teamRoles:
                        items:
                          type: string
                          enum:
                            - OWNER
                            - MEMBER
                            - DEVELOPER
                            - SECURITY
                            - BILLING
                            - VIEWER
                            - VIEWER_FOR_PLUS
                            - CONTRIBUTOR
                        type: array
                      teamPermissions:
                        items:
                          type: string
                          enum:
                            - IntegrationManager
                            - CreateProject
                            - FullProductionDeployment
                            - UsageViewer
                            - EnvVariableManager
                            - EnvironmentManager
                            - V0Builder
                            - V0Chatter
                            - V0Viewer
                        type: array
                      createdAt:
                        type: number
                      created:
                        type: number
                      joinedFrom:
                        properties:
                          origin:
                            type: string
                            enum:
                              - link
                              - saml
                              - mail
                              - import
                              - teams
                              - github
                              - gitlab
                              - bitbucket
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
                    required:
                      - confirmed
                      - role
                      - createdAt
                      - created
                    type: object
                    description: >-
                      The membership of the authenticated User in relation to
                      the Team.
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      UNIX timestamp (in milliseconds) when the Team was
                      created.
                    example: 1630748523395
            description: Data representing a Team.
            refIdentifier: '#/components/schemas/Team'
            requiredProperties:
              - creatorId
              - updatedAt
              - description
              - stagingPrefix
              - id
              - slug
              - name
              - avatar
              - membership
              - createdAt
        examples:
          example:
            value:
              connect:
                enabled: true
              creatorId: R6efeCJQ2HKXywuasPDc0fOWB
              updatedAt: 1611796915677
              emailDomain: example.com
              saml:
                connection:
                  type: OktaSAML
                  status: linked
                  state: active
                  connectedAt: 1611796915677
                  lastReceivedWebhookEvent: 1611796915677
                directory:
                  type: OktaSAML
                  state: active
                  connectedAt: 1611796915677
                  lastReceivedWebhookEvent: 1611796915677
                enforced: true
                defaultRedirectUri: vercel.com
                roles: {}
              inviteCode: hasihf9e89
              description: Our mission is to make cloud computing accessible to everyone.
              defaultRoles:
                teamRoles:
                  - OWNER
                teamPermissions:
                  - IntegrationManager
              stagingPrefix: <string>
              resourceConfig:
                concurrentBuilds: 123
                elasticConcurrencyEnabled: true
                edgeConfigSize: 123
                edgeConfigs: 123
                kvDatabases: 123
                blobStores: 123
                postgresDatabases: 123
                buildEntitlements:
                  enhancedBuilds: true
              previewDeploymentSuffix: example.dev
              platform: true
              disableHardAutoBlocks: 123
              remoteCaching:
                enabled: true
              defaultDeploymentProtection:
                passwordProtection:
                  deploymentType: <string>
                ssoProtection:
                  deploymentType: <string>
              defaultExpirationSettings:
                expirationDays: 123
                expirationDaysProduction: 123
                expirationDaysCanceled: 123
                expirationDaysErrored: 123
                deploymentsToKeep: 123
              enablePreviewFeedback: default
              enableProductionFeedback: default
              sensitiveEnvironmentVariablePolicy: default
              hideIpAddresses: true
              hideIpAddressesInLogDrains: true
              ipBuckets:
                - bucket: <string>
                  supportUntil: 123
              id: team_nllPyCtREAqxxdyFKbbMDlxd
              slug: my-team
              name: My Team
              avatar: 6eb07268bcfadd309905ffb1579354084c24655c
              membership:
                uid: <string>
                entitlements:
                  - entitlement: <string>
                teamId: <string>
                confirmed: true
                accessRequestedAt: 123
                role: OWNER
                teamRoles:
                  - OWNER
                teamPermissions:
                  - IntegrationManager
                createdAt: 123
                created: 123
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
              createdAt: 1630748523395
        description: The requested team
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
            description: |-
              You do not have permission to access this resource.
              Not authorized to access the team.
        examples: {}
        description: |-
          You do not have permission to access this resource.
          Not authorized to access the team.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Team was not found.
        examples: {}
        description: Team was not found.
  deprecated: false
  type: path
components:
  schemas: {}

````