# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/find-a-project-by-id-or-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Find a project by id or name

> Get the information for a specific project by passing either the project `id` or `name` in the URL.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}
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
  /v9/projects/{idOrName}:
    get:
      tags:
        - projects
      summary: Find a project by id or name
      description: >-
        Get the information for a specific project by passing either the project
        `id` or `name` in the URL.
      operationId: getProject
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
            oneOf:
              - type: string
              - type: boolean
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      responses:
        '200':
          description: The project information
          content:
            application/json:
              schema:
                properties:
                  integrations:
                    items:
                      properties:
                        installationId:
                          type: string
                          description: The integration installation ID.
                          example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                        resources:
                          items:
                            properties:
                              externalResourceId:
                                type: string
                            required:
                              - externalResourceId
                            type: object
                            description: >-
                              The list of the installation resources connected
                              to the project.
                          type: array
                          description: >-
                            The list of the installation resources connected to
                            the project.
                      required:
                        - installationId
                      type: object
                      description: Integration installation enabled on the project.
                    type: array
                  accountId:
                    type: string
                  analytics:
                    properties:
                      id:
                        type: string
                      canceledAt:
                        nullable: true
                        type: number
                      disabledAt:
                        type: number
                      enabledAt:
                        type: number
                      paidAt:
                        type: number
                      sampleRatePercent:
                        nullable: true
                        type: number
                      spendLimitInDollars:
                        nullable: true
                        type: number
                    required:
                      - disabledAt
                      - enabledAt
                      - id
                    type: object
                  appliedCve55182Migration:
                    type: boolean
                    enum:
                      - false
                      - true
                  speedInsights:
                    properties:
                      id:
                        type: string
                      enabledAt:
                        type: number
                      disabledAt:
                        type: number
                      canceledAt:
                        type: number
                      hasData:
                        type: boolean
                        enum:
                          - false
                          - true
                      paidAt:
                        type: number
                    required:
                      - id
                    type: object
                  autoExposeSystemEnvs:
                    type: boolean
                    enum:
                      - false
                      - true
                  autoAssignCustomDomains:
                    type: boolean
                    enum:
                      - false
                      - true
                  autoAssignCustomDomainsUpdatedBy:
                    type: string
                  buildCommand:
                    nullable: true
                    type: string
                  commandForIgnoringBuildStep:
                    nullable: true
                    type: string
                  connectConfigurations:
                    nullable: true
                    items:
                      properties:
                        envId:
                          oneOf:
                            - type: string
                            - type: string
                              enum:
                                - production
                                - preview
                        connectConfigurationId:
                          type: string
                        dc:
                          type: string
                        passive:
                          type: boolean
                          enum:
                            - false
                            - true
                        buildsEnabled:
                          type: boolean
                          enum:
                            - false
                            - true
                        aws:
                          properties:
                            subnetIds:
                              items:
                                type: string
                              type: array
                            securityGroupId:
                              type: string
                          required:
                            - securityGroupId
                            - subnetIds
                          type: object
                        createdAt:
                          type: number
                        updatedAt:
                          type: number
                      required:
                        - buildsEnabled
                        - connectConfigurationId
                        - createdAt
                        - envId
                        - passive
                        - updatedAt
                      type: object
                    type: array
                  connectConfigurationId:
                    nullable: true
                    type: string
                  connectBuildsEnabled:
                    type: boolean
                    enum:
                      - false
                      - true
                  passiveConnectConfigurationId:
                    nullable: true
                    type: string
                  createdAt:
                    type: number
                  customerSupportCodeVisibility:
                    type: boolean
                    enum:
                      - false
                      - true
                  crons:
                    properties:
                      enabledAt:
                        type: number
                        description: >-
                          The time the feature was enabled for this project.
                          Note: It enables automatically with the first
                          Deployment that outputs cronjobs.
                      disabledAt:
                        nullable: true
                        type: number
                        description: The time the feature was disabled for this project.
                      updatedAt:
                        type: number
                      deploymentId:
                        nullable: true
                        type: string
                        description: >-
                          The ID of the Deployment from which the definitions
                          originated.
                      definitions:
                        items:
                          properties:
                            host:
                              type: string
                              description: The hostname that should be used.
                              example: vercel.com
                            path:
                              type: string
                              description: The path that should be called for the cronjob.
                              example: /api/crons/sync-something?hello=world
                            schedule:
                              type: string
                              description: The cron expression.
                              example: 0 0 * * *
                          required:
                            - host
                            - path
                            - schedule
                          type: object
                        type: array
                    required:
                      - definitions
                      - deploymentId
                      - disabledAt
                      - enabledAt
                      - updatedAt
                    type: object
                  dataCache:
                    properties:
                      userDisabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      storageSizeBytes:
                        nullable: true
                        type: number
                      unlimited:
                        type: boolean
                        enum:
                          - false
                          - true
                    required:
                      - userDisabled
                    type: object
                  deploymentExpiration:
                    nullable: true
                    properties:
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
                    description: >-
                      Retention policies for deployments. These are enforced at
                      the project level, but we also maintain an instance of
                      this at the team level as a default policy that gets
                      applied to new projects.
                  devCommand:
                    nullable: true
                    type: string
                  directoryListing:
                    type: boolean
                    enum:
                      - false
                      - true
                  installCommand:
                    nullable: true
                    type: string
                  env:
                    items:
                      properties:
                        target:
                          oneOf:
                            - items:
                                type: string
                                enum:
                                  - production
                                  - preview
                                  - development
                                  - preview
                                  - development
                              type: array
                            - type: string
                              enum:
                                - production
                                - preview
                                - development
                        type:
                          type: string
                          enum:
                            - secret
                            - system
                            - encrypted
                            - plain
                            - sensitive
                        sunsetSecretId:
                          type: string
                          description: >-
                            This is used to identify variables that have been
                            migrated from type secret to sensitive.
                        legacyValue:
                          type: string
                          description: >-
                            Legacy now-encryption ciphertext, present after
                            migration swaps value/vsmValue
                        decrypted:
                          type: boolean
                          enum:
                            - false
                            - true
                        value:
                          type: string
                        vsmValue:
                          type: string
                        id:
                          type: string
                        key:
                          type: string
                        configurationId:
                          nullable: true
                          type: string
                        createdAt:
                          type: number
                        updatedAt:
                          type: number
                        createdBy:
                          nullable: true
                          type: string
                        updatedBy:
                          nullable: true
                          type: string
                        gitBranch:
                          type: string
                        edgeConfigId:
                          nullable: true
                          type: string
                        edgeConfigTokenId:
                          nullable: true
                          type: string
                        contentHint:
                          nullable: true
                          oneOf:
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-url
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-url
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-token
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-read-only-token
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - blob-read-write-token
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-non-pooling
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-prisma-url
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-user
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-host
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-password
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-database
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-no-ssl
                                storeId:
                                  type: string
                              required:
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - integration-store-secret
                                storeId:
                                  type: string
                                integrationId:
                                  type: string
                                integrationProductId:
                                  type: string
                                integrationConfigurationId:
                                  type: string
                              required:
                                - integrationConfigurationId
                                - integrationId
                                - integrationProductId
                                - storeId
                                - type
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - flags-connection-string
                                projectId:
                                  type: string
                              required:
                                - projectId
                                - type
                              type: object
                        internalContentHint:
                          nullable: true
                          properties:
                            type:
                              type: string
                              enum:
                                - flags-secret
                            encryptedValue:
                              type: string
                              description: >-
                                Contains the `value` of the env variable,
                                encrypted with a special key to make decryption
                                possible in the subscriber Lambda.
                          required:
                            - encryptedValue
                            - type
                          type: object
                          description: >-
                            Similar to `contentHints`, but should not be exposed
                            to the user.
                        comment:
                          type: string
                        customEnvironmentIds:
                          items:
                            type: string
                          type: array
                      required:
                        - key
                        - type
                        - value
                      type: object
                    type: array
                  customEnvironments:
                    items:
                      properties:
                        id:
                          type: string
                          description: >-
                            Unique identifier for the custom environment
                            (format: env_*)
                        slug:
                          type: string
                          description: URL-friendly name of the environment
                        type:
                          type: string
                          enum:
                            - production
                            - preview
                            - development
                          description: >-
                            The type of environment (production, preview, or
                            development)
                        description:
                          type: string
                          description: Optional description of the environment's purpose
                        branchMatcher:
                          properties:
                            type:
                              type: string
                              enum:
                                - endsWith
                                - startsWith
                                - equals
                              description: The type of matching to perform
                            pattern:
                              type: string
                              description: The pattern to match against branch names
                          required:
                            - pattern
                            - type
                          type: object
                          description: >-
                            Configuration for matching git branches to this
                            environment
                        domains:
                          items:
                            properties:
                              name:
                                type: string
                              apexName:
                                type: string
                              projectId:
                                type: string
                              redirect:
                                nullable: true
                                type: string
                              redirectStatusCode:
                                nullable: true
                                type: number
                                enum:
                                  - 301
                                  - 302
                                  - 307
                                  - 308
                              gitBranch:
                                nullable: true
                                type: string
                              customEnvironmentId:
                                nullable: true
                                type: string
                              updatedAt:
                                type: number
                              createdAt:
                                type: number
                              verified:
                                type: boolean
                                enum:
                                  - false
                                  - true
                                description: >-
                                  `true` if the domain is verified for use with
                                  the project. If `false` it will not be used as
                                  an alias on this project until the challenge
                                  in `verification` is completed.
                              verification:
                                items:
                                  properties:
                                    type:
                                      type: string
                                    domain:
                                      type: string
                                    value:
                                      type: string
                                    reason:
                                      type: string
                                  required:
                                    - domain
                                    - reason
                                    - type
                                    - value
                                  type: object
                                  description: >-
                                    A list of verification challenges, one of
                                    which must be completed to verify the domain
                                    for use on the project. After the challenge
                                    is complete `POST
                                    /projects/:idOrName/domains/:domain/verify`
                                    to verify the domain. Possible challenges: -
                                    If `verification.type = TXT` the
                                    `verification.domain` will be checked for a
                                    TXT record matching `verification.value`.
                                type: array
                                description: >-
                                  A list of verification challenges, one of
                                  which must be completed to verify the domain
                                  for use on the project. After the challenge is
                                  complete `POST
                                  /projects/:idOrName/domains/:domain/verify` to
                                  verify the domain. Possible challenges: - If
                                  `verification.type = TXT` the
                                  `verification.domain` will be checked for a
                                  TXT record matching `verification.value`.
                            required:
                              - apexName
                              - name
                              - projectId
                              - verified
                            type: object
                            description: List of domains associated with this environment
                          type: array
                          description: List of domains associated with this environment
                        currentDeploymentAliases:
                          items:
                            type: string
                          type: array
                          description: List of aliases for the current deployment
                        createdAt:
                          type: number
                          description: Timestamp when the environment was created
                        updatedAt:
                          type: number
                          description: Timestamp when the environment was last updated
                      required:
                        - createdAt
                        - id
                        - slug
                        - type
                        - updatedAt
                      type: object
                      description: >-
                        Internal representation of a custom environment with all
                        required properties
                    type: array
                  framework:
                    nullable: true
                    type: string
                    enum:
                      - blitzjs
                      - nextjs
                      - gatsby
                      - remix
                      - react-router
                      - astro
                      - hexo
                      - eleventy
                      - docusaurus-2
                      - docusaurus
                      - preact
                      - solidstart-1
                      - solidstart
                      - dojo
                      - ember
                      - vue
                      - scully
                      - ionic-angular
                      - angular
                      - polymer
                      - svelte
                      - sveltekit
                      - sveltekit-1
                      - ionic-react
                      - create-react-app
                      - gridsome
                      - umijs
                      - sapper
                      - saber
                      - stencil
                      - nuxtjs
                      - redwoodjs
                      - hugo
                      - jekyll
                      - brunch
                      - middleman
                      - zola
                      - hydrogen
                      - vite
                      - tanstack-start
                      - vitepress
                      - vuepress
                      - parcel
                      - fastapi
                      - flask
                      - fasthtml
                      - sanity-v3
                      - sanity
                      - storybook
                      - nitro
                      - hono
                      - express
                      - h3
                      - koa
                      - nestjs
                      - elysia
                      - fastify
                      - xmcp
                      - python
                      - ruby
                      - rust
                      - node
                      - services
                  gitForkProtection:
                    type: boolean
                    enum:
                      - false
                      - true
                  gitLFS:
                    type: boolean
                    enum:
                      - false
                      - true
                  id:
                    type: string
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
                  latestDeployments:
                    items:
                      properties:
                        alias:
                          items:
                            type: string
                          type: array
                        aliasAssigned:
                          nullable: true
                          oneOf:
                            - type: number
                            - type: boolean
                              enum:
                                - false
                                - true
                        builds:
                          items:
                            properties:
                              use:
                                type: string
                              src:
                                type: string
                              dest:
                                type: string
                            required:
                              - use
                            type: object
                          type: array
                        createdAt:
                          type: number
                        createdIn:
                          type: string
                        creator:
                          nullable: true
                          properties:
                            email:
                              type: string
                            githubLogin:
                              type: string
                            gitlabLogin:
                              type: string
                            uid:
                              type: string
                            username:
                              type: string
                          required:
                            - email
                            - uid
                            - username
                          type: object
                        deploymentHostname:
                          type: string
                        name:
                          type: string
                        forced:
                          type: boolean
                          enum:
                            - false
                            - true
                        id:
                          type: string
                        meta:
                          additionalProperties:
                            type: string
                          type: object
                        plan:
                          type: string
                        private:
                          type: boolean
                          enum:
                            - false
                            - true
                        readyState:
                          type: string
                        requestedAt:
                          type: number
                        target:
                          nullable: true
                          type: string
                        teamId:
                          nullable: true
                          type: string
                        type:
                          type: string
                        url:
                          type: string
                        userId:
                          type: string
                        withCache:
                          type: boolean
                          enum:
                            - false
                            - true
                      required:
                        - createdAt
                        - createdIn
                        - creator
                        - deploymentHostname
                        - id
                        - name
                        - plan
                        - private
                        - readyState
                        - type
                        - url
                        - userId
                      type: object
                    type: array
                  link:
                    oneOf:
                      - properties:
                          org:
                            type: string
                          repoOwnerId:
                            type: number
                            description: >-
                              A new field, should be included in all new project
                              links, is being added just in time when a
                              deployment is created. This is needed for
                              Protected Git scopes.
                          repo:
                            type: string
                          repoId:
                            type: number
                          type:
                            type: string
                            enum:
                              - github
                          createdAt:
                            type: number
                          deployHooks:
                            items:
                              properties:
                                createdAt:
                                  type: number
                                id:
                                  type: string
                                name:
                                  type: string
                                ref:
                                  type: string
                                url:
                                  type: string
                              required:
                                - id
                                - name
                                - ref
                                - url
                              type: object
                            type: array
                          gitCredentialId:
                            type: string
                          updatedAt:
                            type: number
                          sourceless:
                            type: boolean
                            enum:
                              - false
                              - true
                          productionBranch:
                            type: string
                        required:
                          - deployHooks
                          - gitCredentialId
                          - org
                          - productionBranch
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-limited
                          repo:
                            type: string
                          repoId:
                            type: number
                          createdAt:
                            type: number
                          updatedAt:
                            type: number
                          org:
                            type: string
                          repoOwnerId:
                            type: number
                            description: >-
                              A new field, should be included in all new project
                              links, is being added just in time when a
                              deployment is created. This is needed for
                              Protected Git scopes.
                          deployHooks:
                            items:
                              properties:
                                createdAt:
                                  type: number
                                id:
                                  type: string
                                name:
                                  type: string
                                ref:
                                  type: string
                                url:
                                  type: string
                              required:
                                - id
                                - name
                                - ref
                                - url
                              type: object
                            type: array
                          gitCredentialId:
                            type: string
                          sourceless:
                            type: boolean
                            enum:
                              - false
                              - true
                          productionBranch:
                            type: string
                        required:
                          - deployHooks
                          - gitCredentialId
                          - org
                          - productionBranch
                          - type
                        type: object
                      - properties:
                          org:
                            type: string
                          repoOwnerId:
                            type: number
                            description: >-
                              A new field, should be included in all new project
                              links, is being added just in time when a
                              deployment is created. This is needed for
                              Protected Git scopes.
                          repo:
                            type: string
                          repoId:
                            type: number
                          type:
                            type: string
                            enum:
                              - github-custom-host
                          host:
                            type: string
                          createdAt:
                            type: number
                          deployHooks:
                            items:
                              properties:
                                createdAt:
                                  type: number
                                id:
                                  type: string
                                name:
                                  type: string
                                ref:
                                  type: string
                                url:
                                  type: string
                              required:
                                - id
                                - name
                                - ref
                                - url
                              type: object
                            type: array
                          gitCredentialId:
                            type: string
                          updatedAt:
                            type: number
                          sourceless:
                            type: boolean
                            enum:
                              - false
                              - true
                          productionBranch:
                            type: string
                        required:
                          - deployHooks
                          - gitCredentialId
                          - host
                          - org
                          - productionBranch
                          - type
                        type: object
                      - properties:
                          projectId:
                            type: string
                          projectName:
                            type: string
                          projectNameWithNamespace:
                            type: string
                          projectNamespace:
                            type: string
                          projectOwnerId:
                            type: number
                            description: >-
                              A new field, should be included in all new project
                              links, is being added just in time when a
                              deployment is created. This is needed for
                              Protected Git scopes. This is the id of the top
                              level group that a namespace belongs to. Gitlab
                              supports group nesting (up to 20 levels).
                          projectUrl:
                            type: string
                          type:
                            type: string
                            enum:
                              - gitlab
                          createdAt:
                            type: number
                          deployHooks:
                            items:
                              properties:
                                createdAt:
                                  type: number
                                id:
                                  type: string
                                name:
                                  type: string
                                ref:
                                  type: string
                                url:
                                  type: string
                              required:
                                - id
                                - name
                                - ref
                                - url
                              type: object
                            type: array
                          gitCredentialId:
                            type: string
                          updatedAt:
                            type: number
                          sourceless:
                            type: boolean
                            enum:
                              - false
                              - true
                          productionBranch:
                            type: string
                        required:
                          - deployHooks
                          - gitCredentialId
                          - productionBranch
                          - projectId
                          - projectName
                          - projectNameWithNamespace
                          - projectNamespace
                          - projectUrl
                          - type
                        type: object
                      - properties:
                          name:
                            type: string
                          slug:
                            type: string
                          owner:
                            type: string
                          type:
                            type: string
                            enum:
                              - bitbucket
                          uuid:
                            type: string
                          workspaceUuid:
                            type: string
                          createdAt:
                            type: number
                          deployHooks:
                            items:
                              properties:
                                createdAt:
                                  type: number
                                id:
                                  type: string
                                name:
                                  type: string
                                ref:
                                  type: string
                                url:
                                  type: string
                              required:
                                - id
                                - name
                                - ref
                                - url
                              type: object
                            type: array
                          gitCredentialId:
                            type: string
                          updatedAt:
                            type: number
                          sourceless:
                            type: boolean
                            enum:
                              - false
                              - true
                          productionBranch:
                            type: string
                        required:
                          - deployHooks
                          - gitCredentialId
                          - name
                          - owner
                          - productionBranch
                          - slug
                          - type
                          - uuid
                          - workspaceUuid
                        type: object
                  microfrontends:
                    oneOf:
                      - properties:
                          isDefaultApp:
                            type: boolean
                            enum:
                              - true
                          updatedAt:
                            type: number
                            description: >-
                              Timestamp when the microfrontends settings were
                              last updated.
                          groupIds:
                            type: array
                            items:
                              type: string
                            minItems: 1
                            description: >-
                              The group IDs of microfrontends that this project
                              belongs to. Each microfrontend project must belong
                              to a microfrontends group that is the set of
                              microfrontends that are used together.
                          enabled:
                            type: boolean
                            enum:
                              - true
                            description: >-
                              Whether microfrontends are enabled for this
                              project.
                          defaultRoute:
                            type: string
                            description: >-
                              A path that is used to take screenshots and as the
                              default path in preview links when a domain for
                              this microfrontend is shown in the UI. Includes
                              the leading slash, e.g. `/docs`
                          freeProjectForLegacyLimits:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether the project was part of the legacy limits
                              for hobby and pro-trial before billing was added.
                              This field is only set when the team is upgraded
                              to a paid plan and we are backfilling the
                              subscription status. We cap the subscription to 2
                              projects and set this field for the 3rd project.
                              When this field is set, the project is not charged
                              for and we do not call any billing APIs for this
                              project.
                        required:
                          - enabled
                          - groupIds
                          - isDefaultApp
                          - updatedAt
                        type: object
                      - properties:
                          isDefaultApp:
                            type: boolean
                            enum:
                              - false
                          routeObservabilityToThisProject:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether observability data should be routed to
                              this microfrontend project or a root project.
                          doNotRouteWithMicrofrontendsRouting:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether to add microfrontends routing to aliases.
                              This means domains in this project will route as a
                              microfrontend.
                          updatedAt:
                            type: number
                            description: >-
                              Timestamp when the microfrontends settings were
                              last updated.
                          groupIds:
                            type: array
                            items:
                              type: string
                            minItems: 1
                            description: >-
                              The group IDs of microfrontends that this project
                              belongs to. Each microfrontend project must belong
                              to a microfrontends group that is the set of
                              microfrontends that are used together.
                          enabled:
                            type: boolean
                            enum:
                              - true
                            description: >-
                              Whether microfrontends are enabled for this
                              project.
                          defaultRoute:
                            type: string
                            description: >-
                              A path that is used to take screenshots and as the
                              default path in preview links when a domain for
                              this microfrontend is shown in the UI. Includes
                              the leading slash, e.g. `/docs`
                          freeProjectForLegacyLimits:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether the project was part of the legacy limits
                              for hobby and pro-trial before billing was added.
                              This field is only set when the team is upgraded
                              to a paid plan and we are backfilling the
                              subscription status. We cap the subscription to 2
                              projects and set this field for the 3rd project.
                              When this field is set, the project is not charged
                              for and we do not call any billing APIs for this
                              project.
                        required:
                          - enabled
                          - groupIds
                          - updatedAt
                        type: object
                      - properties:
                          updatedAt:
                            type: number
                          groupIds:
                            type: array
                            items: {}
                            minItems: 0
                            maxItems: 0
                          enabled:
                            type: boolean
                            enum:
                              - false
                          freeProjectForLegacyLimits:
                            type: boolean
                            enum:
                              - false
                              - true
                        required:
                          - enabled
                          - groupIds
                          - updatedAt
                        type: object
                  name:
                    type: string
                  nodeVersion:
                    type: string
                    enum:
                      - 24.x
                      - 22.x
                      - 20.x
                      - 18.x
                      - 16.x
                      - 14.x
                      - 12.x
                      - 10.x
                      - 8.10.x
                  optionsAllowlist:
                    nullable: true
                    properties:
                      paths:
                        items:
                          properties:
                            value:
                              type: string
                          required:
                            - value
                          type: object
                        type: array
                    required:
                      - paths
                    type: object
                  outputDirectory:
                    nullable: true
                    type: string
                  passwordProtection:
                    nullable: true
                    type: object
                  productionDeploymentsFastLane:
                    type: boolean
                    enum:
                      - false
                      - true
                  publicSource:
                    nullable: true
                    type: boolean
                    enum:
                      - false
                      - true
                  resourceConfig:
                    properties:
                      elasticConcurrencyEnabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      fluid:
                        type: boolean
                        enum:
                          - false
                          - true
                      functionDefaultRegions:
                        items:
                          type: string
                        type: array
                      functionDefaultTimeout:
                        type: number
                      functionDefaultMemoryType:
                        type: string
                        enum:
                          - standard_legacy
                          - standard
                          - performance
                      functionZeroConfigFailover:
                        type: boolean
                        enum:
                          - false
                          - true
                      buildMachineType:
                        type: string
                        enum:
                          - enhanced
                          - turbo
                      isNSNBDisabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      buildQueue:
                        properties:
                          configuration:
                            type: string
                            enum:
                              - SKIP_NAMESPACE_QUEUE
                              - WAIT_FOR_NAMESPACE_QUEUE
                        type: object
                    type: object
                    required:
                      - functionDefaultRegions
                  rollbackDescription:
                    properties:
                      userId:
                        type: string
                        description: The user who rolled back the project.
                      username:
                        type: string
                        description: The username of the user who rolled back the project.
                      description:
                        type: string
                        description: >-
                          User-supplied explanation of why they rolled back the
                          project. Limited to 250 characters.
                      createdAt:
                        type: number
                        description: Timestamp of when the rollback was requested.
                    required:
                      - createdAt
                      - description
                      - userId
                      - username
                    type: object
                    description: >-
                      Description of why a project was rolled back, and by whom.
                      Note that lastAliasRequest contains the from/to details of
                      the rollback.
                  rollingRelease:
                    nullable: true
                    properties:
                      target:
                        type: string
                        description: >-
                          The environment that the release targets, currently
                          only supports production. Adding in case we want to
                          configure with alias groups or custom environments.
                        example: production
                      stages:
                        nullable: true
                        items:
                          properties:
                            targetPercentage:
                              type: number
                              description: >-
                                The percentage of traffic to serve to the canary
                                deployment (0-100)
                              example: 25
                            requireApproval:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                Whether or not this stage requires manual
                                approval to proceed
                              example: false
                            duration:
                              type: number
                              description: >-
                                Duration in minutes for automatic advancement to
                                the next stage
                              example: 600
                            linearShift:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                Whether to linearly shift traffic over the
                                duration of this stage
                              example: false
                          required:
                            - targetPercentage
                          type: object
                          description: >-
                            An array of all the stages required during a
                            deployment release. Each stage defines a target
                            percentage and advancement rules. The final stage
                            must always have targetPercentage: 100.
                        type: array
                        description: >-
                          An array of all the stages required during a
                          deployment release. Each stage defines a target
                          percentage and advancement rules. The final stage must
                          always have targetPercentage: 100.
                      canaryResponseHeader:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          Whether the request served by a canary deployment
                          should return a header indicating a canary was served.
                          Defaults to `false` when omitted.
                        example: false
                    required:
                      - target
                    type: object
                    description: >-
                      Project-level rolling release configuration that defines
                      how deployments should be gradually rolled out
                  defaultResourceConfig:
                    properties:
                      elasticConcurrencyEnabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      fluid:
                        type: boolean
                        enum:
                          - false
                          - true
                      functionDefaultRegions:
                        items:
                          type: string
                        type: array
                      functionDefaultTimeout:
                        type: number
                      functionDefaultMemoryType:
                        type: string
                        enum:
                          - standard_legacy
                          - standard
                          - performance
                      functionZeroConfigFailover:
                        type: boolean
                        enum:
                          - false
                          - true
                      buildMachineType:
                        type: string
                        enum:
                          - enhanced
                          - turbo
                      isNSNBDisabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      buildQueue:
                        properties:
                          configuration:
                            type: string
                            enum:
                              - SKIP_NAMESPACE_QUEUE
                              - WAIT_FOR_NAMESPACE_QUEUE
                        type: object
                    type: object
                    required:
                      - functionDefaultRegions
                  rootDirectory:
                    nullable: true
                    type: string
                  serverlessFunctionZeroConfigFailover:
                    type: boolean
                    enum:
                      - false
                      - true
                  skewProtectionBoundaryAt:
                    type: number
                  skewProtectionMaxAge:
                    type: number
                  skewProtectionAllowedDomains:
                    items:
                      type: string
                    type: array
                  skipGitConnectDuringLink:
                    type: boolean
                    enum:
                      - false
                      - true
                  staticIps:
                    properties:
                      builds:
                        type: boolean
                        enum:
                          - false
                          - true
                      enabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      regions:
                        items:
                          type: string
                        type: array
                    required:
                      - builds
                      - enabled
                      - regions
                    type: object
                  sourceFilesOutsideRootDirectory:
                    type: boolean
                    enum:
                      - false
                      - true
                  enableAffectedProjectsDeployments:
                    type: boolean
                    enum:
                      - false
                      - true
                  ssoProtection:
                    nullable: true
                    properties:
                      deploymentType:
                        type: string
                        enum:
                          - preview
                          - all
                          - prod_deployment_urls_and_all_previews
                          - all_except_custom_domains
                      cve55182MigrationAppliedFrom:
                        nullable: true
                        type: string
                        enum:
                          - preview
                          - all
                          - prod_deployment_urls_and_all_previews
                          - all_except_custom_domains
                    required:
                      - deploymentType
                    type: object
                  targets:
                    additionalProperties:
                      nullable: true
                      properties:
                        alias:
                          items:
                            type: string
                          type: array
                        aliasAssigned:
                          nullable: true
                          oneOf:
                            - type: number
                            - type: boolean
                              enum:
                                - false
                                - true
                        builds:
                          items:
                            properties:
                              use:
                                type: string
                              src:
                                type: string
                              dest:
                                type: string
                            required:
                              - use
                            type: object
                          type: array
                        createdAt:
                          type: number
                        createdIn:
                          type: string
                        creator:
                          nullable: true
                          properties:
                            email:
                              type: string
                            githubLogin:
                              type: string
                            gitlabLogin:
                              type: string
                            uid:
                              type: string
                            username:
                              type: string
                          required:
                            - email
                            - uid
                            - username
                          type: object
                        deploymentHostname:
                          type: string
                        name:
                          type: string
                        forced:
                          type: boolean
                          enum:
                            - false
                            - true
                        id:
                          type: string
                        meta:
                          additionalProperties:
                            type: string
                          type: object
                        plan:
                          type: string
                        private:
                          type: boolean
                          enum:
                            - false
                            - true
                        readyState:
                          type: string
                        requestedAt:
                          type: number
                        target:
                          nullable: true
                          type: string
                        teamId:
                          nullable: true
                          type: string
                        type:
                          type: string
                        url:
                          type: string
                        userId:
                          type: string
                        withCache:
                          type: boolean
                          enum:
                            - false
                            - true
                      required:
                        - createdAt
                        - createdIn
                        - creator
                        - deploymentHostname
                        - id
                        - name
                        - plan
                        - private
                        - readyState
                        - type
                        - url
                        - userId
                      type: object
                    type: object
                  transferCompletedAt:
                    type: number
                  transferStartedAt:
                    type: number
                  transferToAccountId:
                    type: string
                  transferredFromAccountId:
                    type: string
                  updatedAt:
                    type: number
                  live:
                    type: boolean
                    enum:
                      - false
                      - true
                  enablePreviewFeedback:
                    nullable: true
                    type: boolean
                    enum:
                      - false
                      - true
                  enableProductionFeedback:
                    nullable: true
                    type: boolean
                    enum:
                      - false
                      - true
                  permissions:
                    properties:
                      oauth2Connection:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      user:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      userConnection:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      userSudo:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      webAuthn:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      accessGroup:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      agent:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      alerts:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      alertRules:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      aliasGlobal:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      analyticsSampling:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      analyticsUsage:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      apiKey:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      apiKeyAiGateway:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      apiKeyOwnedBySelf:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      oauth2Application:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      vercelAppInstallation:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      vercelAppInstallationRequest:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      auditLog:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      billingAddress:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      billingInformation:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      billingInvoice:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      billingInvoiceEmailRecipient:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      billingInvoiceLanguage:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      billingPlan:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      billingPurchaseOrder:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      billingRefund:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      billingTaxId:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      blob:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      blobStoreTokenSet:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      budget:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      cacheArtifact:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      cacheArtifactUsageEvent:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      codeChecks:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      concurrentBuilds:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      connect:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      connectConfiguration:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      buildMachineDefault:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      dataCacheBillingSettings:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      defaultDeploymentProtection:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      domain:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      domainAcceptDelegation:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      domainAuthCodes:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      domainCertificate:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      domainCheckConfig:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      domainMove:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      domainPurchase:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      domainRecord:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      domainTransferIn:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      drain:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      edgeConfig:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      edgeConfigItem:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      edgeConfigSchema:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      edgeConfigToken:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      endpointVerification:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      event:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      fileUpload:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      flagsExplorerSubscription:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      gitRepository:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      imageOptimizationNewPrice:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integration:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationAccount:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationConfiguration:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationConfigurationProjects:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationConfigurationRole:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationConfigurationTransfer:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationDeploymentAction:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationEvent:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationLog:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationResource:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationResourceReplCommand:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationResourceSecrets:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationSSOSession:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationStoreTokenSet:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationVercelConfigurationOverride:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      integrationPullRequest:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      ipBlocking:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      jobGlobal:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      logDrain:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      marketplaceBillingData:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      marketplaceExperimentationEdgeConfigData:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      marketplaceExperimentationItem:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      marketplaceInstallationMember:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      marketplaceInvoice:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      marketplaceSettings:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      Monitoring:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      monitoringAlert:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      monitoringChart:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      monitoringQuery:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      monitoringSettings:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationCustomerBudget:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationDeploymentFailed:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationDomainConfiguration:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationDomainExpire:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationDomainMoved:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationDomainPurchase:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationDomainRenewal:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationDomainTransfer:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationDomainUnverified:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      NotificationMonitoringAlert:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationPaymentFailed:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationPreferences:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationStatementOfReasons:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      notificationUsageAlert:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      observabilityConfiguration:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      observabilityFunnel:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      observabilityNotebook:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      openTelemetryEndpoint:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      ownEvent:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      organizationDomain:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      passwordProtectionInvoiceItem:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      paymentMethod:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      permissions:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      postgres:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      postgresStoreTokenSet:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      previewDeploymentSuffix:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectTransferIn:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      proTrialOnboarding:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      rateLimit:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      redis:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      redisStoreTokenSet:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      remoteCaching:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      repository:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      samlConfig:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      secret:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      securityPlusConfiguration:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      sensitiveEnvironmentVariablePolicy:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      sharedEnvVars:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      sharedEnvVarsProduction:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      space:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      spaceRun:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      storeTransfer:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      supportCase:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      supportCaseComment:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      team:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamAccessRequest:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamFellowMembership:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamGitExclusivity:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamInvite:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamInviteCode:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamJoin:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamMemberMfaStatus:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamMicrofrontends:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamOwnMembership:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      teamOwnMembershipDisconnectSAML:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      token:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      usage:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      usageCycle:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      vercelRun:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      vercelRunExec:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      vpcPeeringConnection:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      webAnalyticsPlan:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      webhook:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      webhook-event:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      aliasProject:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      aliasProtectionBypass:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      buildMachine:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      connectConfigurationLink:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      dataCacheNamespace:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deployment:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentBuildLogs:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentCheck:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentCheckPreview:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentCheckReRunFromProductionBranch:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentProductionGit:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentV0:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentPreview:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentPrivate:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentPromote:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      deploymentRollback:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      edgeCacheNamespace:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      environments:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      job:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      logs:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      logsPreset:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      observabilityData:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      onDemandBuild:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      onDemandConcurrency:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      optionsAllowlist:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      passwordProtection:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      productionAliasProtectionBypass:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      project:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectAccessGroup:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectAnalyticsSampling:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectAnalyticsUsage:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectCheck:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectCheckRun:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectDeploymentExpiration:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectDeploymentHook:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectDeploymentProtectionStrict:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectDomain:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectDomainCheckConfig:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectDomainMove:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectEnvVars:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectEnvVarsProduction:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectEnvVarsUnownedByIntegration:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectFlags:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectFlagsProduction:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectFromV0:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectId:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectIntegrationConfiguration:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectLink:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectMember:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectMonitoring:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectOIDCToken:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectPermissions:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectProductionBranch:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectProtectionBypass:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectRollingRelease:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectSupportCase:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectSupportCaseComment:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectTier:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectTransfer:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectTransferOut:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      projectUsage:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      seawallConfig:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      sharedEnvVarConnection:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      skewProtection:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      analytics:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      trustedIps:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      v0Chat:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                      webAnalytics:
                        items:
                          $ref: '#/components/schemas/ACLAction'
                        type: array
                    type: object
                  lastRollbackTarget:
                    nullable: true
                    type: object
                  lastAliasRequest:
                    nullable: true
                    properties:
                      fromDeploymentId:
                        nullable: true
                        type: string
                      toDeploymentId:
                        type: string
                      fromRollingReleaseId:
                        type: string
                        description: >-
                          If rolling back from a rolling release,
                          fromDeploymentId captures the "base" of that rolling
                          release, and fromRollingReleaseId captures the
                          "target" of that rolling release.
                      jobStatus:
                        type: string
                        enum:
                          - succeeded
                          - failed
                          - skipped
                          - pending
                          - in-progress
                      requestedAt:
                        type: number
                      type:
                        type: string
                        enum:
                          - promote
                          - rollback
                    required:
                      - fromDeploymentId
                      - jobStatus
                      - requestedAt
                      - toDeploymentId
                      - type
                    type: object
                  protectionBypass:
                    additionalProperties:
                      oneOf:
                        - properties:
                            createdAt:
                              type: number
                            createdBy:
                              type: string
                            scope:
                              type: string
                              enum:
                                - integration-automation-bypass
                            integrationId:
                              type: string
                            configurationId:
                              type: string
                          required:
                            - configurationId
                            - createdAt
                            - createdBy
                            - integrationId
                            - scope
                          type: object
                        - properties:
                            createdAt:
                              type: number
                            createdBy:
                              type: string
                            scope:
                              type: string
                              enum:
                                - automation-bypass
                            isEnvVar:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                When there was only one bypass, it was
                                automatically set as an env var on deployments.
                                With multiple bypasses, there is always one
                                bypass that is selected as the default, and gets
                                set as an env var on deployments. As this is a
                                new field, undefined means that the bypass is
                                the env var. If there are any automation
                                bypasses, exactly one must be the env var.
                            note:
                              type: string
                              description: >-
                                Optional note about the bypass to be displayed
                                in the UI
                          required:
                            - createdAt
                            - createdBy
                            - scope
                          type: object
                    type: object
                  hasActiveBranches:
                    type: boolean
                    enum:
                      - false
                      - true
                  trustedIps:
                    nullable: true
                    oneOf:
                      - properties:
                          deploymentType:
                            type: string
                            enum:
                              - production
                              - preview
                              - all
                              - prod_deployment_urls_and_all_previews
                              - all_except_custom_domains
                          addresses:
                            items:
                              properties:
                                value:
                                  type: string
                                note:
                                  type: string
                              required:
                                - value
                              type: object
                            type: array
                          protectionMode:
                            type: string
                            enum:
                              - additional
                              - exclusive
                        required:
                          - addresses
                          - deploymentType
                          - protectionMode
                        type: object
                      - properties:
                          deploymentType:
                            type: string
                            enum:
                              - production
                              - preview
                              - all
                              - prod_deployment_urls_and_all_previews
                              - all_except_custom_domains
                        required:
                          - deploymentType
                        type: object
                  gitComments:
                    properties:
                      onPullRequest:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: Whether the Vercel bot should comment on PRs
                      onCommit:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: Whether the Vercel bot should comment on commits
                    required:
                      - onCommit
                      - onPullRequest
                    type: object
                  gitProviderOptions:
                    properties:
                      createDeployments:
                        type: string
                        enum:
                          - enabled
                          - disabled
                        description: >-
                          Whether the Vercel bot should automatically create
                          GitHub deployments
                          https://docs.github.com/en/rest/deployments/deployments#about-deployments
                          NOTE: repository-dispatch events should be used
                          instead
                      disableRepositoryDispatchEvents:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          Whether the Vercel bot should not automatically create
                          GitHub repository-dispatch events on deployment
                          events.
                          https://vercel.com/docs/git/vercel-for-github#repository-dispatch-events
                      requireVerifiedCommits:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          Whether the project requires commits to be signed
                          before deployments will be created.
                    required:
                      - createDeployments
                    type: object
                  paused:
                    type: boolean
                    enum:
                      - false
                      - true
                  concurrencyBucketName:
                    type: string
                  webAnalytics:
                    properties:
                      id:
                        type: string
                      disabledAt:
                        type: number
                      canceledAt:
                        type: number
                      enabledAt:
                        type: number
                      hasData:
                        type: boolean
                        enum:
                          - true
                    required:
                      - id
                    type: object
                  security:
                    properties:
                      attackModeEnabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      attackModeUpdatedAt:
                        type: number
                      firewallEnabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      firewallUpdatedAt:
                        type: number
                      attackModeActiveUntil:
                        nullable: true
                        type: number
                      firewallConfigVersion:
                        type: number
                      firewallSeawallEnabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      ja3Enabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      ja4Enabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      firewallBypassIps:
                        items:
                          type: string
                        type: array
                      managedRules:
                        nullable: true
                        properties:
                          vercel_ruleset:
                            properties:
                              active:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              action:
                                type: string
                                enum:
                                  - log
                                  - deny
                                  - challenge
                            required:
                              - active
                            type: object
                          bot_filter:
                            properties:
                              active:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              action:
                                type: string
                                enum:
                                  - log
                                  - deny
                                  - challenge
                            required:
                              - active
                            type: object
                          ai_bots:
                            properties:
                              active:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              action:
                                type: string
                                enum:
                                  - log
                                  - deny
                                  - challenge
                            required:
                              - active
                            type: object
                          owasp:
                            properties:
                              active:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              action:
                                type: string
                                enum:
                                  - log
                                  - deny
                                  - challenge
                            required:
                              - active
                            type: object
                        required:
                          - ai_bots
                          - bot_filter
                          - owasp
                          - vercel_ruleset
                        type: object
                      botIdEnabled:
                        type: boolean
                        enum:
                          - false
                          - true
                    type: object
                  oidcTokenConfig:
                    properties:
                      enabled:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          Whether or not to generate OpenID Connect JSON Web
                          Tokens.
                      issuerMode:
                        type: string
                        enum:
                          - team
                          - global
                        description: >-
                          - team: `https://oidc.vercel.com/[team_slug]` -
                          global: `https://oidc.vercel.com`
                    type: object
                  tier:
                    type: string
                    enum:
                      - standard
                      - advanced
                      - critical
                  features:
                    properties:
                      webAnalytics:
                        type: boolean
                        enum:
                          - false
                          - true
                    type: object
                  v0:
                    type: boolean
                    enum:
                      - false
                      - true
                  abuse:
                    properties:
                      scanner:
                        type: string
                      history:
                        items:
                          properties:
                            scanner:
                              type: string
                            reason:
                              type: string
                            by:
                              type: string
                            byId:
                              type: string
                            at:
                              type: number
                          required:
                            - at
                            - by
                            - byId
                            - reason
                            - scanner
                          type: object
                        type: array
                      updatedAt:
                        type: number
                      block:
                        properties:
                          action:
                            type: string
                            enum:
                              - blocked
                          reason:
                            type: string
                          statusCode:
                            type: number
                          createdAt:
                            type: number
                          caseId:
                            type: string
                          actor:
                            type: string
                          comment:
                            type: string
                          ineligibleForAppeal:
                            type: boolean
                            enum:
                              - false
                              - true
                          isCascading:
                            type: boolean
                            enum:
                              - false
                              - true
                        required:
                          - action
                          - createdAt
                          - reason
                          - statusCode
                        type: object
                      blockHistory:
                        items:
                          oneOf:
                            - properties:
                                action:
                                  type: string
                                  enum:
                                    - blocked
                                reason:
                                  type: string
                                statusCode:
                                  type: number
                                createdAt:
                                  type: number
                                caseId:
                                  type: string
                                actor:
                                  type: string
                                comment:
                                  type: string
                                ineligibleForAppeal:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                isCascading:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                              required:
                                - action
                                - createdAt
                                - reason
                                - statusCode
                              type: object
                            - properties:
                                action:
                                  type: string
                                  enum:
                                    - unblocked
                                createdAt:
                                  type: number
                                caseId:
                                  type: string
                                actor:
                                  type: string
                                comment:
                                  type: string
                                ineligibleForAppeal:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                isCascading:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                              required:
                                - action
                                - createdAt
                              type: object
                            - properties:
                                action:
                                  type: string
                                  enum:
                                    - route-blocked
                                route:
                                  oneOf:
                                    - properties:
                                        src:
                                          type: string
                                        status:
                                          type: number
                                      required:
                                        - src
                                        - status
                                      type: object
                                    - properties:
                                        has:
                                          items:
                                            oneOf:
                                              - properties:
                                                  type:
                                                    type: string
                                                    enum:
                                                      - header
                                                  key:
                                                    type: string
                                                    enum:
                                                      - x-vercel-ip-country
                                                  value:
                                                    properties:
                                                      eq:
                                                        type: string
                                                    required:
                                                      - eq
                                                    type: object
                                                required:
                                                  - key
                                                  - type
                                                  - value
                                                type: object
                                              - properties:
                                                  type:
                                                    type: string
                                                    enum:
                                                      - host
                                                  value:
                                                    properties:
                                                      eq:
                                                        type: string
                                                    required:
                                                      - eq
                                                    type: object
                                                required:
                                                  - type
                                                  - value
                                                type: object
                                          type: array
                                        mitigate:
                                          properties:
                                            action:
                                              type: string
                                              enum:
                                                - block_legal_cwc
                                          required:
                                            - action
                                          type: object
                                        src:
                                          type: string
                                      required:
                                        - has
                                        - mitigate
                                      type: object
                                reason:
                                  type: string
                                createdAt:
                                  type: number
                                caseId:
                                  type: string
                                actor:
                                  type: string
                                comment:
                                  type: string
                                ineligibleForAppeal:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                isCascading:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                              required:
                                - action
                                - createdAt
                                - reason
                                - route
                              type: object
                            - properties:
                                action:
                                  type: string
                                  enum:
                                    - route-unblocked
                                route:
                                  oneOf:
                                    - properties:
                                        src:
                                          type: string
                                        status:
                                          type: number
                                      required:
                                        - src
                                        - status
                                      type: object
                                    - properties:
                                        has:
                                          items:
                                            oneOf:
                                              - properties:
                                                  type:
                                                    type: string
                                                    enum:
                                                      - header
                                                  key:
                                                    type: string
                                                    enum:
                                                      - x-vercel-ip-country
                                                  value:
                                                    properties:
                                                      eq:
                                                        type: string
                                                    required:
                                                      - eq
                                                    type: object
                                                required:
                                                  - key
                                                  - type
                                                  - value
                                                type: object
                                              - properties:
                                                  type:
                                                    type: string
                                                    enum:
                                                      - host
                                                  value:
                                                    properties:
                                                      eq:
                                                        type: string
                                                    required:
                                                      - eq
                                                    type: object
                                                required:
                                                  - type
                                                  - value
                                                type: object
                                          type: array
                                        mitigate:
                                          properties:
                                            action:
                                              type: string
                                              enum:
                                                - block_legal_cwc
                                          required:
                                            - action
                                          type: object
                                        src:
                                          type: string
                                      required:
                                        - has
                                        - mitigate
                                      type: object
                                statusCode:
                                  type: number
                                createdAt:
                                  type: number
                                caseId:
                                  type: string
                                actor:
                                  type: string
                                comment:
                                  type: string
                                ineligibleForAppeal:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                isCascading:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                              required:
                                - action
                                - createdAt
                                - route
                              type: object
                        type: array
                      interstitial:
                        type: boolean
                        enum:
                          - false
                          - true
                    required:
                      - history
                      - updatedAt
                    type: object
                  internalRoutes:
                    items:
                      oneOf:
                        - properties:
                            src:
                              type: string
                            status:
                              type: number
                          required:
                            - src
                            - status
                          type: object
                        - properties:
                            has:
                              items:
                                oneOf:
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - header
                                      key:
                                        type: string
                                        enum:
                                          - x-vercel-ip-country
                                      value:
                                        properties:
                                          eq:
                                            type: string
                                        required:
                                          - eq
                                        type: object
                                    required:
                                      - key
                                      - type
                                      - value
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - host
                                      value:
                                        properties:
                                          eq:
                                            type: string
                                        required:
                                          - eq
                                        type: object
                                    required:
                                      - type
                                      - value
                                    type: object
                              type: array
                            mitigate:
                              properties:
                                action:
                                  type: string
                                  enum:
                                    - block_legal_cwc
                              required:
                                - action
                              type: object
                            src:
                              type: string
                          required:
                            - has
                            - mitigate
                          type: object
                    type: array
                  hasDeployments:
                    type: boolean
                    enum:
                      - false
                      - true
                  dismissedToasts:
                    items:
                      properties:
                        key:
                          type: string
                        dismissedAt:
                          type: number
                        action:
                          type: string
                          enum:
                            - delete
                            - cancel
                            - accept
                        value:
                          nullable: true
                          oneOf:
                            - type: string
                            - type: number
                            - properties:
                                previousValue:
                                  oneOf:
                                    - type: string
                                    - type: number
                                    - type: boolean
                                      enum:
                                        - false
                                        - true
                                currentValue:
                                  oneOf:
                                    - type: string
                                    - type: number
                                    - type: boolean
                                      enum:
                                        - false
                                        - true
                              required:
                                - currentValue
                                - previousValue
                              type: object
                            - type: boolean
                              enum:
                                - false
                                - true
                      required:
                        - action
                        - dismissedAt
                        - key
                        - value
                      type: object
                    type: array
                  protectedSourcemaps:
                    type: boolean
                    enum:
                      - false
                      - true
                required:
                  - accountId
                  - defaultResourceConfig
                  - directoryListing
                  - id
                  - name
                  - nodeVersion
                  - resourceConfig
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  schemas:
    ACLAction:
      type: string
      enum:
        - create
        - delete
        - read
        - update
        - list
      description: >-
        Enum containing the actions that can be performed against a resource.
        Group operations are included.
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````