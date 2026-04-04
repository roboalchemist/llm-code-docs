# Source: https://tyk.io/docs/api-reference/policies/list-policies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List policies.

> Retrieve all the policies in your Tyk instance. Returns an array policies.



## OpenAPI

````yaml swagger/5.8/gateway-swagger.yml get /tyk/policies
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
  /tyk/policies:
    get:
      tags:
        - Policies
      summary: List policies.
      description: >-
        Retrieve all the policies in your Tyk instance. Returns an array
        policies.
      operationId: listPolicies
      responses:
        '200':
          content:
            application/json:
              examples:
                policiesExample:
                  $ref: '#/components/examples/policiesExample'
              schema:
                items:
                  $ref: '#/components/schemas/Policy'
                type: array
          description: List of all policies.
        '403':
          content:
            application/json:
              example:
                message: Attempted administrative access with invalid or missing key!
                status: error
              schema:
                $ref: '#/components/schemas/ApiStatusMessage'
          description: Forbidden
components:
  examples:
    policiesExample:
      value:
        - _id: ''
          access_rights:
            8ddd91f3cda9453442c477b06c4e2da4:
              allowance_scope: ''
              allowed_types: []
              allowed_urls:
                - methods:
                    - GET
                  url: /users
              api_id: 8ddd91f3cda9453442c477b06c4e2da4
              api_name: Itachi api
              disable_introspection: false
              field_access_rights: []
              limit:
                max_query_depth: 0
                per: 0
                quota_max: 0
                quota_remaining: 0
                quota_renewal_rate: 0
                quota_renews: 0
                rate: 0
                smoothing:
                  delay: 30
                  enabled: false
                  step: 100
                  threshold: 500
                  trigger: 0.8
                throttle_interval: 0
                throttle_retry_limit: 0
              restricted_types: []
              versions:
                - Default
          active: true
          enable_http_signature_validation: false
          graphql_access_rights: null
          hmac_enabled: false
          id: 5ead7120575961000181867e
          is_inactive: false
          key_expires_in: 2592000
          last_updated: '1716980105'
          max_query_depth: -1
          meta_data:
            user_type: mobile_user
          name: Sample policy
          org_id: 664a14650619d40001f1f00f
          partitions:
            acl: true
            complexity: false
            per_api: false
            quota: true
            rate_limit: true
          per: 60
          quota_max: 10000
          quota_renewal_rate: 3600
          rate: 1000
          smoothing:
            delay: 30
            enabled: false
            step: 100
            threshold: 500
            trigger: 0.8
          tags:
            - security
          throttle_interval: 10
          throttle_retry_limit: 10
  schemas:
    Policy:
      properties:
        _id:
          example: 5ead7120575961000181867e
          type: string
        access_rights:
          additionalProperties:
            $ref: '#/components/schemas/AccessDefinition'
          nullable: true
          type: object
        active:
          example: true
          type: boolean
        enable_http_signature_validation:
          example: false
          type: boolean
        graphql_access_rights:
          additionalProperties:
            $ref: '#/components/schemas/GraphAccessDefinition'
          nullable: true
          type: object
        hmac_enabled:
          example: false
          type: boolean
        id:
          example: 5ead7120575961000181867e
          type: string
        is_inactive:
          example: false
          type: boolean
        key_expires_in:
          example: 0
          format: int64
          type: integer
        last_updated:
          example: '1655965189'
          type: string
        max_query_depth:
          example: -1
          type: integer
        meta_data:
          additionalProperties: {}
          nullable: true
          type: object
        name:
          example: Swagger Petstore Policy
          type: string
        org_id:
          example: 5e9d9544a1dcd60001d0ed20
          type: string
        partitions:
          $ref: '#/components/schemas/PolicyPartitions'
        per:
          example: 60
          format: double
          type: number
        quota_max:
          example: -1
          format: int64
          type: integer
        quota_renewal_rate:
          example: 3600
          format: int64
          type: integer
        rate:
          example: 1000
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
          example: -1
          format: double
          type: number
        throttle_retry_limit:
          example: -1
          type: integer
      type: object
    ApiStatusMessage:
      properties:
        message:
          type: string
        status:
          type: string
      type: object
    AccessDefinition:
      properties:
        allowance_scope:
          example: d371b83b249845a2497ab9a947fd6210
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
          example: d1dfc6a927a046c54c0ed470f19757cc
          type: string
        api_name:
          example: Rate Limit Proxy API
          type: string
        disable_introspection:
          example: false
          type: boolean
        endpoints:
          $ref: '#/components/schemas/Endpoints'
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
          example:
            - Default
            - v2
          items:
            type: string
          nullable: true
          type: array
      type: object
    GraphAccessDefinition:
      type: object
    PolicyPartitions:
      properties:
        acl:
          example: true
          type: boolean
        complexity:
          example: false
          type: boolean
        per_api:
          example: false
          type: boolean
        quota:
          example: true
          type: boolean
        rate_limit:
          example: true
          type: boolean
      type: object
    RateLimitSmoothing:
      properties:
        delay:
          type: integer
        enabled:
          type: boolean
        step:
          type: integer
        threshold:
          type: integer
        trigger:
          type: number
      type: object
      nullable: true
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
          example:
            - GET
            - POST
            - DELETE
            - PUT
          items:
            type: string
          nullable: true
          type: array
        url:
          example: anything/rate-limit-1-per-5
          type: string
      type: object
    Endpoints:
      items:
        $ref: '#/components/schemas/Endpoint'
      type: array
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
      properties:
        max_query_depth:
          type: integer
        per:
          type: number
        quota_max:
          type: integer
        quota_remaining:
          type: integer
        quota_renewal_rate:
          type: integer
        quota_renews:
          type: integer
        rate:
          type: number
        smoothing:
          $ref: '#/components/schemas/RateLimitSmoothing'
        throttle_interval:
          type: number
        throttle_retry_limit:
          type: integer
      type: object
    Endpoint:
      properties:
        methods:
          $ref: '#/components/schemas/EndpointMethods'
        path:
          type: string
      type: object
    FieldLimits:
      properties:
        max_query_depth:
          type: integer
      type: object
    EndpointMethods:
      items:
        $ref: '#/components/schemas/EndpointMethod'
      type: array
    EndpointMethod:
      properties:
        limit:
          $ref: '#/components/schemas/RateLimitType2'
        name:
          type: string
      type: object
    RateLimitType2:
      properties:
        per:
          type: number
        rate:
          type: number
        smoothing:
          $ref: '#/components/schemas/RateLimitSmoothing'
      type: object
  securitySchemes:
    api_key:
      description: Api key
      in: header
      name: X-Tyk-Authorization
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).