# Source: https://tyk.io/docs/api-reference/apis/search-list-of-apis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search List of APIs

> This will return a list of APIs whose names matches the provided q query parameter.If q is not sent all APIs will be returned.The returned results are paginated.



## OpenAPI

````yaml swagger/5.8/dashboard-swagger.yml get /api/apis/search
openapi: 3.0.3
info:
  contact:
    email: support@tyk.io
    name: Tyk Technologies
    url: https://tyk.io/contact
  description: >
    <img src="https://tyk.io/docs/img/swagger_dashboard_image.png" width="963"
    height="250">


    ## <a name="introduction"></a> Introduction


    The Tyk Dashboard API offers granular, programmatic access to a centralised
    database of resources that your Tyk nodes can pull from. This API has a
    dynamic user administrative structure which means the secret key that is
    used to communicate with your Tyk nodes can be kept secret and access to the
    wider management functions can be handled on a user-by-user and
    organisation-by-organisation basis.


    A common question around using a database-backed configuration is how to
    programmatically add API definitions to your Tyk nodes, the Dashboard API
    allows much more fine-grained, secure and multi-user access to your Tyk
    cluster, and should be used to manage a database-backed Tyk node.


    The Tyk Dashboard API works seamlessly with the Tyk Dashboard (and the two
    come bundled together).


    ## <a name="security-hierarchy"></a> Security Hierarchy


    The Dashboard API provides a more structured security layer to managing Tyk
    nodes.


    ### Organisations, APIs and Users


    With the Dashboard API and a database-backed Tyk setup, (and to an extent
    with file-based API setups - if diligence is used in naming and creating
    definitions), the following security model is applied to the management of
    Upstream APIs:


    * **Organisations**: All APIs are *owned* by an organisation, this is
    designated by the 'OrgID' parameter in the API Definition.

    * **Users**: All users created in the Dashboard belong to an organisation
    (unless an exception is made for super-administrative access).

    * **APIs**: All APIs belong to an Organisation and only Users that belong to
    that organisation can see the analytics for those APIs and manage their
    configurations.

    * **API Keys**: API Keys are designated by organisation, this means an API
    key that has full access rights will not be allowed to access the APIs of
    another organisation on the same system, but can have full access to all
    APIs within the organisation.

    * **Access Rights**: Access rights are stored with the key, this enables a
    key to give access to multiple APIs, this is defined by the session object
    in the core Tyk API.


    In order to use the Dashboard API, you'll need to get the 'Tyk Dashboard API
    Access Credentials' secret from your user profile on the Dashboard UI.


    The secret you set should then be sent along as a header with each Dashboard
    API Request in order for it to be successful:



    authorization: <your-secret>
  license:
    name: Mozilla Public License Version 2.0
    url: https://github.com/TykTechnologies/tyk/blob/master/LICENSE.md
  title: Tyk Dashboard API
  version: 5.8.9
servers:
  - url: https://{tenant}
    variables:
      tenant:
        default: localhost:3000
        description: Your dashboard host
security:
  - bearerAuth: []
