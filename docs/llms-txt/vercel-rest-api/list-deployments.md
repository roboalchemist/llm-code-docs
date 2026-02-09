# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/list-deployments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List deployments

> List deployments under the authenticated user or team. If a deployment hasn't finished uploading (is incomplete), the `url` property will have a value of `null`.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/deployments
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
  /v6/deployments:
    get:
      tags:
        - deployments
      summary: List deployments
      description: >-
        List deployments under the authenticated user or team. If a deployment
        hasn't finished uploading (is incomplete), the `url` property will have
        a value of `null`.
      operationId: getDeployments
      parameters:
        - name: app
          description: Name of the deployment.
          in: query
          schema:
            description: Name of the deployment.
            type: string
            example: docs
        - name: from
          description: >-
            Gets the deployment created after this Date timestamp. (default:
            current time)
          in: query
          schema:
            description: >-
              Gets the deployment created after this Date timestamp. (default:
              current time)
            type: number
            example: 1612948664566
            deprecated: true
        - name: limit
          description: Maximum number of deployments to list from a request.
          in: query
          schema:
            description: Maximum number of deployments to list from a request.
            type: number
            example: 10
        - name: projectId
          description: Filter deployments from the given ID or name.
          in: query
          schema:
            description: Filter deployments from the given ID or name.
            type: string
            example: QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY
        - name: projectIds
          description: >-
            Filter deployments from the given project IDs. Cannot be used when
            projectId is specified.
          in: query
          schema:
            description: >-
              Filter deployments from the given project IDs. Cannot be used when
              projectId is specified.
            type: array
            items:
              type: string
            example:
              - prj_123
              - prj_456
            minItems: 1
            maxItems: 20
        - name: target
          description: Filter deployments based on the environment.
          in: query
          schema:
            description: Filter deployments based on the environment.
            type: string
            example: production
        - name: to
          description: >-
            Gets the deployment created before this Date timestamp. (default:
            current time)
          in: query
          schema:
            description: >-
              Gets the deployment created before this Date timestamp. (default:
              current time)
            type: number
            example: 1612948664566
            deprecated: true
        - name: users
          description: >-
            Filter out deployments based on users who have created the
            deployment.
          in: query
          schema:
            description: >-
              Filter out deployments based on users who have created the
              deployment.
            type: string
            example: kr1PsOIzqEL5Xg6M4VZcZosf,K4amb7K9dAt5R2vBJWF32bmY
        - name: since
          description: Get Deployments created after this JavaScript timestamp.
          in: query
          schema:
            description: Get Deployments created after this JavaScript timestamp.
            type: number
            example: 1540095775941
        - name: until
          description: Get Deployments created before this JavaScript timestamp.
          in: query
          schema:
            description: Get Deployments created before this JavaScript timestamp.
            type: number
            example: 1540095775951
        - name: state
          description: >-
            Filter deployments based on their state (`BUILDING`, `ERROR`,
            `INITIALIZING`, `QUEUED`, `READY`, `CANCELED`)
          in: query
          schema:
            description: >-
              Filter deployments based on their state (`BUILDING`, `ERROR`,
              `INITIALIZING`, `QUEUED`, `READY`, `CANCELED`)
            type: string
            example: BUILDING,READY
        - name: rollbackCandidate
          description: Filter deployments based on their rollback candidacy
          in: query
          schema:
            description: Filter deployments based on their rollback candidacy
            type: boolean
        - name: branch
          description: Filter deployments based on the branch name
          in: query
          schema:
            description: Filter deployments based on the branch name
            type: string
        - name: sha
          description: Filter deployments based on the SHA
          in: query
          schema:
            description: Filter deployments based on the SHA
            type: string
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
          description: ''
          content:
            application/json:
              schema:
                properties:
                  pagination:
                    $ref: '#/components/schemas/Pagination'
                  deployments:
                    items:
                      properties:
                        uid:
                          type: string
                          description: The unique identifier of the deployment.
                          example: dpl_2euZBFqxYdDMDG1jTrHFnNZ2eUVa
                        name:
                          type: string
                          description: The name of the deployment.
                          example: docs
                        projectId:
                          type: string
                          description: The project ID of the deployment
                        url:
                          type: string
                          description: The URL of the deployment.
                          example: docs-9jaeg38me.vercel.app
                        created:
                          type: number
                          description: Timestamp of when the deployment got created.
                          example: 1609492210000
                        defaultRoute:
                          type: string
                          description: >-
                            The default route that should be used for
                            screenshots and links if configured with
                            microfrontends.
                          example: /docs
                        deleted:
                          type: number
                          description: Timestamp of when the deployment got deleted.
                          example: 1609492210000
                        undeleted:
                          type: number
                          description: Timestamp of when the deployment was undeleted.
                          example: 1609492210000
                        softDeletedByRetention:
                          type: boolean
                          enum:
                            - false
                            - true
                          description: >-
                            Optional flag to indicate if the deployment was soft
                            deleted by retention policy.
                          example: true
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
                          description: The source of the deployment.
                          example: cli
                        state:
                          type: string
                          enum:
                            - BUILDING
                            - ERROR
                            - INITIALIZING
                            - QUEUED
                            - READY
                            - CANCELED
                            - DELETED
                          description: In which state is the deployment.
                          example: READY
                        readyState:
                          type: string
                          enum:
                            - BUILDING
                            - ERROR
                            - INITIALIZING
                            - QUEUED
                            - READY
                            - CANCELED
                            - DELETED
                          description: In which state is the deployment.
                          example: READY
                        type:
                          type: string
                          enum:
                            - LAMBDAS
                          description: The type of the deployment.
                          example: LAMBDAS
                        creator:
                          properties:
                            uid:
                              type: string
                              description: The unique identifier of the user.
                              example: eLrCnEgbKhsHyfbiNR7E8496
                            email:
                              type: string
                              description: The email address of the user.
                              example: example@example.com
                            username:
                              type: string
                              description: The username of the user.
                              example: johndoe
                            githubLogin:
                              type: string
                              description: The GitHub login of the user.
                              example: johndoe
                            gitlabLogin:
                              type: string
                              description: The GitLab login of the user.
                              example: johndoe
                          required:
                            - uid
                          type: object
                          description: >-
                            Metadata information of the user who created the
                            deployment.
                        meta:
                          additionalProperties:
                            type: string
                            description: Metadata information from the Git provider.
                          type: object
                          description: Metadata information from the Git provider.
                        target:
                          nullable: true
                          type: string
                          enum:
                            - production
                            - staging
                          description: >-
                            On which environment has the deployment been
                            deployed to.
                          example: production
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
                            An error object in case aliasing of the deployment
                            failed.
                        aliasAssigned:
                          nullable: true
                          oneOf:
                            - type: number
                            - type: boolean
                              enum:
                                - false
                                - true
                        createdAt:
                          type: number
                          description: Timestamp of when the deployment got created.
                          example: 1609492210000
                        buildingAt:
                          type: number
                          description: >-
                            Timestamp of when the deployment started building
                            at.
                          example: 1609492210000
                        ready:
                          type: number
                          description: Timestamp of when the deployment got ready.
                          example: 1609492210000
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
                            ROLLING: in the process of gradually transitioning
                            production traffic - PROMOTED: has seen production
                            traffic
                        checksState:
                          type: string
                          enum:
                            - registered
                            - running
                            - completed
                          description: State of all registered checks
                        checksConclusion:
                          type: string
                          enum:
                            - succeeded
                            - failed
                            - skipped
                            - canceled
                          description: Conclusion for checks
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
                                Detailed information about v2 deployment checks.
                                Includes information about blocked workflows in
                                the deployment lifecycle.
                          required:
                            - deployment-alias
                          type: object
                          description: >-
                            Detailed information about v2 deployment checks.
                            Includes information about blocked workflows in the
                            deployment lifecycle.
                        inspectorUrl:
                          nullable: true
                          type: string
                          description: Vercel URL to inspect the deployment.
                          example: >-
                            https://vercel.com/acme/nextjs/J1hXN00qjUeoYfpEEf7dnDtpSiVq
                        errorCode:
                          type: string
                          description: Error code when the deployment is in an error state.
                          example: BUILD_FAILED
                        errorMessage:
                          nullable: true
                          type: string
                          description: >-
                            Error message when the deployment is in an canceled
                            or error state.
                          example: >-
                            The Deployment has been canceled because this
                            project was not affected
                        oomReport:
                          type: string
                          enum:
                            - out-of-memory
                          description: >-
                            Indicates if the deployment encountered an
                            out-of-memory error.
                          example: out-of-memory
                        isRollbackCandidate:
                          nullable: true
                          type: boolean
                          enum:
                            - false
                            - true
                          description: Deployment can be used for instant rollback
                        prebuilt:
                          type: boolean
                          enum:
                            - false
                            - true
                        projectSettings:
                          properties:
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
                            customerSupportCodeVisibility:
                              type: boolean
                              enum:
                                - false
                                - true
                            gitLFS:
                              type: boolean
                              enum:
                                - false
                                - true
                            devCommand:
                              nullable: true
                              type: string
                            installCommand:
                              nullable: true
                              type: string
                            buildCommand:
                              nullable: true
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
                            outputDirectory:
                              nullable: true
                              type: string
                            publicSource:
                              nullable: true
                              type: boolean
                              enum:
                                - false
                                - true
                            rootDirectory:
                              nullable: true
                              type: string
                            sourceFilesOutsideRootDirectory:
                              type: boolean
                              enum:
                                - false
                                - true
                            commandForIgnoringBuildStep:
                              nullable: true
                              type: string
                            createdAt:
                              type: number
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
                            skipGitConnectDuringLink:
                              type: boolean
                              enum:
                                - false
                                - true
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
                                  description: >-
                                    Whether the Vercel bot should comment on
                                    commits
                              required:
                                - onCommit
                                - onPullRequest
                              type: object
                              description: Since June '23
                          type: object
                          description: >-
                            The project settings which was used for this
                            deployment
                        connectBuildsEnabled:
                          type: boolean
                          enum:
                            - false
                            - true
                          description: >-
                            The flag saying if Secure Compute network is used
                            for builds
                        connectConfigurationId:
                          type: string
                          description: >-
                            The ID of Secure Compute network used for this
                            deployment
                        passiveConnectConfigurationId:
                          type: string
                          description: >-
                            The ID of Secure Compute network used for this
                            deployment's passive functions
                        expiration:
                          type: number
                          description: >-
                            The expiration configured by the project retention
                            policy
                        proposedExpiration:
                          type: number
                          description: >-
                            The expiration proposed to replace the existing
                            expiration
                        customEnvironment:
                          properties:
                            id:
                              type: string
                            slug:
                              type: string
                          required:
                            - id
                          type: object
                          description: >-
                            The custom environment used for this deployment, if
                            any
                      required:
                        - created
                        - creator
                        - inspectorUrl
                        - name
                        - projectId
                        - type
                        - uid
                        - url
                      type: object
                    type: array
                required:
                  - deployments
                  - pagination
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '422':
          description: ''
      security:
        - bearerToken: []
components:
  schemas:
    Pagination:
      properties:
        count:
          type: number
          description: Amount of items in the current page.
          example: 20
        next:
          nullable: true
          type: number
          description: Timestamp that must be used to request the next page.
          example: 1540095775951
        prev:
          nullable: true
          type: number
          description: Timestamp that must be used to request the previous page.
          example: 1540095775951
      required:
        - count
        - next
        - prev
      type: object
      description: >-
        This object contains information related to the pagination of the
        current request, including the necessary parameters to get the next or
        previous page of data.
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````