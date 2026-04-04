# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/create-integration-store-free-and-paid-plans.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create integration store (free and paid plans)

> Creates an integration store with automatic billing plan handling. For free resources, omit `billingPlanId` to auto-discover free plans. For paid resources, provide a `billingPlanId` from the billing plans endpoint.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/storage/stores/integration/direct
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
  /v1/storage/stores/integration/direct:
    post:
      tags:
        - integrations
      summary: Create integration store (free and paid plans)
      description: >-
        Creates an integration store with automatic billing plan handling. For
        free resources, omit `billingPlanId` to auto-discover free plans. For
        paid resources, provide a `billingPlanId` from the billing plans
        endpoint.
      operationId: createIntegrationStoreDirect
      parameters:
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - integrationConfigurationId
                - integrationProductIdOrSlug
              properties:
                name:
                  type: string
                  maxLength: 128
                  description: Human-readable name for the storage resource
                  example: my-dev-database
                integrationConfigurationId:
                  type: string
                  description: >-
                    ID of your integration configuration. Get this from GET
                    /v1/integrations/configurations
                  example: icfg_cuwj0AdCdH3BwWT4LPijCC7t
                  pattern: ^icfg_[a-zA-Z0-9]+$
                integrationProductIdOrSlug:
                  type: string
                  description: >-
                    ID or slug of the integration product. Get available
                    products from GET
                    /v1/integrations/configuration/{id}/products
                  example: iap_postgres_db
                  oneOf:
                    - pattern: ^iap_[a-zA-Z0-9_]+$
                      description: Product ID format
                    - pattern: ^[a-z0-9-]+$
                      description: Product slug format
                metadata:
                  type: object
                  description: Optional key-value pairs for resource metadata
                  additionalProperties:
                    oneOf:
                      - type: string
                      - type: number
                      - type: boolean
                      - items:
                          type: string
                        type: array
                      - items:
                          type: number
                        type: array
                  example:
                    environment: development
                    project: my-app
                    tags:
                      - database
                      - postgres
                externalId:
                  type: string
                  description: Optional external identifier for tracking purposes
                  example: dev-db-001
                protocolSettings:
                  type: object
                  description: Protocol-specific configuration settings
                  additionalProperties: true
                  example:
                    experimentation:
                      edgeConfigSyncingEnabled: true
                source:
                  description: Source of the store creation request
                  example: marketplace
                  default: marketplace
                  type: string
                  enum:
                    - marketplace
                    - deploy-button
                    - external
                    - v0
                    - resource-claims
                    - cli
                    - oauth
                    - backoffice
                billingPlanId:
                  type: string
                  description: >-
                    ID of the billing plan for paid resources. Get available
                    plans from GET
                    /integrations/integration/{id}/products/{productId}/plans.
                    If not provided, automatically discovers free billing plans.
                  example: bp_abc123def456
                paymentMethodId:
                  type: string
                  description: >-
                    Payment method ID for paid resources. Optional - uses
                    default payment method if not provided.
                  example: pm_1AbcDefGhiJklMno
                prepaymentAmountCents:
                  type: number
                  minimum: 50
                  description: >-
                    Amount in cents for prepayment billing plans. Required only
                    for prepayment plans with variable amounts.
                  example: 5000
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  store:
                    nullable: true
                    type: object
                    properties:
                      projectsMetadata:
                        items:
                          properties:
                            id:
                              type: string
                            projectId:
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
                            environments:
                              items:
                                type: string
                                enum:
                                  - production
                                  - preview
                                  - development
                              type: array
                            envVarPrefix:
                              nullable: true
                              type: string
                            environmentVariables:
                              items:
                                type: string
                              type: array
                            deployments:
                              properties:
                                required:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                actions:
                                  items:
                                    properties:
                                      slug:
                                        type: string
                                      environments:
                                        items:
                                          type: string
                                          enum:
                                            - production
                                            - preview
                                            - development
                                        type: array
                                    required:
                                      - environments
                                      - slug
                                    type: object
                                  type: array
                              required:
                                - actions
                                - required
                              type: object
                          required:
                            - envVarPrefix
                            - environmentVariables
                            - environments
                            - id
                            - name
                            - projectId
                          type: object
                        type: array
                      projectFilter:
                        properties:
                          git:
                            properties:
                              providers:
                                oneOf:
                                  - items:
                                      type: string
                                      enum:
                                        - github
                                        - gitlab
                                        - bitbucket
                                    type: array
                                  - type: string
                                    enum:
                                      - '*'
                              owners:
                                items:
                                  type: string
                                type: array
                              repos:
                                items:
                                  type: string
                                type: array
                            required:
                              - providers
                            type: object
                        type: object
                      totalConnectedProjects:
                        type: number
                      usageQuotaExceeded:
                        type: boolean
                        enum:
                          - false
                          - true
                      status:
                        nullable: true
                        type: string
                        enum:
                          - available
                          - error
                          - suspended
                          - limits-exceeded-suspended
                          - limits-exceeded-suspended-store-count
                          - initializing
                          - onboarding
                          - uninstalled
                      ownership:
                        type: string
                        enum:
                          - owned
                          - linked
                          - sandbox
                      capabilities:
                        properties:
                          mcp:
                            type: boolean
                            enum:
                              - false
                              - true
                          mcpReadonly:
                            type: boolean
                            enum:
                              - false
                              - true
                          sso:
                            type: boolean
                            enum:
                              - false
                              - true
                          billable:
                            type: boolean
                            enum:
                              - false
                              - true
                          transferable:
                            type: boolean
                            enum:
                              - false
                              - true
                          secretsSync:
                            type: boolean
                            enum:
                              - false
                              - true
                          secretRotation:
                            oneOf:
                              - properties:
                                  maxDelayHours:
                                    type: number
                                required:
                                  - maxDelayHours
                                type: object
                              - type: boolean
                                enum:
                                  - false
                          projects:
                            type: boolean
                            enum:
                              - false
                              - true
                          v0:
                            type: boolean
                            enum:
                              - false
                              - true
                        type: object
                      metadata:
                        additionalProperties:
                          oneOf:
                            - type: string
                            - type: number
                            - items:
                                type: string
                              type: array
                            - items:
                                type: number
                              type: array
                            - type: boolean
                              enum:
                                - false
                                - true
                        type: object
                      externalResourceId:
                        type: string
                      externalResourceStatus:
                        nullable: true
                        type: string
                        enum:
                          - error
                          - suspended
                          - onboarding
                          - uninstalled
                          - ready
                          - pending
                          - resumed
                      directPartnerConsoleUrl:
                        type: string
                      product:
                        properties:
                          id:
                            type: string
                          name:
                            type: string
                          slug:
                            type: string
                          iconUrl:
                            type: string
                          capabilities:
                            properties:
                              mcp:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              mcpReadonly:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              sso:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              billable:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              transferable:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              secretsSync:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              secretRotation:
                                oneOf:
                                  - properties:
                                      maxDelayHours:
                                        type: number
                                    required:
                                      - maxDelayHours
                                    type: object
                                  - type: boolean
                                    enum:
                                      - false
                              sandbox:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              linking:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              projects:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              v0:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              importResource:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              connectedImportResource:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              nativeImportResource:
                                type: boolean
                                enum:
                                  - false
                                  - true
                            type: object
                          shortDescription:
                            type: string
                          metadataSchema:
                            properties:
                              type:
                                type: string
                                enum:
                                  - object
                              properties:
                                additionalProperties:
                                  oneOf:
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - string
                                        ui:control:
                                          type: string
                                          enum:
                                            - input
                                        description:
                                          type: string
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: number
                                        minLength:
                                          type: number
                                        pattern:
                                          type: string
                                        default:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                        ui:placeholder:
                                          type: string
                                      required:
                                        - type
                                        - ui:control
                                      type: object
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - number
                                        ui:control:
                                          type: string
                                          enum:
                                            - input
                                        minimum:
                                          type: number
                                        maximum:
                                          type: number
                                        description:
                                          type: string
                                        exclusiveMaximum:
                                          type: number
                                        exclusiveMinimum:
                                          type: number
                                        default:
                                          type: number
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                        ui:placeholder:
                                          type: string
                                      required:
                                        - type
                                        - ui:control
                                      type: object
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - boolean
                                        ui:control:
                                          type: string
                                          enum:
                                            - toggle
                                        description:
                                          type: string
                                        default:
                                          type: boolean
                                          enum:
                                            - false
                                            - true
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                      required:
                                        - type
                                        - ui:control
                                      type: object
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - array
                                        items:
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - number
                                            description:
                                              type: string
                                            minimum:
                                              type: number
                                            exclusiveMinimum:
                                              type: number
                                            maximum:
                                              type: number
                                            exclusiveMaximum:
                                              type: number
                                            default:
                                              type: number
                                          required:
                                            - type
                                          type: object
                                        ui:control:
                                          type: string
                                          enum:
                                            - slider
                                        ui:steps:
                                          items:
                                            type: number
                                          type: array
                                        description:
                                          type: string
                                        maxItems:
                                          type: number
                                        minItems:
                                          type: number
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                        default:
                                          items:
                                            type: number
                                          type: array
                                      required:
                                        - items
                                        - type
                                        - ui:control
                                        - ui:steps
                                      type: object
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - string
                                        ui:control:
                                          type: string
                                          enum:
                                            - select
                                        ui:options:
                                          items:
                                            properties:
                                              value:
                                                type: string
                                              label:
                                                type: string
                                              disabled:
                                                oneOf:
                                                  - properties:
                                                      expr:
                                                        type: string
                                                    required:
                                                      - expr
                                                    type: object
                                                  - type: boolean
                                                    enum:
                                                      - false
                                                      - true
                                                  - type: string
                                                    enum:
                                                      - update
                                                      - create
                                              hidden:
                                                oneOf:
                                                  - properties:
                                                      expr:
                                                        type: string
                                                    required:
                                                      - expr
                                                    type: object
                                                  - type: boolean
                                                    enum:
                                                      - false
                                                      - true
                                                  - type: string
                                                    enum:
                                                      - update
                                                      - create
                                            required:
                                              - label
                                              - value
                                            type: object
                                          type: array
                                        description:
                                          type: string
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: number
                                        minLength:
                                          type: number
                                        pattern:
                                          type: string
                                        default:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                        ui:placeholder:
                                          type: string
                                      required:
                                        - type
                                        - ui:control
                                        - ui:options
                                      type: object
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - array
                                        items:
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - string
                                            description:
                                              type: string
                                            minLength:
                                              type: number
                                            maxLength:
                                              type: number
                                            pattern:
                                              type: string
                                            default:
                                              type: string
                                            enum:
                                              items:
                                                type: string
                                              type: array
                                          required:
                                            - type
                                          type: object
                                        ui:control:
                                          type: string
                                          enum:
                                            - multi-select
                                        ui:options:
                                          items:
                                            properties:
                                              value:
                                                type: string
                                              label:
                                                type: string
                                              disabled:
                                                oneOf:
                                                  - properties:
                                                      expr:
                                                        type: string
                                                    required:
                                                      - expr
                                                    type: object
                                                  - type: boolean
                                                    enum:
                                                      - false
                                                      - true
                                                  - type: string
                                                    enum:
                                                      - update
                                                      - create
                                              hidden:
                                                oneOf:
                                                  - properties:
                                                      expr:
                                                        type: string
                                                    required:
                                                      - expr
                                                    type: object
                                                  - type: boolean
                                                    enum:
                                                      - false
                                                      - true
                                                  - type: string
                                                    enum:
                                                      - update
                                                      - create
                                            required:
                                              - label
                                              - value
                                            type: object
                                          type: array
                                        description:
                                          type: string
                                        maxItems:
                                          type: number
                                        minItems:
                                          type: number
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                        ui:placeholder:
                                          type: string
                                        default:
                                          items:
                                            type: string
                                          type: array
                                        example:
                                          items:
                                            type: string
                                          type: array
                                      required:
                                        - items
                                        - type
                                        - ui:control
                                        - ui:options
                                      type: object
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - string
                                        ui:control:
                                          type: string
                                          enum:
                                            - vercel-region
                                        ui:options:
                                          items:
                                            oneOf:
                                              - properties:
                                                  value:
                                                    type: string
                                                  label:
                                                    type: string
                                                  disabled:
                                                    oneOf:
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: boolean
                                                        enum:
                                                          - false
                                                          - true
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                  hidden:
                                                    oneOf:
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: boolean
                                                        enum:
                                                          - false
                                                          - true
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                required:
                                                  - label
                                                  - value
                                                type: object
                                              - type: string
                                              - properties:
                                                  value:
                                                    type: string
                                                  disabled:
                                                    oneOf:
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: boolean
                                                        enum:
                                                          - false
                                                          - true
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                  hidden:
                                                    oneOf:
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: boolean
                                                        enum:
                                                          - false
                                                          - true
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                required:
                                                  - value
                                                type: object
                                          type: array
                                        description:
                                          type: string
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: number
                                        minLength:
                                          type: number
                                        pattern:
                                          type: string
                                        default:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                        ui:placeholder:
                                          type: string
                                      required:
                                        - type
                                        - ui:control
                                        - ui:options
                                      type: object
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - array
                                        items:
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - string
                                            description:
                                              type: string
                                            minLength:
                                              type: number
                                            maxLength:
                                              type: number
                                            pattern:
                                              type: string
                                            default:
                                              type: string
                                            enum:
                                              items:
                                                type: string
                                              type: array
                                          required:
                                            - type
                                          type: object
                                        ui:control:
                                          type: string
                                          enum:
                                            - multi-vercel-region
                                        ui:options:
                                          items:
                                            oneOf:
                                              - properties:
                                                  value:
                                                    type: string
                                                  label:
                                                    type: string
                                                  disabled:
                                                    oneOf:
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: boolean
                                                        enum:
                                                          - false
                                                          - true
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                  hidden:
                                                    oneOf:
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: boolean
                                                        enum:
                                                          - false
                                                          - true
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                required:
                                                  - label
                                                  - value
                                                type: object
                                              - type: string
                                              - properties:
                                                  value:
                                                    type: string
                                                  disabled:
                                                    oneOf:
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: boolean
                                                        enum:
                                                          - false
                                                          - true
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                  hidden:
                                                    oneOf:
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: boolean
                                                        enum:
                                                          - false
                                                          - true
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                required:
                                                  - value
                                                type: object
                                          type: array
                                        description:
                                          type: string
                                        maxItems:
                                          type: number
                                        minItems:
                                          type: number
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                        ui:placeholder:
                                          type: string
                                        default:
                                          items:
                                            type: string
                                          type: array
                                        example:
                                          items:
                                            type: string
                                          type: array
                                      required:
                                        - items
                                        - type
                                        - ui:control
                                        - ui:options
                                      type: object
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - string
                                        ui:control:
                                          type: string
                                          enum:
                                            - domain
                                        description:
                                          type: string
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: number
                                        minLength:
                                          type: number
                                        pattern:
                                          type: string
                                        default:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                        ui:placeholder:
                                          type: string
                                      required:
                                        - type
                                        - ui:control
                                      type: object
                                    - properties:
                                        type:
                                          type: string
                                          enum:
                                            - string
                                        ui:control:
                                          type: string
                                          enum:
                                            - git-namespace
                                        description:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: boolean
                                              enum:
                                                - false
                                                - true
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:description:
                                          oneOf:
                                            - type: string
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                        ui:formatted-value:
                                          properties:
                                            expr:
                                              type: string
                                          required:
                                            - expr
                                          type: object
                                        ui:placeholder:
                                          type: string
                                        git:providers:
                                          items:
                                            type: string
                                            enum:
                                              - github
                                              - gitlab
                                              - bitbucket
                                          type: array
                                      required:
                                        - type
                                        - ui:control
                                      type: object
                                type: object
                              required:
                                items:
                                  type: string
                                type: array
                            required:
                              - properties
                              - type
                            type: object
                          resourceLinks:
                            items:
                              properties:
                                href:
                                  type: string
                                title:
                                  type: string
                              required:
                                - href
                                - title
                              type: object
                            type: array
                          tags:
                            items:
                              type: string
                              enum:
                                - edge-config
                                - redis
                                - postgres
                                - blob
                                - experimentation
                                - checks
                                - storage
                                - ai
                                - observability
                                - video
                                - authentication
                                - workflow
                                - logDrain
                                - traceDrain
                                - messaging
                                - other
                                - mysql
                                - kv
                                - vector
                                - libsql
                                - sqlite
                                - rds
                                - drains
                                - mcp
                                - tag_agents
                                - tag_ai
                                - tag_analytics
                                - tag_authentication
                                - tag_cms
                                - tag_code_repository
                                - tag_code_review
                                - tag_code_security
                                - tag_code_testing
                                - tag_commerce
                                - tag_databases
                                - tag_dev_tools
                                - tag_experimentation
                                - tag_flags
                                - tag_logging
                                - tag_messaging
                                - tag_monitoring
                                - tag_observability
                                - tag_payments
                                - tag_performance
                                - tag_productivity
                                - tag_searching
                                - tag_security
                                - tag_support_agent
                                - tag_testing
                                - tag_video
                                - tag_web_automation
                                - tag_workflow
                                - tag_checks
                                - tag_storage
                                - tag_logDrain
                                - tag_traceDrain
                                - tag_other
                            type: array
                          projectConnectionScopes:
                            items:
                              type: string
                              enum:
                                - read:deployment
                                - read:domain
                                - read:project
                                - read-write:deployment
                                - read-write:deployment-check
                                - read-write:domain
                                - read-write:global-project-env-vars
                                - read-write:integration-deployment-action
                                - read-write:log-drain
                                - read-write:drains
                                - read-write:project-env-vars
                                - read-write:project-protection-bypass
                            type: array
                          showSSOLinkOnProjectConnection:
                            type: boolean
                            enum:
                              - false
                              - true
                          disableResourceRenaming:
                            type: boolean
                            enum:
                              - false
                              - true
                          repl:
                            properties:
                              enabled:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              supportsReadOnlyMode:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              welcomeMessage:
                                type: string
                            required:
                              - enabled
                              - supportsReadOnlyMode
                            type: object
                          guides:
                            items:
                              properties:
                                framework:
                                  type: string
                                title:
                                  type: string
                                steps:
                                  items:
                                    properties:
                                      title:
                                        type: string
                                      content:
                                        type: string
                                      actions:
                                        items:
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - connect_to_project
                                                - configure_project_connections
                                                - add_drain
                                          required:
                                            - type
                                          type: object
                                        type: array
                                    required:
                                      - content
                                      - title
                                    type: object
                                  type: array
                              required:
                                - framework
                                - steps
                                - title
                              type: object
                            type: array
                          integration:
                            properties:
                              id:
                                type: string
                              name:
                                type: string
                              slug:
                                type: string
                              supportsInstallationBillingPlans:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              icon:
                                type: string
                              flags:
                                items:
                                  type: string
                                type: array
                            required:
                              - icon
                              - id
                              - name
                              - slug
                            type: object
                          integrationConfigurationId:
                            type: string
                          supportedProtocols:
                            items:
                              type: string
                              enum:
                                - experimentation
                                - checks
                                - storage
                                - ai
                                - observability
                                - video
                                - authentication
                                - workflow
                                - logDrain
                                - traceDrain
                                - messaging
                                - other
                            type: array
                          primaryProtocol:
                            type: string
                            enum:
                              - experimentation
                              - checks
                              - storage
                              - ai
                              - observability
                              - video
                              - authentication
                              - workflow
                              - logDrain
                              - traceDrain
                              - messaging
                              - other
                          logDrainStatus:
                            type: string
                            enum:
                              - disabled
                              - enabled
                        required:
                          - integration
                          - integrationConfigurationId
                          - supportedProtocols
                        type: object
                      protocolSettings:
                        properties:
                          experimentation:
                            properties:
                              edgeConfigSyncingEnabled:
                                type: boolean
                                enum:
                                  - false
                                  - true
                              edgeConfigId:
                                type: string
                              edgeConfigTokenId:
                                type: string
                            type: object
                        type: object
                      notification:
                        properties:
                          level:
                            type: string
                            enum:
                              - error
                              - info
                              - warn
                          title:
                            type: string
                          message:
                            type: string
                          href:
                            type: string
                        required:
                          - level
                          - title
                        type: object
                      secrets:
                        items:
                          properties:
                            name:
                              type: string
                            length:
                              type: number
                          required:
                            - length
                            - name
                          type: object
                        type: array
                      billingPlan:
                        properties:
                          type:
                            type: string
                            enum:
                              - prepayment
                              - subscription
                          description:
                            type: string
                          id:
                            type: string
                          name:
                            type: string
                          scope:
                            type: string
                            enum:
                              - installation
                              - resource
                          paymentMethodRequired:
                            type: boolean
                            enum:
                              - false
                              - true
                          preauthorizationAmount:
                            type: number
                          initialCharge:
                            type: string
                          minimumAmount:
                            type: string
                          maximumAmount:
                            type: string
                          maximumAmountAutoPurchasePerPeriod:
                            type: string
                          cost:
                            type: string
                          details:
                            items:
                              properties:
                                label:
                                  type: string
                                value:
                                  type: string
                              required:
                                - label
                              type: object
                            type: array
                          highlightedDetails:
                            items:
                              properties:
                                label:
                                  type: string
                                value:
                                  type: string
                              required:
                                - label
                              type: object
                            type: array
                          quote:
                            items:
                              properties:
                                line:
                                  type: string
                                amount:
                                  type: string
                              required:
                                - amount
                                - line
                              type: object
                            type: array
                          effectiveDate:
                            type: string
                          disabled:
                            type: boolean
                            enum:
                              - false
                              - true
                        required:
                          - description
                          - id
                          - name
                          - paymentMethodRequired
                          - scope
                          - type
                        type: object
                      secretRotationRequestedAt:
                        type: number
                        description: The timestamp when secret rotation was requested.
                      secretRotationRequestedReason:
                        type: string
                        description: The reason for the secret rotation request.
                      secretRotationRequestedBy:
                        type: string
                        description: >-
                          The ID of the user/team who requested the secret
                          rotation.
                      secretRotationCompletedAt:
                        type: number
                        description: The timestamp when secret rotation was completed.
                      parentId:
                        type: string
                        description: >-
                          The ID of the parent resource. Used to establish a
                          parent-child relationship between resources, such as
                          sandbox resources linking to their owner account
                          resource.
                      targets:
                        items:
                          type: string
                          enum:
                            - production
                            - preview
                            - development
                          description: >-
                            The deployment targets that this resource is
                            available for.
                        type: array
                        description: >-
                          The deployment targets that this resource is available
                          for.
                    required:
                      - externalResourceId
                      - product
                      - projectsMetadata
                      - secrets
                      - status
                      - usageQuotaExceeded
                required:
                  - store
                type: object
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '409':
          description: ''
        '429':
          description: ''
        '500':
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