# Source: https://tyk.io/docs/tyk-stack/tyk-operator/create-an-api.md

# Source: https://tyk.io/docs/api-reference/apis/create-an-api.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an API

> Create API. A single Tyk node can have its API Definitions queried, deleted and updated remotely. This functionality enables you to remotely update your Tyk definitions without having to manage the files manually.

## OpenAPI

````yaml swagger/5.11/gateway-swagger.yml post /tyk/apis
openapi: 3.0.3
info:
  contact:
    email: support@tyk.io
    name: Tyk Technologies
    url: https://tyk.io/contact
  description: >+
    <img src="https://tyk.io/docs/img/swagger_gateway_image.png" width="963"
    height="250">

    <img src="https://tyk.io/docs/img/swagger_gateway_direction_image.png"
    width="946" height="392">


    The Tyk Gateway API is the primary means for integrating your application
    with the Tyk API Gateway system. This API is very small, and has no granular
    permissions system. It is intended to be used purely for internal automation
    and integration.


    **Warning: Under no circumstances should outside parties be granted access
    to this API.**


    The Tyk Gateway API is capable of:


    * Managing session objects (key generation).

    * Managing and listing policies.

    * Managing and listing API Definitions (only when not using the Tyk
    Dashboard).

    * Hot reloads / reloading a cluster configuration.

    * OAuth client creation (only when not using the Tyk Dashboard).


    In order to use the Gateway API, you'll need to set the **secret** parameter
    in your tyk.conf file.


    The shared secret you set should then be sent along as a header with each
    Gateway API Request in order for it to be successful:


    **x-tyk-authorization: <your-secret>***

    <br/>


    <b>The Tyk Gateway API is subsumed by the Tyk Dashboard API in Pro
    installations.</b>

  license:
    name: Mozilla Public License Version 2.0
    url: https://github.com/TykTechnologies/tyk/blob/master/LICENSE.md
  title: Tyk Gateway API
  version: 5.11.0
servers:
  - url: https://{tenant}
    variables:
      tenant:
        default: localhost:8080
        description: Your gateway host
security:
  - api_key: []
