# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/update-a-team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Team

> Update the information of a Team specified by the `teamId` parameter. The request body should contain the information that will be updated on the Team.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v2/teams/{teamId}
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
    patch:
      tags:
        - teams
      summary: Update a Team
      description: >-
        Update the information of a Team specified by the `teamId` parameter.
        The request body should contain the information that will be updated on
        the Team.
      operationId: patchTeam
      parameters:
        - description: The Team identifier to perform the request on behalf of.
          in: path
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
          required: true
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              properties:
                avatar:
                  type: string
                  format: regex
                  description: The hash value of an uploaded image.
                description:
                  type: string
                  maxLength: 140
                  example: >-
                    Our mission is to make cloud computing accessible to
                    everyone
                  description: A short text that describes the team.
                emailDomain:
                  type: string
                  format: regex
                  example: example.com
                  nullable: true
                name:
                  type: string
                  maxLength: 256
                  example: My Team
                  description: The name of the team.
                previewDeploymentSuffix:
                  type: string
                  format: hostname
                  example: example.dev
                  description: Suffix that will be used for all preview deployments.
                  nullable: true
                regenerateInviteCode:
                  type: boolean
                  example: true
                  description: Create a new invite code and replace the current one.
                saml:
                  type: object
                  additionalProperties: false
                  properties:
                    enforced:
                      type: boolean
                      example: true
                      description: >-
                        Require that members of the team use SAML Single
                        Sign-On.
                    roles:
                      type: object
                      description: Directory groups to role or access group mappings.
                      additionalProperties:
                        anyOf:
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
                          - type: object
                            additionalProperties: false
                            required:
                              - accessGroupId
                            properties:
                              accessGroupId:
                                type: string
                                pattern: ^ag_[A-z0-9_ -]+$
                slug:
                  type: string
                  example: my-team
                  description: A new slug for the team.
                enablePreviewFeedback:
                  type: string
                  example: 'on'
                  description: 'Enable preview toolbar: one of on, off or default.'
                enableProductionFeedback:
                  type: string
                  example: 'on'
                  description: 'Enable production toolbar: one of on, off or default.'
                sensitiveEnvironmentVariablePolicy:
                  type: string
                  example: 'on'
                  description: >-
                    Sensitive environment variable policy: one of on, off or
                    default.
                remoteCaching:
                  type: object
                  description: Whether or not remote caching is enabled for the team
                  additionalProperties: false
                  properties:
                    enabled:
                      type: boolean
                      example: true
                      description: Enable or disable remote caching for the team.
                hideIpAddresses:
                  type: boolean
                  example: false
                  description: Display or hide IP addresses in Monitoring queries.
                hideIpAddressesInLogDrains:
                  type: boolean
                  example: false
                  description: Display or hide IP addresses in Log Drains.
                defaultDeploymentProtection:
                  type: object
                  description: Default deployment protection settings for new projects.
                  additionalProperties: false
                  properties:
                    passwordProtection:
                      additionalProperties: false
                      description: Allows to protect project deployments with a password
                      properties:
                        deploymentType:
                          description: >-
                            Specify if the password will apply to every
                            Deployment Target or just Preview
                          enum:
                            - all
                            - preview
                            - prod_deployment_urls_and_all_previews
                            - all_except_custom_domains
                          type: string
                        password:
                          description: >-
                            The password that will be used to protect Project
                            Deployments
                          maxLength: 72
                          type: string
                          nullable: true
                      required:
                        - deploymentType
                      type: object
                      nullable: true
                    ssoProtection:
                      additionalProperties: false
                      description: >-
                        Ensures visitors to your Preview Deployments are logged
                        into Vercel and have a minimum of Viewer access on your
                        team
                      properties:
                        deploymentType:
                          default: preview
                          description: >-
                            Specify if the Vercel Authentication (SSO
                            Protection) will apply to every Deployment Target or
                            just Preview
                          enum:
                            - all
                            - preview
                            - prod_deployment_urls_and_all_previews
                            - all_except_custom_domains
                          type: string
                      required:
                        - deploymentType
                      type: object
                      nullable: true
                defaultExpirationSettings:
                  properties:
                    expiration:
                      description: The time period to keep non-production deployments for
                      example: 1y
                      type: string
                      enum:
                        - 3y
                        - 2y
                        - 1y
                        - 6m
                        - 3m
                        - 2m
                        - 1m
                        - 2w
                        - 1w
                        - 1d
                        - unlimited
                    expirationProduction:
                      description: The time period to keep production deployments for
                      example: 1y
                      type: string
                      enum:
                        - 3y
                        - 2y
                        - 1y
                        - 6m
                        - 3m
                        - 2m
                        - 1m
                        - 2w
                        - 1w
                        - 1d
                        - unlimited
                    expirationCanceled:
                      description: The time period to keep canceled deployments for
                      example: 1y
                      type: string
                      enum:
                        - 1y
                        - 6m
                        - 3m
                        - 2m
                        - 1m
                        - 2w
                        - 1w
                        - 1d
                        - unlimited
                    expirationErrored:
                      description: The time period to keep errored deployments for
                      example: 1y
                      type: string
                      enum:
                        - 1y
                        - 6m
                        - 3m
                        - 2m
                        - 1m
                        - 2w
                        - 1w
                        - 1d
                        - unlimited
                  type: object
                  additionalProperties: false
                strictDeploymentProtectionSettings:
                  type: object
                  description: >-
                    When enabled, deployment protection settings require
                    stricter permissions (owner-only).
                  additionalProperties: false
                  properties:
                    enabled:
                      type: boolean
                      example: true
                      description: Enable or disable strict deployment protection settings.
                  required:
                    - enabled
                nsnbConfig:
                  anyOf:
                    - type: object
                      description: NSNB configuration for the team.
                      additionalProperties: false
                      properties:
                        preference:
                          type: string
                          enum:
                            - auto-approval
                            - manual-approval
                            - block
                          description: The NSNB preference for the team.
                      required:
                        - preference
                    - type: string
                resourceConfig:
                  type: object
                  description: Resource configuration for the team.
                  additionalProperties: false
                  properties:
                    buildMachine:
                      type: object
                      description: Build machine configuration.
                      additionalProperties: false
                      properties:
                        default:
                          type: string
                          enum:
                            - standard
                            - enhanced
                            - turbo
                          example: standard
                          description: >-
                            Default build machine type for new builds: standard,
                            enhanced, or turbo.
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Team'
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: ''
        '403':
          description: |-
            You do not have permission to access this resource.
            Not authorized to update the team. Must be an OWNER.
        '428':
          description: |-
            Owner does not have protection add-on
            Advanced Deployment Protection is not available for the user plan
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