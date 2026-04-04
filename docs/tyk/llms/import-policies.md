# Source: https://tyk.io/docs/api-reference/import/import-policies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import Policies

> The import Policies operates on lists of Policies.



## OpenAPI

````yaml swagger/5.8/dashboard-admin-swagger.yml post /admin/policies/import
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
  /admin/policies/import:
    post:
      tags:
        - Import
      summary: Import Policies
      description: The import Policies operates on lists of Policies.
      operationId: importPolicies
      requestBody:
        content:
          application/json:
            example:
              Data:
                - _id: ''
                  access_rights: null
                  active: true
                  date_created: '0001-01-01T00:00:00Z'
                  hmac_enabled: false
                  id: ''
                  is_inactive: false
                  key_expires_in: 0
                  last_updated: '1478791603'
                  max_query_depth: 0
                  meta_data: null
                  name: Default
                  org_id: 53ac07777cbb8c2d53000002
                  partitions:
                    acl: false
                    complexity: false
                    per_api: false
                    quota: false
                    rate_limit: false
                  per: 60
                  quota_max: -1
                  quota_renewal_rate: 3600
                  rate: 1000
                  smoothing: null
                  tags: []
                  throttle_interval: 0
                  throttle_retry_limit: 0
              Pages: 0
            schema:
              $ref: '#/components/schemas/ImportDataStruct'
      responses:
        '200':
          content:
            application/json:
              example:
                Message: Policies imported
                Meta:
                  61df10078f11dd00097cb55f: true
                Status: OK
              schema:
                $ref: '#/components/schemas/ApiError'
          description: OK
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
        '403':
          content:
            application/json:
              example:
                Message: Request body malformed
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Forbidden
        '500':
          content:
            application/json:
              example:
                Message: Failed to read response body, body empty
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Internal Server Error
components:
  schemas:
    ImportDataStruct:
      properties:
        Data:
          items:
            $ref: '#/components/schemas/DBPolicy'
          nullable: true
          type: array
        Pages:
          type: integer
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
    DBPolicy:
      properties:
        _id:
          type: string
        access_rights:
          additionalProperties:
            $ref: '#/components/schemas/DBAccessDefinition'
          nullable: true
          type: object
        active:
          type: boolean
        date_created:
          format: date-time
          type: string
        hmac_enabled:
          type: boolean
        id:
          type: string
        is_inactive:
          type: boolean
        key_expires_in:
          format: int64
          type: integer
        last_updated:
          type: string
        max_query_depth:
          type: integer
        meta_data:
          additionalProperties: {}
          nullable: true
          type: object
        name:
          type: string
        org_id:
          type: string
        partitions:
          properties:
            acl:
              type: boolean
            complexity:
              type: boolean
            per_api:
              type: boolean
            quota:
              type: boolean
            rate_limit:
              type: boolean
          type: object
        per:
          format: double
          type: number
        quota_max:
          format: int64
          type: integer
        quota_renewal_rate:
          format: int64
          type: integer
        rate:
          format: double
          type: number
        smoothing:
          $ref: '#/components/schemas/RateLimitSmoothing'
        tags:
          items:
            type: string
          nullable: true
          type: array
        throttle_interval:
          format: double
          type: number
        throttle_retry_limit:
          type: integer
      type: object
    DBAccessDefinition:
      properties:
        allowed_types:
          items:
            $ref: '#/components/schemas/GraphqlType'
          nullable: true
          type: array
        allowed_urls:
          items:
            $ref: '#/components/schemas/AccessSpec'
          nullable: true
          type: array
        api_id:
          type: string
        api_name:
          type: string
        disable_introspection:
          type: boolean
        endpoints:
          items:
            $ref: '#/components/schemas/SessionEndpoint'
          type: array
        restricted_types:
          items:
            $ref: '#/components/schemas/GraphqlType'
          nullable: true
          type: array
        versions:
          items:
            type: string
          nullable: true
          type: array
      type: object
    RateLimitSmoothing:
      nullable: true
      properties:
        delay:
          format: int64
          type: integer
        enabled:
          type: boolean
        step:
          format: int64
          type: integer
        threshold:
          format: int64
          type: integer
        trigger:
          format: double
          type: number
      type: object
    GraphqlType:
      properties:
        fields:
          items:
            type: string
          nullable: true
          type: array
        name:
          type: string
      type: object
    AccessSpec:
      properties:
        methods:
          items:
            type: string
          nullable: true
          type: array
        url:
          type: string
      type: object
    SessionEndpoint:
      properties:
        methods:
          items:
            $ref: '#/components/schemas/SessionEndpointMethod'
          type: array
        path:
          type: string
      type: object
    SessionEndpointMethod:
      properties:
        limit:
          $ref: '#/components/schemas/SessionEndpointRateLimit'
        name:
          type: string
      type: object
    SessionEndpointRateLimit:
      properties:
        per:
          format: int64
          type: integer
        rate:
          format: int64
          type: integer
      type: object
  securitySchemes:
    api_key:
      description: Api key
      in: header
      name: Admin-Auth
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).