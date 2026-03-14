# Source: https://tyk.io/docs/api-reference/import/import-apis.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import APIs

> The import APIs operates on lists of APIs.

## OpenAPI

````yaml swagger/5.8/dashboard-admin-swagger.yml post /admin/apis/import
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
  /admin/apis/import:
    post:
      tags:
        - Import
      summary: Import APIs
      description: The import APIs operates on lists of APIs.
      operationId: importAPIs
      requestBody:
        content:
          application/json:
            example:
              apis:
                - api_definition:
                    api_id: 5fa2db834e07444f760b7ceb314209fb
                    name: API 2
                  hook_references: []
                  is_streams: false
                  sort_by: 0
            schema:
              $ref: '#/components/schemas/ApiDefinitions'
      responses:
        '200':
          content:
            application/json:
              example:
                Message: APIs imported
                Meta:
                  5fa2db834e07444f760b7ceb314209fb: true
                  7a6ddeca9244448a4233866938a0d6e2: true
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
    ApiDefinitions:
      properties:
        apis:
          items:
            $ref: '#/components/schemas/ApiDefinition'
          nullable: true
          type: array
        pages:
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
    ApiDefinition:
      properties:
        api_definition:
          $ref: '#/components/schemas/APIDefinition'
        api_model:
          $ref: '#/components/schemas/ApiModel'
        categories:
          $ref: '#/components/schemas/Categories'
        created_at:
          format: date-time
          nullable: true
          type: string
        hook_references:
          items:
            $ref: '#/components/schemas/HookReference'
          nullable: true
          type: array
        is_site:
          type: boolean
        is_streams:
          type: boolean
        oas:
          $ref: '#/components/schemas/OAS'
        sort_by:
          type: integer
        updated_at:
          format: date-time
          nullable: true
          type: string
        user_group_owners:
          items:
            type: string
          nullable: true
          type: array
        user_owners:
          items:
            type: string
          nullable: true
          type: array
      type: object
    APIDefinition:
      properties:
        CORS:
          $ref: '#/components/schemas/CORSConfig'
        active:
          type: boolean
        allowed_ips:
          items:
            type: string
          nullable: true
          type: array
        analytics_plugin:
          $ref: '#/components/schemas/AnalyticsPluginConfig'
        api_id:
          type: string
        auth:
          $ref: '#/components/schemas/AuthConfig'
        auth_configs:
          additionalProperties:
            $ref: '#/components/schemas/AuthConfig'
          nullable: true
          type: object
        auth_provider:
          $ref: '#/components/schemas/AuthProviderMeta'
        base_identity_provided_by:
          type: string
        basic_auth:
          properties:
            body_password_regexp:
              type: string
            body_user_regexp:
              type: string
            cache_ttl:
              type: integer
            disable_caching:
              type: boolean
            extract_from_body:
              type: boolean
          type: object
        blacklisted_ips:
          items:
            type: string
          nullable: true
          type: array
        cache_options:
          $ref: '#/components/schemas/CacheOptions'
        certificate_pinning_disabled:
          type: boolean
        certificates:
          items:
            type: string
          nullable: true
          type: array
        client_certificates:
          items:
            type: string
          nullable: true
          type: array
        config_data:
          additionalProperties: {}
          nullable: true
          type: object
        config_data_disabled:
          type: boolean
        custom_middleware:
          $ref: '#/components/schemas/MiddlewareSection'
        custom_middleware_bundle:
          type: string
        custom_middleware_bundle_disabled:
          type: boolean
        custom_plugin_auth_enabled:
          type: boolean
        definition:
          $ref: '#/components/schemas/VersionDefinition'
        detailed_tracing:
          type: boolean
        disable_quota:
          type: boolean
        disable_rate_limit:
          type: boolean
        do_not_track:
          type: boolean
        domain:
          type: string
        domain_disabled:
          type: boolean
        dont_set_quota_on_create:
          type: boolean
        enable_batch_request_support:
          type: boolean
        enable_context_vars:
          type: boolean
        enable_coprocess_auth:
          type: boolean
        enable_detailed_recording:
          type: boolean
        enable_ip_blacklisting:
          type: boolean
        enable_ip_whitelisting:
          type: boolean
        enable_jwt:
          type: boolean
        enable_proxy_protocol:
          type: boolean
        enable_signature_checking:
          type: boolean
        event_handlers:
          $ref: '#/components/schemas/EventHandlerMetaConfig'
        expiration:
          type: string
        expire_analytics_after:
          format: int64
          type: integer
        external_oauth:
          $ref: '#/components/schemas/ExternalOAuth'
        global_rate_limit:
          $ref: '#/components/schemas/GlobalRateLimit'
        graphql:
          $ref: '#/components/schemas/GraphQLConfig'
        hmac_allowed_algorithms:
          items:
            type: string
          nullable: true
          type: array
        hmac_allowed_clock_skew:
          format: double
          type: number
        id:
          type: string
        idp_client_id_mapping_disabled:
          type: boolean
        internal:
          type: boolean
        ip_access_control_disabled:
          type: boolean
        is_oas:
          type: boolean
        jwt_client_base_field:
          type: string
        jwt_default_policies:
          items:
            type: string
          nullable: true
          type: array
        jwt_expires_at_validation_skew:
          minimum: 0
          type: integer
        jwt_identity_base_field:
          type: string
        jwt_issued_at_validation_skew:
          minimum: 0
          type: integer
        jwt_not_before_validation_skew:
          minimum: 0
          type: integer
        jwt_policy_field_name:
          type: string
        jwt_scope_claim_name:
          type: string
        jwt_scope_to_policy_mapping:
          additionalProperties:
            type: string
          nullable: true
          type: object
        jwt_signing_method:
          type: string
        jwt_skip_kid:
          type: boolean
        jwt_source:
          type: string
        listen_port:
          type: integer
        name:
          type: string
        notifications:
          $ref: '#/components/schemas/NotificationsManager'
        oauth_meta:
          properties:
            allowed_access_types:
              items:
                type: string
              nullable: true
              type: array
            allowed_authorize_types:
              items:
                type: string
              nullable: true
              type: array
            auth_login_redirect:
              type: string
          type: object
        openid_options:
          $ref: '#/components/schemas/OpenIDOptions'
        org_id:
          type: string
        pinned_public_keys:
          additionalProperties:
            type: string
          nullable: true
          type: object
        protocol:
          type: string
        proxy:
          $ref: '#/components/schemas/ProxyConfig'
        request_signing:
          $ref: '#/components/schemas/RequestSigningMeta'
        response_processors:
          items:
            $ref: '#/components/schemas/ResponseProcessor'
          nullable: true
          type: array
        scopes:
          $ref: '#/components/schemas/Scopes'
        session_lifetime:
          format: int64
          type: integer
        session_lifetime_respects_key_expiration:
          type: boolean
        session_provider:
          $ref: '#/components/schemas/SessionProviderMeta'
        slug:
          type: string
        strip_auth_data:
          type: boolean
        tag_headers:
          items:
            type: string
          nullable: true
          type: array
        tags:
          items:
            type: string
          nullable: true
          type: array
        tags_disabled:
          type: boolean
        upstream_auth:
          $ref: '#/components/schemas/UpstreamAuth'
        upstream_certificates:
          additionalProperties:
            type: string
          nullable: true
          type: object
        upstream_certificates_disabled:
          type: boolean
        uptime_tests:
          $ref: '#/components/schemas/UptimeTests'
        use_basic_auth:
          type: boolean
        use_go_plugin_auth:
          type: boolean
        use_keyless:
          type: boolean
        use_mutual_tls_auth:
          type: boolean
        use_oauth2:
          type: boolean
        use_openid:
          type: boolean
        use_standard_auth:
          type: boolean
        version_data:
          $ref: '#/components/schemas/VersionData'
      type: object
    ApiModel:
      type: object
    Categories:
      items:
        type: string
      type: array
    HookReference:
      properties:
        event_name:
          type: string
        event_timeout:
          format: int64
          type: integer
        hook:
          $ref: '#/components/schemas/WebHookHandlerConf'
      type: object
    OAS:
      nullable: true
      properties:
        components:
          $ref: '#/components/schemas/Openapi3Components'
        externalDocs:
          $ref: '#/components/schemas/Openapi3ExternalDocs'
        info:
          $ref: '#/components/schemas/Openapi3Info'
        openapi:
          type: string
        paths:
          $ref: '#/components/schemas/Openapi3Paths'
        security:
          $ref: '#/components/schemas/Openapi3SecurityRequirements'
        servers:
          $ref: '#/components/schemas/Openapi3Servers'
        tags:
          $ref: '#/components/schemas/Openapi3Tags'
      type: object
    CORSConfig:
      properties:
        allow_credentials:
          type: boolean
        allowed_headers:
          items:
            type: string
          nullable: true
          type: array
        allowed_methods:
          items:
            type: string
          nullable: true
          type: array
        allowed_origins:
          items:
            type: string
          nullable: true
          type: array
        debug:
          type: boolean
        enable:
          type: boolean
        exposed_headers:
          items:
            type: string
          nullable: true
          type: array
        max_age:
          type: integer
        options_passthrough:
          type: boolean
      type: object
    AnalyticsPluginConfig:
      properties:
        enable:
          type: boolean
        func_name:
          type: string
        plugin_path:
          type: string
      type: object
    AuthConfig:
      properties:
        auth_header_name:
          type: string
        cookie_name:
          type: string
        disable_header:
          type: boolean
        name:
          type: string
        param_name:
          type: string
        signature:
          $ref: '#/components/schemas/SignatureConfig'
        use_certificate:
          type: boolean
        use_cookie:
          type: boolean
        use_param:
          type: boolean
        validate_signature:
          type: boolean
      type: object
    AuthProviderMeta:
      properties:
        meta:
          additionalProperties: {}
          nullable: true
          type: object
        name:
          type: string
        storage_engine:
          type: string
      type: object
    CacheOptions:
      properties:
        cache_all_safe_requests:
          type: boolean
        cache_by_headers:
          items:
            type: string
          nullable: true
          type: array
        cache_control_ttl_header:
          type: string
        cache_response_codes:
          items:
            type: integer
          nullable: true
          type: array
        cache_timeout:
          format: int64
          type: integer
        enable_cache:
          type: boolean
        enable_upstream_cache_control:
          type: boolean
      type: object
    MiddlewareSection:
      properties:
        auth_check:
          $ref: '#/components/schemas/MiddlewareDefinition'
        driver:
          type: string
        id_extractor:
          $ref: '#/components/schemas/MiddlewareIdExtractor'
        post:
          items:
            $ref: '#/components/schemas/MiddlewareDefinition'
          nullable: true
          type: array
        post_key_auth:
          items:
            $ref: '#/components/schemas/MiddlewareDefinition'
          nullable: true
          type: array
        pre:
          items:
            $ref: '#/components/schemas/MiddlewareDefinition'
          nullable: true
          type: array
        response:
          items:
            $ref: '#/components/schemas/MiddlewareDefinition'
          nullable: true
          type: array
      type: object
    VersionDefinition:
      properties:
        default:
          type: string
        enabled:
          type: boolean
        fallback_to_default:
          type: boolean
        key:
          type: string
        location:
          type: string
        name:
          type: string
        strip_path:
          type: boolean
        strip_versioning_data:
          type: boolean
        url_versioning_pattern:
          type: string
        versions:
          additionalProperties:
            type: string
          nullable: true
          type: object
      type: object
    EventHandlerMetaConfig:
      properties:
        events:
          additionalProperties:
            items:
              $ref: '#/components/schemas/EventHandlerTriggerConfig'
            type: array
          nullable: true
          type: object
      type: object
    ExternalOAuth:
      properties:
        enabled:
          type: boolean
        providers:
          items:
            $ref: '#/components/schemas/Provider'
          nullable: true
          type: array
      type: object
    GlobalRateLimit:
      properties:
        disabled:
          type: boolean
        per:
          format: double
          type: number
        rate:
          format: double
          type: number
      type: object
    GraphQLConfig:
      properties:
        enabled:
          type: boolean
        engine:
          $ref: '#/components/schemas/GraphQLEngineConfig'
        execution_mode:
          type: string
        introspection:
          $ref: '#/components/schemas/GraphQLIntrospectionConfig'
        last_schema_update:
          format: date-time
          nullable: true
          type: string
        playground:
          $ref: '#/components/schemas/GraphQLPlayground'
        proxy:
          $ref: '#/components/schemas/GraphQLProxyConfig'
        schema:
          type: string
        subgraph:
          $ref: '#/components/schemas/GraphQLSubgraphConfig'
        supergraph:
          $ref: '#/components/schemas/GraphQLSupergraphConfig'
        type_field_configurations:
          items:
            $ref: '#/components/schemas/DatasourceTypeFieldConfiguration'
          nullable: true
          type: array
        version:
          type: string
      type: object
    NotificationsManager:
      properties:
        oauth_on_keychange_url:
          type: string
        shared_secret:
          type: string
      type: object
    OpenIDOptions:
      properties:
        providers:
          items:
            $ref: '#/components/schemas/OIDProviderConfig'
          nullable: true
          type: array
        segregate_by_client:
          type: boolean
      type: object
    ProxyConfig:
      properties:
        check_host_against_uptime_tests:
          type: boolean
        disable_strip_slash:
          type: boolean
        enable_load_balancing:
          type: boolean
        listen_path:
          type: string
        preserve_host_header:
          type: boolean
        service_discovery:
          $ref: '#/components/schemas/ServiceDiscoveryConfiguration'
        strip_listen_path:
          type: boolean
        target_list:
          items:
            type: string
          nullable: true
          type: array
        target_url:
          type: string
        transport:
          properties:
            proxy_url:
              type: string
            ssl_ciphers:
              items:
                type: string
              nullable: true
              type: array
            ssl_force_common_name_check:
              type: boolean
            ssl_insecure_skip_verify:
              type: boolean
            ssl_max_version:
              minimum: 0
              type: integer
            ssl_min_version:
              minimum: 0
              type: integer
          type: object
      type: object
    RequestSigningMeta:
      properties:
        algorithm:
          type: string
        certificate_id:
          type: string
        header_list:
          items:
            type: string
          nullable: true
          type: array
        is_enabled:
          type: boolean
        key_id:
          type: string
        secret:
          type: string
        signature_header:
          type: string
      type: object
    ResponseProcessor:
      properties:
        name:
          type: string
        options: {}
      type: object
    Scopes:
      properties:
        jwt:
          $ref: '#/components/schemas/ScopeClaim'
        oidc:
          $ref: '#/components/schemas/ScopeClaim'
      type: object
    SessionProviderMeta:
      properties:
        meta:
          additionalProperties: {}
          nullable: true
          type: object
        name:
          type: string
        storage_engine:
          type: string
      type: object
    UpstreamAuth:
      properties:
        basic_auth:
          $ref: '#/components/schemas/UpstreamBasicAuth'
        enabled:
          type: boolean
        oauth:
          $ref: '#/components/schemas/UpstreamOAuth'
      type: object
    UptimeTests:
      properties:
        check_list:
          items:
            $ref: '#/components/schemas/HostCheckObject'
          nullable: true
          type: array
        config:
          $ref: '#/components/schemas/UptimeTestsConfig'
      type: object
    VersionData:
      properties:
        default_version:
          type: string
        not_versioned:
          type: boolean
        versions:
          additionalProperties:
            $ref: '#/components/schemas/VersionInfo'
          nullable: true
          type: object
      type: object
    WebHookHandlerConf:
      properties:
        api_model:
          $ref: '#/components/schemas/ApiModel'
        event_timeout:
          format: int64
          type: integer
        header_map:
          additionalProperties:
            type: string
          nullable: true
          type: object
        id:
          type: string
        method:
          type: string
        name:
          type: string
        org_id:
          type: string
        target_path:
          type: string
        template_path:
          type: string
        webhook_id:
          type: string
      type: object
    Openapi3Components:
      nullable: true
      properties:
        callbacks:
          $ref: '#/components/schemas/Openapi3Callbacks'
        examples:
          $ref: '#/components/schemas/Openapi3Examples'
        headers:
          $ref: '#/components/schemas/Openapi3Headers'
        links:
          $ref: '#/components/schemas/Openapi3Links'
        parameters:
          $ref: '#/components/schemas/Openapi3ParametersMap'
        requestBodies:
          $ref: '#/components/schemas/Openapi3RequestBodies'
        responses:
          $ref: '#/components/schemas/Openapi3Responses'
        schemas:
          $ref: '#/components/schemas/Openapi3Schemas'
        securitySchemes:
          $ref: '#/components/schemas/Openapi3SecuritySchemes'
      type: object
    Openapi3ExternalDocs:
      nullable: true
      properties:
        description:
          type: string
        url:
          type: string
      type: object
    Openapi3Info:
      nullable: true
      properties:
        contact:
          $ref: '#/components/schemas/Openapi3Contact'
        description:
          type: string
        license:
          $ref: '#/components/schemas/Openapi3License'
        termsOfService:
          type: string
        title:
          type: string
        version:
          type: string
      type: object
    Openapi3Paths:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3PathItem'
      type: object
    Openapi3SecurityRequirements:
      items:
        $ref: '#/components/schemas/Openapi3SecurityRequirement'
      nullable: true
      type: array
    Openapi3Servers:
      items:
        $ref: '#/components/schemas/Openapi3Server'
      nullable: true
      type: array
    Openapi3Tags:
      items:
        $ref: '#/components/schemas/Openapi3Tag'
      type: array
    SignatureConfig:
      properties:
        algorithm:
          type: string
        allowed_clock_skew:
          format: int64
          type: integer
        error_code:
          type: integer
        error_message:
          type: string
        header:
          type: string
        param_name:
          type: string
        secret:
          type: string
        use_param:
          type: boolean
      type: object
    MiddlewareDefinition:
      properties:
        disabled:
          type: boolean
        name:
          type: string
        path:
          type: string
        raw_body_only:
          type: boolean
        require_session:
          type: boolean
      type: object
    MiddlewareIdExtractor:
      properties:
        disabled:
          type: boolean
        extract_from:
          type: string
        extract_with:
          type: string
        extractor_config:
          additionalProperties: {}
          nullable: true
          type: object
      type: object
    EventHandlerTriggerConfig:
      properties:
        handler_meta:
          additionalProperties: {}
          nullable: true
          type: object
        handler_name:
          type: string
      type: object
    Provider:
      properties:
        introspection:
          $ref: '#/components/schemas/Introspection'
        jwt:
          $ref: '#/components/schemas/JWTValidation'
      type: object
    GraphQLEngineConfig:
      properties:
        data_sources:
          items:
            $ref: '#/components/schemas/GraphQLEngineDataSource'
          nullable: true
          type: array
        field_configs:
          items:
            $ref: '#/components/schemas/GraphQLFieldConfig'
          nullable: true
          type: array
        global_headers:
          items:
            $ref: '#/components/schemas/UDGGlobalHeader'
          nullable: true
          type: array
      type: object
    GraphQLIntrospectionConfig:
      properties:
        disabled:
          type: boolean
      type: object
    GraphQLPlayground:
      properties:
        enabled:
          type: boolean
        path:
          type: string
      type: object
    GraphQLProxyConfig:
      properties:
        auth_headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
        features:
          $ref: '#/components/schemas/GraphQLProxyFeaturesConfig'
        request_headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
        request_headers_rewrite:
          additionalProperties:
            $ref: '#/components/schemas/RequestHeadersRewriteConfig'
          nullable: true
          type: object
        subscription_type:
          type: string
        use_response_extensions:
          $ref: '#/components/schemas/GraphQLResponseExtensions'
      type: object
    GraphQLSubgraphConfig:
      properties:
        sdl:
          type: string
      type: object
    GraphQLSupergraphConfig:
      properties:
        disable_query_batching:
          type: boolean
        global_headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
        merged_sdl:
          type: string
        subgraphs:
          items:
            $ref: '#/components/schemas/GraphQLSubgraphEntity'
          nullable: true
          type: array
        updated_at:
          format: date-time
          nullable: true
          type: string
      type: object
    DatasourceTypeFieldConfiguration:
      properties:
        data_source:
          $ref: '#/components/schemas/DatasourceSourceConfig'
        field_name:
          type: string
        mapping:
          $ref: '#/components/schemas/DatasourceMappingConfiguration'
        type_name:
          type: string
      type: object
    OIDProviderConfig:
      properties:
        client_ids:
          additionalProperties:
            type: string
          nullable: true
          type: object
        issuer:
          type: string
      type: object
    ServiceDiscoveryConfiguration:
      properties:
        cache_disabled:
          type: boolean
        cache_timeout:
          format: int64
          type: integer
        data_path:
          type: string
        endpoint_returns_list:
          type: boolean
        parent_data_path:
          type: string
        port_data_path:
          type: string
        query_endpoint:
          type: string
        target_path:
          type: string
        use_discovery_service:
          type: boolean
        use_nested_query:
          type: boolean
        use_target_list:
          type: boolean
      type: object
    ScopeClaim:
      properties:
        scope_claim_name:
          type: string
        scope_to_policy:
          additionalProperties:
            type: string
          type: object
      type: object
    UpstreamBasicAuth:
      properties:
        enabled:
          type: boolean
        header:
          $ref: '#/components/schemas/AuthSource'
        password:
          type: string
        username:
          type: string
      type: object
    UpstreamOAuth:
      properties:
        allowed_authorize_types:
          items:
            type: string
          nullable: true
          type: array
        client_credentials:
          $ref: '#/components/schemas/ClientCredentials'
        enabled:
          type: boolean
        password:
          $ref: '#/components/schemas/PasswordAuthentication'
      type: object
    HostCheckObject:
      properties:
        body:
          type: string
        commands:
          items:
            $ref: '#/components/schemas/CheckCommand'
          nullable: true
          type: array
        enable_proxy_protocol:
          type: boolean
        headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
        method:
          type: string
        protocol:
          type: string
        timeout:
          $ref: '#/components/schemas/TimeDuration'
        url:
          type: string
      type: object
    UptimeTestsConfig:
      properties:
        expire_utime_after:
          format: int64
          type: integer
        recheck_wait:
          type: integer
        service_discovery:
          $ref: '#/components/schemas/ServiceDiscoveryConfiguration'
      type: object
    VersionInfo:
      properties:
        expires:
          type: string
        extended_paths:
          $ref: '#/components/schemas/ExtendedPathsSet'
        global_headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
        global_headers_disabled:
          type: boolean
        global_headers_remove:
          items:
            type: string
          nullable: true
          type: array
        global_response_headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
        global_response_headers_disabled:
          type: boolean
        global_response_headers_remove:
          items:
            type: string
          nullable: true
          type: array
        global_size_limit:
          format: int64
          type: integer
        global_size_limit_disabled:
          type: boolean
        ignore_endpoint_case:
          type: boolean
        name:
          type: string
        override_target:
          type: string
        paths:
          properties:
            black_list:
              items:
                type: string
              nullable: true
              type: array
            ignored:
              items:
                type: string
              nullable: true
              type: array
            white_list:
              items:
                type: string
              nullable: true
              type: array
          type: object
        use_extended_paths:
          type: boolean
      type: object
    Openapi3Callbacks:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3CallbackRef'
      type: object
    Openapi3Examples:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3ExampleRef'
      type: object
    Openapi3Headers:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3HeaderRef'
      type: object
    Openapi3Links:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3LinkRef'
      type: object
    Openapi3ParametersMap:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3ParameterRef'
      type: object
    Openapi3RequestBodies:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3RequestBodyRef'
      type: object
    Openapi3Responses:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3ResponseRef'
      type: object
    Openapi3Schemas:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3SchemaRef'
      type: object
    Openapi3SecuritySchemes:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3SecuritySchemeRef'
      type: object
    Openapi3Contact:
      nullable: true
      properties:
        email:
          type: string
        name:
          type: string
        url:
          type: string
      type: object
    Openapi3License:
      nullable: true
      properties:
        name:
          type: string
        url:
          type: string
      type: object
    Openapi3PathItem:
      properties:
        $ref: c8264e4f-4377-43d1-8a8a-c70595c2d219
        connect:
          $ref: '#/components/schemas/Openapi3Operation'
        delete:
          $ref: '#/components/schemas/Openapi3Operation'
        description:
          type: string
        get:
          $ref: '#/components/schemas/Openapi3Operation'
        head:
          $ref: '#/components/schemas/Openapi3Operation'
        options:
          $ref: '#/components/schemas/Openapi3Operation'
        parameters:
          $ref: '#/components/schemas/Openapi3Parameters'
        patch:
          $ref: '#/components/schemas/Openapi3Operation'
        post:
          $ref: '#/components/schemas/Openapi3Operation'
        put:
          $ref: '#/components/schemas/Openapi3Operation'
        servers:
          $ref: '#/components/schemas/Openapi3Servers'
        summary:
          type: string
        trace:
          $ref: '#/components/schemas/Openapi3Operation'
      type: object
    Openapi3SecurityRequirement:
      additionalProperties:
        items:
          type: string
        type: array
      type: object
    Openapi3Server:
      nullable: true
      properties:
        description:
          type: string
        url:
          type: string
        variables:
          additionalProperties:
            $ref: '#/components/schemas/Openapi3ServerVariable'
          type: object
      type: object
    Openapi3Tag:
      properties:
        description:
          type: string
        externalDocs:
          $ref: '#/components/schemas/Openapi3ExternalDocs'
        name:
          type: string
      type: object
    Introspection:
      properties:
        cache:
          $ref: '#/components/schemas/IntrospectionCache'
        client_id:
          type: string
        client_secret:
          type: string
        enabled:
          type: boolean
        identity_base_field:
          type: string
        url:
          type: string
      type: object
    JWTValidation:
      properties:
        enabled:
          type: boolean
        expires_at_validation_skew:
          minimum: 0
          type: integer
        identity_base_field:
          type: string
        issued_at_validation_skew:
          minimum: 0
          type: integer
        not_before_validation_skew:
          minimum: 0
          type: integer
        signing_method:
          type: string
        source:
          type: string
      type: object
    GraphQLEngineDataSource:
      properties:
        config: {}
        internal:
          type: boolean
        kind:
          type: string
        name:
          type: string
        root_fields:
          items:
            $ref: '#/components/schemas/GraphQLTypeFields'
          nullable: true
          type: array
      type: object
    GraphQLFieldConfig:
      properties:
        disable_default_mapping:
          type: boolean
        field_name:
          type: string
        path:
          items:
            type: string
          nullable: true
          type: array
        type_name:
          type: string
      type: object
    UDGGlobalHeader:
      properties:
        key:
          type: string
        value:
          type: string
      type: object
    GraphQLProxyFeaturesConfig:
      properties:
        use_immutable_headers:
          type: boolean
      type: object
    RequestHeadersRewriteConfig:
      properties:
        remove:
          type: boolean
        value:
          type: string
      type: object
    GraphQLResponseExtensions:
      properties:
        on_error_forwarding:
          type: boolean
      type: object
    GraphQLSubgraphEntity:
      properties:
        api_id:
          type: string
        headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
        name:
          type: string
        sdl:
          type: string
        subscription_type:
          type: string
        url:
          type: string
      type: object
    DatasourceSourceConfig:
      properties:
        data_source_config: {}
        kind:
          type: string
      type: object
    DatasourceMappingConfiguration:
      nullable: true
      properties:
        disabled:
          type: boolean
        path:
          type: string
      type: object
    AuthSource:
      properties:
        enabled:
          type: boolean
        name:
          type: string
      type: object
    ClientCredentials:
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        extra_metadata:
          items:
            type: string
          type: array
        header:
          $ref: '#/components/schemas/AuthSource'
        scopes:
          items:
            type: string
          type: array
        token_url:
          type: string
      type: object
    PasswordAuthentication:
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        extra_metadata:
          items:
            type: string
          type: array
        header:
          $ref: '#/components/schemas/AuthSource'
        password:
          type: string
        scopes:
          items:
            type: string
          type: array
        token_url:
          type: string
        username:
          type: string
      type: object
    CheckCommand:
      properties:
        message:
          type: string
        name:
          type: string
      type: object
    TimeDuration:
      format: int64
      type: integer
    ExtendedPathsSet:
      properties:
        advance_cache_config:
          items:
            $ref: '#/components/schemas/CacheMeta'
          type: array
        black_list:
          items:
            $ref: '#/components/schemas/EndPointMeta'
          type: array
        cache:
          items:
            type: string
          type: array
        circuit_breakers:
          items:
            $ref: '#/components/schemas/CircuitBreakerMeta'
          type: array
        do_not_track_endpoints:
          items:
            $ref: '#/components/schemas/TrackEndpointMeta'
          type: array
        go_plugin:
          items:
            $ref: '#/components/schemas/GoPluginMeta'
          type: array
        hard_timeouts:
          items:
            $ref: '#/components/schemas/HardTimeoutMeta'
          type: array
        ignored:
          items:
            $ref: '#/components/schemas/EndPointMeta'
          type: array
        internal:
          items:
            $ref: '#/components/schemas/InternalMeta'
          type: array
        method_transforms:
          items:
            $ref: '#/components/schemas/MethodTransformMeta'
          type: array
        mock_response:
          items:
            $ref: '#/components/schemas/MockResponseMeta'
          type: array
        persist_graphql:
          items:
            $ref: '#/components/schemas/PersistGraphQLMeta'
          nullable: true
          type: array
        rate_limit:
          items:
            $ref: '#/components/schemas/RateLimitMeta'
          nullable: true
          type: array
        size_limits:
          items:
            $ref: '#/components/schemas/RequestSizeMeta'
          type: array
        track_endpoints:
          items:
            $ref: '#/components/schemas/TrackEndpointMeta'
          type: array
        transform:
          items:
            $ref: '#/components/schemas/TemplateMeta'
          type: array
        transform_headers:
          items:
            $ref: '#/components/schemas/HeaderInjectionMeta'
          type: array
        transform_jq:
          items:
            $ref: '#/components/schemas/TransformJQMeta'
          type: array
        transform_jq_response:
          items:
            $ref: '#/components/schemas/TransformJQMeta'
          type: array
        transform_response:
          items:
            $ref: '#/components/schemas/TemplateMeta'
          type: array
        transform_response_headers:
          items:
            $ref: '#/components/schemas/HeaderInjectionMeta'
          type: array
        url_rewrites:
          items:
            $ref: '#/components/schemas/URLRewriteMeta'
          type: array
        validate_json:
          items:
            $ref: '#/components/schemas/ValidatePathMeta'
          type: array
        validate_request:
          items:
            $ref: '#/components/schemas/ValidateRequestMeta'
          type: array
        virtual:
          items:
            $ref: '#/components/schemas/VirtualMeta'
          type: array
        white_list:
          items:
            $ref: '#/components/schemas/EndPointMeta'
          type: array
      type: object
    Openapi3CallbackRef:
      properties:
        Ref:
          type: string
        Value:
          $ref: '#/components/schemas/Openapi3Callback'
      type: object
    Openapi3ExampleRef:
      properties:
        Ref:
          type: string
        Value:
          $ref: '#/components/schemas/Openapi3Example'
      type: object
    Openapi3HeaderRef:
      properties:
        Ref:
          type: string
        Value:
          $ref: '#/components/schemas/Openapi3Header'
      type: object
    Openapi3LinkRef:
      properties:
        Ref:
          type: string
        Value:
          $ref: '#/components/schemas/Openapi3Link'
      type: object
    Openapi3ParameterRef:
      properties:
        Ref:
          type: string
        Value:
          $ref: '#/components/schemas/Openapi3Parameter'
      type: object
    Openapi3RequestBodyRef:
      properties:
        Ref:
          type: string
        Value:
          $ref: '#/components/schemas/Openapi3RequestBody'
      type: object
    Openapi3ResponseRef:
      properties:
        Ref:
          type: string
        Value:
          $ref: '#/components/schemas/Openapi3Response'
      type: object
    Openapi3SchemaRef:
      properties:
        Ref:
          type: string
        Value:
          $ref: '#/components/schemas/Openapi3Schema'
      type: object
    Openapi3SecuritySchemeRef:
      properties:
        Ref:
          type: string
        Value:
          $ref: '#/components/schemas/Openapi3SecurityScheme'
      type: object
    Openapi3Operation:
      nullable: true
      properties:
        callbacks:
          $ref: '#/components/schemas/Openapi3Callbacks'
        deprecated:
          type: boolean
        description:
          type: string
        externalDocs:
          $ref: '#/components/schemas/Openapi3ExternalDocs'
        operationId:
          type: string
        parameters:
          $ref: '#/components/schemas/Openapi3Parameters'
        requestBody:
          $ref: '#/components/schemas/Openapi3RequestBodyRef'
        responses:
          $ref: '#/components/schemas/Openapi3Responses'
        security:
          $ref: '#/components/schemas/Openapi3SecurityRequirements'
        servers:
          $ref: '#/components/schemas/Openapi3Servers'
        summary:
          type: string
        tags:
          items:
            type: string
          type: array
      type: object
    Openapi3Parameters:
      items:
        $ref: '#/components/schemas/Openapi3ParameterRef'
      type: array
    Openapi3ServerVariable:
      properties:
        default:
          type: string
        description:
          type: string
        enum:
          items:
            type: string
          type: array
      type: object
    IntrospectionCache:
      properties:
        enabled:
          type: boolean
        timeout:
          format: int64
          type: integer
      type: object
    GraphQLTypeFields:
      properties:
        fields:
          items:
            type: string
          nullable: true
          type: array
        type:
          type: string
      type: object
    CacheMeta:
      properties:
        cache_key_regex:
          type: string
        cache_response_codes:
          items:
            type: integer
          nullable: true
          type: array
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
        timeout:
          format: int64
          type: integer
      type: object
    EndPointMeta:
      properties:
        disabled:
          type: boolean
        ignore_case:
          type: boolean
        method:
          type: string
        method_actions:
          additionalProperties:
            $ref: '#/components/schemas/EndpointMethodMeta'
          type: object
        path:
          type: string
      type: object
    CircuitBreakerMeta:
      properties:
        disable_half_open_state:
          type: boolean
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
        return_to_service_after:
          type: integer
        samples:
          format: int64
          type: integer
        threshold_percent:
          format: double
          type: number
      type: object
    TrackEndpointMeta:
      properties:
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
      type: object
    GoPluginMeta:
      properties:
        disabled:
          type: boolean
        func_name:
          type: string
        method:
          type: string
        path:
          type: string
        plugin_path:
          type: string
      type: object
    HardTimeoutMeta:
      properties:
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
        timeout:
          type: integer
      type: object
    InternalMeta:
      properties:
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
      type: object
    MethodTransformMeta:
      properties:
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
        to_method:
          type: string
      type: object
    MockResponseMeta:
      properties:
        body:
          type: string
        code:
          type: integer
        disabled:
          type: boolean
        headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
        ignore_case:
          type: boolean
        method:
          type: string
        path:
          type: string
      type: object
    PersistGraphQLMeta:
      properties:
        method:
          type: string
        operation:
          type: string
        path:
          type: string
        variables:
          additionalProperties: {}
          nullable: true
          type: object
      type: object
    RateLimitMeta:
      properties:
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
        per:
          format: double
          type: number
        rate:
          format: double
          type: number
      type: object
    RequestSizeMeta:
      properties:
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
        size_limit:
          format: int64
          type: integer
      type: object
    TemplateMeta:
      properties:
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
        template_data:
          $ref: '#/components/schemas/TemplateData'
      type: object
    HeaderInjectionMeta:
      properties:
        act_on:
          type: boolean
        add_headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
        delete_headers:
          items:
            type: string
          nullable: true
          type: array
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
      type: object
    TransformJQMeta:
      properties:
        filter:
          type: string
        method:
          type: string
        path:
          type: string
      type: object
    URLRewriteMeta:
      properties:
        disabled:
          type: boolean
        match_pattern:
          type: string
        method:
          type: string
        path:
          type: string
        rewrite_to:
          type: string
        triggers:
          items:
            $ref: '#/components/schemas/RoutingTrigger'
          nullable: true
          type: array
      type: object
    ValidatePathMeta:
      properties:
        disabled:
          type: boolean
        error_response_code:
          type: integer
        method:
          type: string
        path:
          type: string
        schema:
          additionalProperties: {}
          nullable: true
          type: object
        schema_b64:
          type: string
      type: object
    ValidateRequestMeta:
      properties:
        enabled:
          type: boolean
        error_response_code:
          type: integer
        method:
          type: string
        path:
          type: string
      type: object
    VirtualMeta:
      properties:
        disabled:
          type: boolean
        function_source_type:
          type: string
        function_source_uri:
          type: string
        method:
          type: string
        path:
          type: string
        proxy_on_error:
          type: boolean
        response_function_name:
          type: string
        use_session:
          type: boolean
      type: object
    Openapi3Callback:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3PathItem'
      nullable: true
      type: object
    Openapi3Example:
      nullable: true
      properties:
        description:
          type: string
        externalValue:
          type: string
        summary:
          type: string
        value: {}
      type: object
    Openapi3Header:
      nullable: true
      properties:
        allowEmptyValue:
          type: boolean
        allowReserved:
          type: boolean
        content:
          $ref: '#/components/schemas/Openapi3Content'
        deprecated:
          type: boolean
        description:
          type: string
        example: {}
        examples:
          $ref: '#/components/schemas/Openapi3Examples'
        explode:
          nullable: true
          type: boolean
        in:
          type: string
        name:
          type: string
        required:
          type: boolean
        schema:
          $ref: '#/components/schemas/Openapi3SchemaRef'
        style:
          type: string
      type: object
    Openapi3Link:
      nullable: true
      properties:
        description:
          type: string
        operationId:
          type: string
        operationRef:
          type: string
        parameters:
          additionalProperties: {}
          type: object
        requestBody: {}
        server:
          $ref: '#/components/schemas/Openapi3Server'
      type: object
    Openapi3Parameter:
      nullable: true
      properties:
        allowEmptyValue:
          type: boolean
        allowReserved:
          type: boolean
        content:
          $ref: '#/components/schemas/Openapi3Content'
        deprecated:
          type: boolean
        description:
          type: string
        example: {}
        examples:
          $ref: '#/components/schemas/Openapi3Examples'
        explode:
          nullable: true
          type: boolean
        in:
          type: string
        name:
          type: string
        required:
          type: boolean
        schema:
          $ref: '#/components/schemas/Openapi3SchemaRef'
        style:
          type: string
      type: object
    Openapi3RequestBody:
      nullable: true
      properties:
        content:
          $ref: '#/components/schemas/Openapi3Content'
        description:
          type: string
        required:
          type: boolean
      type: object
    Openapi3Response:
      nullable: true
      properties:
        content:
          $ref: '#/components/schemas/Openapi3Content'
        description:
          nullable: true
          type: string
        headers:
          $ref: '#/components/schemas/Openapi3Headers'
        links:
          $ref: '#/components/schemas/Openapi3Links'
      type: object
    Openapi3Schema:
      nullable: true
      properties:
        additionalProperties:
          $ref: '#/components/schemas/Openapi3AdditionalProperties'
        allOf:
          $ref: '#/components/schemas/Openapi3SchemaRefs'
        allowEmptyValue:
          type: boolean
        anyOf:
          $ref: '#/components/schemas/Openapi3SchemaRefs'
        default: {}
        deprecated:
          type: boolean
        description:
          type: string
        discriminator:
          $ref: '#/components/schemas/Openapi3Discriminator'
        enum:
          items: {}
          type: array
        example: {}
        exclusiveMaximum:
          type: boolean
        exclusiveMinimum:
          type: boolean
        externalDocs:
          $ref: '#/components/schemas/Openapi3ExternalDocs'
        format:
          type: string
        items:
          $ref: '#/components/schemas/Openapi3SchemaRef'
        maxItems:
          minimum: 0
          nullable: true
          type: integer
        maxLength:
          minimum: 0
          nullable: true
          type: integer
        maxProperties:
          minimum: 0
          nullable: true
          type: integer
        maximum:
          nullable: true
          type: number
        minItems:
          minimum: 0
          type: integer
        minLength:
          minimum: 0
          type: integer
        minProperties:
          minimum: 0
          type: integer
        minimum:
          nullable: true
          type: number
        multipleOf:
          nullable: true
          type: number
        not:
          $ref: '#/components/schemas/Openapi3SchemaRef'
        nullable:
          type: boolean
        oneOf:
          $ref: '#/components/schemas/Openapi3SchemaRefs'
        pattern:
          type: string
        properties:
          $ref: '#/components/schemas/Openapi3Schemas'
        readOnly:
          type: boolean
        required:
          items:
            type: string
          type: array
        title:
          type: string
        type:
          type: string
        uniqueItems:
          type: boolean
        writeOnly:
          type: boolean
        xml:
          $ref: '#/components/schemas/Openapi3XML'
      type: object
    Openapi3SecurityScheme:
      nullable: true
      properties:
        bearerFormat:
          type: string
        description:
          type: string
        flows:
          $ref: '#/components/schemas/Openapi3OAuthFlows'
        in:
          type: string
        name:
          type: string
        openIdConnectUrl:
          type: string
        scheme:
          type: string
        type:
          type: string
      type: object
    EndpointMethodMeta:
      properties:
        action:
          type: string
        code:
          type: integer
        data:
          type: string
        headers:
          additionalProperties:
            type: string
          nullable: true
          type: object
      type: object
    TemplateData:
      properties:
        enable_session:
          type: boolean
        input_type:
          type: string
        template_mode:
          type: string
        template_source:
          type: string
      type: object
    RoutingTrigger:
      properties:
        'on':
          type: string
        options:
          $ref: '#/components/schemas/RoutingTriggerOptions'
        rewrite_to:
          type: string
      type: object
    Openapi3Content:
      additionalProperties:
        $ref: '#/components/schemas/Openapi3MediaType'
      type: object
    Openapi3AdditionalProperties:
      properties:
        Has:
          nullable: true
          type: boolean
        Schema:
          $ref: '#/components/schemas/Openapi3SchemaRef'
      type: object
    Openapi3SchemaRefs:
      items:
        $ref: '#/components/schemas/Openapi3SchemaRef'
      type: array
    Openapi3Discriminator:
      nullable: true
      properties:
        mapping:
          additionalProperties:
            type: string
          type: object
        propertyName:
          type: string
      type: object
    Openapi3XML:
      nullable: true
      properties:
        attribute:
          type: boolean
        name:
          type: string
        namespace:
          type: string
        prefix:
          type: string
        wrapped:
          type: boolean
      type: object
    Openapi3OAuthFlows:
      nullable: true
      properties:
        authorizationCode:
          $ref: '#/components/schemas/Openapi3OAuthFlow'
        clientCredentials:
          $ref: '#/components/schemas/Openapi3OAuthFlow'
        implicit:
          $ref: '#/components/schemas/Openapi3OAuthFlow'
        password:
          $ref: '#/components/schemas/Openapi3OAuthFlow'
      type: object
    RoutingTriggerOptions:
      properties:
        header_matches:
          additionalProperties:
            $ref: '#/components/schemas/StringRegexMap'
          nullable: true
          type: object
        path_part_matches:
          additionalProperties:
            $ref: '#/components/schemas/StringRegexMap'
          nullable: true
          type: object
        payload_matches:
          $ref: '#/components/schemas/StringRegexMap'
        query_val_matches:
          additionalProperties:
            $ref: '#/components/schemas/StringRegexMap'
          nullable: true
          type: object
        request_context_matches:
          additionalProperties:
            $ref: '#/components/schemas/StringRegexMap'
          nullable: true
          type: object
        session_meta_matches:
          additionalProperties:
            $ref: '#/components/schemas/StringRegexMap'
          nullable: true
          type: object
      type: object
    Openapi3MediaType:
      properties:
        encoding:
          additionalProperties:
            $ref: '#/components/schemas/Openapi3Encoding'
          type: object
        example: {}
        examples:
          $ref: '#/components/schemas/Openapi3Examples'
        schema:
          $ref: '#/components/schemas/Openapi3SchemaRef'
      type: object
    Openapi3OAuthFlow:
      nullable: true
      properties:
        authorizationUrl:
          type: string
        refreshUrl:
          type: string
        scopes:
          additionalProperties:
            type: string
          nullable: true
          type: object
        tokenUrl:
          type: string
      type: object
    StringRegexMap:
      properties:
        match_rx:
          type: string
        reverse:
          type: boolean
      type: object
    Openapi3Encoding:
      properties:
        allowReserved:
          type: boolean
        contentType:
          type: string
        explode:
          nullable: true
          type: boolean
        headers:
          $ref: '#/components/schemas/Openapi3Headers'
        style:
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
