# Source: https://tyk.io/docs/api-reference/keys/create-a-key.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a key

> Creates a key.

## OpenAPI

````yaml swagger/5.8/dashboard-admin-swagger.yml post /admin/org/keys
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
  /admin/org/keys:
    post:
      tags:
        - keys
      summary: Create a key.
      description: Creates a key.
      operationId: createOrgKey
      requestBody:
        content:
          application/json:
            example:
              alias: portal-key
              allowance: 1000
              apply_policies:
                - 62a0ec9092faf50001395817
              enable_detailed_recording: true
              expires: 1718439136
              hmac_enabled: false
              is_inactive: false
              meta_data:
                tyk_developer_id: 62b3fb9a1d5e4f00017226f5
              org_id: 5e9d9544a1dcd60001d0ed20
              per: 60
              quota_max: -1
              quota_remaining: 0
              quota_renewal_rate: -1
              quota_renews: 1715847135
              rate: 1000
              tags:
                - edge-eu
                - edge
              throttle_interval: 0
              throttle_retry_limit: 0
            schema:
              $ref: '#/components/schemas/SessionState'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/KeyData'
          description: Key added successfully
        '403':
          content:
            application/json:
              example:
                Message: 'Failed to save new session object to Tyk:'
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: 'Failed to save new session object to Tyk:'
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
    SessionState:
      properties:
        access_rights:
          additionalProperties:
            $ref: '#/components/schemas/AccessDefinition'
          nullable: true
          type: object
        alias:
          type: string
        allowance:
          format: double
          type: number
        apply_policies:
          items:
            type: string
          nullable: true
          type: array
        apply_policy_id:
          type: string
        basic_auth_data:
          properties:
            hash_type:
              type: string
            password:
              type: string
            user:
              type: string
          type: object
        certificate:
          type: string
        data_expires:
          format: int64
          type: integer
        date_created:
          format: date-time
          type: string
        enable_detailed_recording:
          type: boolean
        expires:
          format: int64
          type: integer
        hmac_enabled:
          type: boolean
        hmac_string:
          type: string
        id_extractor_deadline:
          format: int64
          type: integer
        is_inactive:
          type: boolean
        jwt_data:
          properties:
            secret:
              type: string
          type: object
        key_id:
          type: string
        last_check:
          format: int64
          type: integer
        last_updated:
          type: string
        max_query_depth:
          type: integer
        meta_data: {}
        monitor:
          properties:
            trigger_limits:
              items:
                format: double
                type: number
              nullable: true
              type: array
          type: object
        oauth_client_id:
          type: string
        oauth_keys:
          additionalProperties:
            type: string
          nullable: true
          type: object
        org_id:
          type: string
        per:
          format: double
          type: number
        quota_max:
          format: int64
          type: integer
        quota_remaining:
          format: int64
          type: integer
        quota_renewal_rate:
          format: int64
          type: integer
        quota_renews:
          format: int64
          type: integer
        rate:
          format: double
          type: number
        session_lifetime:
          format: int64
          type: integer
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
    KeyData:
      properties:
        api_model:
          $ref: '#/components/schemas/ApiModel'
        data:
          $ref: '#/components/schemas/SessionState'
        key_hash:
          type: string
        key_id:
          type: string
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
    AccessDefinition:
      properties:
        allowance_scope:
          type: string
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
        field_access_rights:
          items:
            $ref: '#/components/schemas/FieldAccessDefinition'
          nullable: true
          type: array
        limit:
          $ref: '#/components/schemas/APILimit'
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
    ApiModel:
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
    FieldAccessDefinition:
      properties:
        field_name:
          type: string
        limits:
          $ref: '#/components/schemas/FieldLimits'
        type_name:
          type: string
      type: object
    APILimit:
      nullable: true
      properties:
        max_query_depth:
          type: integer
        per:
          format: double
          type: number
        quota_max:
          format: int64
          type: integer
        quota_remaining:
          format: int64
          type: integer
        quota_renewal_rate:
          format: int64
          type: integer
        quota_renews:
          format: int64
          type: integer
        rate:
          format: double
          type: number
        set_by_policy:
          type: boolean
        smoothing:
          $ref: '#/components/schemas/RateLimitSmoothing'
        throttle_interval:
          format: double
          type: number
        throttle_retry_limit:
          type: integer
      type: object
    SessionEndpointMethod:
      properties:
        limit:
          $ref: '#/components/schemas/SessionEndpointRateLimit'
        name:
          type: string
      type: object
    FieldLimits:
      properties:
        max_query_depth:
          type: integer
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
