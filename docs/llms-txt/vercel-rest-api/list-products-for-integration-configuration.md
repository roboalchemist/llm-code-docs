# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/list-products-for-integration-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List products for integration configuration

> Returns products available for an integration configuration. Each product includes a `metadataSchema` field with the JSON Schema for required and optional metadata fields.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configuration/{id}/products
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
  /v1/integrations/configuration/{id}/products:
    get:
      tags:
        - integrations
      summary: List products for integration configuration
      description: >-
        Returns products available for an integration configuration. Each
        product includes a `metadataSchema` field with the JSON Schema for
        required and optional metadata fields.
      operationId: getConfigurationProducts
      parameters:
        - name: id
          description: ID of the integration configuration
          in: path
          required: true
          schema:
            type: string
            description: ID of the integration configuration
            example: icfg_cuwj0AdCdH3BwWT4LPijCC7t
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
          description: List of products available for this integration configuration
          content:
            application/json:
              schema:
                properties:
                  products:
                    items:
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
                                  enum:
                                    - false
                                    - true
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
                                - endpoint
                                - format
                                - status
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
                                - endpoint
                                - format
                                - status
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
                            - checks
                            - ai
                            - authentication
                            - storage
                            - experimentation
                            - messaging
                            - observability
                            - video
                            - workflow
                            - logDrain
                            - traceDrain
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
                      required:
                        - id
                        - metadataSchema
                        - name
                        - protocols
                        - slug
                      type: object
                    type: array
                  integration:
                    properties:
                      id:
                        type: string
                      slug:
                        type: string
                      name:
                        type: string
                    required:
                      - id
                      - name
                      - slug
                    type: object
                  configuration:
                    type: object
                    required:
                      - id
                    properties:
                      id:
                        type: string
                required:
                  - configuration
                  - integration
                  - products
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
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