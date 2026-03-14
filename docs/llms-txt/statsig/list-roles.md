# Source: https://docs.statsig.com/api-reference/roles/list-roles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Roles



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/roles
openapi: 3.0.0
info:
  title: Console API
  description: >-
    The "Console API" is the CRUD API for performing the actions offered on
    console.statsig.com without needing to go through the web UI.

    If you have any feature requests, drop on in to our [slack
    channel](https://www.statsig.com/slack) and let us know.

    <br /><br />

    <b>Authorization</b>

    <br />

    All requests must include the **STATSIG-API-KEY** field in the header. The
    value should be a **Console API Key** which can be created in the Project
    Settings on
    [console.statsig.com/api_keys](https://console.statsig.com/api_keys)

    <br /><br />

    <b>Rate Limiting</b>

    <br />

    Requests to the Console API are limited to <code>~ 100reqs / 10secs and ~
    900reqs / 15 mins</code>.

    <br /><br />

    <b>Keyboard Search</b>

    <br />

    Use <code>Ctrl/Cmd + K</code> to search for specific endpoints.
  version: 20240601.0.0
  contact: {}
servers:
  - url: https://statsigapi.net
security: []
tags: []
paths:
  /console/v1/roles:
    get:
      tags:
        - Roles
      summary: List Roles
      parameters:
        - name: limit
          required: false
          in: query
          description: Results per page
          schema:
            example: 10
            oneOf:
              - type: string
              - type: number
            type: integer
        - name: page
          required: false
          in: query
          description: Page number
          schema:
            example: 1
            oneOf:
              - type: string
              - type: number
            type: integer
      responses:
        '200':
          description: List Roles Response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/RoleContractDto'
                example:
                  message: Roles listed successfully.
                  data:
                    - name: Custom Role
                      permissions:
                        invitation_access: false
                        create_configs: false
                        edit_or_delete_configs: false
                        launch_to_production: false
                        launch_or_disable_configs: false
                        start_experiments: false
                        create_or_edit_templates: false
                        create_or_edit_dashboards: false
                        create_teams: false
                        edit_dynamic_config_schemas: false
                        create_release_pipelines: false
                        approve_required_review_release_pipeline_phase: false
                        self_approve_review: false
                        approve_reviews: false
                        bypass_reviews_for_overrides: false
                        metric_management: false
                        verify_metrics: false
                        use_metrics_explorer: false
                        local_metrics: false
                        manage_alerts: false
                        integrations_edit_access: false
                        source_connection_and_creation: false
                        data_warehouse_ingestion_and_exports_edit_access: false
                        edit_and_tag_configs_with_core_tag: false
                        reset_experiments: false
                  pagination:
                    itemsPerPage: 100
                    pageNumber: 1
                    totalItems: 1
                    nextPage: null
                    previousPage: null
                    all: /console/v1/roles
              example:
                message: Roles listed successfully.
                data:
                  - name: Custom Role
                    permissions:
                      invitation_access: false
                      create_configs: false
                      edit_or_delete_configs: false
                      launch_to_production: false
                      launch_or_disable_configs: false
                      start_experiments: false
                      create_or_edit_templates: false
                      create_or_edit_dashboards: false
                      create_teams: false
                      edit_dynamic_config_schemas: false
                      create_release_pipelines: false
                      approve_required_review_release_pipeline_phase: false
                      self_approve_review: false
                      approve_reviews: false
                      bypass_reviews_for_overrides: false
                      metric_management: false
                      verify_metrics: false
                      use_metrics_explorer: false
                      local_metrics: false
                      manage_alerts: false
                      integrations_edit_access: false
                      source_connection_and_creation: false
                      data_warehouse_ingestion_and_exports_edit_access: false
                      edit_and_tag_configs_with_core_tag: false
                      reset_experiments: false
                pagination:
                  itemsPerPage: 100
                  pageNumber: 1
                  totalItems: 1
                  nextPage: null
                  previousPage: null
                  all: /console/v1/roles
        '400':
          description: Invalid request. Please check the request input and try again.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 400
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Invalid Request:
                  value:
                    status: 400
                    message: >-
                      Invalid request. Please check the request input and try
                      again.
        '401':
          description: >-
            This endpoint only accepts an active CONSOLE key, but an invalid key
            was sent. Key: console-xxxXXXxxxXXXxxx
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 401
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Invalid Endpoint:
                  value:
                    status: 401
                    message: >-
                      This endpoint only accepts an active CONSOLE key, but an
                      invalid key was sent. Key: console-xxxXXXxxxXXXxxx
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    PaginationResponseWithMessage:
      type: object
      properties:
        message:
          type: string
          description: A simple string explaining the result of the operation.
        data:
          description: Array of results returned by pagination limit.
          type: array
          items:
            type: object
        pagination:
          description: Pagination metadata for checking if there is next page for example.
          allOf:
            - $ref: '#/components/schemas/PaginationResponseMetadataDto'
      required:
        - message
        - data
        - pagination
    RoleContractDto:
      type: object
      properties:
        name:
          type: string
          description: The name of the role.
        permissions:
          type: object
          properties:
            invitation_access:
              type: boolean
            create_configs:
              type: boolean
            edit_or_delete_configs:
              type: boolean
            launch_to_production:
              type: boolean
            launch_or_disable_configs:
              type: boolean
            start_experiments:
              type: boolean
            create_or_edit_templates:
              type: boolean
            create_or_edit_dashboards:
              type: boolean
            create_teams:
              type: boolean
            edit_dynamic_config_schemas:
              type: boolean
            create_release_pipelines:
              type: boolean
            approve_required_review_release_pipeline_phase:
              type: boolean
            self_approve_review:
              type: boolean
            approve_reviews:
              type: boolean
            bypass_reviews_for_overrides:
              type: boolean
            bypass_precommit_webhook:
              type: boolean
            metric_management:
              type: boolean
            event_dimensions_access:
              type: boolean
            verify_metrics:
              type: boolean
            use_metrics_explorer:
              type: boolean
            local_metrics:
              type: boolean
            manage_alerts:
              type: boolean
            integrations_edit_access:
              type: boolean
            source_connection_and_creation:
              type: boolean
            whn_connection:
              type: boolean
            data_warehouse_ingestion_and_exports_edit_access:
              type: boolean
            edit_and_tag_configs_with_core_tag:
              type: boolean
            reset_experiments:
              type: boolean
            manual_whn_reload:
              type: boolean
          description: The permissions of the role.
      required:
        - name
        - permissions
    PaginationResponseMetadataDto:
      type: object
      properties:
        itemsPerPage:
          type: number
          format: double
        pageNumber:
          type: number
          format: double
        nextPage:
          type: string
          nullable: true
        previousPage:
          type: string
          nullable: true
        totalItems:
          type: number
          format: double
        all:
          type: string
      required:
        - itemsPerPage
        - pageNumber
        - nextPage
        - previousPage
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).