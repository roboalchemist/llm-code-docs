# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/create-a-new-drain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new Drain

> Create a new Drain with the provided configuration.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/drains
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
  /v1/drains:
    post:
      tags:
        - drains
      summary: Create a new Drain
      description: Create a new Drain with the provided configuration.
      operationId: createDrain
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
              additionalProperties: false
              required:
                - name
                - projects
                - schemas
              properties:
                name:
                  type: string
                projects:
                  type: string
                  enum:
                    - some
                    - all
                projectIds:
                  items:
                    type: string
                  type: array
                filter:
                  oneOf:
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
                                      items:
                                        type: string
                                      type: array
                                log:
                                  type: object
                                  additionalProperties: false
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
                                deployment:
                                  type: object
                                  additionalProperties: false
                                  properties:
                                    environments:
                                      items:
                                        type: string
                                        enum:
                                          - production
                                          - preview
                                      type: array
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
                  type: object
                  additionalProperties:
                    type: object
                    required:
                      - version
                    properties:
                      version:
                        type: string
                delivery:
                  type: object
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
                          additionalProperties:
                            type: string
                          type: object
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
                          additionalProperties:
                            type: string
                          type: object
                        secret:
                          type: string
                sampling:
                  type: array
                  maxItems: 10
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
                  type: array
                  items:
                    type: object
                    required:
                      - id
                    properties:
                      id:
                        type: string
                source:
                  type: object
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
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
                  - properties:
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
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````