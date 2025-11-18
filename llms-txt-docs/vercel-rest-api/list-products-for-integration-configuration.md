# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/list-products-for-integration-configuration.md

# List products for integration configuration

> Lists all products available for an integration configuration. Use this endpoint to discover what integration products are available for your integration configuration. The returned product IDs or slugs can then be used with storage provisioning endpoints like `POST /v1/storage/stores/integration/direct`. ## Workflow 1. Get your integration configurations: `GET /v1/integrations/configurations` 2. **Use this endpoint**: Get products for a configuration: `GET /v1/integrations/configuration/{id}/products` 3. Create storage resource: `POST /v1/storage/stores/integration/direct` ## Response Returns an array of products with their IDs, slugs, names, supported protocols, and metadata requirements. Each product represents a different type of resource you can provision. The `metadataSchema` field contains a JSON Schema that defines: - **Required metadata**: Fields that must be provided during storage creation - **Optional metadata**: Fields that can be provided but are not mandatory - **Field validation**: Data types, allowed values, and constraints Use this schema to validate metadata before calling the storage creation endpoint.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configuration/{id}/products
paths:
  path: /v1/integrations/configuration/{id}/products
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: ID of the integration configuration
              example: icfg_cuwj0AdCdH3BwWT4LPijCC7t
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
    body: {}
    codeSamples:
      - label: getConfigurationProducts
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.getConfigurationProducts({
              id: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",
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
              products:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        slug:
                          type: string
                        name:
                          type: string
                        protocols:
                          properties:
                            storage:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
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
                              required:
                                - status
                              type: object
                            experimentation:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                                edgeConfigSyncingSupport:
                                  type: boolean
                              required:
                                - status
                              type: object
                            ai:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            authentication:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            observability:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            video:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            workflow:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            checks:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            logDrain:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                                endpoint:
                                  type: string
                                headers:
                                  additionalProperties:
                                    type: string
                                  type: object
                                format:
                                  type: string
                                  enum:
                                    - json
                                    - ndjson
                              required:
                                - status
                                - endpoint
                                - format
                              type: object
                            traceDrain:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                                endpoint:
                                  type: string
                                headers:
                                  additionalProperties:
                                    type: string
                                  type: object
                                format:
                                  type: string
                                  enum:
                                    - json
                                    - proto
                              required:
                                - status
                                - endpoint
                                - format
                              type: object
                            messaging:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            other:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                          type: object
                        primaryProtocol:
                          type: string
                          enum:
                            - storage
                            - experimentation
                            - ai
                            - observability
                            - video
                            - authentication
                            - workflow
                            - checks
                            - logDrain
                            - traceDrain
                            - messaging
                            - other
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
                                      minLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      maxLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      pattern:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      default:
                                        type: string
                                      enum:
                                        items:
                                          type: string
                                        type: array
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
                                      minimum:
                                        type: number
                                      maximum:
                                        type: number
                                      description:
                                        type: string
                                      default:
                                        type: number
                                      exclusiveMinimum:
                                        type: number
                                      exclusiveMaximum:
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
                                      ui:control:
                                        type: string
                                        enum:
                                          - slider
                                      ui:steps:
                                        items:
                                          type: number
                                        type: array
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
                                      description:
                                        type: string
                                      minItems:
                                        type: number
                                      maxItems:
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
                                      default:
                                        items:
                                          type: number
                                        type: array
                                    required:
                                      - type
                                      - ui:control
                                      - ui:steps
                                      - items
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
                                      description:
                                        type: string
                                      minLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      maxLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      pattern:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      default:
                                        type: string
                                      enum:
                                        items:
                                          type: string
                                        type: array
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
                                      ui:control:
                                        type: string
                                        enum:
                                          - multi-select
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
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          maxLength:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          pattern:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          default:
                                            type: string
                                          enum:
                                            items:
                                              type: string
                                            type: array
                                        required:
                                          - type
                                        type: object
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
                                      description:
                                        type: string
                                      minItems:
                                        type: number
                                      maxItems:
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
                                      - ui:control
                                      - items
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
                                                __@BRAND@647815:
                                                  type: object
                                              required:
                                                - __@BRAND@647815
                                            - properties:
                                                value:
                                                  type: object
                                                  properties:
                                                    __@BRAND@647815:
                                                      type: object
                                                  required:
                                                    - __@BRAND@647815
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
                                      description:
                                        type: string
                                      minLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      maxLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      pattern:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      default:
                                        type: string
                                      enum:
                                        items:
                                          type: string
                                        type: array
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
                                      ui:control:
                                        type: string
                                        enum:
                                          - multi-vercel-region
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
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          maxLength:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          pattern:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          default:
                                            type: string
                                          enum:
                                            items:
                                              type: string
                                            type: array
                                        required:
                                          - type
                                        type: object
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
                                                __@BRAND@647815:
                                                  type: object
                                              required:
                                                - __@BRAND@647815
                                            - properties:
                                                value:
                                                  type: object
                                                  properties:
                                                    __@BRAND@647815:
                                                      type: object
                                                  required:
                                                    - __@BRAND@647815
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
                                      description:
                                        type: string
                                      minItems:
                                        type: number
                                      maxItems:
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
                                      default:
                                        items:
                                          type: object
                                          properties:
                                            __@BRAND@647815:
                                              type: object
                                          required:
                                            - __@BRAND@647815
                                        type: array
                                      example:
                                        items:
                                          type: object
                                          properties:
                                            __@BRAND@647815:
                                              type: object
                                          required:
                                            - __@BRAND@647815
                                        type: array
                                    required:
                                      - type
                                      - ui:control
                                      - items
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
                                      minLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      maxLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      pattern:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      default:
                                        type: string
                                      enum:
                                        items:
                                          type: string
                                        type: array
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
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
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
                      required:
                        - id
                        - slug
                        - name
                        - protocols
                        - metadataSchema
                      type: object
                    type: array
              integration:
                allOf:
                  - properties:
                      id:
                        type: string
                      slug:
                        type: string
                      name:
                        type: string
                    required:
                      - id
                      - slug
                      - name
                    type: object
              configuration:
                allOf:
                  - properties:
                      id:
                        type: string
                    required:
                      - id
                    type: object
            requiredProperties:
              - products
              - integration
              - configuration
        examples:
          example:
            value:
              products:
                - id: <string>
                  slug: <string>
                  name: <string>
                  protocols:
                    storage:
                      status: disabled
                      repl:
                        enabled: true
                        supportsReadOnlyMode: true
                        welcomeMessage: <string>
                    experimentation:
                      status: disabled
                      edgeConfigSyncingSupport: true
                    ai:
                      status: disabled
                    authentication:
                      status: disabled
                    observability:
                      status: disabled
                    video:
                      status: disabled
                    workflow:
                      status: disabled
                    checks:
                      status: disabled
                    logDrain:
                      status: disabled
                      endpoint: <string>
                      headers: {}
                      format: json
                    traceDrain:
                      status: disabled
                      endpoint: <string>
                      headers: {}
                      format: json
                    messaging:
                      status: disabled
                    other:
                      status: disabled
                  primaryProtocol: storage
                  metadataSchema:
                    type: object
                    properties: {}
                    required:
                      - <string>
              integration:
                id: <string>
                slug: <string>
                name: <string>
              configuration:
                id: <string>
        description: List of products available for this integration configuration
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````