tags:
  - description: >-
      Use the endpoints under this tag to manage your certificates. You can add,
      delete and list certificates using these endpoints.
    name: Certificates
  - description: >-
      The Tyk Dashboard provides a full set of analytics functions and graphs
      that you can use to segment and view your API traffic and activity.
    externalDocs:
      description: Traffic Analytics.
      url: https://tyk.io/docs/tyk-dashboard-analytics/
    name: Analytics
  - description: Use the endpoints in this tag to manage OAuth flow.
    externalDocs:
      description: OAuth Documentation
      url: >-
        https://tyk.io/docs/basic-config-and-security/security/authentication-authorization/oauth-2-0/
    name: Oauth
  - description: >
      An API template is an asset managed by Tyk Dashboard that is used as the
      starting point - a blueprint - from which you can create a new Tyk OAS API
      definition. <br/>


      Templates are used only during the creation of an API, they cannot be
      applied later.


      [Read more about API template assets
      here](https://tyk.io/docs/product-stack/tyk-dashboard/advanced-configurations/templates/template-overview/)
    externalDocs:
      description: API Templates full documentation.
      url: >-
        https://tyk.io/docs/product-stack/tyk-dashboard/advanced-configurations/templates/template-overview/
    name: Assets
  - description: >
      The Tyk Dashboard permission system can be extended by writing custom
      rules using an Open Policy Agent (OPA). The rules engine works on top of
      your Dashboard API, which means you can control not only access rules, but
      also behaviour of all Dashboard APIs (except your public developer
      portal)  <br/>


      By default the Dashboard OPA engine is turned off, and you need to
      explicitly enable it via your Dashboard tyk_analytics.conf file. <br/>


      You can use OPA rule to accomplish tasks like: <br/>


      1. Prevent users from creating keyless APIs.

      2. Assign specific categories to APIs created to certain user groups or
      users.

      3. Control access for individual fields. For example, do not allow
      changing the API “active” status (e.g. deploy), unless you have a specific
      permission set.

      4. And many more <br/>


      [Read more about Tyk Open Policy Agent
      here](https://tyk.io/docs/tyk-dashboard/open-policy-agent/)
    externalDocs:
      description: Tyk Open Policy Agent Full Documentation.
      url: https://tyk.io/docs/tyk-dashboard/open-policy-agent/
    name: Open Policy Agent
  - description: >
      These APIs helps you get,add and delete (CRUD) a list of additional
      (custom) permissions for your Dashboard users. You can use the created
      additional permissions with Open Policy Agent (OPA). <br/>

       Once created, a custom permission will be added to standard list of user permissions. <br/>

      You can also configure these custom permissions in the
      security.additional_permissions map in the Tyk Dashboard configuration
      file.


      You can check the [full documentation
      here](https://tyk.io/docs/tyk-dashboard-api/org/permissions/).
    externalDocs:
      description: Additional Permissions full documentation.
      url: https://tyk.io/docs/tyk-dashboard-api/org/permissions/
    name: Additional Permissions
  - description: Get schemas.
    name: Schemas
  - description: >
      Webhooks are a great way to let external applications know about the
      status of a user, an API or an event that has occurred in the Tyk gateway
      <br/>


      You can create webhooks that you can then re-use in your API definitions
      and assign to different Tyk Events such as quota violations or
      rate-limiting violations.<br/>


      Each webhook require a target_path (which is an absolute URL that should
      be targeted by the webhook e.g https://httpbin.org/expired-keys) and a
      method which can be any of GET, PUT, POST, PATCH or DELETE.<br/>


      Request types that do not support an encoded body will not have the event
      metadata encoded as part of the request. We would advise using POST where
      possible.
    name: Webhooks
  - description: >-
      Policies are a template that enable you to create access rules, usage
      quota and rate limits that can be applied to multiple keys. They are a
      useful way to manage large groups of users, and to enforce quota changes
      on a global scale across any number of keys that are using a policy. When
      used in conjunction with the portal, developers that enroll for API access
      will be given a key that is attached to a specific policy. The policy
      settings are refreshed every time a key attempts access, meaning that
      updating a policy will have an effect across any keys that are attached to
      it.
    externalDocs:
      description: Security Policies Documentation.
      url: >-
        https://tyk.io/docs/basic-config-and-security/security/security-policies/
    name: Policies
  - description: >-
      When you have a large number of users and teams with different access
      requirements, instead of setting permissions per user, you can create a
      user group and configure the permissions for all users in the group. Note
      that a user can only belong to one group.
    externalDocs:
      description: Manage Tyk Dashboard User Groups.
      url: >-
        https://tyk.io/docs/basic-config-and-security/security/dashboard/create-user-groups/
    name: UserGroup
  - description: >-
      Users have twofold access to the dashboard: they can access both the
      Dashboard API and the Dashboard itself, it is possible to generate users
      that have read-only access to certain sections of the dashboard and the
      underlying API. Use the endpoints in this tag to manage users.
    externalDocs:
      description: Manage Tyk Dashboard Users.
      url: >-
        https://tyk.io/docs/basic-config-and-security/security/dashboard/create-users/
    name: Users
  - description: >-
      All keys that are used to access services via Tyk correspond to a session
      object that informs Tyk about the context of this particular token, like
      access rules and rate/quota allowance.
    externalDocs:
      description: API Key Management.
      url: https://tyk.io/docs/tyk-apis/tyk-dashboard-api/api-keys/
    name: Keys
  - description: >-
      An API request made using Basic Authentication will have an Authorization
      header that contains the API key. The value of the Authorization header
      will be in the form:</br>

      `Basic base64Encode(username:password)`.
    externalDocs:
      description: Basic Authentication.
      url: >-
        https://tyk.io/docs/basic-config-and-security/security/authentication-authorization/basic-auth/
    name: Basic Authentication
  - description: >-
      Tyk allows you to work with APIs that you’ve designed with the OpenAPI
      Specification version 3.0.x, making it even easier to get your API up and
      running. Use the endpoints in this tag to create,delete,import and update
      OAS APIs.
    externalDocs:
      description: Tyk OAS Documentation.
      url: https://tyk.io/docs/getting-started/key-concepts/high-level-concepts/
    name: OAS APIs
  - description: >-
      Use the endpoints under this tags to update,add ,delete and fetch the
      classic APIs.
    name: APIs
  - description: >-
      The Dashboard SSO API allows you to implement custom authentication
      schemes for the Dashboard and Portal. Our Tyk Identity Broker (TIB)
      internally also uses this API. The Dashboard exposes the /api/sso
      Dashboard API which allows you to generate a temporary authentication
      token, valid for 60 seconds.
    externalDocs:
      description: Dashboard API Single Sign On.
      url: https://tyk.io/docs/tyk-apis/tyk-dashboard-api/sso/
    name: Single Sign On
  - description: System API.
    name: System
paths:
  /api/apis/search:
    get:
      tags:
        - APIs
      summary: Search List of APIs
      description: >-
        This will return a list of APIs whose names matches the provided q query
        parameter.If q is not sent all APIs will be returned.The returned
        results are paginated.
      operationId: searchApis
      parameters:
        - description: >-
            Use p query parameter to say which page you want returned. Send
            number less than 0 to return all items.
          example: 1
          in: query
          name: p
          required: false
          schema:
            type: integer
        - description: The name of the APIs you want to search
          example: Rate Limit Path API 1
          in: query
          name: q
          required: false
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              examples:
                paginatedApiExample:
                  $ref: '#/components/examples/paginatedApiExample'
              schema:
                $ref: '#/components/schemas/ApiDefinitionsResponse'
          description: List of API definitions
        '400':
          content:
            application/json:
              example:
                Message: Could not retrieve APIs
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Bad Request
        '401':
          content:
            application/json:
              example:
                Message: Not authorised
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Unauthorized
        '403':
          content:
            application/json:
              example:
                Message: >-
                  access denied: You do not have permission to access 
                  /api/apis/search
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Forbidden
        '500':
          content:
            application/json:
              example:
                Message: Failed to unmarshal APIs data
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Internal server error.
components:
  examples:
    paginatedApiExample:
      value:
        apis:
          - api_definition:
              api_id: b84fe1a04e5648927971c0557971565c
              auth:
                auth_header_name: authorization
              definition:
                key: version
                location: header
              name: Tyk Test API
              org_id: 664a14650619d40001f1f00f
              proxy:
                listen_path: /tyk-api-test/
                strip_listen_path: true
                target_url: https://httpbin.org
              use_oauth2: true
              version_data:
                not_versioned: true
                versions:
                  Default:
                    name: Default
        pages: 1
  schemas:
    ApiDefinitionsResponse:
      properties:
        apis:
          items:
            $ref: '#/components/schemas/ApiDefinitionWrapper'
          nullable: true
          type: array
        pages:
          type: integer
      type: object
    ApiResponse:
      properties:
        ID:
          type: string
        Message:
          type: string
        Meta: {}
        Status:
          type: string
      type: object
    ApiDefinitionWrapper:
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
          $ref: '#/components/schemas/ScopesType2'
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
          $ref: '#/components/schemas/Components'
        externalDocs:
          $ref: '#/components/schemas/ExternalDocs'
        info:
          $ref: '#/components/schemas/InfoType2'
        openapi:
          type: string
        paths:
          $ref: '#/components/schemas/Paths'
        security:
          $ref: '#/components/schemas/SecurityRequirements'
        servers:
          $ref: '#/components/schemas/Servers'
        tags:
          $ref: '#/components/schemas/Tags'
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    AnalyticsPluginConfig:
      properties:
        enable:
          type: boolean
        func_name:
          type: string
        plugin_path:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    ExternalOAuth:
      properties:
        enabled:
          type: boolean
        providers:
          items:
            $ref: '#/components/schemas/ProviderType2'
          nullable: true
          type: array
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    NotificationsManager:
      properties:
        oauth_on_keychange_url:
          type: string
        shared_secret:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    ResponseProcessor:
      properties:
        name:
          type: string
        options: {}
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
    ScopesType2:
      properties:
        jwt:
          $ref: '#/components/schemas/ScopeClaim'
        oidc:
          $ref: '#/components/schemas/ScopeClaim'
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    WebHookHandlerConf:
      properties:
        api_model:
          $ref: '#/components/schemas/ApiModel'
        event_timeout:
          example: 0
          format: int64
          type: integer
        header_map:
          additionalProperties:
            type: string
          example:
            secret: superscretkey
            x-auth: authvalue
          nullable: true
          type: object
        id:
          example: 664b613f5715ec4c96cbef3e
          type: string
        method:
          example: POST
          type: string
        name:
          example: Expired Keys webhook
          type: string
        org_id:
          example: 5e9d9544a1dcd60001d0ed20
          type: string
        target_path:
          example: https://httpbin.org/expired-keys
          type: string
        template_path:
          example: templates/default_webhook.json
          type: string
        webhook_id:
          example: 1f78e319202b430e92286cff3ca759e3
          type: string
      required:
        - method
        - target_path
      type: object
    Components:
      nullable: true
      properties:
        callbacks:
          $ref: '#/components/schemas/Callbacks'
        examples:
          $ref: '#/components/schemas/Examples'
        headers:
          $ref: '#/components/schemas/HeadersType2'
        links:
          $ref: '#/components/schemas/Links'
        parameters:
          $ref: '#/components/schemas/ParametersMap'
        requestBodies:
          $ref: '#/components/schemas/RequestBodies'
        responses:
          $ref: '#/components/schemas/Responses'
        schemas:
          $ref: '#/components/schemas/Schemas'
        securitySchemes:
          $ref: '#/components/schemas/SecuritySchemesType2'
      type: object
    ExternalDocs:
      nullable: true
      properties:
        description:
          type: string
        url:
          type: string
      type: object
    InfoType2:
      nullable: true
      properties:
        contact:
          $ref: '#/components/schemas/Contact'
        description:
          type: string
        license:
          $ref: '#/components/schemas/License'
        termsOfService:
          type: string
        title:
          type: string
        version:
          type: string
      type: object
    Paths:
      additionalProperties:
        $ref: '#/components/schemas/PathItem'
      type: object
    SecurityRequirements:
      items:
        $ref: '#/components/schemas/SecurityRequirement'
      nullable: true
      type: array
    Servers:
      items:
        $ref: '#/components/schemas/ServerType2'
      nullable: true
      type: array
    Tags:
      items:
        $ref: '#/components/schemas/Tag'
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    EventHandlerTriggerConfig:
      properties:
        handler_meta:
          additionalProperties: {}
          nullable: true
          type: object
        handler_name:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
    ProviderType2:
      properties:
        introspection:
          $ref: '#/components/schemas/Introspection'
        jwt:
          $ref: '#/components/schemas/JWTValidation'
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    GraphQLIntrospectionConfig:
      properties:
        disabled:
          type: boolean
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
    GraphQLPlayground:
      properties:
        enabled:
          type: boolean
        path:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    GraphQLSubgraphConfig:
      properties:
        sdl:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    ScopeClaim:
      properties:
        scope_claim_name:
          type: string
        scope_to_policy:
          additionalProperties:
            type: string
          type: object
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    Callbacks:
      additionalProperties:
        $ref: '#/components/schemas/CallbackRef'
      type: object
    Examples:
      additionalProperties:
        $ref: '#/components/schemas/ExampleRef'
      type: object
    HeadersType2:
      additionalProperties:
        $ref: '#/components/schemas/HeaderRef'
      type: object
    Links:
      additionalProperties:
        $ref: '#/components/schemas/LinkRef'
      type: object
    ParametersMap:
      additionalProperties:
        $ref: '#/components/schemas/ParameterRef'
      type: object
    RequestBodies:
      additionalProperties:
        $ref: '#/components/schemas/RequestBodyRef'
      type: object
    Responses:
      additionalProperties:
        $ref: '#/components/schemas/ResponseRef'
      type: object
    Schemas:
      additionalProperties:
        $ref: '#/components/schemas/SchemaRef'
      type: object
    SecuritySchemesType2:
      additionalProperties:
        $ref: '#/components/schemas/SecuritySchemeRef'
      type: object
    Contact:
      nullable: true
      properties:
        email:
          type: string
        name:
          type: string
        url:
          type: string
      type: object
    License:
      nullable: true
      properties:
        name:
          type: string
        url:
          type: string
      type: object
    PathItem:
      properties:
        $ref: f1d6d13c-90eb-484b-8081-102b98a9d071
        connect:
          $ref: '#/components/schemas/OperationType2'
        delete:
          $ref: '#/components/schemas/OperationType2'
        description:
          type: string
        get:
          $ref: '#/components/schemas/OperationType2'
        head:
          $ref: '#/components/schemas/OperationType2'
        options:
          $ref: '#/components/schemas/OperationType2'
        parameters:
          $ref: '#/components/schemas/Parameters'
        patch:
          $ref: '#/components/schemas/OperationType2'
        post:
          $ref: '#/components/schemas/OperationType2'
        put:
          $ref: '#/components/schemas/OperationType2'
        servers:
          $ref: '#/components/schemas/Servers'
        summary:
          type: string
        trace:
          $ref: '#/components/schemas/OperationType2'
      type: object
    SecurityRequirement:
      additionalProperties:
        items:
          type: string
        type: array
      type: object
    ServerType2:
      properties:
        description:
          type: string
        url:
          type: string
        variables:
          additionalProperties:
            $ref: '#/components/schemas/ServerVariable'
          type: object
      type: object
    Tag:
      properties:
        description:
          type: string
        externalDocs:
          $ref: '#/components/schemas/ExternalDocs'
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    UDGGlobalHeader:
      properties:
        key:
          type: string
        value:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
    GraphQLProxyFeaturesConfig:
      properties:
        use_immutable_headers:
          type: boolean
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
    RequestHeadersRewriteConfig:
      properties:
        remove:
          type: boolean
        value:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
    GraphQLResponseExtensions:
      properties:
        on_error_forwarding:
          type: boolean
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
    CheckCommand:
      properties:
        message:
          type: string
        name:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
    TimeDuration:
      format: duration
      type: string
      example: 30s
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    CallbackRef:
      type: object
    ExampleRef:
      type: object
    HeaderRef:
      type: object
    LinkRef:
      type: object
    ParameterRef:
      type: object
    RequestBodyRef:
      type: object
    ResponseRef:
      type: object
    SchemaRef:
      type: object
    SecuritySchemeRef:
      type: object
    OperationType2:
      nullable: true
      properties:
        callbacks:
          $ref: '#/components/schemas/Callbacks'
        deprecated:
          type: boolean
        description:
          type: string
        externalDocs:
          $ref: '#/components/schemas/ExternalDocs'
        operationId:
          type: string
        parameters:
          $ref: '#/components/schemas/Parameters'
        requestBody:
          $ref: '#/components/schemas/RequestBodyRef'
        responses:
          $ref: '#/components/schemas/Responses'
        security:
          $ref: '#/components/schemas/SecurityRequirements'
        servers:
          $ref: '#/components/schemas/Servers'
        summary:
          type: string
        tags:
          items:
            type: string
          type: array
      type: object
    Parameters:
      items:
        $ref: '#/components/schemas/ParameterRef'
      type: array
    ServerVariable:
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    TrackEndpointMeta:
      properties:
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    InternalMeta:
      properties:
        disabled:
          type: boolean
        method:
          type: string
        path:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    TransformJQMeta:
      properties:
        filter:
          type: string
        method:
          type: string
        path:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    RoutingTrigger:
      properties:
        'on':
          type: string
        options:
          $ref: '#/components/schemas/RoutingTriggerOptions'
        rewrite_to:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
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
      x-go-package: github.com/TykTechnologies/tyk/apidef
    StringRegexMap:
      properties:
        match_rx:
          type: string
        reverse:
          type: boolean
      type: object
      x-go-package: github.com/TykTechnologies/tyk/apidef
  securitySchemes:
    bearerAuth:
      description: The Tyk Dashboard API Access Credentials
      scheme: bearer
      type: http

````

Built with [Mintlify](https://mintlify.com).