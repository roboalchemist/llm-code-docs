# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/retrieve-an-integration-configuration.md

# Retrieve an integration configuration

> Allows to retrieve a the configuration with the provided id in case it exists. The authenticated user or team must be the owner of the config in order to access it.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configuration/{id}
paths:
  path: /v1/integrations/configuration/{id}
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
              description: ID of the configuration to check
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
      - label: getConfiguration
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Integrations.GetConfiguration(ctx, \"icfg_cuwj0AdCdH3BwWT4LPijCC7t\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getConfiguration
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.getConfiguration({
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
              projectSelection:
                allOf:
                  - type: string
                    enum:
                      - selected
                      - all
                    description: >-
                      A string representing the permission for projects.
                      Possible values are `all` or `selected`.
                    example: all
              notification:
                allOf:
                  - properties:
                      level:
                        type: string
                        enum:
                          - info
                          - warn
                          - error
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
              transferRequest:
                allOf:
                  - oneOf:
                      - properties:
                          kind:
                            type: string
                            enum:
                              - transfer-to-marketplace
                          metadata:
                            additionalProperties: true
                            type: object
                          billingPlan:
                            properties:
                              id:
                                type: string
                              type:
                                type: string
                                enum:
                                  - subscription
                                  - prepayment
                              scope:
                                type: string
                                enum:
                                  - installation
                                  - resource
                              name:
                                type: string
                              description:
                                type: string
                              paymentMethodRequired:
                                type: boolean
                              preauthorizationAmount:
                                type: number
                            required:
                              - id
                              - type
                              - name
                              - description
                            type: object
                          requestId:
                            type: string
                          transferId:
                            type: string
                          requester:
                            properties:
                              name:
                                type: string
                              email:
                                type: string
                            required:
                              - name
                            type: object
                          createdAt:
                            type: number
                          expiresAt:
                            type: number
                          discardedAt:
                            type: number
                          discardedBy:
                            type: string
                          approvedAt:
                            type: number
                          approvedBy:
                            type: string
                          authorizationId:
                            type: string
                        required:
                          - kind
                          - requestId
                          - transferId
                          - requester
                          - createdAt
                          - expiresAt
                        type: object
                      - properties:
                          kind:
                            type: string
                            enum:
                              - transfer-from-marketplace
                          requestId:
                            type: string
                          transferId:
                            type: string
                          requester:
                            properties:
                              name:
                                type: string
                              email:
                                type: string
                            required:
                              - name
                            type: object
                          createdAt:
                            type: number
                          expiresAt:
                            type: number
                          discardedAt:
                            type: number
                          discardedBy:
                            type: string
                          approvedAt:
                            type: number
                          approvedBy:
                            type: string
                          authorizationId:
                            type: string
                        required:
                          - kind
                          - requestId
                          - transferId
                          - requester
                          - createdAt
                          - expiresAt
                        type: object
              projects:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      When a configuration is limited to access certain
                      projects, this will contain each of the project ID it is
                      allowed to access. If it is not defined, the configuration
                      has full access.
                    example:
                      - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      created
                    example: 1558531915505
              completedAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      installed successfully
                    example: 1558531915505
              id:
                allOf:
                  - type: string
                    description: The unique identifier of the configuration
                    example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              integrationId:
                allOf:
                  - type: string
                    description: >-
                      The unique identifier of the app the configuration was
                      created for
                    example: oac_xzpVzcUOgcB1nrVlirtKhbWV
              ownerId:
                allOf:
                  - type: string
                    description: The user or team ID that owns the configuration
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              slug:
                allOf:
                  - type: string
                    description: >-
                      The slug of the integration the configuration is created
                      for.
                    example: slack
              teamId:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      When the configuration was created for a team, this will
                      show the ID of the team.
                    example: team_nLlpyC6RE1qxydlFKbrxDlud
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      updated.
                    example: 1558531915505
              userId:
                allOf:
                  - type: string
                    description: The ID of the user that created the configuration.
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              scopes:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      The resources that are allowed to be accessed by the
                      configuration.
                    example:
                      - read:project
                      - read-write:log-drain
              disabledAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      disabled. Note: Configurations can be disabled when the
                      associated user loses access to a team. They do not
                      function during this time until the configuration is
                      'transferred', meaning the associated user is changed to
                      one with access to the team.
                    example: 1558531915505
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - disabled-by-admin
                      - original-owner-left-the-team
                      - account-plan-downgrade
                      - original-owner-role-downgraded
              source:
                allOf:
                  - type: string
                    enum:
                      - marketplace
                      - deploy-button
                      - external
                      - v0
                      - resource-claims
                    description: >-
                      Source defines where the configuration was installed from.
                      It is used to analyze user engagement for integration
                      installations in product metrics.
                    example: marketplace
              canConfigureOpenTelemetry:
                allOf:
                  - type: boolean
              installationType:
                allOf:
                  - type: string
                    enum:
                      - marketplace
                      - external
                    description: >-
                      Defines the installation type. - 'external' integrations
                      are installed via the existing integrations flow -
                      'marketplace' integrations are natively installed: - when
                      accepting the TOS of a partner during the store creation
                      process - if undefined, assume 'external'
              deleteRequestedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A timestamp that tells you when the configuration deletion
                      has been started for cases when the deletion needs to be
                      settled/approved by partners, such as when marketplace
                      invoices have been paid.
                    example: 1558531915505
              type:
                allOf:
                  - type: string
                    enum:
                      - integration-configuration
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      deleted.
                    example: 1558531915505
            requiredProperties:
              - projectSelection
              - notification
              - transferRequest
              - createdAt
              - id
              - integrationId
              - ownerId
              - slug
              - updatedAt
              - userId
              - scopes
              - type
          - type: object
            properties:
              completedAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      installed successfully
                    example: 1558531915505
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      created
                    example: 1558531915505
              id:
                allOf:
                  - type: string
                    description: The unique identifier of the configuration
                    example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              integrationId:
                allOf:
                  - type: string
                    description: >-
                      The unique identifier of the app the configuration was
                      created for
                    example: oac_xzpVzcUOgcB1nrVlirtKhbWV
              ownerId:
                allOf:
                  - type: string
                    description: The user or team ID that owns the configuration
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              projects:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      When a configuration is limited to access certain
                      projects, this will contain each of the project ID it is
                      allowed to access. If it is not defined, the configuration
                      has full access.
                    example:
                      - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
              source:
                allOf:
                  - type: string
                    enum:
                      - marketplace
                      - deploy-button
                      - external
                      - v0
                      - resource-claims
                    description: >-
                      Source defines where the configuration was installed from.
                      It is used to analyze user engagement for integration
                      installations in product metrics.
                    example: marketplace
              slug:
                allOf:
                  - type: string
                    description: >-
                      The slug of the integration the configuration is created
                      for.
                    example: slack
              teamId:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      When the configuration was created for a team, this will
                      show the ID of the team.
                    example: team_nLlpyC6RE1qxydlFKbrxDlud
              type:
                allOf:
                  - type: string
                    enum:
                      - integration-configuration
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      updated.
                    example: 1558531915505
              userId:
                allOf:
                  - type: string
                    description: The ID of the user that created the configuration.
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              scopes:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      The resources that are allowed to be accessed by the
                      configuration.
                    example:
                      - read:project
                      - read-write:log-drain
              disabledAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      disabled. Note: Configurations can be disabled when the
                      associated user loses access to a team. They do not
                      function during this time until the configuration is
                      'transferred', meaning the associated user is changed to
                      one with access to the team.
                    example: 1558531915505
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      deleted.
                    example: 1558531915505
              deleteRequestedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A timestamp that tells you when the configuration deletion
                      has been started for cases when the deletion needs to be
                      settled/approved by partners, such as when marketplace
                      invoices have been paid.
                    example: 1558531915505
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - disabled-by-admin
                      - original-owner-left-the-team
                      - account-plan-downgrade
                      - original-owner-role-downgraded
              installationType:
                allOf:
                  - type: string
                    enum:
                      - marketplace
                      - external
                    description: >-
                      Defines the installation type. - 'external' integrations
                      are installed via the existing integrations flow -
                      'marketplace' integrations are natively installed: - when
                      accepting the TOS of a partner during the store creation
                      process - if undefined, assume 'external'
            description: The configuration with the provided id
            requiredProperties:
              - createdAt
              - id
              - integrationId
              - ownerId
              - slug
              - type
              - updatedAt
              - userId
              - scopes
        examples:
          example:
            value:
              projectSelection: all
              notification:
                level: info
                title: <string>
                message: <string>
                href: <string>
              transferRequest:
                kind: transfer-to-marketplace
                metadata: {}
                billingPlan:
                  id: <string>
                  type: subscription
                  scope: installation
                  name: <string>
                  description: <string>
                  paymentMethodRequired: true
                  preauthorizationAmount: 123
                requestId: <string>
                transferId: <string>
                requester:
                  name: <string>
                  email: <string>
                createdAt: 123
                expiresAt: 123
                discardedAt: 123
                discardedBy: <string>
                approvedAt: 123
                approvedBy: <string>
                authorizationId: <string>
              projects:
                - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
              createdAt: 1558531915505
              completedAt: 1558531915505
              id: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              integrationId: oac_xzpVzcUOgcB1nrVlirtKhbWV
              ownerId: kr1PsOIzqEL5Xg6M4VZcZosf
              slug: slack
              teamId: team_nLlpyC6RE1qxydlFKbrxDlud
              updatedAt: 1558531915505
              userId: kr1PsOIzqEL5Xg6M4VZcZosf
              scopes:
                - read:project
                - read-write:log-drain
              disabledAt: 1558531915505
              disabledReason: disabled-by-owner
              source: marketplace
              canConfigureOpenTelemetry: true
              installationType: marketplace
              deleteRequestedAt: 1558531915505
              type: integration-configuration
              deletedAt: 1558531915505
        description: The configuration with the provided id
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The configuration was not found
        examples: {}
        description: The configuration was not found
  deprecated: false
  type: path
components:
  schemas: {}

````