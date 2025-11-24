# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/get-configurations-for-the-authenticated-user-or-team.md

# Get configurations for the authenticated user or team

> Allows to retrieve all configurations for an authenticated integration. When the `project` view is used, configurations generated for the authorization flow will be filtered out of the results.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configurations
paths:
  path: /v1/integrations/configurations
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
      path: {}
      query:
        view:
          schema:
            - type: enum<string>
              enum:
                - account
                - project
              required: true
        installationType:
          schema:
            - type: enum<string>
              enum:
                - marketplace
                - external
              required: false
        integrationIdOrSlug:
          schema:
            - type: string
              required: false
              description: ID of the integration
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
      - label: getConfigurations
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Integrations.GetConfigurations(ctx, operations.GetConfigurationsRequest{\n        View: operations.ViewAccount,\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getConfigurations
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.getConfigurations({
              view: "account",
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
          - type: array
            items:
              allOf:
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
                    projects:
                      items:
                        type: string
                      type: array
                      description: >-
                        When a configuration is limited to access certain
                        projects, this will contain each of the project ID it is
                        allowed to access. If it is not defined, the
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
                      description: >-
                        Source defines where the configuration was installed
                        from. It is used to analyze user engagement for
                        integration installations in product metrics.
                      example: marketplace
                    slug:
                      type: string
                      description: >-
                        The slug of the integration the configuration is created
                        for.
                      example: slack
                    teamId:
                      nullable: true
                      type: string
                      description: >-
                        When the configuration was created for a team, this will
                        show the ID of the team.
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
                        disabled. Note: Configurations can be disabled when the
                        associated user loses access to a team. They do not
                        function during this time until the configuration is
                        'transferred', meaning the associated user is changed to
                        one with access to the team.
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
                        Defines the installation type. - 'external' integrations
                        are installed via the existing integrations flow -
                        'marketplace' integrations are natively installed: -
                        when accepting the TOS of a partner during the store
                        creation process - if undefined, assume 'external'
                  type: object
                  description: The list of configurations for the authenticated user
            description: The list of configurations for the authenticated user
          - type: array
            items:
              allOf:
                - properties:
                    integration:
                      properties:
                        name:
                          type: string
                        icon:
                          type: string
                        isLegacy:
                          type: boolean
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
                        - name
                        - icon
                        - isLegacy
                      type: object
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
                    projects:
                      items:
                        type: string
                      type: array
                      description: >-
                        When a configuration is limited to access certain
                        projects, this will contain each of the project ID it is
                        allowed to access. If it is not defined, the
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
                      description: >-
                        Source defines where the configuration was installed
                        from. It is used to analyze user engagement for
                        integration installations in product metrics.
                      example: marketplace
                    slug:
                      type: string
                      description: >-
                        The slug of the integration the configuration is created
                        for.
                      example: slack
                    teamId:
                      nullable: true
                      type: string
                      description: >-
                        When the configuration was created for a team, this will
                        show the ID of the team.
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
                        disabled. Note: Configurations can be disabled when the
                        associated user loses access to a team. They do not
                        function during this time until the configuration is
                        'transferred', meaning the associated user is changed to
                        one with access to the team.
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
                        Defines the installation type. - 'external' integrations
                        are installed via the existing integrations flow -
                        'marketplace' integrations are natively installed: -
                        when accepting the TOS of a partner during the store
                        creation process - if undefined, assume 'external'
                  required:
                    - integration
                    - createdAt
                    - id
                    - integrationId
                    - ownerId
                    - slug
                    - type
                    - updatedAt
                    - userId
                    - scopes
                  type: object
        examples:
          example:
            value:
              - completedAt: 1558531915505
                createdAt: 1558531915505
                id: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                integrationId: oac_xzpVzcUOgcB1nrVlirtKhbWV
                ownerId: kr1PsOIzqEL5Xg6M4VZcZosf
                projects:
                  - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
                source: marketplace
                slug: slack
                teamId: team_nLlpyC6RE1qxydlFKbrxDlud
                type: integration-configuration
                updatedAt: 1558531915505
                userId: kr1PsOIzqEL5Xg6M4VZcZosf
                scopes:
                  - read:project
                  - read-write:log-drain
                disabledAt: 1558531915505
                deletedAt: 1558531915505
                deleteRequestedAt: 1558531915505
                disabledReason: disabled-by-owner
                installationType: marketplace
        description: The list of configurations for the authenticated user
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
  deprecated: false
  type: path
components:
  schemas: {}

````