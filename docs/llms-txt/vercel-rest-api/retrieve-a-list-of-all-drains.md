# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/retrieve-a-list-of-all-drains.md

# Retrieve a list of all Drains

> Allows to retrieve the list of Drains of the authenticated team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/drains
paths:
  path: /v1/drains
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
        projectId:
          schema:
            - type: string
        includeMetadata:
          schema:
            - type: boolean
              default: false
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
      - label: getDrains
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.drains.getDrains({
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
              drains:
                allOf:
                  - oneOf:
                      - items:
                          properties:
                            id:
                              type: string
                            ownerId:
                              type: string
                            name:
                              type: string
                            createdAt:
                              type: number
                            createdFrom:
                              type: string
                              enum:
                                - self-served
                                - integration
                            updatedAt:
                              type: number
                            projectIds:
                              items:
                                type: string
                              type: array
                            schemas:
                              properties:
                                log:
                                  type: object
                                trace:
                                  type: object
                                analytics:
                                  type: object
                                speed_insights:
                                  type: object
                              type: object
                            delivery:
                              oneOf:
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - http
                                    endpoint:
                                      type: string
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - ndjson
                                    compression:
                                      type: string
                                      enum:
                                        - gzip
                                        - none
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - otlphttp
                                    endpoint:
                                      properties:
                                        traces:
                                          type: string
                                      required:
                                        - traces
                                      type: object
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - proto
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - syslog
                                    endpoint:
                                      type: string
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - secret
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - clickhouse
                                    endpoint:
                                      type: string
                                    table:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - table
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - internal
                                    target:
                                      type: string
                                      enum:
                                        - vercel-otel-traces-db
                                  required:
                                    - type
                                    - target
                                  type: object
                            sampling:
                              items:
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - head_sampling
                                  rate:
                                    type: number
                                  env:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                  requestPath:
                                    type: string
                                required:
                                  - type
                                  - rate
                                type: object
                              type: array
                            teamId:
                              nullable: true
                              type: string
                            status:
                              type: string
                              enum:
                                - enabled
                                - disabled
                                - errored
                            disabledAt:
                              type: number
                            disabledReason:
                              type: string
                              enum:
                                - disabled-by-owner
                                - feature-not-available
                                - account-plan-downgrade
                                - disabled-by-admin
                            disabledBy:
                              type: string
                            firstErrorTimestamp:
                              type: number
                            configurationId:
                              type: string
                            clientId:
                              type: string
                            source:
                              oneOf:
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - self-served
                                  required:
                                    - kind
                                  type: object
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - integration
                                    resourceId:
                                      type: string
                                    externalResourceId:
                                      type: string
                                    integrationId:
                                      type: string
                                    integrationConfigurationId:
                                      type: string
                                  required:
                                    - kind
                                    - integrationId
                                    - integrationConfigurationId
                                  type: object
                            filter:
                              type: string
                            filterV2:
                              oneOf:
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v1
                                  required:
                                    - version
                                  type: object
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v2
                                    filter:
                                      oneOf:
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - basic
                                            project:
                                              properties:
                                                ids:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            log:
                                              properties:
                                                sources:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            deployment:
                                              properties:
                                                environments:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                          required:
                                            - type
                                          type: object
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - odata
                                            text:
                                              type: string
                                          required:
                                            - type
                                            - text
                                          type: object
                                  required:
                                    - version
                                    - filter
                                  type: object
                          required:
                            - id
                            - ownerId
                            - name
                            - createdAt
                            - updatedAt
                            - source
                          type: object
                        type: array
                      - items:
                          properties:
                            id:
                              type: string
                            ownerId:
                              type: string
                            name:
                              type: string
                            createdAt:
                              type: number
                            createdFrom:
                              type: string
                              enum:
                                - self-served
                                - integration
                            updatedAt:
                              type: number
                            projectIds:
                              items:
                                type: string
                              type: array
                            schemas:
                              properties:
                                log:
                                  type: object
                                trace:
                                  type: object
                                analytics:
                                  type: object
                                speed_insights:
                                  type: object
                              type: object
                            delivery:
                              oneOf:
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - http
                                    endpoint:
                                      type: string
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - ndjson
                                    compression:
                                      type: string
                                      enum:
                                        - gzip
                                        - none
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - otlphttp
                                    endpoint:
                                      properties:
                                        traces:
                                          type: string
                                      required:
                                        - traces
                                      type: object
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - proto
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - syslog
                                    endpoint:
                                      type: string
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - secret
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - clickhouse
                                    endpoint:
                                      type: string
                                    table:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - table
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - internal
                                    target:
                                      type: string
                                      enum:
                                        - vercel-otel-traces-db
                                  required:
                                    - type
                                    - target
                                  type: object
                            sampling:
                              items:
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - head_sampling
                                  rate:
                                    type: number
                                  env:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                  requestPath:
                                    type: string
                                required:
                                  - type
                                  - rate
                                type: object
                              type: array
                            teamId:
                              nullable: true
                              type: string
                            status:
                              type: string
                              enum:
                                - enabled
                                - disabled
                                - errored
                            disabledAt:
                              type: number
                            disabledReason:
                              type: string
                              enum:
                                - disabled-by-owner
                                - feature-not-available
                                - account-plan-downgrade
                                - disabled-by-admin
                            disabledBy:
                              type: string
                            firstErrorTimestamp:
                              type: number
                            configurationId:
                              type: string
                            clientId:
                              type: string
                            source:
                              oneOf:
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - self-served
                                  required:
                                    - kind
                                  type: object
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - integration
                                    resourceId:
                                      type: string
                                    externalResourceId:
                                      type: string
                                    integrationId:
                                      type: string
                                    integrationConfigurationId:
                                      type: string
                                  required:
                                    - kind
                                    - integrationId
                                    - integrationConfigurationId
                                  type: object
                            filter:
                              type: string
                            filterV2:
                              oneOf:
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v1
                                  required:
                                    - version
                                  type: object
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v2
                                    filter:
                                      oneOf:
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - basic
                                            project:
                                              properties:
                                                ids:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            log:
                                              properties:
                                                sources:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            deployment:
                                              properties:
                                                environments:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                          required:
                                            - type
                                          type: object
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - odata
                                            text:
                                              type: string
                                          required:
                                            - type
                                            - text
                                          type: object
                                  required:
                                    - version
                                    - filter
                                  type: object
                            integrationIcon:
                              type: string
                            integrationConfigurationUri:
                              type: string
                            integrationWebsite:
                              type: string
                            projectsMetadata:
                              items:
                                properties:
                                  id:
                                    type: string
                                  name:
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
                                  latestDeployment:
                                    type: string
                                required:
                                  - id
                                  - name
                                type: object
                              type: array
                          required:
                            - id
                            - ownerId
                            - name
                            - createdAt
                            - updatedAt
                            - source
                          type: object
                        type: array
            requiredProperties:
              - drains
        examples:
          example:
            value:
              drains:
                - id: <string>
                  ownerId: <string>
                  name: <string>
                  createdAt: 123
                  createdFrom: self-served
                  updatedAt: 123
                  projectIds:
                    - <string>
                  schemas:
                    log: {}
                    trace: {}
                    analytics: {}
                    speed_insights: {}
                  delivery:
                    type: http
                    endpoint: <string>
                    encoding: json
                    compression: gzip
                    headers: {}
                    secret: <string>
                  sampling:
                    - type: head_sampling
                      rate: 123
                      env: production
                      requestPath: <string>
                  teamId: <string>
                  status: enabled
                  disabledAt: 123
                  disabledReason: disabled-by-owner
                  disabledBy: <string>
                  firstErrorTimestamp: 123
                  configurationId: <string>
                  clientId: <string>
                  source:
                    kind: self-served
                  filter: <string>
                  filterV2:
                    version: v1
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
  deprecated: false
  type: path
components:
  schemas: {}

````