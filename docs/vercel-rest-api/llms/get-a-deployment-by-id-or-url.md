# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/get-a-deployment-by-id-or-url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a deployment by ID or URL

> Retrieves information for a deployment either by supplying its ID (`id` property) or Hostname (`url` property). Additional details will be included when the authenticated user or team is an owner of the deployment.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v13/deployments/{idOrUrl}
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
  /v13/deployments/{idOrUrl}:
    get:
      tags:
        - deployments
      summary: Get a deployment by ID or URL
      description: >-
        Retrieves information for a deployment either by supplying its ID (`id`
        property) or Hostname (`url` property). Additional details will be
        included when the authenticated user or team is an owner of the
        deployment.
      operationId: getDeployment
      parameters:
        - name: idOrUrl
          description: The unique identifier or hostname of the deployment.
          in: path
          required: true
          schema:
            example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
            description: The unique identifier or hostname of the deployment.
            type: string
        - name: withGitRepoInfo
          description: Whether to add in gitRepo information.
          in: query
          required: false
          schema:
            description: Whether to add in gitRepo information.
            type: string
            example: 'true'
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
          description: |-
            The deployment including only public information
            The deployment including both public and private information
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
                      aliasAssignedAt:
                        nullable: true
                        oneOf:
                          - type: number
                          - type: boolean
                            enum:
                              - false
                              - true
                      alwaysRefuseToBuild:
                        type: boolean
                        enum:
                          - false
                          - true
                      build:
                        properties:
                          env:
                            items:
                              type: string
                            type: array
                        required:
                          - env
                        type: object
                      buildArtifactUrls:
                        items:
                          type: string
                        type: array
                      builds:
                        items:
                          properties:
                            use:
                              type: string
                            src:
                              type: string
                            config:
                              additionalProperties: true
                              type: object
                          required:
                            - use
                          type: object
                        type: array
                      env:
                        items:
                          type: string
                        type: array
                      inspectorUrl:
                        nullable: true
                        type: string
                      isInConcurrentBuildsQueue:
                        type: boolean
                        enum:
                          - false
                          - true
                      isInSystemBuildsQueue:
                        type: boolean
                        enum:
                          - false
                          - true
                      projectSettings:
                        properties:
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
                          buildCommand:
                            nullable: true
                            type: string
                          devCommand:
                            nullable: true
                            type: string
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
                          commandForIgnoringBuildStep:
                            nullable: true
                            type: string
                          installCommand:
                            nullable: true
                            type: string
                          outputDirectory:
                            nullable: true
                            type: string
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
                        type: object
                      readyStateReason:
                        type: string
                      integrations:
                        properties:
                          status:
                            type: string
                            enum:
                              - skipped
                              - pending
                              - ready
                              - error
                              - timeout
                          startedAt:
                            type: number
                          completedAt:
                            type: number
                          skippedAt:
                            type: number
                          skippedBy:
                            type: string
                        required:
                          - startedAt
                          - status
                        type: object
                      images:
                        properties:
                          sizes:
                            items:
                              type: number
                            type: array
                          qualities:
                            items:
                              type: number
                            type: array
                          domains:
                            items:
                              type: string
                            type: array
                          remotePatterns:
                            items:
                              properties:
                                protocol:
                                  type: string
                                  enum:
                                    - http
                                    - https
                                  description: Must be `http` or `https`.
                                hostname:
                                  type: string
                                  description: >-
                                    Can be literal or wildcard. Single `*`
                                    matches a single subdomain. Double `**`
                                    matches any number of subdomains.
                                port:
                                  type: string
                                  description: >-
                                    Can be literal port such as `8080` or empty
                                    string meaning no port.
                                pathname:
                                  type: string
                                  description: >-
                                    Can be literal or wildcard. Single `*`
                                    matches a single path segment. Double `**`
                                    matches any number of path segments.
                                search:
                                  type: string
                                  description: >-
                                    Can be literal query string such as `?v=1`
                                    or empty string meaning no query string.
                              required:
                                - hostname
                              type: object
                            type: array
                          localPatterns:
                            items:
                              properties:
                                pathname:
                                  type: string
                                  description: >-
                                    Can be literal or wildcard. Single `*`
                                    matches a single path segment. Double `**`
                                    matches any number of path segments.
                                search:
                                  type: string
                                  description: >-
                                    Can be literal query string such as `?v=1`
                                    or empty string meaning no query string.
                              type: object
                            type: array
                          minimumCacheTTL:
                            type: number
                          formats:
                            items:
                              type: string
                              enum:
                                - image/avif
                                - image/webp
                            type: array
                          dangerouslyAllowSVG:
                            type: boolean
                            enum:
                              - false
                              - true
                          contentSecurityPolicy:
                            type: string
                          contentDispositionType:
                            type: string
                            enum:
                              - inline
                              - attachment
                        type: object
                      alias:
                        items:
                          type: string
                        type: array
                        description: >-
                          A list of all the aliases (default aliases, staging
                          aliases and production aliases) that were assigned
                          upon deployment creation
                        example: []
                      aliasAssigned:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          A boolean that will be true when the aliases from the
                          alias property were assigned successfully
                        example: true
                      bootedAt:
                        type: number
                      buildingAt:
                        type: number
                      buildContainerFinishedAt:
                        type: number
                        description: >-
                          Since April 2025 it necessary for On-Demand
                          Concurrency Minutes calculation
                      buildSkipped:
                        type: boolean
                        enum:
                          - false
                          - true
                      creator:
                        properties:
                          uid:
                            type: string
                            description: The ID of the user that created the deployment
                            example: 96SnxkFiMyVKsK3pnoHfx3Hz
                          username:
                            type: string
                            description: >-
                              The username of the user that created the
                              deployment
                            example: john-doe
                          avatar:
                            type: string
                            description: The avatar of the user that created the deployment
                        required:
                          - uid
                        type: object
                        description: Information about the deployment creator
                      initReadyAt:
                        type: number
                      isFirstBranchDeployment:
                        type: boolean
                        enum:
                          - false
                          - true
                      lambdas:
                        items:
                          properties:
                            id:
                              type: string
                            createdAt:
                              type: number
                            readyState:
                              type: string
                              enum:
                                - BUILDING
                                - ERROR
                                - INITIALIZING
                                - READY
                            entrypoint:
                              nullable: true
                              type: string
                            readyStateAt:
                              type: number
                            output:
                              items:
                                properties:
                                  path:
                                    type: string
                                  functionName:
                                    type: string
                                required:
                                  - functionName
                                  - path
                                type: object
                              type: array
                          required:
                            - id
                            - output
                          type: object
                          description: >-
                            A partial representation of a Build used by the
                            deployment endpoint.
                        type: array
                      public:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          A boolean representing if the deployment is public or
                          not. By default this is `false`
                        example: false
                      ready:
                        type: number
                      status:
                        type: string
                        enum:
                          - QUEUED
                          - BUILDING
                          - ERROR
                          - INITIALIZING
                          - READY
                          - CANCELED
                      team:
                        properties:
                          id:
                            type: string
                          name:
                            type: string
                          slug:
                            type: string
                          avatar:
                            type: string
                        required:
                          - id
                          - name
                          - slug
                        type: object
                        description: The team that owns the deployment if any
                      userAliases:
                        items:
                          type: string
                        type: array
                        description: >-
                          An array of domains that were provided by the user
                          when creating the Deployment.
                        example:
                          - sub1.example.com
                          - sub2.example.com
                      previewCommentsEnabled:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          Whether or not preview comments are enabled for the
                          deployment
                        example: false
                      ttyBuildLogs:
                        type: boolean
                        enum:
                          - false
                          - true
                      customEnvironment:
                        oneOf:
                          - properties:
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
                                  The type of environment (production, preview,
                                  or development)
                              description:
                                type: string
                                description: >-
                                  Optional description of the environment's
                                  purpose
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
                                  Configuration for matching git branches to
                                  this environment
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
                                        - 307
                                        - 301
                                        - 302
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
                                        `true` if the domain is verified for use
                                        with the project. If `false` it will not
                                        be used as an alias on this project
                                        until the challenge in `verification` is
                                        completed.
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
                                          A list of verification challenges, one
                                          of which must be completed to verify the
                                          domain for use on the project. After the
                                          challenge is complete `POST
                                          /projects/:idOrName/domains/:domain/verify`
                                          to verify the domain. Possible
                                          challenges: - If `verification.type =
                                          TXT` the `verification.domain` will be
                                          checked for a TXT record matching
                                          `verification.value`.
                                      type: array
                                      description: >-
                                        A list of verification challenges, one
                                        of which must be completed to verify the
                                        domain for use on the project. After the
                                        challenge is complete `POST
                                        /projects/:idOrName/domains/:domain/verify`
                                        to verify the domain. Possible
                                        challenges: - If `verification.type =
                                        TXT` the `verification.domain` will be
                                        checked for a TXT record matching
                                        `verification.value`.
                                  required:
                                    - apexName
                                    - name
                                    - projectId
                                    - verified
                                  type: object
                                  description: >-
                                    List of domains associated with this
                                    environment
                                type: array
                                description: >-
                                  List of domains associated with this
                                  environment
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
                                description: >-
                                  Timestamp when the environment was last
                                  updated
                            required:
                              - createdAt
                              - id
                              - slug
                              - type
                              - updatedAt
                            type: object
                            description: >-
                              If the deployment was created using a Custom
                              Environment, then this property contains
                              information regarding the environment used.
                          - properties:
                              id:
                                type: string
                            required:
                              - id
                            type: object
                            description: >-
                              If the deployment was created using a Custom
                              Environment, then this property contains
                              information regarding the environment used.
                      oomReport:
                        type: string
                        enum:
                          - out-of-memory
                      aliasWarning:
                        nullable: true
                        properties:
                          code:
                            type: string
                          message:
                            type: string
                          link:
                            type: string
                          action:
                            type: string
                        required:
                          - code
                          - message
                        type: object
                      id:
                        type: string
                        description: A string holding the unique ID of the deployment
                        example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                      createdAt:
                        type: number
                        description: >-
                          A number containing the date when the deployment was
                          created in milliseconds
                        example: 1540257589405
                      readyState:
                        type: string
                        enum:
                          - QUEUED
                          - BUILDING
                          - ERROR
                          - INITIALIZING
                          - READY
                          - CANCELED
                        description: >-
                          The state of the deployment depending on the process
                          of deploying, or if it is ready or in an error state
                        example: READY
                      name:
                        type: string
                        description: >-
                          The name of the project associated with the deployment
                          at the time that the deployment was created
                        example: my-project
                      type:
                        type: string
                        enum:
                          - LAMBDAS
                      aliasError:
                        nullable: true
                        properties:
                          code:
                            type: string
                          message:
                            type: string
                        required:
                          - code
                          - message
                        type: object
                        description: >-
                          An object that will contain a `code` and a `message`
                          when the aliasing fails, otherwise the value will be
                          `null`
                        example: null
                      aliasFinal:
                        nullable: true
                        type: string
                      autoAssignCustomDomains:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: applies to custom domains only, defaults to `true`
                      automaticAliases:
                        items:
                          type: string
                        type: array
                      buildErrorAt:
                        type: number
                      checksState:
                        type: string
                        enum:
                          - registered
                          - running
                          - completed
                      checksConclusion:
                        type: string
                        enum:
                          - succeeded
                          - failed
                          - skipped
                          - canceled
                      deletedAt:
                        nullable: true
                        type: number
                        description: >-
                          A number containing the date when the deployment was
                          deleted at milliseconds
                        example: 1540257589405
                      defaultRoute:
                        type: string
                        description: >-
                          Computed field that is only available for deployments
                          with a microfrontend configuration.
                      canceledAt:
                        type: number
                      errorCode:
                        type: string
                      errorLink:
                        type: string
                      errorMessage:
                        nullable: true
                        type: string
                      errorStep:
                        type: string
                      passiveRegions:
                        items:
                          type: string
                        type: array
                        description: >-
                          Since November 2023 this field defines a set of
                          regions that we will deploy the lambda to passively
                          Lambdas will be deployed to these regions but only
                          invoked if all of the primary `regions` are marked as
                          out of service
                      gitSource:
                        oneOf:
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github
                              repoId:
                                oneOf:
                                  - type: string
                                  - type: number
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - repoId
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github
                              org:
                                type: string
                              repo:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - org
                              - repo
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-custom-host
                              host:
                                type: string
                              repoId:
                                oneOf:
                                  - type: string
                                  - type: number
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - host
                              - repoId
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-custom-host
                              host:
                                type: string
                              org:
                                type: string
                              repo:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - host
                              - org
                              - repo
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-limited
                              repoId:
                                oneOf:
                                  - type: string
                                  - type: number
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - repoId
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-limited
                              org:
                                type: string
                              repo:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - org
                              - repo
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - gitlab
                              projectId:
                                oneOf:
                                  - type: string
                                  - type: number
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - projectId
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - bitbucket
                              workspaceUuid:
                                type: string
                              repoUuid:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - repoUuid
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - bitbucket
                              owner:
                                type: string
                              slug:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - owner
                              - slug
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - custom
                              ref:
                                type: string
                              sha:
                                type: string
                              gitUrl:
                                type: string
                            required:
                              - gitUrl
                              - ref
                              - sha
                              - type
                            type: object
                            description: >-
                              Allows custom git sources (local folder mounted to
                              the container) in test mode
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github
                              ref:
                                type: string
                              sha:
                                type: string
                              repoId:
                                type: number
                              org:
                                type: string
                              repo:
                                type: string
                            required:
                              - ref
                              - repoId
                              - sha
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-custom-host
                              host:
                                type: string
                              ref:
                                type: string
                              sha:
                                type: string
                              repoId:
                                type: number
                              org:
                                type: string
                              repo:
                                type: string
                            required:
                              - host
                              - ref
                              - repoId
                              - sha
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-limited
                              ref:
                                type: string
                              sha:
                                type: string
                              repoId:
                                type: number
                              org:
                                type: string
                              repo:
                                type: string
                            required:
                              - ref
                              - repoId
                              - sha
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - gitlab
                              ref:
                                type: string
                              sha:
                                type: string
                              projectId:
                                type: number
                            required:
                              - projectId
                              - ref
                              - sha
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - bitbucket
                              ref:
                                type: string
                              sha:
                                type: string
                              owner:
                                type: string
                              slug:
                                type: string
                              workspaceUuid:
                                type: string
                              repoUuid:
                                type: string
                            required:
                              - ref
                              - repoUuid
                              - sha
                              - type
                              - workspaceUuid
                            type: object
                      manualProvisioning:
                        properties:
                          state:
                            type: string
                            enum:
                              - PENDING
                              - COMPLETE
                              - TIMEOUT
                            description: Current provisioning state
                          completedAt:
                            type: number
                            description: Timestamp when manual provisioning completed
                        required:
                          - state
                        type: object
                        description: >-
                          Present when deployment was created with
                          VERCEL_MANUAL_PROVISIONING=true. The deployment stays
                          in INITIALIZING until /continue is called.
                      meta:
                        additionalProperties:
                          type: string
                        type: object
                      originCacheRegion:
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
                        description: >-
                          If set it overrides the `projectSettings.nodeVersion`
                          for this deployment.
                      project:
                        properties:
                          id:
                            type: string
                          name:
                            type: string
                          framework:
                            nullable: true
                            type: string
                        required:
                          - id
                          - name
                        type: object
                        description: >-
                          The public project information associated with the
                          deployment.
                      prebuilt:
                        type: boolean
                        enum:
                          - false
                          - true
                      readySubstate:
                        type: string
                        enum:
                          - STAGED
                          - ROLLING
                          - PROMOTED
                        description: >-
                          Substate of deployment when readyState is 'READY'
                          Tracks whether or not deployment has seen production
                          traffic: - STAGED: never seen production traffic -
                          ROLLING: in the process of having production traffic
                          gradually transitioned. - PROMOTED: has seen
                          production traffic
                      regions:
                        items:
                          type: string
                        type: array
                        description: The regions the deployment exists in
                        example:
                          - sfo1
                      softDeletedByRetention:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          flag to indicate if the deployment was deleted by
                          retention policy
                        example: 'true'
                      source:
                        type: string
                        enum:
                          - api-trigger-git-deploy
                          - cli
                          - clone/repo
                          - git
                          - import
                          - import/repo
                          - redeploy
                          - v0-web
                        description: Where was the deployment created from
                        example: cli
                      target:
                        nullable: true
                        type: string
                        enum:
                          - staging
                          - production
                        description: >-
                          If defined, either `staging` if a staging alias in the
                          format `<project>.<team>.now.sh` was assigned upon
                          creation, or `production` if the aliases from `alias`
                          were assigned. `null` value indicates the "preview"
                          deployment.
                        example: null
                      undeletedAt:
                        type: number
                        description: >-
                          A number containing the date when the deployment was
                          undeleted at milliseconds
                        example: 1540257589405
                      url:
                        type: string
                        description: A string with the unique URL of the deployment
                        example: my-instant-deployment-3ij3cxz9qr.now.sh
                      userConfiguredDeploymentId:
                        type: string
                        description: >-
                          Since January 2025 User-configured deployment ID for
                          skew protection with pre-built deployments. This is
                          set when users configure a custom deploymentId in
                          their next.config.js file. This allows Next.js to use
                          skew protection even when deployments are pre-built
                          outside of Vercel's build system.
                        example: abc123
                      version:
                        type: number
                        enum:
                          - 2
                        description: >-
                          The platform version that was used to create the
                          deployment.
                        example: 2
                      oidcTokenClaims:
                        properties:
                          iss:
                            type: string
                          sub:
                            type: string
                          scope:
                            type: string
                          aud:
                            type: string
                          owner:
                            type: string
                          owner_id:
                            type: string
                          project:
                            type: string
                          project_id:
                            type: string
                          environment:
                            type: string
                          plan:
                            type: string
                        required:
                          - aud
                          - environment
                          - iss
                          - owner
                          - owner_id
                          - project
                          - project_id
                          - scope
                          - sub
                        type: object
                      projectId:
                        type: string
                      plan:
                        type: string
                        enum:
                          - pro
                          - enterprise
                          - hobby
                      connectBuildsEnabled:
                        type: boolean
                        enum:
                          - false
                          - true
                      connectConfigurationId:
                        type: string
                      createdIn:
                        type: string
                      crons:
                        items:
                          properties:
                            schedule:
                              type: string
                            path:
                              type: string
                          required:
                            - path
                            - schedule
                          type: object
                        type: array
                      functions:
                        nullable: true
                        additionalProperties:
                          properties:
                            architecture:
                              type: string
                              enum:
                                - x86_64
                                - arm64
                            memory:
                              type: number
                            maxDuration:
                              type: number
                            runtime:
                              type: string
                            includeFiles:
                              type: string
                            excludeFiles:
                              type: string
                            experimentalTriggers:
                              items:
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - queue/v1beta
                                    description: >-
                                      Event type - must be "queue/v1beta"
                                      (REQUIRED)
                                  topic:
                                    type: string
                                    description: >-
                                      Name of the queue topic to consume from
                                      (REQUIRED)
                                  consumer:
                                    type: string
                                    description: >-
                                      Name of the consumer group for this
                                      trigger (REQUIRED)
                                  maxDeliveries:
                                    type: number
                                    description: >-
                                      Maximum number of delivery attempts for
                                      message processing (OPTIONAL) This
                                      represents the total number of times a
                                      message can be delivered, not the number
                                      of retries. Must be at least 1 if
                                      specified. Behavior when not specified
                                      depends on the server's default
                                      configuration.
                                  retryAfterSeconds:
                                    type: number
                                    description: >-
                                      Delay in seconds before retrying failed
                                      executions (OPTIONAL) Behavior when not
                                      specified depends on the server's default
                                      configuration.
                                  initialDelaySeconds:
                                    type: number
                                    description: >-
                                      Initial delay in seconds before first
                                      execution attempt (OPTIONAL) Must be 0 or
                                      greater. Use 0 for no initial delay.
                                      Behavior when not specified depends on the
                                      server's default configuration.
                                  maxConcurrency:
                                    type: number
                                    description: >-
                                      Maximum number of concurrent executions
                                      for this consumer (OPTIONAL) Must be at
                                      least 1 if specified. Behavior when not
                                      specified depends on the server's default
                                      configuration.
                                required:
                                  - consumer
                                  - topic
                                  - type
                                type: object
                                description: >-
                                  Queue trigger event for Vercel's queue system.
                                  Handles "queue/v1beta" events with
                                  queue-specific configuration.
                              type: array
                            supportsCancellation:
                              type: boolean
                              enum:
                                - false
                                - true
                          type: object
                        type: object
                      monorepoManager:
                        nullable: true
                        type: string
                      ownerId:
                        type: string
                      passiveConnectConfigurationId:
                        type: string
                        description: >-
                          Since November 2023 this field defines a Secure
                          Compute network that will only be used to deploy
                          passive lambdas to (as in passiveRegions)
                      routes:
                        nullable: true
                        items:
                          oneOf:
                            - properties:
                                src:
                                  type: string
                                dest:
                                  type: string
                                headers:
                                  additionalProperties:
                                    type: string
                                  type: object
                                methods:
                                  items:
                                    type: string
                                  type: array
                                continue:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                override:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                caseSensitive:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                check:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                important:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                status:
                                  type: number
                                has:
                                  items:
                                    oneOf:
                                      - properties:
                                          type:
                                            type: string
                                            enum:
                                              - host
                                          value:
                                            oneOf:
                                              - type: string
                                              - properties:
                                                  eq:
                                                    oneOf:
                                                      - type: string
                                                      - type: number
                                                  neq:
                                                    type: string
                                                  inc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  ninc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  pre:
                                                    type: string
                                                  suf:
                                                    type: string
                                                  re:
                                                    type: string
                                                  gt:
                                                    type: number
                                                  gte:
                                                    type: number
                                                  lt:
                                                    type: number
                                                  lte:
                                                    type: number
                                                type: object
                                        required:
                                          - type
                                          - value
                                        type: object
                                      - properties:
                                          type:
                                            type: string
                                            enum:
                                              - header
                                              - cookie
                                              - query
                                          key:
                                            type: string
                                          value:
                                            oneOf:
                                              - type: string
                                              - properties:
                                                  eq:
                                                    oneOf:
                                                      - type: string
                                                      - type: number
                                                  neq:
                                                    type: string
                                                  inc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  ninc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  pre:
                                                    type: string
                                                  suf:
                                                    type: string
                                                  re:
                                                    type: string
                                                  gt:
                                                    type: number
                                                  gte:
                                                    type: number
                                                  lt:
                                                    type: number
                                                  lte:
                                                    type: number
                                                type: object
                                        required:
                                          - key
                                          - type
                                        type: object
                                  type: array
                                missing:
                                  items:
                                    oneOf:
                                      - properties:
                                          type:
                                            type: string
                                            enum:
                                              - host
                                          value:
                                            oneOf:
                                              - type: string
                                              - properties:
                                                  eq:
                                                    oneOf:
                                                      - type: string
                                                      - type: number
                                                  neq:
                                                    type: string
                                                  inc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  ninc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  pre:
                                                    type: string
                                                  suf:
                                                    type: string
                                                  re:
                                                    type: string
                                                  gt:
                                                    type: number
                                                  gte:
                                                    type: number
                                                  lt:
                                                    type: number
                                                  lte:
                                                    type: number
                                                type: object
                                        required:
                                          - type
                                          - value
                                        type: object
                                      - properties:
                                          type:
                                            type: string
                                            enum:
                                              - header
                                              - cookie
                                              - query
                                          key:
                                            type: string
                                          value:
                                            oneOf:
                                              - type: string
                                              - properties:
                                                  eq:
                                                    oneOf:
                                                      - type: string
                                                      - type: number
                                                  neq:
                                                    type: string
                                                  inc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  ninc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  pre:
                                                    type: string
                                                  suf:
                                                    type: string
                                                  re:
                                                    type: string
                                                  gt:
                                                    type: number
                                                  gte:
                                                    type: number
                                                  lt:
                                                    type: number
                                                  lte:
                                                    type: number
                                                type: object
                                        required:
                                          - key
                                          - type
                                        type: object
                                  type: array
                                mitigate:
                                  properties:
                                    action:
                                      type: string
                                      enum:
                                        - challenge
                                        - deny
                                  required:
                                    - action
                                  type: object
                                transforms:
                                  items:
                                    properties:
                                      type:
                                        type: string
                                        enum:
                                          - request.headers
                                          - request.query
                                          - response.headers
                                      op:
                                        type: string
                                        enum:
                                          - append
                                          - set
                                          - delete
                                      target:
                                        properties:
                                          key:
                                            oneOf:
                                              - type: string
                                              - properties:
                                                  eq:
                                                    oneOf:
                                                      - type: string
                                                      - type: number
                                                  neq:
                                                    type: string
                                                  inc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  ninc:
                                                    items:
                                                      type: string
                                                    type: array
                                                  pre:
                                                    type: string
                                                  suf:
                                                    type: string
                                                  gt:
                                                    type: number
                                                  gte:
                                                    type: number
                                                  lt:
                                                    type: number
                                                  lte:
                                                    type: number
                                                type: object
                                        required:
                                          - key
                                        type: object
                                      args:
                                        oneOf:
                                          - type: string
                                          - items:
                                              type: string
                                            type: array
                                      env:
                                        items:
                                          type: string
                                        type: array
                                    required:
                                      - op
                                      - target
                                      - type
                                    type: object
                                  type: array
                                env:
                                  items:
                                    type: string
                                  type: array
                                locale:
                                  properties:
                                    redirect:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    cookie:
                                      type: string
                                  type: object
                                middlewarePath:
                                  type: string
                                  description: >-
                                    A middleware key within the `output` key
                                    under the build result. Overrides a
                                    `middleware` definition.
                                middlewareRawSrc:
                                  items:
                                    type: string
                                  type: array
                                  description: The original middleware matchers.
                                middleware:
                                  type: number
                                  description: >-
                                    A middleware index in the `middleware` key
                                    under the build result
                                respectOriginCacheControl:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                              required:
                                - src
                              type: object
                            - properties:
                                handle:
                                  type: string
                                  enum:
                                    - error
                                    - filesystem
                                    - hit
                                    - miss
                                    - rewrite
                                    - resource
                                src:
                                  type: string
                                dest:
                                  type: string
                                status:
                                  type: number
                              required:
                                - handle
                              type: object
                            - properties:
                                src:
                                  type: string
                                continue:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                middleware:
                                  type: number
                                  enum:
                                    - 0
                              required:
                                - continue
                                - middleware
                                - src
                              type: object
                        type: array
                      gitRepo:
                        nullable: true
                        oneOf:
                          - properties:
                              namespace:
                                type: string
                              projectId:
                                type: number
                              type:
                                type: string
                                enum:
                                  - gitlab
                              url:
                                type: string
                              path:
                                type: string
                              defaultBranch:
                                type: string
                              name:
                                type: string
                              private:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              ownerType:
                                type: string
                                enum:
                                  - team
                                  - user
                            required:
                              - defaultBranch
                              - name
                              - namespace
                              - ownerType
                              - path
                              - private
                              - projectId
                              - type
                              - url
                            type: object
                          - properties:
                              org:
                                type: string
                              repo:
                                type: string
                              repoId:
                                type: number
                              type:
                                type: string
                                enum:
                                  - github
                              repoOwnerId:
                                type: number
                              path:
                                type: string
                              defaultBranch:
                                type: string
                              name:
                                type: string
                              private:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              ownerType:
                                type: string
                                enum:
                                  - team
                                  - user
                            required:
                              - defaultBranch
                              - name
                              - org
                              - ownerType
                              - path
                              - private
                              - repo
                              - repoId
                              - repoOwnerId
                              - type
                            type: object
                          - properties:
                              owner:
                                type: string
                              repoUuid:
                                type: string
                              slug:
                                type: string
                              type:
                                type: string
                                enum:
                                  - bitbucket
                              workspaceUuid:
                                type: string
                              path:
                                type: string
                              defaultBranch:
                                type: string
                              name:
                                type: string
                              private:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              ownerType:
                                type: string
                                enum:
                                  - team
                                  - user
                            required:
                              - defaultBranch
                              - name
                              - owner
                              - ownerType
                              - path
                              - private
                              - repoUuid
                              - slug
                              - type
                              - workspaceUuid
                            type: object
                      flags:
                        oneOf:
                          - properties:
                              definitions:
                                additionalProperties:
                                  properties:
                                    options:
                                      items:
                                        properties:
                                          value:
                                            $ref: '#/components/schemas/FlagJSONValue'
                                          label:
                                            type: string
                                        required:
                                          - value
                                        type: object
                                      type: array
                                    url:
                                      type: string
                                    description:
                                      type: string
                                  type: object
                                type: object
                            required:
                              - definitions
                            type: object
                            description: >-
                              Flags defined in the Build Output API, used by
                              this deployment. Primarily used by the Toolbar to
                              know about the used flags.
                          - items:
                              type: object
                              description: >-
                                Flags defined in the Build Output API, used by
                                this deployment. Primarily used by the Toolbar
                                to know about the used flags.
                            type: array
                            description: >-
                              Flags defined in the Build Output API, used by
                              this deployment. Primarily used by the Toolbar to
                              know about the used flags.
                      microfrontends:
                        oneOf:
                          - properties:
                              isDefaultApp:
                                type: boolean
                                enum:
                                  - false
                              defaultAppProjectName:
                                type: string
                                description: >-
                                  The project name of the default app of this
                                  deployment's microfrontends group.
                              defaultRoute:
                                type: string
                                description: >-
                                  A path that is used to take screenshots and as
                                  the default path in preview links when a
                                  domain for this microfrontend is shown in the
                                  UI.
                              groupIds:
                                type: array
                                items:
                                  type: string
                                minItems: 1
                                description: >-
                                  The group of microfrontends that this project
                                  belongs to. Each microfrontend project must
                                  belong to a microfrontends group that is the
                                  set of microfrontends that are used together.
                            required:
                              - defaultAppProjectName
                              - groupIds
                            type: object
                          - properties:
                              isDefaultApp:
                                type: boolean
                                enum:
                                  - true
                              mfeConfigUploadState:
                                type: string
                                enum:
                                  - success
                                  - waiting_on_build
                                  - no_config
                                description: >-
                                  The result of the microfrontends config upload
                                  during deployment creation / build. Only set
                                  for default app deployments. The config upload
                                  is attempted during deployment create, and
                                  then again during the build. If the config is
                                  not in the root directory, or the deployment
                                  is prebuilt, the config cannot be uploaded
                                  during deployment create. The upload during
                                  deployment build finds the config even if it's
                                  not in the root directory, as it has access to
                                  all files. Uploading the config during create
                                  is ideal, as then all child deployments are
                                  guaranteed to have access to the default app
                                  deployment config even if the default app has
                                  not yet started building. If the config is not
                                  uploaded, the child app will show as building
                                  until the config has been uploaded during the
                                  default app build. - `success` - The config
                                  was uploaded successfully, either when the
                                  deployment was created or during the build. -
                                  `waiting_on_build` - The config could not be
                                  uploaded during deployment create, will be
                                  attempted again during the build. -
                                  `no_config` - No config was found. Only set
                                  once the build has not found the config in any
                                  of the deployment's files. - `undefined` -
                                  Legacy deployments, or there was an error
                                  uploading the config during deployment create.
                              defaultAppProjectName:
                                type: string
                                description: >-
                                  The project name of the default app of this
                                  deployment's microfrontends group.
                              defaultRoute:
                                type: string
                                description: >-
                                  A path that is used to take screenshots and as
                                  the default path in preview links when a
                                  domain for this microfrontend is shown in the
                                  UI.
                              groupIds:
                                type: array
                                items:
                                  type: string
                                minItems: 1
                                description: >-
                                  The group of microfrontends that this project
                                  belongs to. Each microfrontend project must
                                  belong to a microfrontends group that is the
                                  set of microfrontends that are used together.
                            required:
                              - defaultAppProjectName
                              - groupIds
                              - isDefaultApp
                            type: object
                      config:
                        properties:
                          version:
                            type: number
                          functionType:
                            type: string
                            enum:
                              - standard
                              - fluid
                          functionMemoryType:
                            type: string
                            enum:
                              - standard
                              - standard_legacy
                              - performance
                          functionTimeout:
                            nullable: true
                            type: number
                          secureComputePrimaryRegion:
                            nullable: true
                            type: string
                          secureComputeFallbackRegion:
                            nullable: true
                            type: string
                          isUsingActiveCPU:
                            type: boolean
                            enum:
                              - false
                              - true
                          resourceConfig:
                            properties:
                              buildQueue:
                                properties:
                                  configuration:
                                    type: string
                                    enum:
                                      - SKIP_NAMESPACE_QUEUE
                                      - WAIT_FOR_NAMESPACE_QUEUE
                                    description: >-
                                      Build resource configuration snapshot for
                                      this deployment.
                                type: object
                                description: >-
                                  Build resource configuration snapshot for this
                                  deployment.
                              buildMachine:
                                properties:
                                  default:
                                    type: string
                                    enum:
                                      - enhanced
                                      - turbo
                                      - standard
                                    description: >-
                                      Build resource configuration snapshot for
                                      this deployment.
                                  purchaseType:
                                    type: string
                                    enum:
                                      - enhanced
                                      - turbo
                                    description: >-
                                      Build resource configuration snapshot for
                                      this deployment.
                                  isDefaultBuildMachine:
                                    type: boolean
                                    enum:
                                      - false
                                      - true
                                    description: >-
                                      Build resource configuration snapshot for
                                      this deployment.
                                  cores:
                                    type: number
                                    description: >-
                                      Build resource configuration snapshot for
                                      this deployment.
                                  memory:
                                    type: number
                                    description: >-
                                      Build resource configuration snapshot for
                                      this deployment.
                                type: object
                                description: >-
                                  Build resource configuration snapshot for this
                                  deployment.
                              elasticConcurrency:
                                type: string
                                enum:
                                  - TEAM_SETTING
                                  - PROJECT_SETTING
                                  - SKIP_QUEUE
                                description: >-
                                  When elastic concurrency is used for this
                                  deployment, a value is set. The value tells
                                  the reason where the setting was coming from.
                                  - TEAM_SETTING: Inherited from team settings -
                                  PROJECT_SETTING: Inherited from project
                                  settings - SKIP_QUEUE: Manually triggered by
                                  user to skip the queues
                            type: object
                            description: >-
                              Build resource configuration snapshot for this
                              deployment.
                        required:
                          - functionMemoryType
                          - functionTimeout
                          - functionType
                          - secureComputeFallbackRegion
                          - secureComputePrimaryRegion
                        type: object
                        description: >-
                          Since February 2025 the configuration must include
                          snapshot data at the time of deployment creation to
                          capture properties for the /deployments/:id/config
                          endpoint utilized for displaying Deployment
                          Configuration on the frontend This is optional because
                          older deployments may not have this data captured
                      checks:
                        properties:
                          deployment-alias:
                            properties:
                              state:
                                type: string
                                enum:
                                  - succeeded
                                  - failed
                                  - pending
                              startedAt:
                                type: number
                              completedAt:
                                type: number
                            required:
                              - startedAt
                              - state
                            type: object
                            description: >-
                              Condensed check data. Retrieve individual check
                              and check run data using api-checks v2 routes.
                        required:
                          - deployment-alias
                        type: object
                    required:
                      - aliasAssigned
                      - bootedAt
                      - build
                      - buildSkipped
                      - buildingAt
                      - createdAt
                      - createdIn
                      - creator
                      - env
                      - id
                      - inspectorUrl
                      - isInConcurrentBuildsQueue
                      - isInSystemBuildsQueue
                      - meta
                      - name
                      - ownerId
                      - plan
                      - projectId
                      - projectSettings
                      - public
                      - readyState
                      - regions
                      - routes
                      - status
                      - type
                      - url
                      - version
                    type: object
                    description: >-
                      The deployment including both public and private
                      information
                  - properties:
                      alias:
                        items:
                          type: string
                        type: array
                        description: >-
                          A list of all the aliases (default aliases, staging
                          aliases and production aliases) that were assigned
                          upon deployment creation
                        example: []
                      aliasAssigned:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          A boolean that will be true when the aliases from the
                          alias property were assigned successfully
                        example: true
                      bootedAt:
                        type: number
                      buildingAt:
                        type: number
                      buildContainerFinishedAt:
                        type: number
                        description: >-
                          Since April 2025 it necessary for On-Demand
                          Concurrency Minutes calculation
                      buildSkipped:
                        type: boolean
                        enum:
                          - false
                          - true
                      creator:
                        properties:
                          uid:
                            type: string
                            description: The ID of the user that created the deployment
                            example: 96SnxkFiMyVKsK3pnoHfx3Hz
                          username:
                            type: string
                            description: >-
                              The username of the user that created the
                              deployment
                            example: john-doe
                          avatar:
                            type: string
                            description: The avatar of the user that created the deployment
                        required:
                          - uid
                        type: object
                        description: Information about the deployment creator
                      initReadyAt:
                        type: number
                      isFirstBranchDeployment:
                        type: boolean
                        enum:
                          - false
                          - true
                      lambdas:
                        items:
                          properties:
                            id:
                              type: string
                            createdAt:
                              type: number
                            readyState:
                              type: string
                              enum:
                                - BUILDING
                                - ERROR
                                - INITIALIZING
                                - READY
                            entrypoint:
                              nullable: true
                              type: string
                            readyStateAt:
                              type: number
                            output:
                              items:
                                properties:
                                  path:
                                    type: string
                                  functionName:
                                    type: string
                                required:
                                  - functionName
                                  - path
                                type: object
                              type: array
                          required:
                            - id
                            - output
                          type: object
                          description: >-
                            A partial representation of a Build used by the
                            deployment endpoint.
                        type: array
                      public:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          A boolean representing if the deployment is public or
                          not. By default this is `false`
                        example: false
                      ready:
                        type: number
                      status:
                        type: string
                        enum:
                          - QUEUED
                          - BUILDING
                          - ERROR
                          - INITIALIZING
                          - READY
                          - CANCELED
                      team:
                        properties:
                          id:
                            type: string
                          name:
                            type: string
                          slug:
                            type: string
                          avatar:
                            type: string
                        required:
                          - id
                          - name
                          - slug
                        type: object
                        description: The team that owns the deployment if any
                      userAliases:
                        items:
                          type: string
                        type: array
                        description: >-
                          An array of domains that were provided by the user
                          when creating the Deployment.
                        example:
                          - sub1.example.com
                          - sub2.example.com
                      previewCommentsEnabled:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          Whether or not preview comments are enabled for the
                          deployment
                        example: false
                      ttyBuildLogs:
                        type: boolean
                        enum:
                          - false
                          - true
                      customEnvironment:
                        oneOf:
                          - properties:
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
                                  The type of environment (production, preview,
                                  or development)
                              description:
                                type: string
                                description: >-
                                  Optional description of the environment's
                                  purpose
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
                                  Configuration for matching git branches to
                                  this environment
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
                                        - 307
                                        - 301
                                        - 302
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
                                        `true` if the domain is verified for use
                                        with the project. If `false` it will not
                                        be used as an alias on this project
                                        until the challenge in `verification` is
                                        completed.
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
                                          A list of verification challenges, one
                                          of which must be completed to verify the
                                          domain for use on the project. After the
                                          challenge is complete `POST
                                          /projects/:idOrName/domains/:domain/verify`
                                          to verify the domain. Possible
                                          challenges: - If `verification.type =
                                          TXT` the `verification.domain` will be
                                          checked for a TXT record matching
                                          `verification.value`.
                                      type: array
                                      description: >-
                                        A list of verification challenges, one
                                        of which must be completed to verify the
                                        domain for use on the project. After the
                                        challenge is complete `POST
                                        /projects/:idOrName/domains/:domain/verify`
                                        to verify the domain. Possible
                                        challenges: - If `verification.type =
                                        TXT` the `verification.domain` will be
                                        checked for a TXT record matching
                                        `verification.value`.
                                  required:
                                    - apexName
                                    - name
                                    - projectId
                                    - verified
                                  type: object
                                  description: >-
                                    List of domains associated with this
                                    environment
                                type: array
                                description: >-
                                  List of domains associated with this
                                  environment
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
                                description: >-
                                  Timestamp when the environment was last
                                  updated
                            required:
                              - createdAt
                              - id
                              - slug
                              - type
                              - updatedAt
                            type: object
                            description: >-
                              If the deployment was created using a Custom
                              Environment, then this property contains
                              information regarding the environment used.
                          - properties:
                              id:
                                type: string
                            required:
                              - id
                            type: object
                            description: >-
                              If the deployment was created using a Custom
                              Environment, then this property contains
                              information regarding the environment used.
                      oomReport:
                        type: string
                        enum:
                          - out-of-memory
                      aliasWarning:
                        nullable: true
                        properties:
                          code:
                            type: string
                          message:
                            type: string
                          link:
                            type: string
                          action:
                            type: string
                        required:
                          - code
                          - message
                        type: object
                      id:
                        type: string
                        description: A string holding the unique ID of the deployment
                        example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                      createdAt:
                        type: number
                        description: >-
                          A number containing the date when the deployment was
                          created in milliseconds
                        example: 1540257589405
                      readyState:
                        type: string
                        enum:
                          - QUEUED
                          - BUILDING
                          - ERROR
                          - INITIALIZING
                          - READY
                          - CANCELED
                        description: >-
                          The state of the deployment depending on the process
                          of deploying, or if it is ready or in an error state
                        example: READY
                      name:
                        type: string
                        description: >-
                          The name of the project associated with the deployment
                          at the time that the deployment was created
                        example: my-project
                      type:
                        type: string
                        enum:
                          - LAMBDAS
                      aliasError:
                        nullable: true
                        properties:
                          code:
                            type: string
                          message:
                            type: string
                        required:
                          - code
                          - message
                        type: object
                        description: >-
                          An object that will contain a `code` and a `message`
                          when the aliasing fails, otherwise the value will be
                          `null`
                        example: null
                      aliasFinal:
                        nullable: true
                        type: string
                      autoAssignCustomDomains:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: applies to custom domains only, defaults to `true`
                      automaticAliases:
                        items:
                          type: string
                        type: array
                      buildErrorAt:
                        type: number
                      checksState:
                        type: string
                        enum:
                          - registered
                          - running
                          - completed
                      checksConclusion:
                        type: string
                        enum:
                          - succeeded
                          - failed
                          - skipped
                          - canceled
                      deletedAt:
                        nullable: true
                        type: number
                        description: >-
                          A number containing the date when the deployment was
                          deleted at milliseconds
                        example: 1540257589405
                      defaultRoute:
                        type: string
                        description: >-
                          Computed field that is only available for deployments
                          with a microfrontend configuration.
                      canceledAt:
                        type: number
                      errorCode:
                        type: string
                      errorLink:
                        type: string
                      errorMessage:
                        nullable: true
                        type: string
                      errorStep:
                        type: string
                      passiveRegions:
                        items:
                          type: string
                        type: array
                        description: >-
                          Since November 2023 this field defines a set of
                          regions that we will deploy the lambda to passively
                          Lambdas will be deployed to these regions but only
                          invoked if all of the primary `regions` are marked as
                          out of service
                      gitSource:
                        oneOf:
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github
                              repoId:
                                oneOf:
                                  - type: string
                                  - type: number
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - repoId
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github
                              org:
                                type: string
                              repo:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - org
                              - repo
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-custom-host
                              host:
                                type: string
                              repoId:
                                oneOf:
                                  - type: string
                                  - type: number
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - host
                              - repoId
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-custom-host
                              host:
                                type: string
                              org:
                                type: string
                              repo:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - host
                              - org
                              - repo
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-limited
                              repoId:
                                oneOf:
                                  - type: string
                                  - type: number
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - repoId
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-limited
                              org:
                                type: string
                              repo:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - org
                              - repo
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - gitlab
                              projectId:
                                oneOf:
                                  - type: string
                                  - type: number
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - projectId
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - bitbucket
                              workspaceUuid:
                                type: string
                              repoUuid:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - repoUuid
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - bitbucket
                              owner:
                                type: string
                              slug:
                                type: string
                              ref:
                                nullable: true
                                type: string
                              sha:
                                type: string
                              prId:
                                nullable: true
                                type: number
                            required:
                              - owner
                              - slug
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - custom
                              ref:
                                type: string
                              sha:
                                type: string
                              gitUrl:
                                type: string
                            required:
                              - gitUrl
                              - ref
                              - sha
                              - type
                            type: object
                            description: >-
                              Allows custom git sources (local folder mounted to
                              the container) in test mode
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github
                              ref:
                                type: string
                              sha:
                                type: string
                              repoId:
                                type: number
                              org:
                                type: string
                              repo:
                                type: string
                            required:
                              - ref
                              - repoId
                              - sha
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-custom-host
                              host:
                                type: string
                              ref:
                                type: string
                              sha:
                                type: string
                              repoId:
                                type: number
                              org:
                                type: string
                              repo:
                                type: string
                            required:
                              - host
                              - ref
                              - repoId
                              - sha
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - github-limited
                              ref:
                                type: string
                              sha:
                                type: string
                              repoId:
                                type: number
                              org:
                                type: string
                              repo:
                                type: string
                            required:
                              - ref
                              - repoId
                              - sha
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - gitlab
                              ref:
                                type: string
                              sha:
                                type: string
                              projectId:
                                type: number
                            required:
                              - projectId
                              - ref
                              - sha
                              - type
                            type: object
                          - properties:
                              type:
                                type: string
                                enum:
                                  - bitbucket
                              ref:
                                type: string
                              sha:
                                type: string
                              owner:
                                type: string
                              slug:
                                type: string
                              workspaceUuid:
                                type: string
                              repoUuid:
                                type: string
                            required:
                              - ref
                              - repoUuid
                              - sha
                              - type
                              - workspaceUuid
                            type: object
                      manualProvisioning:
                        properties:
                          state:
                            type: string
                            enum:
                              - PENDING
                              - COMPLETE
                              - TIMEOUT
                            description: Current provisioning state
                          completedAt:
                            type: number
                            description: Timestamp when manual provisioning completed
                        required:
                          - state
                        type: object
                        description: >-
                          Present when deployment was created with
                          VERCEL_MANUAL_PROVISIONING=true. The deployment stays
                          in INITIALIZING until /continue is called.
                      meta:
                        additionalProperties:
                          type: string
                        type: object
                      originCacheRegion:
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
                        description: >-
                          If set it overrides the `projectSettings.nodeVersion`
                          for this deployment.
                      project:
                        properties:
                          id:
                            type: string
                          name:
                            type: string
                          framework:
                            nullable: true
                            type: string
                        required:
                          - id
                          - name
                        type: object
                        description: >-
                          The public project information associated with the
                          deployment.
                      prebuilt:
                        type: boolean
                        enum:
                          - false
                          - true
                      readySubstate:
                        type: string
                        enum:
                          - STAGED
                          - ROLLING
                          - PROMOTED
                        description: >-
                          Substate of deployment when readyState is 'READY'
                          Tracks whether or not deployment has seen production
                          traffic: - STAGED: never seen production traffic -
                          ROLLING: in the process of having production traffic
                          gradually transitioned. - PROMOTED: has seen
                          production traffic
                      regions:
                        items:
                          type: string
                        type: array
                        description: The regions the deployment exists in
                        example:
                          - sfo1
                      softDeletedByRetention:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          flag to indicate if the deployment was deleted by
                          retention policy
                        example: 'true'
                      source:
                        type: string
                        enum:
                          - api-trigger-git-deploy
                          - cli
                          - clone/repo
                          - git
                          - import
                          - import/repo
                          - redeploy
                          - v0-web
                        description: Where was the deployment created from
                        example: cli
                      target:
                        nullable: true
                        type: string
                        enum:
                          - staging
                          - production
                        description: >-
                          If defined, either `staging` if a staging alias in the
                          format `<project>.<team>.now.sh` was assigned upon
                          creation, or `production` if the aliases from `alias`
                          were assigned. `null` value indicates the "preview"
                          deployment.
                        example: null
                      undeletedAt:
                        type: number
                        description: >-
                          A number containing the date when the deployment was
                          undeleted at milliseconds
                        example: 1540257589405
                      url:
                        type: string
                        description: A string with the unique URL of the deployment
                        example: my-instant-deployment-3ij3cxz9qr.now.sh
                      userConfiguredDeploymentId:
                        type: string
                        description: >-
                          Since January 2025 User-configured deployment ID for
                          skew protection with pre-built deployments. This is
                          set when users configure a custom deploymentId in
                          their next.config.js file. This allows Next.js to use
                          skew protection even when deployments are pre-built
                          outside of Vercel's build system.
                        example: abc123
                      version:
                        type: number
                        enum:
                          - 2
                        description: >-
                          The platform version that was used to create the
                          deployment.
                        example: 2
                      oidcTokenClaims:
                        properties:
                          iss:
                            type: string
                          sub:
                            type: string
                          scope:
                            type: string
                          aud:
                            type: string
                          owner:
                            type: string
                          owner_id:
                            type: string
                          project:
                            type: string
                          project_id:
                            type: string
                          environment:
                            type: string
                          plan:
                            type: string
                        required:
                          - aud
                          - environment
                          - iss
                          - owner
                          - owner_id
                          - project
                          - project_id
                          - scope
                          - sub
                        type: object
                    required:
                      - aliasAssigned
                      - bootedAt
                      - buildSkipped
                      - buildingAt
                      - createdAt
                      - creator
                      - id
                      - meta
                      - name
                      - public
                      - readyState
                      - regions
                      - status
                      - type
                      - url
                      - version
                    type: object
                    description: The deployment including only public information
        '400':
          description: One of the provided values in the request query is invalid.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: The deployment was not found
      security:
        - bearerToken: []
components:
  schemas:
    FlagJSONValue:
      nullable: true
      oneOf:
        - type: string
        - type: number
        - items:
            $ref: '#/components/schemas/FlagJSONValue'
          type: array
          description: >-
            TODO: The following types will eventually be exported by a more
            relevant package.
        - additionalProperties:
            $ref: '#/components/schemas/FlagJSONValue'
          type: object
        - type: boolean
          enum:
            - false
            - true
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````