# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/get-configurations-for-the-authenticated-user-or-team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get configurations for the authenticated user or team

> Allows to retrieve all configurations for an authenticated integration. When the `project` view is used, configurations generated for the authorization flow will be filtered out of the results.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configurations
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
  /v1/integrations/configurations:
    get:
      tags:
        - integrations
      summary: Get configurations for the authenticated user or team
      description: >-
        Allows to retrieve all configurations for an authenticated integration.
        When the `project` view is used, configurations generated for the
        authorization flow will be filtered out of the results.
      operationId: getConfigurations
      parameters:
        - name: view
          in: query
          required: true
          schema:
            type: string
            enum:
              - account
              - project
        - name: installationType
          in: query
          required: false
          schema:
            type: string
            enum:
              - marketplace
              - external
              - provisioning
        - name: integrationIdOrSlug
          description: ID of the integration
          in: query
          required: false
          schema:
            type: string
            description: ID of the integration
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
          description: The list of configurations for the authenticated user
          content:
            application/json:
              schema:
                oneOf:
                  - items:
                      properties:
                        completedAt:
                          type: number
                          description: >-
                            A timestamp that tells you when the configuration
                            was installed successfully
                          example: 1558531915505
                        createdAt:
                          type: number
                          description: >-
                            A timestamp that tells you when the configuration
                            was created
                          example: 1558531915505
                        id:
                          type: string
                          description: The unique identifier of the configuration
                          example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                        integrationId:
                          type: string
                          description: >-
                            The unique identifier of the app the configuration
                            was created for
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
                            projects, this will contain each of the project ID
                            it is allowed to access. If it is not defined, the
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
                            A timestamp that tells you when the configuration
                            was updated.
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
                            A timestamp that tells you when the configuration
                            was disabled. Note: Configurations can be disabled
                            when the associated user loses access to a team.
                            They do not function during this time until the
                            configuration is 'transferred', meaning the
                            associated user is changed to one with access to the
                            team.
                          example: 1558531915505
                        deletedAt:
                          nullable: true
                          type: number
                          description: >-
                            A timestamp that tells you when the configuration
                            was deleted.
                          example: 1558531915505
                        deleteRequestedAt:
                          nullable: true
                          type: number
                          description: >-
                            A timestamp that tells you when the configuration
                            deletion has been started for cases when the
                            deletion needs to be settled/approved by partners,
                            such as when marketplace invoices have been paid.
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
                      description: The list of configurations for the authenticated user
                    type: array
                    description: The list of configurations for the authenticated user
                  - items:
                      properties:
                        integration:
                          properties:
                            name:
                              type: string
                            icon:
                              type: string
                            isLegacy:
                              type: boolean
                              enum:
                                - false
                                - true
                            flags:
                              items:
                                type: string
                              type: array
                            assignedBetaLabelAt:
                              type: number
                            tagIds:
                              items:
                                type: string
                                enum:
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
                              type: array
                          required:
                            - icon
                            - isLegacy
                            - name
                          type: object
                        completedAt:
                          type: number
                          description: >-
                            A timestamp that tells you when the configuration
                            was installed successfully
                          example: 1558531915505
                        createdAt:
                          type: number
                          description: >-
                            A timestamp that tells you when the configuration
                            was created
                          example: 1558531915505
                        id:
                          type: string
                          description: The unique identifier of the configuration
                          example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                        integrationId:
                          type: string
                          description: >-
                            The unique identifier of the app the configuration
                            was created for
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
                            projects, this will contain each of the project ID
                            it is allowed to access. If it is not defined, the
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
                            A timestamp that tells you when the configuration
                            was updated.
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
                            A timestamp that tells you when the configuration
                            was disabled. Note: Configurations can be disabled
                            when the associated user loses access to a team.
                            They do not function during this time until the
                            configuration is 'transferred', meaning the
                            associated user is changed to one with access to the
                            team.
                          example: 1558531915505
                        deletedAt:
                          nullable: true
                          type: number
                          description: >-
                            A timestamp that tells you when the configuration
                            was deleted.
                          example: 1558531915505
                        deleteRequestedAt:
                          nullable: true
                          type: number
                          description: >-
                            A timestamp that tells you when the configuration
                            deletion has been started for cases when the
                            deletion needs to be settled/approved by partners,
                            such as when marketplace invoices have been paid.
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
                        - integration
                        - integrationId
                        - ownerId
                        - scopes
                        - slug
                        - type
                        - updatedAt
                        - userId
                      type: object
                    type: array
        '400':
          description: One of the provided values in the request query is invalid.
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