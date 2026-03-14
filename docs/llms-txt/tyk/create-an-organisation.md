# Source: https://tyk.io/docs/api-reference/organisations/create-an-organisation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an Organisation

> Create an Organisation



## OpenAPI

````yaml swagger/5.8/dashboard-admin-swagger.yml post /admin/organisations
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
  /admin/organisations:
    post:
      tags:
        - Organisations
      summary: Create an Organisation
      description: Create an Organisation
      operationId: createOrg
      requestBody:
        content:
          application/json:
            example:
              cname: jive.ly
              cname_enabled: true
              owner_name: Jively
            schema:
              $ref: '#/components/schemas/OrganisationDocument'
      responses:
        '200':
          content:
            application/json:
              example:
                Message: Org created
                Meta: 54b53d3aeba6db5c35000002
                Status: OK
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Organisation created
        '403':
          content:
            application/json:
              example:
                Message: Request body malformed
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Unmarshalling request body failed, malformed
        '500':
          content:
            application/json:
              example:
                Message: Failed to read response body, body empty
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Could not read request body
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