# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/get-a-team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a Team

> Get information for the Team specified by the `teamId` parameter.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/teams/{teamId}
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v2/teams/{teamId}:
    get:
      tags:
        - teams
      summary: Get a Team
      description: Get information for the Team specified by the `teamId` parameter.
      operationId: getTeam
      parameters:
        - name: slug
          in: query
          schema:
            type: string
            example: my-team-url-slug
        - description: The Team identifier to perform the request on behalf of.
          in: path
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
          required: true
      responses:
        '200':
          description: The requested team
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Team'
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: |-
            You do not have permission to access this resource.
            Not authorized to access the team.
        '404':
          description: Team was not found.
      security:
        - bearerToken: []
components:
  schemas:
    Team:
      properties:
        connect:
          properties:
            enabled:
              type: boolean
              enum:
                - false
                - true
          type: object
        creatorId:
          type: string
          description: The ID of the user who created the Team.
          example: R6efeCJQ2HKXywuasPDc0fOWB
        updatedAt:
          type: number
          description: Timestamp (in milliseconds) of when the Team was last updated.
          example: 1611796915677
        emailDomain:
          nullable: true
          type: string
          description: >-
            Hostname that'll be matched with emails on sign-up to automatically
            join the Team.
          example: example.com
        saml:
          properties:
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
                    Timestamp (in milliseconds) of when the configuration was
                    connected.
                  example: 1611796915677
                lastReceivedWebhookEvent:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the last webhook event
                    was received from WorkOS.
                  example: 1611796915677
                lastSyncedAt:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the last directory sync
                    was performed.
                  example: 1611796915677
                syncState:
                  type: string
                  enum:
                    - SETUP
                    - ACTIVE
                  description: >-
                    Controls whether directory sync events are processed. -
                    'SETUP': Directory connected but role mappings not yet
                    configured. Events are acknowledged but not processed. -
                    'ACTIVE': Fully configured. Events are processed normally. -
                    undefined: Legacy directory (pre-feature), treat as 'ACTIVE'
                    for backwards compatibility.
              required:
                - connectedAt
                - state
                - status
                - type
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
                    Timestamp (in milliseconds) of when the configuration was
                    connected.
                  example: 1611796915677
                lastReceivedWebhookEvent:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the last webhook event
                    was received from WorkOS.
                  example: 1611796915677
                lastSyncedAt:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the last directory sync
                    was performed.
                  example: 1611796915677
                syncState:
                  type: string
                  enum:
                    - SETUP
                    - ACTIVE
                  description: >-
                    Controls whether directory sync events are processed. -
                    'SETUP': Directory connected but role mappings not yet
                    configured. Events are acknowledged but not processed. -
                    'ACTIVE': Fully configured. Events are processed normally. -
                    undefined: Legacy directory (pre-feature), treat as 'ACTIVE'
                    for backwards compatibility.
              required:
                - connectedAt
                - state
                - type
              type: object
              description: Information for the Directory Sync configuration.
            enforced:
              type: boolean
              enum:
                - false
                - true
              description: >-
                When `true`, interactions with the Team **must** be done with an
                authentication token that has been authenticated with the Team's
                SAML Single Sign-On provider.
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
                      When "Directory Sync" is configured, this object contains
                      a mapping of which Directory Group (by ID) should be
                      assigned to which Vercel Team "role".
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
                When "Directory Sync" is configured, this object contains a
                mapping of which Directory Group (by ID) should be assigned to
                which Vercel Team "role".
          required:
            - enforced
          type: object
          description: >-
            When "Single Sign-On (SAML)" is configured, this object contains
            information regarding the configuration of the Identity Provider
            (IdP).
        inviteCode:
          type: string
          description: >-
            Code that can be used to join this Team. Only visible to Team
            owners.
          example: hasihf9e89
        description:
          nullable: true
          type: string
          description: A short description of the Team.
          example: Our mission is to make cloud computing accessible to everyone.
        defaultRoles:
          properties:
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
          type: string
          description: The prefix that is prepended to automatic aliases.
        resourceConfig:
          properties:
            concurrentBuilds:
              type: number
              description: The total amount of concurrent builds that can be used.
            elasticConcurrencyEnabled:
              type: boolean
              enum:
                - false
                - true
              description: >-
                Whether every build for this team / user has elastic concurrency
                enabled automatically.
            edgeConfigSize:
              type: number
              description: >-
                The maximum size in kilobytes of an Edge Config. Only specified
                if a custom limit is set.
            edgeConfigs:
              type: number
              description: The maximum number of edge configs an account can create.
            kvDatabases:
              type: number
              description: The maximum number of kv databases an account can create.
            blobStores:
              type: number
              description: The maximum number of blob stores an account can create.
            postgresDatabases:
              type: number
              description: The maximum number of postgres databases an account can create.
            buildEntitlements:
              properties:
                enhancedBuilds:
                  type: boolean
                  enum:
                    - false
                    - true
              type: object
            buildMachine:
              properties:
                default:
                  type: string
                  enum:
                    - standard
                    - enhanced
                    - turbo
                  description: Default build machine type for new builds
              type: object
              description: Build machine configuration
          type: object
        previewDeploymentSuffix:
          nullable: true
          type: string
          description: The hostname that is current set as preview deployment suffix.
          example: example.dev
        platform:
          type: boolean
          enum:
            - false
            - true
          description: Whether the team is a platform team.
          example: true
        disableHardAutoBlocks:
          oneOf:
            - type: number
            - type: boolean
              enum:
                - false
                - true
        remoteCaching:
          properties:
            enabled:
              type: boolean
              enum:
                - false
                - true
          type: object
          description: Is remote caching enabled for this team
        defaultDeploymentProtection:
          properties:
            passwordProtection:
              nullable: true
              properties:
                deploymentType:
                  type: string
              required:
                - deploymentType
              type: object
            ssoProtection:
              nullable: true
              properties:
                deploymentType:
                  type: string
              required:
                - deploymentType
              type: object
          type: object
          description: >-
            Default deployment protection for this team null indicates
            protection is disabled
        defaultExpirationSettings:
          properties:
            expirationDays:
              type: number
              description: >-
                Number of days to keep non-production deployments (mostly
                preview deployments) before soft deletion.
            expirationDaysProduction:
              type: number
              description: >-
                Number of days to keep production deployments before soft
                deletion.
            expirationDaysCanceled:
              type: number
              description: >-
                Number of days to keep canceled deployments before soft
                deletion.
            expirationDaysErrored:
              type: number
              description: Number of days to keep errored deployments before soft deletion.
            deploymentsToKeep:
              type: number
              description: >-
                Minimum number of production deployments to keep for this
                project, even if they are over the production expiration limit.
          type: object
          description: Default deployment expiration settings for this team
        enablePreviewFeedback:
          nullable: true
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
          nullable: true
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
          nullable: true
          type: string
          enum:
            - default
            - 'on'
            - 'off'
          description: Sensitive environment variable policy for this team
        hideIpAddresses:
          nullable: true
          type: boolean
          enum:
            - false
            - true
          description: >-
            Indicates if IP addresses should be accessible in observability
            (o11y) tooling
        hideIpAddressesInLogDrains:
          nullable: true
          type: boolean
          enum:
            - false
            - true
          description: Indicates if IP addresses should be accessible in log drains
        ipBuckets:
          items:
            properties:
              bucket:
                type: string
              supportUntil:
                type: number
            required:
              - bucket
            type: object
          type: array
        strictDeploymentProtectionSettings:
          properties:
            enabled:
              type: boolean
              enum:
                - false
                - true
            updatedAt:
              type: number
          required:
            - enabled
            - updatedAt
          type: object
          description: >-
            When enabled, deployment protection settings require stricter
            permissions (owner-only).
        nsnbConfig:
          properties:
            preference:
              type: string
              enum:
                - auto-approval
                - manual-approval
                - block
          required:
            - preference
          type: object
          description: NSNB configuration for the team.
        id:
          type: string
          description: The Team's unique identifier.
          example: team_nllPyCtREAqxxdyFKbbMDlxd
        slug:
          type: string
          description: The Team's slug, which is unique across the Vercel platform.
          example: my-team
        name:
          nullable: true
          type: string
          description: >-
            Name associated with the Team account, or `null` if none has been
            provided.
          example: My Team
        avatar:
          nullable: true
          type: string
          description: The ID of the file used as avatar for this Team.
          example: 6eb07268bcfadd309905ffb1579354084c24655c
        membership:
          properties:
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
              enum:
                - true
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
                    - nsnb-auto-approve
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
            - created
            - createdAt
            - role
          type: object
          description: The membership of the authenticated User in relation to the Team.
        createdAt:
          type: number
          description: UNIX timestamp (in milliseconds) when the Team was created.
          example: 1630748523395
      required:
        - avatar
        - createdAt
        - creatorId
        - description
        - id
        - membership
        - name
        - slug
        - stagingPrefix
        - updatedAt
      type: object
      description: Data representing a Team.
      additionalProperties: true
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````