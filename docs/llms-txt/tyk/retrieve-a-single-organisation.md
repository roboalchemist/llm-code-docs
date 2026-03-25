# Source: https://tyk.io/docs/api-reference/organisations/retrieve-a-single-organisation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a single organisation

> Retrieve a single organisation



## OpenAPI

````yaml swagger/5.8/dashboard-admin-swagger.yml get /admin/organisations/{orgID}
openapi: 3.0.3
info:
  contact:
    email: support@tyk.io
    name: Tyk Technologies
    url: https://tyk.io/contact
  description: >-
    <img src="https://tyk.io/docs/img/dashboard_admin_swagger_image.png"
    width="963" height="250">


    For Tyk On-Premises installations only, the Dashboard Admin API has two
    endpoints and is used to set up and provision a Tyk Dashboard instance
    without the command line.


    In order to use the Dashboard Admin API, you'll need to get the
    `admin_secret` value from your Tyk Dashboard configurations.


    The secret you set should then be sent along as a header with each Dashboard
    Admin API Request in order for it to be successful:


    ```

    admin-auth: <your-secret>

    ```
  license:
    name: Mozilla Public License Version 2.0
    url: https://github.com/TykTechnologies/tyk/blob/master/LICENSE.md
  title: Tyk Dashboard Admin API
  version: 5.8.0
servers:
  - url: https://{tenant}
    variables:
      tenant:
        default: localhost:3000
        description: Your dashboard host
security:
  - api_key: []
tags:
  - description: >-
      The import API enables you to add Organisations, APIs and Policies back
      into a Tyk installation while retaining their base IDs so that they work
      together.
    name: Import
  - description: >-
      To make Tyk installations more portable, the Export API enables you to
      export key configuration objects required to back-up and re-deploy a basic
      Tyk Pro installation.
    name: Export
  - description: >-
      The admin portion of the users API gives you the ability to manage
      password reset policies for your Dashboard users.
    name: Users
  - description: >-
      Since the Dashboard can have multiple URLs associated with it. It is
      possible to force a URL reload by calling an API endpoint of the Dashboard
      API.
    name: Dashboard URL Reload
  - description: >-
      The organisations API gives the ability to manage your Tyk
      organisation(s).
    name: Organisations
  - description: >-
      The Dashboard exposes the /admin/sso Dashboard API which allows you to
      generate a temporary authentication token, valid for 60 seconds.
    name: Single Sign On
paths:
  /admin/organisations/{orgID}:
    get:
      tags:
        - Organisations
      summary: Retrieve a single organisation
      description: Retrieve a single organisation
      operationId: getOrg
      parameters:
        - description: Organisation ID of the org to add, update, or delete.
          example: 5e9f9b9b4d7b4a0020e3c4f5
          in: path
          required: true
          name: orgID
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              example:
                apis:
                  - api_human_name: API 2
                    api_id: 5fa2db834e07444f760b7ceb314209fb
                  - api_human_name: API 1
                    api_id: 7a6ddeca9244448a4233866938a0d6e2
                  - api_human_name: API 3
                    api_id: 109eacaa50b24b64651a1d4dce8ec385
                cname: my.domain.com
                cname_enabled: true
                developer_count: 21
                developer_quota: 123
                event_options:
                  key_event:
                    email: ''
                    redis: true
                    webhook: ''
                  key_request_event:
                    email: ''
                    redis: false
                    webhook: ''
                hybrid_enabled: false
                id: 53ac07777cbb8c2d53000002
                owner_name: Test
                owner_slug: test
                ui:
                  default_lang: ''
                  designer: {}
                  dont_allow_license_management: false
                  dont_allow_license_management_view: false
                  dont_show_admin_sockets: false
                  hide_help: false
                  languages: {}
                  login_page: {}
                  nav: {}
                  portal_section: {}
                  uptime: {}
              schema:
                $ref: '#/components/schemas/OrganisationDocument'
          description: Organisation retrieved
        '401':
          content:
            application/json:
              example:
                Message: Not authorised
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Unauthorized
        '404':
          content:
            application/json:
              example:
                Message: Could not retrieve org detail
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Org not found.
        '500':
          content:
            application/json:
              example:
                Message: Failed to marshal org data from DB
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Failed to marshal org data from DB
components:
  schemas:
    OrganisationDocument:
      properties:
        additional_permissions:
          additionalProperties:
            type: string
          nullable: true
          type: object
        apis:
          items:
            $ref: '#/components/schemas/ApiDocument'
          nullable: true
          type: array
        cname:
          type: string
        cname_enabled:
          type: boolean
        developer_count:
          type: integer
        developer_quota:
          type: integer
        event_options:
          additionalProperties:
            $ref: '#/components/schemas/EventConfig'
          nullable: true
          type: object
        hybrid_enabled:
          type: boolean
        id:
          type: string
        open_policy:
          $ref: '#/components/schemas/OpenPolicyConf'
        org_options_meta:
          additionalProperties: {}
          nullable: true
          type: object
        owner_name:
          type: string
        owner_slug:
          type: string
        sso_enabled:
          type: boolean
        ui:
          $ref: '#/components/schemas/ConfigUIOptions'
      type: object
    ApiError:
      properties:
        ID:
          type: string
        Message:
          type: string
        Meta: {}
        Status:
          type: string
      type: object
    ApiDocument:
      properties:
        api_human_name:
          type: string
        api_id:
          type: string
      type: object
    EventConfig:
      properties:
        email:
          type: string
        redis:
          type: boolean
        webhook:
          type: string
      type: object
    OpenPolicyConf:
      properties:
        enabled:
          type: boolean
        rules:
          type: string
      type: object
    ConfigUIOptions:
      properties:
        cloud:
          type: boolean
        cloudmenu:
          type: boolean
        default_lang:
          type: string
        designer:
          additionalProperties: {}
          nullable: true
          type: object
        dev:
          type: boolean
        dont_allow_license_management:
          type: boolean
        dont_allow_license_management_view:
          type: boolean
        dont_show_admin_sockets:
          type: boolean
        hide_help:
          type: boolean
        labs:
          $ref: '#/components/schemas/ConfigLabsConfig'
        languages:
          additionalProperties:
            type: string
          nullable: true
          type: object
        login_page:
          additionalProperties: {}
          nullable: true
          type: object
        nav:
          additionalProperties: {}
          nullable: true
          type: object
        onboarding:
          $ref: '#/components/schemas/ConfigOnboarding'
        portal_section:
          additionalProperties: {}
          nullable: true
          type: object
        trial:
          $ref: '#/components/schemas/ConfigTrial'
        uptime:
          additionalProperties: {}
          nullable: true
          type: object
      type: object
    ConfigLabsConfig:
      nullable: true
      properties:
        streaming:
          additionalProperties: {}
          nullable: true
          type: object
      type: object
    ConfigOnboarding:
      properties:
        enabled:
          type: boolean
      type: object
    ConfigTrial:
      properties:
        end_date:
          format: int64
          type: integer
        hubspot_form:
          $ref: '#/components/schemas/ConfigHubspotForm'
      type: object
    ConfigHubspotForm:
      properties:
        form_id:
          type: string
        portal_id:
          type: string
        region:
          type: string
      type: object
  securitySchemes:
    api_key:
      description: Api key
      in: header
      name: Admin-Auth
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).