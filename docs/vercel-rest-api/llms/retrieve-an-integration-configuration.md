# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/retrieve-an-integration-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve an integration configuration

> Allows to retrieve a the configuration with the provided id in case it exists. The authenticated user or team must be the owner of the config in order to access it.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configuration/{id}
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
  /v1/integrations/configuration/{id}:
    get:
      tags:
        - integrations
      summary: Retrieve an integration configuration
      description: >-
        Allows to retrieve a the configuration with the provided id in case it
        exists. The authenticated user or team must be the owner of the config
        in order to access it.
      operationId: getConfiguration
      parameters:
        - name: id
          description: ID of the configuration to check
          in: path
          required: true
          schema:
            type: string
            description: ID of the configuration to check
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
          description: The configuration with the provided id
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
                      projectSelection:
                        type: string
                        enum:
                          - selected
                          - all
                        description: >-
                          A string representing the permission for projects.
                          Possible values are `all` or `selected`.
                        example: all
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
                      transferRequest:
                        oneOf:
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
                                      - prepayment
                                      - subscription
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
                                    enum:
                                      - false
                                      - true
                                  preauthorizationAmount:
                                    type: number
                                required:
                                  - description
                                  - id
                                  - name
                                  - type
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
                              - createdAt
                              - expiresAt
                              - kind
                              - requestId
                              - requester
                              - transferId
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
                              - createdAt
                              - expiresAt
                              - kind
                              - requestId
                              - requester
                              - transferId
                            type: object
                      projects:
                        items:
                          type: string
                        type: array
                        description: >-
                          When a configuration is limited to access certain
                          projects, this will contain each of the project ID it
                          is allowed to access. If it is not defined, the
                          configuration has full access.
                        example:
                          - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
                      status:
                        type: string
                        enum:
                          - error
                          - ready
                          - pending
                          - onboarding
                          - suspended
                          - resumed
                          - uninstalled
                        description: >-
                          The configuration status. Optional. If not defined,
                          assume 'ready'.
                      type:
                        type: string
                        enum:
                          - integration-configuration
                      createdAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          created
                        example: 1558531915505
                      deletedAt:
                        nullable: true
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          deleted.
                        example: 1558531915505
                      id:
                        type: string
                        description: The unique identifier of the configuration
                        example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                      slug:
                        type: string
                        description: >-
                          The slug of the integration the configuration is
                          created for.
                        example: slack
                      teamId:
                        nullable: true
                        type: string
                        description: >-
                          When the configuration was created for a team, this
                          will show the ID of the team.
                        example: team_nLlpyC6RE1qxydlFKbrxDlud
                      updatedAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          updated.
                        example: 1558531915505
                      userId:
                        type: string
                        description: The ID of the user that created the configuration.
                        example: kr1PsOIzqEL5Xg6M4VZcZosf
                      scopes:
                        items:
                          type: string
                        type: array
                        description: >-
                          The resources that are allowed to be accessed by the
                          configuration.
                        example:
                          - read:project
                          - read-write:log-drain
                      source:
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
                        description: >-
                          Source defines where the configuration was installed
                          from. It is used to analyze user engagement for
                          integration installations in product metrics.
                        example: marketplace
                      integrationId:
                        type: string
                        description: >-
                          The unique identifier of the app the configuration was
                          created for
                        example: oac_xzpVzcUOgcB1nrVlirtKhbWV
                      ownerId:
                        type: string
                        description: The user or team ID that owns the configuration
                        example: kr1PsOIzqEL5Xg6M4VZcZosf
                      canConfigureOpenTelemetry:
                        type: boolean
                        enum:
                          - false
                          - true
                      completedAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          installed successfully
                        example: 1558531915505
                      externalId:
                        type: string
                        description: >-
                          An external identifier defined by the integration
                          vendor.
                      disabledAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          disabled. Note: Configurations can be disabled when
                          the associated user loses access to a team. They do
                          not function during this time until the configuration
                          is 'transferred', meaning the associated user is
                          changed to one with access to the team.
                        example: 1558531915505
                      deleteRequestedAt:
                        nullable: true
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration
                          deletion has been started for cases when the deletion
                          needs to be settled/approved by partners, such as when
                          marketplace invoices have been paid.
                        example: 1558531915505
                      disabledReason:
                        type: string
                        enum:
                          - disabled-by-owner
                          - feature-not-available
                          - disabled-by-admin
                          - original-owner-left-the-team
                          - account-plan-downgrade
                          - original-owner-role-downgraded
                      installationType:
                        type: string
                        enum:
                          - marketplace
                          - external
                        description: >-
                          Defines the installation type. - 'external'
                          integrations are installed via the existing
                          integrations flow - 'marketplace' integrations are
                          natively installed: - when accepting the TOS of a
                          partner during the store creation process - if
                          undefined, assume 'external'
                    required:
                      - createdAt
                      - id
                      - integrationId
                      - notification
                      - ownerId
                      - projectSelection
                      - scopes
                      - slug
                      - transferRequest
                      - type
                      - updatedAt
                      - userId
                    type: object
                  - properties:
                      completedAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          installed successfully
                        example: 1558531915505
                      createdAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          created
                        example: 1558531915505
                      id:
                        type: string
                        description: The unique identifier of the configuration
                        example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                      integrationId:
                        type: string
                        description: >-
                          The unique identifier of the app the configuration was
                          created for
                        example: oac_xzpVzcUOgcB1nrVlirtKhbWV
                      ownerId:
                        type: string
                        description: The user or team ID that owns the configuration
                        example: kr1PsOIzqEL5Xg6M4VZcZosf
                      status:
                        type: string
                        enum:
                          - error
                          - ready
                          - pending
                          - onboarding
                          - suspended
                          - resumed
                          - uninstalled
                        description: >-
                          The configuration status. Optional. If not defined,
                          assume 'ready'.
                      externalId:
                        type: string
                        description: >-
                          An external identifier defined by the integration
                          vendor.
                      projects:
                        items:
                          type: string
                        type: array
                        description: >-
                          When a configuration is limited to access certain
                          projects, this will contain each of the project ID it
                          is allowed to access. If it is not defined, the
                          configuration has full access.
                        example:
                          - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
                      source:
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
                        description: >-
                          Source defines where the configuration was installed
                          from. It is used to analyze user engagement for
                          integration installations in product metrics.
                        example: marketplace
                      slug:
                        type: string
                        description: >-
                          The slug of the integration the configuration is
                          created for.
                        example: slack
                      teamId:
                        nullable: true
                        type: string
                        description: >-
                          When the configuration was created for a team, this
                          will show the ID of the team.
                        example: team_nLlpyC6RE1qxydlFKbrxDlud
                      type:
                        type: string
                        enum:
                          - integration-configuration
                      updatedAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          updated.
                        example: 1558531915505
                      userId:
                        type: string
                        description: The ID of the user that created the configuration.
                        example: kr1PsOIzqEL5Xg6M4VZcZosf
                      scopes:
                        items:
                          type: string
                        type: array
                        description: >-
                          The resources that are allowed to be accessed by the
                          configuration.
                        example:
                          - read:project
                          - read-write:log-drain
                      disabledAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          disabled. Note: Configurations can be disabled when
                          the associated user loses access to a team. They do
                          not function during this time until the configuration
                          is 'transferred', meaning the associated user is
                          changed to one with access to the team.
                        example: 1558531915505
                      deletedAt:
                        nullable: true
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          deleted.
                        example: 1558531915505
                      deleteRequestedAt:
                        nullable: true
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration
                          deletion has been started for cases when the deletion
                          needs to be settled/approved by partners, such as when
                          marketplace invoices have been paid.
                        example: 1558531915505
                      disabledReason:
                        type: string
                        enum:
                          - disabled-by-owner
                          - feature-not-available
                          - disabled-by-admin
                          - original-owner-left-the-team
                          - account-plan-downgrade
                          - original-owner-role-downgraded
                      installationType:
                        type: string
                        enum:
                          - marketplace
                          - external
                        description: >-
                          Defines the installation type. - 'external'
                          integrations are installed via the existing
                          integrations flow - 'marketplace' integrations are
                          natively installed: - when accepting the TOS of a
                          partner during the store creation process - if
                          undefined, assume 'external'
                    required:
                      - createdAt
                      - id
                      - integrationId
                      - ownerId
                      - scopes
                      - slug
                      - type
                      - updatedAt
                      - userId
                    type: object
                    description: The configuration with the provided id
                  - properties:
                      completedAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          installed successfully
                        example: 1558531915505
                      createdAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          created
                        example: 1558531915505
                      id:
                        type: string
                        description: The unique identifier of the configuration
                        example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                      integrationId:
                        type: string
                        description: >-
                          The unique identifier of the app the configuration was
                          created for
                        example: oac_xzpVzcUOgcB1nrVlirtKhbWV
                      ownerId:
                        type: string
                        description: The user or team ID that owns the configuration
                        example: kr1PsOIzqEL5Xg6M4VZcZosf
                      status:
                        type: string
                        enum:
                          - error
                          - ready
                          - pending
                          - onboarding
                          - suspended
                          - resumed
                          - uninstalled
                        description: >-
                          The configuration status. Optional. If not defined,
                          assume 'ready'.
                      externalId:
                        type: string
                        description: >-
                          An external identifier defined by the integration
                          vendor.
                      projects:
                        items:
                          type: string
                        type: array
                        description: >-
                          When a configuration is limited to access certain
                          projects, this will contain each of the project ID it
                          is allowed to access. If it is not defined, the
                          configuration has full access.
                        example:
                          - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
                      source:
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
                        description: >-
                          Source defines where the configuration was installed
                          from. It is used to analyze user engagement for
                          integration installations in product metrics.
                        example: marketplace
                      slug:
                        type: string
                        description: >-
                          The slug of the integration the configuration is
                          created for.
                        example: slack
                      teamId:
                        nullable: true
                        type: string
                        description: >-
                          When the configuration was created for a team, this
                          will show the ID of the team.
                        example: team_nLlpyC6RE1qxydlFKbrxDlud
                      type:
                        type: string
                        enum:
                          - integration-configuration
                      updatedAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          updated.
                        example: 1558531915505
                      userId:
                        type: string
                        description: The ID of the user that created the configuration.
                        example: kr1PsOIzqEL5Xg6M4VZcZosf
                      scopes:
                        items:
                          type: string
                        type: array
                        description: >-
                          The resources that are allowed to be accessed by the
                          configuration.
                        example:
                          - read:project
                          - read-write:log-drain
                      disabledAt:
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          disabled. Note: Configurations can be disabled when
                          the associated user loses access to a team. They do
                          not function during this time until the configuration
                          is 'transferred', meaning the associated user is
                          changed to one with access to the team.
                        example: 1558531915505
                      deletedAt:
                        nullable: true
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration was
                          deleted.
                        example: 1558531915505
                      deleteRequestedAt:
                        nullable: true
                        type: number
                        description: >-
                          A timestamp that tells you when the configuration
                          deletion has been started for cases when the deletion
                          needs to be settled/approved by partners, such as when
                          marketplace invoices have been paid.
                        example: 1558531915505
                      disabledReason:
                        type: string
                        enum:
                          - disabled-by-owner
                          - feature-not-available
                          - disabled-by-admin
                          - original-owner-left-the-team
                          - account-plan-downgrade
                          - original-owner-role-downgraded
                      installationType:
                        type: string
                        enum:
                          - marketplace
                          - external
                        description: >-
                          Defines the installation type. - 'external'
                          integrations are installed via the existing
                          integrations flow - 'marketplace' integrations are
                          natively installed: - when accepting the TOS of a
                          partner during the store creation process - if
                          undefined, assume 'external'
                    type: object
                    description: >-
                      A configuration represents information about a single
                      installation of an integration within an individual or
                      team account
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: The configuration was not found
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````