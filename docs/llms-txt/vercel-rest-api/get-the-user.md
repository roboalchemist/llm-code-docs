# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/user/get-the-user.md

# Get the User

> Retrieves information related to the currently authenticated User.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/user
paths:
  path: /v2/user
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getAuthUser
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.User.GetAuthUser(ctx)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getAuthUser
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.user.getAuthUser();

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              user:
                allOf:
                  - oneOf:
                      - $ref: '#/components/schemas/AuthUser'
                      - $ref: '#/components/schemas/AuthUserLimited'
            description: Successful response.
            requiredProperties:
              - user
        examples:
          example:
            value:
              user:
                createdAt: 1630748523395
                softBlock:
                  blockedAt: 123
                  reason: SUBSCRIPTION_CANCELED
                  blockedDueToOverageType: analyticsUsage
                billing: {}
                resourceConfig:
                  nodeType: <string>
                  concurrentBuilds: 123
                  elasticConcurrencyEnabled: true
                  buildEntitlements:
                    enhancedBuilds: true
                  buildQueue:
                    configuration: SKIP_NAMESPACE_QUEUE
                  awsAccountType: <string>
                  awsAccountIds:
                    - <string>
                  cfZoneName: <string>
                  imageOptimizationType: <string>
                  edgeConfigs: 123
                  edgeConfigSize: 123
                  edgeFunctionMaxSizeBytes: 123
                  edgeFunctionExecutionTimeoutMs: 123
                  serverlessFunctionMaxMemorySize: 123
                  kvDatabases: 123
                  postgresDatabases: 123
                  blobStores: 123
                  integrationStores: 123
                  cronJobs: 123
                  cronJobsPerProject: 123
                  microfrontendGroupsPerTeam: 123
                  microfrontendProjectsPerGroup: 123
                  flagsExplorerOverridesThreshold: 123
                  flagsExplorerUnlimitedOverrides: true
                  customEnvironmentsPerProject: 123
                  buildMachine:
                    purchaseType: enhanced
                    isDefaultBuildMachine: true
                    cores: 123
                    memory: 123
                  security:
                    customRules: 123
                    ipBlocks: 123
                    ipBypass: 123
                    rateLimit: 123
                stagingPrefix: <string>
                activeDashboardViews:
                  - scopeId: <string>
                    viewPreference: list
                    favoritesViewPreference: open
                    recentsViewPreference: open
                importFlowGitNamespace: <string>
                importFlowGitNamespaceId: <string>
                importFlowGitProvider: gitlab
                preferredScopesAndGitNamespaces:
                  - scopeId: <string>
                    gitNamespaceId: <string>
                dismissedToasts:
                  - name: <string>
                    dismissals:
                      - scopeId: <string>
                        createdAt: 123
                favoriteProjectsAndSpaces:
                  - teamId: <string>
                    projectId: <string>
                hasTrialAvailable: true
                remoteCaching:
                  enabled: true
                dataCache:
                  excessBillingEnabled: true
                featureBlocks:
                  webAnalytics:
                    blockedFrom: 123
                    blockedUntil: 123
                    isCurrentlyBlocked: true
                id: AEIIDYVk59zbFF2Sxfyxxmua
                email: me@example.com
                name: John Doe
                username: jdoe
                avatar: 22cb30c85ff45ac4c72de8981500006b28114aa1
                defaultTeamId: <string>
        description: Successful response.
    '400': {}
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas:
    AuthUser:
      properties:
        createdAt:
          type: number
          description: UNIX timestamp (in milliseconds) when the User account was created.
          example: 1630748523395
        softBlock:
          nullable: true
          properties:
            blockedAt:
              type: number
            reason:
              type: string
              enum:
                - SUBSCRIPTION_CANCELED
                - SUBSCRIPTION_EXPIRED
                - UNPAID_INVOICE
                - ENTERPRISE_TRIAL_ENDED
                - FAIR_USE_LIMITS_EXCEEDED
                - BLOCKED_FOR_PLATFORM_ABUSE
            blockedDueToOverageType:
              type: string
              enum:
                - analyticsUsage
                - artifacts
                - bandwidth
                - blobTotalAdvancedRequests
                - blobTotalAvgSizeInBytes
                - blobTotalGetResponseObjectSizeInBytes
                - blobTotalSimpleRequests
                - connectDataTransfer
                - dataCacheRead
                - dataCacheWrite
                - edgeConfigRead
                - edgeConfigWrite
                - edgeFunctionExecutionUnits
                - edgeMiddlewareInvocations
                - edgeRequestAdditionalCpuDuration
                - edgeRequest
                - elasticConcurrencyBuildSlots
                - fastDataTransfer
                - fastOriginTransfer
                - fluidCpuDuration
                - fluidDuration
                - functionDuration
                - functionInvocation
                - imageOptimizationCacheRead
                - imageOptimizationCacheWrite
                - imageOptimizationTransformation
                - logDrainsVolume
                - monitoringMetric
                - blobDataTransfer
                - observabilityEvent
                - onDemandConcurrencyMinutes
                - runtimeCacheRead
                - runtimeCacheWrite
                - serverlessFunctionExecution
                - sourceImages
                - wafOwaspExcessBytes
                - wafOwaspRequests
                - wafRateLimitRequest
                - webAnalyticsEvent
          required:
            - blockedAt
            - reason
          type: object
          description: >-
            When the User account has been "soft blocked", this property will
            contain the date when the restriction was enacted, and the
            identifier for why.
        billing:
          nullable: true
          type: object
          description: >-
            An object containing billing infomation associated with the User
            account.
        resourceConfig:
          properties:
            nodeType:
              type: string
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            concurrentBuilds:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            elasticConcurrencyEnabled:
              type: boolean
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            buildEntitlements:
              properties:
                enhancedBuilds:
                  type: boolean
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
              type: object
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            buildQueue:
              properties:
                configuration:
                  type: string
                  enum:
                    - SKIP_NAMESPACE_QUEUE
                    - WAIT_FOR_NAMESPACE_QUEUE
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
              type: object
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            awsAccountType:
              type: string
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            awsAccountIds:
              items:
                type: string
              type: array
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            cfZoneName:
              type: string
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            imageOptimizationType:
              type: string
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            edgeConfigs:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            edgeConfigSize:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            edgeFunctionMaxSizeBytes:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            edgeFunctionExecutionTimeoutMs:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            serverlessFunctionMaxMemorySize:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            kvDatabases:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            postgresDatabases:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            blobStores:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            integrationStores:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            cronJobs:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            cronJobsPerProject:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            microfrontendGroupsPerTeam:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            microfrontendProjectsPerGroup:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            flagsExplorerOverridesThreshold:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            flagsExplorerUnlimitedOverrides:
              type: boolean
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            customEnvironmentsPerProject:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            buildMachine:
              properties:
                purchaseType:
                  type: string
                  enum:
                    - enhanced
                    - turbo
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                isDefaultBuildMachine:
                  type: boolean
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                cores:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                memory:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
              type: object
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            security:
              properties:
                customRules:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                ipBlocks:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                ipBypass:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                rateLimit:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
              type: object
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
          type: object
          description: >-
            An object containing infomation related to the amount of platform
            resources may be allocated to the User account.
        stagingPrefix:
          type: string
          description: >-
            Prefix that will be used in the URL of "Preview" deployments created
            by the User account.
        activeDashboardViews:
          items:
            properties:
              scopeId:
                type: string
              viewPreference:
                nullable: true
                type: string
                enum:
                  - list
                  - cards
              favoritesViewPreference:
                nullable: true
                type: string
                enum:
                  - open
                  - closed
              recentsViewPreference:
                nullable: true
                type: string
                enum:
                  - open
                  - closed
            required:
              - scopeId
            type: object
            description: set of dashboard view preferences (cards or list) per scopeId
          type: array
          description: set of dashboard view preferences (cards or list) per scopeId
        importFlowGitNamespace:
          nullable: true
          oneOf:
            - type: string
            - type: number
        importFlowGitNamespaceId:
          nullable: true
          oneOf:
            - type: string
            - type: number
        importFlowGitProvider:
          nullable: true
          type: string
          enum:
            - gitlab
            - bitbucket
            - github
            - github-limited
            - github-custom-host
        preferredScopesAndGitNamespaces:
          items:
            properties:
              scopeId:
                type: string
              gitNamespaceId:
                nullable: true
                oneOf:
                  - type: string
                  - type: number
            required:
              - scopeId
              - gitNamespaceId
            type: object
          type: array
        dismissedToasts:
          items:
            properties:
              name:
                type: string
              dismissals:
                items:
                  properties:
                    scopeId:
                      type: string
                    createdAt:
                      type: number
                  required:
                    - scopeId
                    - createdAt
                  type: object
                type: array
            required:
              - name
              - dismissals
            type: object
            description: A record of when, under a certain scopeId, a toast was dismissed
          type: array
          description: A record of when, under a certain scopeId, a toast was dismissed
        favoriteProjectsAndSpaces:
          items:
            properties:
              teamId:
                type: string
              projectId:
                type: string
            required:
              - teamId
              - projectId
            type: object
            description: >-
              A list of projects and spaces across teams that a user has marked
              as a favorite.
          type: array
          description: >-
            A list of projects and spaces across teams that a user has marked as
            a favorite.
        hasTrialAvailable:
          type: boolean
          description: Whether the user has a trial available for a paid plan subscription.
        remoteCaching:
          properties:
            enabled:
              type: boolean
          type: object
          description: remote caching settings
        dataCache:
          properties:
            excessBillingEnabled:
              type: boolean
          type: object
          description: data cache settings
        featureBlocks:
          properties:
            webAnalytics:
              properties:
                blockedFrom:
                  type: number
                blockedUntil:
                  type: number
                isCurrentlyBlocked:
                  type: boolean
              required:
                - isCurrentlyBlocked
              type: object
          type: object
          description: Feature blocks for the user
        id:
          type: string
          description: The User's unique identifier.
          example: AEIIDYVk59zbFF2Sxfyxxmua
        email:
          type: string
          description: Email address associated with the User account.
          example: me@example.com
        name:
          nullable: true
          type: string
          description: >-
            Name associated with the User account, or `null` if none has been
            provided.
          example: John Doe
        username:
          type: string
          description: Unique username associated with the User account.
          example: jdoe
        avatar:
          nullable: true
          type: string
          description: >-
            SHA1 hash of the avatar for the User account. Can be used in
            conjuction with the ... endpoint to retrieve the avatar image.
          example: 22cb30c85ff45ac4c72de8981500006b28114aa1
        defaultTeamId:
          nullable: true
          type: string
          description: The user's default team.
      required:
        - createdAt
        - softBlock
        - billing
        - resourceConfig
        - stagingPrefix
        - hasTrialAvailable
        - id
        - email
        - name
        - username
        - avatar
        - defaultTeamId
      type: object
      description: Data for the currently authenticated User.
    AuthUserLimited:
      properties:
        limited:
          type: boolean
          description: >-
            Property indicating that this User data contains only limited
            information, due to the authentication token missing privileges to
            read the full User data. Re-login with email, GitHub, GitLab or
            Bitbucket in order to upgrade the authentication token with the
            necessary privileges.
        id:
          type: string
          description: The User's unique identifier.
          example: AEIIDYVk59zbFF2Sxfyxxmua
        email:
          type: string
          description: Email address associated with the User account.
          example: me@example.com
        name:
          nullable: true
          type: string
          description: >-
            Name associated with the User account, or `null` if none has been
            provided.
          example: John Doe
        username:
          type: string
          description: Unique username associated with the User account.
          example: jdoe
        avatar:
          nullable: true
          type: string
          description: >-
            SHA1 hash of the avatar for the User account. Can be used in
            conjuction with the ... endpoint to retrieve the avatar image.
          example: 22cb30c85ff45ac4c72de8981500006b28114aa1
        defaultTeamId:
          nullable: true
          type: string
          description: The user's default team.
      required:
        - limited
        - id
        - email
        - name
        - username
        - avatar
        - defaultTeamId
      type: object
      description: >-
        A limited form of data for the currently authenticated User, due to the
        authentication token missing privileges to read the full User data.

````