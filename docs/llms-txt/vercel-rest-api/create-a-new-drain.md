# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/create-a-new-drain.md

# Create a new Drain

> Create a new Drain with the provided configuration.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/drains
paths:
  path: /v1/drains
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
              projects:
                allOf:
                  - type: string
                    enum:
                      - some
                      - all
              projectIds:
                allOf:
                  - type: array
                    items:
                      type: string
              filter:
                allOf:
                  - oneOf:
                      - type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - version
                          - filter
                        properties:
                          version:
                            type: string
                          filter:
                            oneOf:
                              - type: object
                                additionalProperties: false
                                required:
                                  - type
                                properties:
                                  type:
                                    type: string
                                  project:
                                    type: object
                                    additionalProperties: false
                                    properties:
                                      ids:
                                        type: array
                                        items:
                                          type: string
                                  log:
                                    type: object
                                    additionalProperties: false
                                    properties:
                                      sources:
                                        type: array
                                        items:
                                          type: string
                                  deployment:
                                    type: object
                                    additionalProperties: false
                                    properties:
                                      environments:
                                        type: array
                                        items:
                                          type: string
                              - type: object
                                additionalProperties: false
                                required:
                                  - type
                                  - text
                                properties:
                                  type:
                                    type: string
                                  text:
                                    type: string
              schemas:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - version
                      properties:
                        version:
                          type: string
              delivery:
                allOf:
                  - type: object
                    oneOf:
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          compression:
                            type: string
                            enum:
                              - gzip
                              - none
                          encoding:
                            type: string
                            enum:
                              - json
                              - ndjson
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            oneOf:
                              - type: object
                                additionalProperties: false
                                required:
                                  - traces
                                properties:
                                  traces:
                                    type: string
                          encoding:
                            type: string
                            enum:
                              - proto
                              - json
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - secret
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          secret:
                            type: string
              sampling:
                allOf:
                  - type: array
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - type
                        - rate
                      properties:
                        type:
                          type: string
                        rate:
                          type: number
                          minimum: 0
                          maximum: 1
                          description: Sampling rate from 0 to 1 (e.g., 0.1 for 10%)
                        env:
                          type: string
                          enum:
                            - production
                            - preview
                          description: Environment to apply sampling to
                        requestPath:
                          type: string
                          description: Request path prefix to apply the sampling rule to
              transforms:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - id
                      properties:
                        id:
                          type: string
              source:
                allOf:
                  - type: object
                    oneOf:
                      - oneOf:
                          - properties:
                              kind:
                                type: string
                                default: integration
                              externalResourceId:
                                type: string
                            additionalProperties: false
                            required:
                              - externalResourceId
                          - properties:
                              kind:
                                type: string
                                default: integration
                              resourceId:
                                type: string
                            additionalProperties: false
                            required:
                              - resourceId
                          - properties:
                              kind:
                                type: string
                                default: integration
                            additionalProperties: false
                            required:
                              - kind
                      - properties:
                          kind:
                            type: string
                            default: self-served
                        additionalProperties: false
                        required:
                          - kind
            requiredProperties:
              - name
              - projects
              - schemas
            additionalProperties: false
        examples:
          example:
            value:
              name: <string>
              projects: some
              projectIds:
                - <string>
              filter: <string>
              schemas: {}
              delivery:
                type: <string>
                endpoint: <string>
                compression: gzip
                encoding: json
                headers: {}
                secret: <string>
              sampling:
                - type: <string>
                  rate: 0.5
                  env: production
                  requestPath: <string>
              transforms:
                - id: <string>
              source:
                kind: integration
                externalResourceId: <string>
    codeSamples:
      - label: createDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.drains.createDrain({
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
              id:
                allOf:
                  - type: string
              ownerId:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - self-served
                      - integration
              updatedAt:
                allOf:
                  - type: number
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
              schemas:
                allOf:
                  - properties:
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
                allOf:
                  - oneOf:
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
                allOf:
                  - items:
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
                allOf:
                  - nullable: true
                    type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
                      - errored
              disabledAt:
                allOf:
                  - type: number
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - account-plan-downgrade
                      - disabled-by-admin
              disabledBy:
                allOf:
                  - type: string
              firstErrorTimestamp:
                allOf:
                  - type: number
              configurationId:
                allOf:
                  - type: string
              clientId:
                allOf:
                  - type: string
              source:
                allOf:
                  - oneOf:
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
                allOf:
                  - type: string
              filterV2:
                allOf:
                  - oneOf:
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
            requiredProperties:
              - id
              - ownerId
              - name
              - createdAt
              - updatedAt
              - source
          - type: object
            properties:
              id:
                allOf:
                  - type: string
              ownerId:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - self-served
                      - integration
              updatedAt:
                allOf:
                  - type: number
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
              schemas:
                allOf:
                  - properties:
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
                allOf:
                  - oneOf:
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
                allOf:
                  - items:
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
                allOf:
                  - nullable: true
                    type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
                      - errored
              disabledAt:
                allOf:
                  - type: number
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - account-plan-downgrade
                      - disabled-by-admin
              disabledBy:
                allOf:
                  - type: string
              firstErrorTimestamp:
                allOf:
                  - type: number
              configurationId:
                allOf:
                  - type: string
              clientId:
                allOf:
                  - type: string
              source:
                allOf:
                  - oneOf:
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
                allOf:
                  - type: string
              filterV2:
                allOf:
                  - oneOf:
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
                allOf:
                  - type: string
              integrationConfigurationUri:
                allOf:
                  - type: string
              integrationWebsite:
                allOf:
                  - type: string
              projectsMetadata:
                allOf:
                  - items:
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
            requiredProperties:
              - id
              - ownerId
              - name
              - createdAt
              - updatedAt
              - source
        examples:
          example:
            value:
              id: <string>
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
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
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
  deprecated: false
  type: path
components:
  schemas: {}

````