# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/list-deployments.md

# List deployments

> List deployments under the authenticated user or team. If a deployment hasn't finished uploading (is incomplete), the `url` property will have a value of `null`.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/deployments
paths:
  path: /v6/deployments
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
      query:
        app:
          schema:
            - type: string
              description: Name of the deployment.
              example: docs
        from:
          schema:
            - type: number
              description: >-
                Gets the deployment created after this Date timestamp. (default:
                current time)
              deprecated: true
              example: 1612948664566
        limit:
          schema:
            - type: number
              description: Maximum number of deployments to list from a request.
              example: 10
        projectId:
          schema:
            - type: string
              description: Filter deployments from the given ID or name.
              example: QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY
        projectIds:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              description: >-
                Filter deployments from the given project IDs. Cannot be used
                when projectId is specified.
              maxItems: 20
              minItems: 1
              example:
                - prj_123
                - prj_456
        target:
          schema:
            - type: string
              description: Filter deployments based on the environment.
              example: production
        to:
          schema:
            - type: number
              description: >-
                Gets the deployment created before this Date timestamp.
                (default: current time)
              deprecated: true
              example: 1612948664566
        users:
          schema:
            - type: string
              description: >-
                Filter out deployments based on users who have created the
                deployment.
              example: kr1PsOIzqEL5Xg6M4VZcZosf,K4amb7K9dAt5R2vBJWF32bmY
        since:
          schema:
            - type: number
              description: Get Deployments created after this JavaScript timestamp.
              example: 1540095775941
        until:
          schema:
            - type: number
              description: Get Deployments created before this JavaScript timestamp.
              example: 1540095775951
        state:
          schema:
            - type: string
              description: >-
                Filter deployments based on their state (`BUILDING`, `ERROR`,
                `INITIALIZING`, `QUEUED`, `READY`, `CANCELED`)
              example: BUILDING,READY
        rollbackCandidate:
          schema:
            - type: boolean
              description: Filter deployments based on their rollback candidacy
        branch:
          schema:
            - type: string
              description: Filter deployments based on the branch name
        sha:
          schema:
            - type: string
              description: Filter deployments based on the SHA
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getDeployments
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.GetDeployments(ctx, operations.GetDeploymentsRequest{\n        App: vercel.String(\"docs\"),\n        From: vercel.Float64(1612948664566),\n        Limit: vercel.Float64(10),\n        ProjectID: vercel.String(\"QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY\"),\n        Target: vercel.String(\"production\"),\n        To: vercel.Float64(1612948664566),\n        Users: vercel.String(\"kr1PsOIzqEL5Xg6M4VZcZosf,K4amb7K9dAt5R2vBJWF32bmY\"),\n        Since: vercel.Float64(1540095775941),\n        Until: vercel.Float64(1540095775951),\n        State: vercel.String(\"BUILDING,READY\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getDeployments
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.getDeployments({
              app: "docs",
              from: 1612948664566,
              limit: 10,
              projectId: "QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY",
              projectIds: [
                "prj_123",
                "prj_456",
              ],
              target: "production",
              to: 1612948664566,
              users: "kr1PsOIzqEL5Xg6M4VZcZosf,K4amb7K9dAt5R2vBJWF32bmY",
              since: 1540095775941,
              until: 1540095775951,
              state: "BUILDING,READY",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
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
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
              deployments:
                allOf:
                  - items:
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
                                - state
                                - startedAt
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
                          description: Deployment can be used for instant rollback
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
                                - nestjs
                                - fastify
                                - xmcp
                            gitForkProtection:
                              type: boolean
                            customerSupportCodeVisibility:
                              type: boolean
                            gitLFS:
                              type: boolean
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
                            rootDirectory:
                              nullable: true
                              type: string
                            sourceFilesOutsideRootDirectory:
                              type: boolean
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
                              required:
                                - id
                              type: object
                            skipGitConnectDuringLink:
                              type: boolean
                            gitComments:
                              properties:
                                onPullRequest:
                                  type: boolean
                                  description: Whether the Vercel bot should comment on PRs
                                onCommit:
                                  type: boolean
                                  description: >-
                                    Whether the Vercel bot should comment on
                                    commits
                              required:
                                - onPullRequest
                                - onCommit
                              type: object
                              description: Since June '23
                          type: object
                          description: >-
                            The project settings which was used for this
                            deployment
                        connectBuildsEnabled:
                          type: boolean
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
                        - uid
                        - name
                        - projectId
                        - url
                        - created
                        - type
                        - creator
                        - inspectorUrl
                      type: object
                    type: array
            requiredProperties:
              - pagination
              - deployments
        examples:
          example:
            value:
              pagination:
                count: 20
                next: 1540095775951
                prev: 1540095775951
              deployments:
                - uid: dpl_2euZBFqxYdDMDG1jTrHFnNZ2eUVa
                  name: docs
                  projectId: <string>
                  url: docs-9jaeg38me.vercel.app
                  created: 1609492210000
                  defaultRoute: /docs
                  deleted: 1609492210000
                  undeleted: 1609492210000
                  softDeletedByRetention: true
                  source: cli
                  state: READY
                  readyState: READY
                  type: LAMBDAS
                  creator:
                    uid: eLrCnEgbKhsHyfbiNR7E8496
                    email: example@example.com
                    username: johndoe
                    githubLogin: johndoe
                    gitlabLogin: johndoe
                  meta: {}
                  target: production
                  aliasError:
                    code: <string>
                    message: <string>
                  aliasAssigned: 123
                  createdAt: 1609492210000
                  buildingAt: 1609492210000
                  ready: 1609492210000
                  readySubstate: STAGED
                  checksState: registered
                  checksConclusion: succeeded
                  checks:
                    deployment-alias:
                      state: succeeded
                      startedAt: 123
                      completedAt: 123
                  inspectorUrl: https://vercel.com/acme/nextjs/J1hXN00qjUeoYfpEEf7dnDtpSiVq
                  errorCode: BUILD_FAILED
                  errorMessage: >-
                    The Deployment has been canceled because this project was
                    not affected
                  oomReport: out-of-memory
                  isRollbackCandidate: true
                  projectSettings:
                    framework: blitzjs
                    gitForkProtection: true
                    customerSupportCodeVisibility: true
                    gitLFS: true
                    devCommand: <string>
                    installCommand: <string>
                    buildCommand: <string>
                    nodeVersion: 22.x
                    outputDirectory: <string>
                    publicSource: true
                    rootDirectory: <string>
                    sourceFilesOutsideRootDirectory: true
                    commandForIgnoringBuildStep: <string>
                    createdAt: 123
                    speedInsights:
                      id: <string>
                      enabledAt: 123
                      disabledAt: 123
                      canceledAt: 123
                      hasData: true
                      paidAt: 123
                    webAnalytics:
                      id: <string>
                      disabledAt: 123
                      canceledAt: 123
                      enabledAt: 123
                      hasData: true
                    skipGitConnectDuringLink: true
                    gitComments:
                      onPullRequest: true
                      onCommit: true
                  connectBuildsEnabled: true
                  connectConfigurationId: <string>
                  passiveConnectConfigurationId: <string>
                  expiration: 123
                  proposedExpiration: 123
                  customEnvironment:
                    id: <string>
                    slug: <string>
        description: ''
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
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '422': {}
  deprecated: false
  type: path
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

````