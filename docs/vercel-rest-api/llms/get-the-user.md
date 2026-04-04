# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/user/get-the-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the User

> Retrieves information related to the currently authenticated User.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/user
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
  /v2/user:
    get:
      tags:
        - user
      summary: Get the User
      description: Retrieves information related to the currently authenticated User.
      operationId: getAuthUser
      parameters: []
      responses:
        '200':
          description: Successful response.
          content:
            application/json:
              schema:
                properties:
                  user:
                    oneOf:
                      - $ref: '#/components/schemas/AuthUser'
                      - $ref: '#/components/schemas/AuthUserLimited'
                required:
                  - user
                type: object
                description: Successful response.
        '302':
          description: ''
        '400':
          description: ''
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '409':
          description: ''
      security:
        - bearerToken: []
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
              enum:
                - false
                - true
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            buildEntitlements:
              properties:
                enhancedBuilds:
                  type: boolean
                  enum:
                    - false
                    - true
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
              enum:
                - false
                - true
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
                default:
                  type: string
                  enum:
                    - enhanced
                    - turbo
                    - standard
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
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
                  enum:
                    - false
                    - true
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
            bulkRedirectsFreeLimitOverride:
              type: number
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
              - gitNamespaceId
              - scopeId
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
                    - createdAt
                    - scopeId
                  type: object
                type: array
            required:
              - dismissals
              - name
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
              - projectId
              - teamId
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
          enum:
            - false
            - true
          description: Whether the user has a trial available for a paid plan subscription.
        remoteCaching:
          properties:
            enabled:
              type: boolean
              enum:
                - false
                - true
          type: object
          description: remote caching settings
        dataCache:
          properties:
            excessBillingEnabled:
              type: boolean
              enum:
                - false
                - true
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
                  enum:
                    - false
                    - true
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
        - avatar
        - billing
        - createdAt
        - defaultTeamId
        - email
        - hasTrialAvailable
        - id
        - name
        - resourceConfig
        - softBlock
        - stagingPrefix
        - username
      type: object
      description: Data for the currently authenticated User.
    AuthUserLimited:
      properties:
        limited:
          type: boolean
          enum:
            - true
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
        - avatar
        - defaultTeamId
        - email
        - id
        - limited
        - name
        - username
      type: object
      description: >-
        A limited form of data for the currently authenticated User, due to the
        authentication token missing privileges to read the full User data.
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````