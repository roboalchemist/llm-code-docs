# Source: https://tyk.io/docs/api-reference/tyk-oas-apis/create-an-api-with-tyk-oas-format.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an API with Tyk OAS format

> Create an API with Tyk OAS API format on the Tyk Gateway.

## OpenAPI

````yaml swagger/5.8/gateway-swagger.yml post /tyk/apis/oas
openapi: 3.0.3
info:
  contact:
    email: support@tyk.io
    name: Tyk Technologies
    url: https://tyk.io/contact
  description: >+
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
  version: 5.8.9
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
  /tyk/apis/oas:
    post:
      tags:
        - Tyk OAS APIs
      summary: Create an API with Tyk OAS format.
      description: Create an API with Tyk OAS API format on the Tyk Gateway.
      operationId: createApiOAS
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
              components:
                securitySchemes:
                  bearerAuth:
                    description: The API Access Credentials
                    scheme: bearer
                    type: http
              info:
                description: This is a sample OAS.
                title: OAS Sample
                version: 1.0.0
              openapi: 3.0.3
              paths:
                /api/sample/users:
                  get:
                    operationId: getUsers
                    responses:
                      '200':
                        content:
                          application/json:
                            schema:
                              items:
                                properties:
                                  name:
                                    type: string
                                type: object
                              type: array
                        description: fetched users
                    summary: Get users
                    tags:
                      - users
              security:
                - bearerAuth: []
              servers:
                - url: https://localhost:8080
              x-tyk-api-gateway:
                info:
                  name: user
                  state:
                    active: true
                server:
                  listenPath:
                    strip: true
                    value: /user-test/
                upstream:
                  url: https://localhost:8080
            schema:
              allOf:
                - $ref: '#/components/schemas/OpenAPI3Schema'
                - $ref: '#/components/schemas/TykVendorExtension'
      responses:
        '200':
          content:
            application/json:
              example:
                action: added
                key: e30bee13ad4248c3b529a4c58bb7be4e
                status: ok
              schema:
                $ref: '#/components/schemas/ApiModifyKeySuccess'
          description: API created.
        '400':
          content:
            application/json:
              example:
                message: the payload should contain x-tyk-api-gateway
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
    OpenAPI3Schema:
      type: object
      additionalProperties: true
    TykVendorExtension:
      properties:
        x-tyk-api-gateway:
          $ref: '#/components/schemas/XTykAPIGateway'
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
    XTykAPIGateway:
      properties:
        info:
          $ref: '#/components/schemas/Info'
        middleware:
          $ref: '#/components/schemas/Middleware'
        server:
          $ref: '#/components/schemas/Server'
        upstream:
          $ref: '#/components/schemas/Upstream'
      type: object
    Info:
      properties:
        dbId:
          type: string
        expiration:
          type: string
        id:
          type: string
        name:
          type: string
        orgId:
          type: string
        state:
          $ref: '#/components/schemas/State'
        versioning:
          $ref: '#/components/schemas/Versioning'
      type: object
    Middleware:
      properties:
        global:
          $ref: '#/components/schemas/Global'
        operations:
          $ref: '#/components/schemas/Operations'
      type: object
    Server:
      properties:
        authentication:
          $ref: '#/components/schemas/Authentication'
        clientCertificates:
          $ref: '#/components/schemas/ClientCertificates'
        customDomain:
          $ref: '#/components/schemas/Domain'
        detailedActivityLogs:
          $ref: '#/components/schemas/DetailedActivityLogs'
        detailedTracing:
          $ref: '#/components/schemas/DetailedTracing'
        eventHandlers:
          $ref: '#/components/schemas/EventHandlers'
        gatewayTags:
          $ref: '#/components/schemas/GatewayTags'
        listenPath:
          $ref: '#/components/schemas/ListenPath'
      type: object
    Upstream:
      properties:
        certificatePinning:
          $ref: '#/components/schemas/CertificatePinning'
        mutualTLS:
          $ref: '#/components/schemas/MutualTLS'
        rateLimit:
          $ref: '#/components/schemas/RateLimit'
        serviceDiscovery:
          $ref: '#/components/schemas/ServiceDiscovery'
        test:
          $ref: '#/components/schemas/Test'
        url:
          type: string
      type: object
    State:
      properties:
        active:
          type: boolean
        internal:
          type: boolean
      type: object
    Versioning:
      properties:
        default:
          type: string
        enabled:
          type: boolean
        fallbackToDefault:
          type: boolean
        key:
          type: string
        location:
          type: string
        name:
          type: string
        stripVersioningData:
          type: boolean
        urlVersioningPattern:
          type: string
        versions:
          items:
            $ref: '#/components/schemas/VersionToID'
          nullable: true
          type: array
      type: object
    Global:
      properties:
        cache:
          $ref: '#/components/schemas/Cache'
        contextVariables:
          $ref: '#/components/schemas/ContextVariables'
        cors:
          $ref: '#/components/schemas/CORS'
        pluginConfig:
          $ref: '#/components/schemas/PluginConfig'
        postAuthenticationPlugin:
          $ref: '#/components/schemas/PostAuthenticationPlugin'
        postAuthenticationPlugins:
          $ref: '#/components/schemas/CustomPlugins'
        postPlugin:
          $ref: '#/components/schemas/PostPlugin'
        postPlugins:
          $ref: '#/components/schemas/CustomPlugins'
        prePlugin:
          $ref: '#/components/schemas/PrePlugin'
        prePlugins:
          $ref: '#/components/schemas/CustomPlugins'
        responsePlugin:
          $ref: '#/components/schemas/ResponsePlugin'
        responsePlugins:
          $ref: '#/components/schemas/CustomPlugins'
        trafficLogs:
          $ref: '#/components/schemas/TrafficLogs'
        transformRequestHeaders:
          $ref: '#/components/schemas/TransformHeaders'
        transformResponseHeaders:
          $ref: '#/components/schemas/TransformHeaders'
      type: object
    Operations:
      additionalProperties:
        $ref: '#/components/schemas/Operation'
      type: object
    Authentication:
      properties:
        baseIdentityProvider:
          type: string
        custom:
          $ref: '#/components/schemas/CustomPluginAuthentication'
        enabled:
          type: boolean
        hmac:
          $ref: '#/components/schemas/HMAC'
        oidc:
          $ref: '#/components/schemas/OIDC'
        securitySchemes:
          $ref: '#/components/schemas/SecuritySchemes'
        stripAuthorizationData:
          type: boolean
      type: object
    ClientCertificates:
      properties:
        allowlist:
          items:
            type: string
          nullable: true
          type: array
        enabled:
          type: boolean
      type: object
    Domain:
      properties:
        certificates:
          items:
            type: string
          type: array
        enabled:
          type: boolean
        name:
          type: string
      type: object
    DetailedActivityLogs:
      properties:
        enabled:
          type: boolean
      type: object
    DetailedTracing:
      properties:
        enabled:
          type: boolean
      type: object
    EventHandlers:
      items:
        $ref: '#/components/schemas/EventHandler'
      type: array
    GatewayTags:
      properties:
        enabled:
          type: boolean
        tags:
          items:
            type: string
          nullable: true
          type: array
      type: object
    ListenPath:
      properties:
        strip:
          type: boolean
        value:
          type: string
      type: object
    CertificatePinning:
      properties:
        domainToPublicKeysMapping:
          $ref: '#/components/schemas/PinnedPublicKeys'
        enabled:
          type: boolean
      type: object
    MutualTLS:
      properties:
        domainToCertificateMapping:
          items:
            $ref: '#/components/schemas/DomainToCertificate'
          nullable: true
          type: array
        enabled:
          type: boolean
      type: object
    RateLimit:
      properties:
        enabled:
          type: boolean
        per:
          type: integer
        rate:
          type: integer
      type: object
    ServiceDiscovery:
      properties:
        cache:
          $ref: '#/components/schemas/ServiceDiscoveryCache'
        cacheTimeout:
          type: integer
        dataPath:
          type: string
        enabled:
          type: boolean
        endpointReturnsList:
          type: boolean
        parentDataPath:
          type: string
        portDataPath:
          type: string
        queryEndpoint:
          type: string
        targetPath:
          type: string
        useNestedQuery:
          type: boolean
        useTargetList:
          type: boolean
      type: object
    Test:
      properties:
        serviceDiscovery:
          $ref: '#/components/schemas/ServiceDiscovery'
      type: object
    VersionToID:
      properties:
        id:
          type: string
        name:
          type: string
      type: object
    Cache:
      properties:
        cacheAllSafeRequests:
          type: boolean
        cacheByHeaders:
          items:
            type: string
          type: array
        cacheResponseCodes:
          items:
            type: integer
          type: array
        controlTTLHeaderName:
          type: string
        enableUpstreamCacheControl:
          type: boolean
        enabled:
          type: boolean
        timeout:
          type: integer
      type: object
    ContextVariables:
      properties:
        enabled:
          type: boolean
      type: object
    CORS:
      properties:
        allowCredentials:
          type: boolean
        allowedHeaders:
          items:
            type: string
          type: array
        allowedMethods:
          items:
            type: string
          type: array
        allowedOrigins:
          items:
            type: string
          type: array
        debug:
          type: boolean
        enabled:
          type: boolean
        exposedHeaders:
          items:
            type: string
          type: array
        maxAge:
          type: integer
        optionsPassthrough:
          type: boolean
      type: object
    PluginConfig:
      properties:
        bundle:
          $ref: '#/components/schemas/PluginBundle'
        data:
          $ref: '#/components/schemas/PluginConfigData'
        driver:
          type: string
      type: object
    PostAuthenticationPlugin:
      properties:
        plugins:
          $ref: '#/components/schemas/CustomPlugins'
      type: object
    CustomPlugins:
      items:
        $ref: '#/components/schemas/CustomPlugin'
      type: array
    PostPlugin:
      properties:
        plugins:
          $ref: '#/components/schemas/CustomPlugins'
      type: object
    PrePlugin:
      properties:
        plugins:
          $ref: '#/components/schemas/CustomPlugins'
      type: object
    ResponsePlugin:
      properties:
        plugins:
          $ref: '#/components/schemas/CustomPlugins'
      type: object
    TrafficLogs:
      properties:
        enabled:
          type: boolean
      type: object
    TransformHeaders:
      properties:
        add:
          $ref: '#/components/schemas/Headers'
        enabled:
          type: boolean
        remove:
          items:
            type: string
          type: array
      type: object
    Operation:
      properties:
        allow:
          $ref: '#/components/schemas/Allowance'
        block:
          $ref: '#/components/schemas/Allowance'
        cache:
          $ref: '#/components/schemas/CachePlugin'
        circuitBreaker:
          $ref: '#/components/schemas/CircuitBreaker'
        doNotTrackEndpoint:
          $ref: '#/components/schemas/TrackEndpoint'
        enforceTimeout:
          $ref: '#/components/schemas/EnforceTimeout'
        ignoreAuthentication:
          $ref: '#/components/schemas/Allowance'
        internal:
          $ref: '#/components/schemas/Internal'
        mockResponse:
          $ref: '#/components/schemas/MockResponse'
        postPlugins:
          $ref: '#/components/schemas/EndpointPostPlugins'
        rateLimit:
          $ref: '#/components/schemas/RateLimitEndpoint'
        requestSizeLimit:
          $ref: '#/components/schemas/RequestSizeLimit'
        trackEndpoint:
          $ref: '#/components/schemas/TrackEndpoint'
        transformRequestBody:
          $ref: '#/components/schemas/TransformBody'
        transformRequestHeaders:
          $ref: '#/components/schemas/TransformHeaders'
        transformRequestMethod:
          $ref: '#/components/schemas/TransformRequestMethod'
        transformResponseBody:
          $ref: '#/components/schemas/TransformBody'
        transformResponseHeaders:
          $ref: '#/components/schemas/TransformHeaders'
        urlRewrite:
          $ref: '#/components/schemas/URLRewrite'
        validateRequest:
          $ref: '#/components/schemas/ValidateRequest'
        virtualEndpoint:
          $ref: '#/components/schemas/VirtualEndpoint'
      type: object
    CustomPluginAuthentication:
      properties:
        AuthSources:
          $ref: '#/components/schemas/AuthSources'
        config:
          $ref: '#/components/schemas/AuthenticationPlugin'
        enabled:
          type: boolean
      type: object
    HMAC:
      properties:
        AuthSources:
          $ref: '#/components/schemas/AuthSources'
        allowedAlgorithms:
          items:
            type: string
          type: array
        allowedClockSkew:
          type: number
        enabled:
          type: boolean
      type: object
    OIDC:
      properties:
        AuthSources:
          $ref: '#/components/schemas/AuthSources'
        enabled:
          type: boolean
        providers:
          items:
            $ref: '#/components/schemas/ProviderType2'
          type: array
        scopes:
          $ref: '#/components/schemas/ScopesType2'
        segregateByClientId:
          type: boolean
      type: object
    SecuritySchemes:
      additionalProperties: {}
      type: object
    EventHandler:
      properties:
        enabled:
          type: boolean
        id:
          type: string
        name:
          type: string
        trigger:
          type: string
        type:
          type: string
      type: object
    PinnedPublicKeys:
      items:
        $ref: '#/components/schemas/PinnedPublicKey'
      nullable: true
      type: array
    DomainToCertificate:
      properties:
        certificate:
          type: string
        domain:
          type: string
      type: object
    ServiceDiscoveryCache:
      properties:
        enabled:
          type: boolean
        timeout:
          type: integer
      type: object
    PluginBundle:
      properties:
        enabled:
          type: boolean
        path:
          type: string
      type: object
    PluginConfigData:
      properties:
        enabled:
          type: boolean
        value:
          additionalProperties: {}
          nullable: true
          type: object
      type: object
    CustomPlugin:
      properties:
        enabled:
          type: boolean
        functionName:
          type: string
        path:
          type: string
        rawBodyOnly:
          type: boolean
        requireSession:
          type: boolean
      type: object
    Headers:
      items:
        $ref: '#/components/schemas/Header'
      type: array
    Allowance:
      properties:
        enabled:
          type: boolean
        ignoreCase:
          type: boolean
      type: object
    CachePlugin:
      properties:
        cacheByRegex:
          type: string
        cacheResponseCodes:
          items:
            type: integer
          type: array
        enabled:
          type: boolean
        timeout:
          type: integer
      type: object
    CircuitBreaker:
      properties:
        coolDownPeriod:
          type: integer
        enabled:
          type: boolean
        halfOpenStateEnabled:
          type: boolean
        sampleSize:
          type: integer
        threshold:
          type: number
      type: object
    TrackEndpoint:
      properties:
        enabled:
          type: boolean
      type: object
    EnforceTimeout:
      properties:
        enabled:
          type: boolean
        value:
          type: integer
      type: object
    Internal:
      properties:
        enabled:
          type: boolean
      type: object
    MockResponse:
      properties:
        body:
          type: string
        code:
          type: integer
        enabled:
          type: boolean
        fromOASExamples:
          $ref: '#/components/schemas/FromOASExamples'
        headers:
          $ref: '#/components/schemas/Headers'
      type: object
    EndpointPostPlugins:
      items:
        $ref: '#/components/schemas/EndpointPostPlugin'
      type: array
    RateLimitEndpoint:
      properties:
        enabled:
          type: boolean
        per:
          type: integer
        rate:
          type: integer
      type: object
    RequestSizeLimit:
      properties:
        enabled:
          type: boolean
        value:
          type: integer
      type: object
    TransformBody:
      properties:
        body:
          type: string
        enabled:
          type: boolean
        format:
          type: string
        path:
          type: string
      type: object
    TransformRequestMethod:
      properties:
        enabled:
          type: boolean
        toMethod:
          type: string
      type: object
    URLRewrite:
      properties:
        enabled:
          type: boolean
        pattern:
          type: string
        rewriteTo:
          type: string
        triggers:
          items:
            $ref: '#/components/schemas/URLRewriteTrigger'
          type: array
      type: object
    ValidateRequest:
      properties:
        enabled:
          type: boolean
        errorResponseCode:
          type: integer
      type: object
    VirtualEndpoint:
      properties:
        body:
          type: string
        enabled:
          type: boolean
        functionName:
          type: string
        name:
          type: string
        path:
          type: string
        proxyOnError:
          type: boolean
        requireSession:
          type: boolean
      type: object
    AuthSources:
      properties:
        cookie:
          $ref: '#/components/schemas/AuthSource'
        header:
          $ref: '#/components/schemas/AuthSource'
        query:
          $ref: '#/components/schemas/AuthSource'
      type: object
    AuthenticationPlugin:
      properties:
        enabled:
          type: boolean
        functionName:
          type: string
        idExtractor:
          $ref: '#/components/schemas/IDExtractor'
        path:
          type: string
        rawBodyOnly:
          type: boolean
      type: object
    ProviderType2:
      properties:
        clientToPolicyMapping:
          items:
            $ref: '#/components/schemas/ClientToPolicy'
          type: array
        issuer:
          type: string
      type: object
    ScopesType2:
      properties:
        claimName:
          type: string
        scopeToPolicyMapping:
          items:
            $ref: '#/components/schemas/ScopeToPolicy'
          type: array
      type: object
    PinnedPublicKey:
      properties:
        domain:
          type: string
        publicKeys:
          items:
            type: string
          nullable: true
          type: array
      type: object
    Header:
      properties:
        name:
          type: string
        value:
          type: string
      type: object
    FromOASExamples:
      properties:
        code:
          type: integer
        contentType:
          type: string
        enabled:
          type: boolean
        exampleName:
          type: string
      type: object
    EndpointPostPlugin:
      properties:
        enabled:
          type: boolean
        functionName:
          type: string
        name:
          type: string
        path:
          type: string
      type: object
    URLRewriteTrigger:
      properties:
        condition:
          type: string
        rewriteTo:
          type: string
        rules:
          items:
            $ref: '#/components/schemas/URLRewriteRule'
          type: array
      type: object
    AuthSource:
      properties:
        enabled:
          type: boolean
        name:
          type: string
      type: object
    IDExtractor:
      properties:
        config:
          $ref: '#/components/schemas/IDExtractorConfig'
        enabled:
          type: boolean
        source:
          type: string
        with:
          type: string
      type: object
    ClientToPolicy:
      properties:
        clientId:
          type: string
        policyId:
          type: string
      type: object
    ScopeToPolicy:
      properties:
        policyId:
          type: string
        scope:
          type: string
      type: object
    URLRewriteRule:
      properties:
        in:
          type: string
        name:
          type: string
        negate:
          type: boolean
        pattern:
          type: string
      type: object
    IDExtractorConfig:
      properties:
        formParamName:
          type: string
        headerName:
          type: string
        regexp:
          type: string
        regexpMatchIndex:
          type: integer
        xPathExp:
          type: string
      type: object
  securitySchemes:
    api_key:
      description: Api key
      in: header
      name: X-Tyk-Authorization
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).