tags:
  - description: >
      **Note: Applies only to Tyk Gateway Community Edition** <br/>


      API management is very simple using the Tyk Rest API: each update only
      affects the underlying file, and this endpoint will only work with disk
      based installations, not database-backed ones.<br/>


      APIs that are added this way are flushed to to disk into the app_path
      folder using the format: *{api-id}.json*. Updating existing APIs that use
      a different naming convention will cause those APIs to be added, which
      could subsequently lead to a loading error and crash if they use the same
      listen_path. <br/>


      These methods only work on a single API node. If updating a cluster, it is
      important to ensure that all nodes are updated before initiating a
      reload.<br/>
    name: APIs
  - description: |+
      **Note: Applies only to Tyk Gateway Community Edition** <br/>

    name: Tyk OAS APIs
  - description: >
      All keys that are used to access services via Tyk correspond to a session
      object that informs Tyk about the context of this particular token, like
      access rules and rate/quota allowance.
    name: Keys
  - description: >
      It is possible to force API quota and rate limit across all keys that
      belong to a specific organisation ID. Rate limiting at an organisation
      level is useful for creating tiered access levels and trial accounts.<br
      />


      The Organisation rate limiting middleware works with both Quotas and Rate
      Limiters. In order to manage this functionality, a simple API has been put
      in place to manage these sessions. <br />


      Although the Organisation session-limiter uses the same session object,
      all other security keys are optional as they are not used. <br />


      <h3>Managing active status</h3> <br />


      To disallow access to an entire group of keys without rate limiting the
      organisation, create a session object with the "is_inactive" key set to
      true. This will block access before any other middleware is executed. It
      is useful when managing subscriptions for an organisation group and access
      needs to be blocked because of non-payment. <br />
    name: Organisation Quotas
  - description: >
      Sometimes a cache might contain stale data, or it may just need to be
      cleared because of an invalid configuration. This call will purge all keys
      associated with a cache on an API-by-API basis.
    name: Cache Invalidation
  - description: >-
      Use the endpoints under this tag to manage your certificates. You can add,
      delete and list certificates using these endpoints.
    name: Certs
  - description: |
      Force restart of the Gateway or whole cluster.
    name: Hot Reload
  - description: |
      Check health status of the Tyk Gateway and loaded APIs.
    name: Health Checking
  - description: >
      A Tyk security policy incorporates several security options that can be
      applied to an API key. It acts as a template that can override individual
      sections of an API key (or identity) in Tyk.
    name: Policies
  - description: |
      Manage OAuth clients, and manage their tokens
    name: OAuth
  - description: >
      Tyk supports batch requests, so a client makes a single request to the API
      but gets a compound response object back.


      This is especially handy if clients have complex requests that have
      multiple synchronous dependencies and do not wish to have the entire
      request / response cycle running for each event.


      To enable batch request support, set the `enable_batch_request_support`
      value to `true`


      Batch requests that come into Tyk are *run through the whole Tyk
      machinery* and *use a relative path to prevent spamming*. This means that
      a batch request to Tyk for three resources with the same API key will have
      three requests applied to their session quota and request limiting could
      become active if they are being throttled.


      Tyk reconstructs the API request based on the data in the batch request.
      This is to ensure that Tyk is not being used to proxy requests to other
      hosts outside of the upstream API being accessed.


      Batch requests are created by POSTING to the `/{listen_path}/tyk/batch/`
      endpoint. These requests **do not require a valid key**, but their request
      list does.


      <h3>Sample Request</h3>

          ```{json}
          {
            "requests": [
              {
                "method": "GET",
                "headers": {
                  "x-tyk-test": "1",
                  "x-tyk-version": "1.2",
                  "authorization": "1dbc83b9c431649d7698faa9797e2900f"
                },
                "body": "",
                "relative_url": "get"
            },
            {
              "method": "GET",
              "headers": {
                "x-tyk-test": "2",
                "x-tyk-version": "1.2",
                "authorization": "1dbc83b9c431649d7698faa9797e2900f"
              },
              "body": "",
              "relative_url": "get"
              }
            ],
            "suppress_parallel_execution": false
          }
          ```

      The response will be a structured reply that encapsulates the responses
      for each of the outbound requests. If `suppress_parallel_execution` is set
      to `true`, requests will be made synchronously. If set to `false` then
      they will run in parallel and the response order is not guaranteed.


      <h3>Sample Response</h3>

        ```
        [
          {
            "relative_url": "get",
            "code": 200,
            "headers": {
              "Access-Control-Allow-Credentials": [
                "true"
              ],
              "Access-Control-Allow-Origin": [
                "*"
              ],
              "Content-Length": [
                "497"
              ],
              "Content-Type": [
                "application/json"
              ],
              "Date": [
                "Wed, 12 Nov 2014 15:32:43 GMT"
              ],
              "Server": [
                "gunicorn/18.0"
              ],
              "Via": [
                "1.1 vegur"
              ]
            },
            "body": "{
          "args": {},
          "headers": {
            "Accept-Encoding": "gzip",
            "Authorization": "1dbc83b9c431649d7698faa9797e2900f",
            "Connect-Time": "2",
            "Connection": "close",
            "Host": "httpbin.org",
            "Total-Route-Time": "0",
            "User-Agent": "Go 1.1 package http",
            "Via": "1.1 vegur",
            "X-Request-Id": "6a22499a-2776-4aa1-80c0-686581a8be4d",
            "X-Tyk-Test": "2",
            "X-Tyk-Version": "1.2"
          },
          "origin": "127.0.0.1, 62.232.114.250",
          "url": "http://httpbin.org/get"
        }"
            },
            {
              "relative_url": "get",
              "code": 200,
              "headers": {
                "Access-Control-Allow-Credentials": [
                  "true"
                ],
                "Access-Control-Allow-Origin": [
                  "*"
                ],
                "Content-Length": [
                  "497"
                ],
                "Content-Type": [
                  "application/json"
                ],
                "Date": [
                  "Wed, 12 Nov 2014 15:32:43 GMT"
                ],
                "Server": [
                  "gunicorn/18.0"
                ],
                "Via": [
                  "1.1 vegur"
                ]
              },
              "body": "{
          "args": {},
          "headers": {
            "Accept-Encoding": "gzip",
            "Authorization": "1dbc83b9c431649d7698faa9797e2900f",
            "Connect-Time": "7",
            "Connection": "close",
            "Host": "httpbin.org",
            "Total-Route-Time": "0",
            "User-Agent": "Go 1.1 package http",
            "Via": "1.1 vegur",
            "X-Request-Id": "1ab61f50-51ff-4828-a7e2-17240385a6d2",
            "X-Tyk-Test": "1",
            "X-Tyk-Version": "1.2"
          },
          "origin": "127.0.0.1, 62.232.114.250",
          "url": "http://httpbin.org/get"
        }"
            }
        ]
        ```
      With the body for each request string encoded in the `body` field.


      * `expire_analytics_after`: If you are running a busy API, you may want to
      ensure that your MongoDB database does not overflow with old data. Set the
      `expire_analytics_after` value to the number of seconds you would like the
      data to last for. Setting this flag to anything above `0` will set an
      `expireAt` field for each record that is written to the database.


      **Important:** Tyk will not create the expiry index for you. In order to
      implement data expiry for your analytics data, ensure that the index is
      created This is easily achieved using the [MongoDB command line
      interface](https://docs.mongodb.com/getting-started/shell/client/).


      * `dont_set_quota_on_create`: This setting defaults to `false`, but if set
      to `true`, when the API is used to edit, create or add keys, the quota
      cache in Redis will not be re-set. By default, all updates or creates to
      Keys that have Quotas set will re-set the quota (This has been the default
      behaviour since 1.0).

        This behaviour can be bypassed on a case-by-case basis by using the `suppress_reset` parameter when making a REST API request. This is the advised mode of operation as it allows for manual, granular control over key quotas and reset timings.

      * `cache_options`: This section enables you to configure the caching
      behaviour of Tyk and to enable or disable the caching middleware for your
      API.


      * `cache_options.enable_cache`: Set this value to `true` if the cache
      should be enabled for this endpoint, setting it to false will stop all
      caching behaviour.


      * `cache_options.cache_timeout`: The amount of time, in seconds, to keep
      cached objects, defaults to `60` seconds.


      * `cache_options.cache_all_safe_requests`: Set this to `true` if you want
      all *safe* requests (GET, HEAD, OPTIONS) to be cached. This is a blanket
      setting for APIs where caching is required but you don't want to set
      individual paths up in the definition.


      * `cache_options.enable_upstream_cache_control`: Set this to `true` if you
      want your application to control the cache options for Tyk (TTL and
      whether to cache or not). See
      [Caching](/docs/basic-config-and-security/reduce-latency/caching/) for
      more details.


      * `response_processors`: Response processors need to be specifically
      defined so they are loaded on API creation, otherwise the middleware will
      not fire. In order to have the two main response middleware components
      fire, the following configuration object should be supplied.


      ```{json}
        "response_processors": [
          {
              "name": "header_injector",
              "options": {
                  "add_headers": {"name": "value"},
                  "remove_headers": ["name"]
              }
          },
          {
            "name": "response_body_transform",
            "options": {}
          }
        ]
      ```


      The options for the `header_injector` are global, and will apply to all
      outbound requests.
    name: Batch requests
paths:
  /tyk/apis:
    post:
      tags:
        - APIs
      summary: Create an API
      description: >-
        Create API. A single Tyk node can have its API Definitions queried,
        deleted and updated remotely. This functionality enables you to remotely
        update your Tyk definitions without having to manage the files manually.
      operationId: createApi
      parameters:
        - description: The base API which the new version will be linked to.
          example: 663a4ed9b6be920001b191ae
          in: query
          name: base_api_id
          required: false
          schema:
            type: string
        - description: >-
            The version name of the base API while creating the first version.
            This doesn't have to be sent for the next versions but if it is set,
            it will override base API version name.
          example: Default
          in: query
          name: base_api_version_name
          required: false
          schema:
            type: string
        - description: The version name of the created version.
          example: v2
          in: query
          name: new_version_name
          required: false
          schema:
            type: string
        - description: If true, the new version is set as default version.
          example: true
          in: query
          name: set_default
          required: false
          schema:
            type: boolean
      requestBody:
        content:
          application/json:
            example:
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
            schema:
              $ref: '#/components/schemas/APIDefinition'
      responses:
        '200':
          content:
            application/json:
              example:
                action: added
                key: b84fe1a04e5648927971c0557971565c
                status: ok
              schema:
                $ref: '#/components/schemas/ApiModifyKeySuccess'
          description: API created.
        '400':
          content:
            application/json:
              example:
                message: Request malformed
                status: error
              schema:
                $ref: '#/components/schemas/ApiStatusMessage'
          description: Bad Request
        '403':
          content:
            application/json:
              example:
                message: Attempted administrative access with invalid or missing key!
                status: error
              schema:
                $ref: '#/components/schemas/ApiStatusMessage'
          description: Forbidden
        '500':
          content:
            application/json:
              example:
                message: file object creation failed, write error
                status: error
              schema:
                $ref: '#/components/schemas/ApiStatusMessage'
          description: Internal server error.
components:
  schemas:
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
          $ref: '#/components/schemas/Scopes'
        session_lifetime:
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
          example:
            - Default
            - v1
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
    ApiModifyKeySuccess:
      properties:
        action:
          example: modified
          type: string
        key:
          example: b13d928b9972bd18
          type: string
        key_hash:
          type: string
        status:
          example: ok
          type: string
      type: object
    ApiStatusMessage:
      properties:
        message:
          type: string
        status:
          type: string
      type: object
    CORSConfig:
      properties:
        allow_credentials:
          example: false
          type: boolean
        allowed_headers:
          example:
            - Origin
            - Accept
            - Content-Type
            - Authorization
          items:
            type: string
          nullable: true
          type: array
        allowed_methods:
          example:
            - GET
            - HEAD
            - POST
          items:
            type: string
          nullable: true
          type: array
        allowed_origins:
          example:
            - https://*.foo.com
          items:
            type: string
          nullable: true
          type: array
        debug:
          example: true
          type: boolean
        enable:
          example: false
          type: boolean
        exposed_headers:
          example:
            - Accept
            - Content-Type
          items:
            type: string
          nullable: true
          type: array
        max_age:
          example: 24
          type: integer
        options_passthrough:
          example: false
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
          example: Authorization
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
          example: false
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
          example: 60
          format: int64
          type: integer
        enable_cache:
          example: true
          type: boolean
        enable_upstream_cache_control:
          example: false
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
          example: x-api-version
          type: string
        location:
          example: header
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
          type: number
        rate:
          type: number
      type: object
    GraphQLConfig:
      properties:
        enabled:
          type: boolean
        engine:
          $ref: '#/components/schemas/GraphQLEngineConfig'
        execution_mode:
          enum:
            - proxyOnly
            - executionEngine
            - subgraph
            - supergraph
            - ''
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
          enum:
            - '1'
            - '2'
            - ''
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
          example: /relative-path-examples/
          type: string
        preserve_host_header:
          type: boolean
        service_discovery:
          $ref: '#/components/schemas/ServiceDiscoveryConfiguration'
        strip_listen_path:
          example: true
          type: boolean
        target_list:
          items:
            type: string
          nullable: true
          type: array
        target_url:
          example: https://httpbin.org/
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
    SignatureConfig:
      properties:
        algorithm:
          type: string
        allowed_clock_skew:
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
          example: PreMiddlewareFunction
          type: string
        path:
          type: string
        raw_body_only:
          example: false
          type: boolean
        require_session:
          example: false
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
          type: integer
        url:
          type: string
      type: object
    UptimeTestsConfig:
      properties:
        expire_utime_after:
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
          example: true
          type: boolean
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
          type: number
        rate:
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
          enum:
            - blob
            - file
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
    EndpointMethodMeta:
      properties:
        action:
          enum:
            - no_action
            - reply
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
          enum:
            - json
            - xml
          type: string
        template_mode:
          enum:
            - blob
            - file
          type: string
        template_source:
          type: string
      type: object
    RoutingTrigger:
      properties:
        'on':
          enum:
            - all
            - any
          type: string
        options:
          $ref: '#/components/schemas/RoutingTriggerOptions'
        rewrite_to:
          type: string
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
    StringRegexMap:
      properties:
        match_rx:
          type: string
        reverse:
          type: boolean
      type: object
  securitySchemes:
    api_key:
      description: Api key
      in: header
      name: X-Tyk-Authorization
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).
