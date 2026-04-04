# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-list-of-all-the-log-drains-deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieves a list of all the Log Drains (deprecated)

> Retrieves a list of all the Log Drains owned by the account. This endpoint must be called with an account AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated account can be accessed.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/log-drains
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
  /v1/log-drains:
    get:
      tags:
        - logDrains
      summary: Retrieves a list of all the Log Drains (deprecated)
      description: >-
        Retrieves a list of all the Log Drains owned by the account. This
        endpoint must be called with an account AccessToken (integration OAuth2
        clients are not allowed). Only log drains owned by the authenticated
        account can be accessed.
      operationId: getAllLogDrains
      parameters:
        - name: projectId
          in: query
          schema:
            pattern: ^[a-zA-z0-9_]+$
            type: string
        - name: projectIdOrName
          in: query
          schema:
            type: string
        - name: includeMetadata
          in: query
          schema:
            type: boolean
            default: false
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
                oneOf:
                  - items:
                      type: object
                      properties:
                        createdFrom:
                          type: string
                        clientId:
                          type: string
                        configurationId:
                          type: string
                        projectsMetadata:
                          nullable: true
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
                              latestDeployment:
                                type: string
                            required:
                              - id
                              - name
                            type: object
                          type: array
                        integrationIcon:
                          type: string
                        integrationConfigurationUri:
                          type: string
                        integrationWebsite:
                          type: string
                      required:
                        - createdFrom
                    type: array
                  - properties:
                      drains:
                        oneOf:
                          - items:
                              properties:
                                id:
                                  type: string
                                createdAt:
                                  type: number
                                updatedAt:
                                  type: number
                                projectIds:
                                  items:
                                    type: string
                                  type: array
                                name:
                                  type: string
                                teamId:
                                  nullable: true
                                  type: string
                                ownerId:
                                  type: string
                                status:
                                  type: string
                                  enum:
                                    - enabled
                                    - disabled
                                    - errored
                                firstErrorTimestamp:
                                  type: number
                                disabledAt:
                                  type: number
                                disabledBy:
                                  type: string
                                disabledReason:
                                  type: string
                                  enum:
                                    - disabled-by-owner
                                    - feature-not-available
                                    - account-plan-downgrade
                                    - disabled-by-admin
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
                                            - none
                                            - gzip
                                        headers:
                                          additionalProperties:
                                            type: string
                                          type: object
                                        secret:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                kind:
                                                  type: string
                                                  enum:
                                                    - INTEGRATION_SECRET
                                              required:
                                                - kind
                                              type: object
                                      required:
                                        - encoding
                                        - endpoint
                                        - headers
                                        - type
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
                                          oneOf:
                                            - type: string
                                            - properties:
                                                kind:
                                                  type: string
                                                  enum:
                                                    - INTEGRATION_SECRET
                                              required:
                                                - kind
                                              type: object
                                      required:
                                        - encoding
                                        - endpoint
                                        - headers
                                        - type
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
                                        - endpoint
                                        - table
                                        - type
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
                                        - target
                                        - type
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
                                      - rate
                                      - type
                                    type: object
                                  type: array
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
                                        - integrationConfigurationId
                                        - integrationId
                                        - kind
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
                                                        enum:
                                                          - build
                                                          - edge
                                                          - lambda
                                                          - static
                                                          - external
                                                          - firewall
                                                          - redirect
                                                      type: array
                                                    legacy_excludeCachedStaticAssetLogs:
                                                      type: boolean
                                                      enum:
                                                        - false
                                                        - true
                                                  type: object
                                                deployment:
                                                  properties:
                                                    environments:
                                                      items:
                                                        type: string
                                                        enum:
                                                          - production
                                                          - preview
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
                                                - text
                                                - type
                                              type: object
                                      required:
                                        - filter
                                        - version
                                      type: object
                              required:
                                - createdAt
                                - delivery
                                - id
                                - name
                                - ownerId
                                - schemas
                                - source
                                - updatedAt
                              type: object
                            type: array
                          - items:
                              properties:
                                id:
                                  type: string
                                createdAt:
                                  type: number
                                updatedAt:
                                  type: number
                                projectIds:
                                  items:
                                    type: string
                                  type: array
                                name:
                                  type: string
                                teamId:
                                  nullable: true
                                  type: string
                                ownerId:
                                  type: string
                                status:
                                  type: string
                                  enum:
                                    - enabled
                                    - disabled
                                    - errored
                                firstErrorTimestamp:
                                  type: number
                                disabledAt:
                                  type: number
                                disabledBy:
                                  type: string
                                disabledReason:
                                  type: string
                                  enum:
                                    - disabled-by-owner
                                    - feature-not-available
                                    - account-plan-downgrade
                                    - disabled-by-admin
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
                                            - none
                                            - gzip
                                        headers:
                                          additionalProperties:
                                            type: string
                                          type: object
                                        secret:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                kind:
                                                  type: string
                                                  enum:
                                                    - INTEGRATION_SECRET
                                              required:
                                                - kind
                                              type: object
                                      required:
                                        - encoding
                                        - endpoint
                                        - headers
                                        - type
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
                                          oneOf:
                                            - type: string
                                            - properties:
                                                kind:
                                                  type: string
                                                  enum:
                                                    - INTEGRATION_SECRET
                                              required:
                                                - kind
                                              type: object
                                      required:
                                        - encoding
                                        - endpoint
                                        - headers
                                        - type
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
                                        - endpoint
                                        - table
                                        - type
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
                                        - target
                                        - type
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
                                      - rate
                                      - type
                                    type: object
                                  type: array
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
                                        - integrationConfigurationId
                                        - integrationId
                                        - kind
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
                                                        enum:
                                                          - build
                                                          - edge
                                                          - lambda
                                                          - static
                                                          - external
                                                          - firewall
                                                          - redirect
                                                      type: array
                                                    legacy_excludeCachedStaticAssetLogs:
                                                      type: boolean
                                                      enum:
                                                        - false
                                                        - true
                                                  type: object
                                                deployment:
                                                  properties:
                                                    environments:
                                                      items:
                                                        type: string
                                                        enum:
                                                          - production
                                                          - preview
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
                                                - text
                                                - type
                                              type: object
                                      required:
                                        - filter
                                        - version
                                      type: object
                                integrationIcon:
                                  type: string
                                integrationConfigurationUri:
                                  type: string
                                integrationWebsite:
                                  type: string
                                projectAccess:
                                  oneOf:
                                    - properties:
                                        access:
                                          type: string
                                          enum:
                                            - all
                                      required:
                                        - access
                                      type: object
                                    - properties:
                                        access:
                                          type: string
                                          enum:
                                            - some
                                        projectIds:
                                          items:
                                            type: string
                                          type: array
                                      required:
                                        - access
                                        - projectIds
                                      type: object
                              required:
                                - createdAt
                                - delivery
                                - id
                                - name
                                - ownerId
                                - schemas
                                - source
                                - updatedAt
                              type: object
                            type: array
                    required:
                      - drains
                    type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````