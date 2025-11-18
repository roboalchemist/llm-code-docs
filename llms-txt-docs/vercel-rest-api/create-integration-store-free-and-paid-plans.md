# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/create-integration-store-free-and-paid-plans.md

# Create integration store (free and paid plans)

> Creates an integration store for both FREE and PAID billing plans. This simplified endpoint automatically provisions real integration storage resources while handling billing complexity behind the scenes. It supports both free and paid billing plans with automatic authorization creation for paid resources. ## How it works 1. Validates the integration configuration and product 2. For free resources: Auto-discovers available free billing plans 3. For paid resources: Creates billing authorization inline using provided billingPlanId 4. Provisions real resources through the Vercel Marketplace 5. Returns the created store with connection details ## Workflow Before using this endpoint, discover available products and billing plans: 1. List your configurations: `GET /v1/integrations/configurations` 2. Get products for a configuration: `GET /v1/integrations/configuration/{id}/products` 3. Get billing plans for a product: `GET /integrations/integration/{integrationId}/products/{productId}/plans` 4. Review the `metadataSchema` for each product to understand required metadata 5. Create storage with discovered product: `POST /v1/storage/stores/integration/direct` ## Usage Patterns - **Free resources**: Omit `billingPlanId` - endpoint will auto-discover free plans - **Paid resources**: Provide `billingPlanId` from billing plans discovery - **Prepayment plans**: Also provide `prepaymentAmountCents` for variable amount plans ## Limitations - **Admin access required**: Only integration configuration admins can create stores - **Storage limits apply**: Subject to your team's storage quotas - **Payment method required**: For paid plans, ensure valid payment method is configured ## Error Responses - `400 Bad Request`: Invalid input, no plans available, or billing issues - `403 Forbidden`: Insufficient permissions (non-admin users) - `404 Not Found`: Integration configuration or product not found - `429 Too Many Requests`: Rate limit exceeded

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/storage/stores/integration/direct
paths:
  path: /v1/storage/stores/integration/direct
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
                    maxLength: 128
                    description: Human-readable name for the storage resource
                    example: my-dev-database
              integrationConfigurationId:
                allOf:
                  - type: string
                    description: >-
                      ID of your integration configuration. Get this from GET
                      /v1/integrations/configurations
                    example: icfg_cuwj0AdCdH3BwWT4LPijCC7t
                    pattern: ^icfg_[a-zA-Z0-9]+$
              integrationProductIdOrSlug:
                allOf:
                  - type: string
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
                allOf:
                  - type: object
                    description: Optional key-value pairs for resource metadata
                    additionalProperties:
                      oneOf:
                        - type: string
                        - type: number
                        - type: boolean
                        - type: array
                          items:
                            type: string
                        - type: array
                          items:
                            type: number
                    example:
                      environment: development
                      project: my-app
                      tags:
                        - database
                        - postgres
              externalId:
                allOf:
                  - type: string
                    description: Optional external identifier for tracking purposes
                    example: dev-db-001
              protocolSettings:
                allOf:
                  - type: object
                    description: Protocol-specific configuration settings
                    additionalProperties: true
                    example:
                      experimentation:
                        edgeConfigSyncingEnabled: true
              source:
                allOf:
                  - type: string
                    description: Source of the store creation request
                    example: api
                    default: marketplace
              billingPlanId:
                allOf:
                  - type: string
                    description: >-
                      ID of the billing plan for paid resources. Get available
                      plans from GET
                      /integrations/integration/{id}/products/{productId}/plans.
                      If not provided, automatically discovers free billing
                      plans.
                    example: bp_abc123def456
              paymentMethodId:
                allOf:
                  - type: string
                    description: >-
                      Payment method ID for paid resources. Optional - uses
                      default payment method if not provided.
                    example: pm_1AbcDefGhiJklMno
              prepaymentAmountCents:
                allOf:
                  - type: number
                    minimum: 50
                    description: >-
                      Amount in cents for prepayment billing plans. Required
                      only for prepayment plans with variable amounts.
                    example: 5000
            requiredProperties:
              - name
              - integrationConfigurationId
              - integrationProductIdOrSlug
        examples:
          example:
            value:
              name: my-dev-database
              integrationConfigurationId: icfg_cuwj0AdCdH3BwWT4LPijCC7t
              integrationProductIdOrSlug: iap_postgres_db
              metadata:
                environment: development
                project: my-app
                tags:
                  - database
                  - postgres
              externalId: dev-db-001
              protocolSettings:
                experimentation:
                  edgeConfigSyncingEnabled: true
              source: api
              billingPlanId: bp_abc123def456
              paymentMethodId: pm_1AbcDefGhiJklMno
              prepaymentAmountCents: 5000
    codeSamples:
      - label: createIntegrationStoreDirect
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.createIntegrationStoreDirect({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "my-dev-database",
                integrationConfigurationId: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",
                integrationProductIdOrSlug: "iap_postgres_db",
                metadata: {
                  "environment": "development",
                  "project": "my-app",
                  "tags": [
                    "database",
                    "postgres",
                  ],
                },
                externalId: "dev-db-001",
                protocolSettings: {
                  "experimentation": {
                    "edgeConfigSyncingEnabled": true,
                  },
                },
                source: "api",
                billingPlanId: "bp_abc123def456",
                paymentMethodId: "pm_1AbcDefGhiJklMno",
                prepaymentAmountCents: 5000,
              },
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
              store:
                allOf:
                  - nullable: true
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
                                      - slug
                                      - environments
                                    type: object
                                  type: array
                              required:
                                - required
                                - actions
                              type: object
                          required:
                            - id
                            - projectId
                            - name
                            - environments
                            - envVarPrefix
                            - environmentVariables
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
                          sso:
                            type: boolean
                          billable:
                            type: boolean
                          transferable:
                            type: boolean
                          secretsSync:
                            type: boolean
                          projects:
                            type: boolean
                        type: object
                      metadata:
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
                              sso:
                                type: boolean
                              billable:
                                type: boolean
                              transferable:
                                type: boolean
                              secretsSync:
                                type: boolean
                              sandbox:
                                type: boolean
                              linking:
                                type: boolean
                              projects:
                                type: boolean
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
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        minLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        pattern:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        description:
                                          type: string
                                        default:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
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
                                        maximum:
                                          type: number
                                        exclusiveMaximum:
                                          type: number
                                        minimum:
                                          type: number
                                        exclusiveMinimum:
                                          type: number
                                        description:
                                          type: string
                                        default:
                                          type: number
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
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
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
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
                                        maxItems:
                                          type: number
                                        minItems:
                                          type: number
                                        description:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
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
                                        - type
                                        - items
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
                                                  - type: boolean
                                                  - properties:
                                                      expr:
                                                        type: string
                                                    required:
                                                      - expr
                                                    type: object
                                                  - type: string
                                                    enum:
                                                      - update
                                                      - create
                                              hidden:
                                                oneOf:
                                                  - type: boolean
                                                  - properties:
                                                      expr:
                                                        type: string
                                                    required:
                                                      - expr
                                                    type: object
                                                  - type: string
                                                    enum:
                                                      - update
                                                      - create
                                            required:
                                              - value
                                              - label
                                            type: object
                                          type: array
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        minLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        pattern:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        description:
                                          type: string
                                        default:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
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
                                              type: object
                                              properties:
                                                __@BRAND@8675:
                                                  type: object
                                              required:
                                                - __@BRAND@8675
                                            maxLength:
                                              type: object
                                              properties:
                                                __@BRAND@8675:
                                                  type: object
                                              required:
                                                - __@BRAND@8675
                                            pattern:
                                              type: object
                                              properties:
                                                __@BRAND@8675:
                                                  type: object
                                              required:
                                                - __@BRAND@8675
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
                                                  - type: boolean
                                                  - properties:
                                                      expr:
                                                        type: string
                                                    required:
                                                      - expr
                                                    type: object
                                                  - type: string
                                                    enum:
                                                      - update
                                                      - create
                                              hidden:
                                                oneOf:
                                                  - type: boolean
                                                  - properties:
                                                      expr:
                                                        type: string
                                                    required:
                                                      - expr
                                                    type: object
                                                  - type: string
                                                    enum:
                                                      - update
                                                      - create
                                            required:
                                              - value
                                              - label
                                            type: object
                                          type: array
                                        maxItems:
                                          type: number
                                        minItems:
                                          type: number
                                        description:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
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
                                        - type
                                        - items
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
                                                      - type: boolean
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                  hidden:
                                                    oneOf:
                                                      - type: boolean
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                required:
                                                  - value
                                                  - label
                                                type: object
                                              - type: object
                                                properties:
                                                  __@BRAND@8675:
                                                    type: object
                                                required:
                                                  - __@BRAND@8675
                                              - properties:
                                                  value:
                                                    type: object
                                                    properties:
                                                      __@BRAND@8675:
                                                        type: object
                                                    required:
                                                      - __@BRAND@8675
                                                  disabled:
                                                    oneOf:
                                                      - type: boolean
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                  hidden:
                                                    oneOf:
                                                      - type: boolean
                                                      - properties:
                                                          expr:
                                                            type: string
                                                        required:
                                                          - expr
                                                        type: object
                                                      - type: string
                                                        enum:
                                                          - update
                                                          - create
                                                required:
                                                  - value
                                                type: object
                                          type: array
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        minLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        pattern:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        description:
                                          type: string
                                        default:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
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
                                            - string
                                        ui:control:
                                          type: string
                                          enum:
                                            - domain
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        minLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        pattern:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        description:
                                          type: string
                                        default:
                                          type: string
                                        ui:label:
                                          type: string
                                        ui:read-only:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:hidden:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        ui:disabled:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
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
                                        value:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        disabled:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                        hidden:
                                          oneOf:
                                            - type: boolean
                                            - properties:
                                                expr:
                                                  type: string
                                              required:
                                                - expr
                                              type: object
                                            - type: string
                                              enum:
                                                - update
                                                - create
                                      required:
                                        - value
                                      type: object
                                type: object
                              required:
                                items:
                                  type: string
                                type: array
                            required:
                              - type
                              - properties
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
                                - vector
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
                          disableResourceRenaming:
                            type: boolean
                          repl:
                            properties:
                              enabled:
                                type: boolean
                              supportsReadOnlyMode:
                                type: boolean
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
                                      - title
                                      - content
                                    type: object
                                  type: array
                              required:
                                - framework
                                - title
                                - steps
                              type: object
                            type: array
                          value:
                            type: object
                            properties:
                              __@BRAND@8675:
                                type: object
                            required:
                              - __@BRAND@8675
                          disabled:
                            oneOf:
                              - type: boolean
                              - properties:
                                  expr:
                                    type: string
                                required:
                                  - expr
                                type: object
                              - type: string
                                enum:
                                  - update
                                  - create
                          hidden:
                            oneOf:
                              - type: boolean
                              - properties:
                                  expr:
                                    type: string
                                required:
                                  - expr
                                type: object
                              - type: string
                                enum:
                                  - update
                                  - create
                        required:
                          - value
                        type: object
                      protocolSettings:
                        properties:
                          experimentation:
                            properties:
                              edgeConfigSyncingEnabled:
                                type: boolean
                              edgeConfigId:
                                type: string
                              edgeConfigTokenId:
                                type: string
                            type: object
                        type: object
                      notification:
                        properties:
                          title:
                            type: string
                          level:
                            type: string
                            enum:
                              - error
                              - info
                              - warn
                          message:
                            type: string
                          href:
                            type: string
                        required:
                          - title
                          - level
                        type: object
                      secrets:
                        items:
                          properties:
                            name:
                              type: string
                            length:
                              type: number
                          required:
                            - name
                            - length
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
                                - line
                                - amount
                              type: object
                            type: array
                          effectiveDate:
                            type: string
                          disabled:
                            type: boolean
                        required:
                          - type
                          - description
                          - id
                          - name
                          - scope
                          - paymentMethodRequired
                        type: object
                    required:
                      - projectsMetadata
                      - usageQuotaExceeded
                      - status
                      - externalResourceId
                      - product
                      - secrets
            requiredProperties:
              - store
        examples:
          example:
            value:
              store:
                projectsMetadata:
                  - id: <string>
                    projectId: <string>
                    name: <string>
                    framework: blitzjs
                    latestDeployment: <string>
                    environments:
                      - production
                    envVarPrefix: <string>
                    environmentVariables:
                      - <string>
                    deployments:
                      required: true
                      actions:
                        - slug: <string>
                          environments:
                            - production
                projectFilter:
                  git:
                    providers:
                      - github
                    owners:
                      - <string>
                    repos:
                      - <string>
                totalConnectedProjects: 123
                usageQuotaExceeded: true
                status: available
                ownership: owned
                capabilities:
                  mcp: true
                  sso: true
                  billable: true
                  transferable: true
                  secretsSync: true
                  projects: true
                metadata: {}
                externalResourceId: <string>
                externalResourceStatus: error
                product:
                  id: <string>
                  name: <string>
                  slug: <string>
                  iconUrl: <string>
                  capabilities:
                    mcp: true
                    sso: true
                    billable: true
                    transferable: true
                    secretsSync: true
                    sandbox: true
                    linking: true
                    projects: true
                  shortDescription: <string>
                  metadataSchema:
                    type: object
                    properties: {}
                    required:
                      - <string>
                  resourceLinks:
                    - href: <string>
                      title: <string>
                  tags:
                    - edge-config
                  projectConnectionScopes:
                    - read:deployment
                  showSSOLinkOnProjectConnection: true
                  disableResourceRenaming: true
                  repl:
                    enabled: true
                    supportsReadOnlyMode: true
                    welcomeMessage: <string>
                  guides:
                    - framework: <string>
                      title: <string>
                      steps:
                        - title: <string>
                          content: <string>
                          actions:
                            - type: connect_to_project
                  value:
                    __@BRAND@8675: {}
                  disabled: true
                  hidden: true
                protocolSettings:
                  experimentation:
                    edgeConfigSyncingEnabled: true
                    edgeConfigId: <string>
                    edgeConfigTokenId: <string>
                notification:
                  title: <string>
                  level: error
                  message: <string>
                  href: <string>
                secrets:
                  - name: <string>
                    length: 123
                billingPlan:
                  type: prepayment
                  description: <string>
                  id: <string>
                  name: <string>
                  scope: installation
                  paymentMethodRequired: true
                  preauthorizationAmount: 123
                  initialCharge: <string>
                  minimumAmount: <string>
                  maximumAmount: <string>
                  maximumAmountAutoPurchasePerPeriod: <string>
                  cost: <string>
                  details:
                    - label: <string>
                      value: <string>
                  highlightedDetails:
                    - label: <string>
                      value: <string>
                  quote:
                    - line: <string>
                      amount: <string>
                  effectiveDate: <string>
                  disabled: true
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
    '402':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The account was soft-blocked for an unhandled reason.
              The account is missing a payment so payment method must be updated
        examples: {}
        description: |-
          The account was soft-blocked for an unhandled reason.
          The account is missing a payment so payment method must be updated
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '409': {}
    '429': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````