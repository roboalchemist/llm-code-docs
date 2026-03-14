# Source: https://tyk.io/docs/api-reference/organisation-quotas/create-an-organisation-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an organisation key

> This work similar to Keys API except that Key ID is always equals Organisation ID



## OpenAPI

````yaml swagger/5.8/gateway-swagger.yml post /tyk/org/keys/{keyID}
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
  /tyk/org/keys/{keyID}:
    post:
      tags:
        - Organisation Quotas
      summary: Create an organisation key
      description: >-
        This work similar to Keys API except that Key ID is always equals
        Organisation ID
      operationId: addOrgKey
      parameters:
        - description: The Key ID
          example: e389ae00a2b145feaf28d6cc11f0f86d
          in: path
          name: keyID
          required: true
          schema:
            type: string
        - description: >-
            Adding the reset_quota parameter and setting it to 1, will cause Tyk
            reset the organisations quota in the live quota manager, it is
            recommended to use this mechanism to reset organisation-level access
            if a monthly subscription is in place.
          example: '1'
          in: query
          name: reset_quota
          required: false
          schema:
            enum:
              - '1'
            type: string
      requestBody:
        content:
          application/json:
            example:
              access_rights:
                itachi-api:
                  allowed_urls:
                    - methods:
                        - GET
                      url: /users
                  api_id: 8ddd91f3cda9453442c477b06c4e2da4
                  api_name: Itachi api
                  limit:
                    per: 60
                    quota_max: 10000
                    quota_remaining: 10000
                    quota_renewal_rate: 3600
                    rate: 1000
                    throttle_interval: 10
                    throttle_retry_limit: 10
                  versions:
                    - Default
              alias: portal-key
              allowance: 1000
              apply_policies:
                - 5ead7120575961000181867e
              date_created: '2024-08-09T14:40:34.87614+03:00'
              enable_detailed_recording: true
              last_updated: '1723203634'
              meta_data:
                new-update-key-sample: update-key-sample
                tyk_developer_id: 62b3fb9a1d5e4f00017226f5
                update: sample policy update
                user_type: mobile_user
              org_id: 5e9d9544a1dcd60001d0ed20
              per: 60
              quota_max: 10000
              quota_renewal_rate: 3600
              quota_renews: 1723207234
              rate: 1000
              tags:
                - security
                - edge
                - edge-eu
              throttle_interval: 10
              throttle_retry_limit: 10
            schema:
              $ref: '#/components/schemas/SessionState'
      responses:
        '200':
          content:
            application/json:
              example:
                action: added
                key: e389ae00a2b145feaf28d6cc11f0f86d
                status: ok
              schema:
                $ref: '#/components/schemas/ApiModifyKeySuccess'
          description: OK
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
        '404':
          content:
            application/json:
              example:
                message: No such organisation found in Active API list
                status: error
              schema:
                $ref: '#/components/schemas/ApiStatusMessage'
          description: Not Found
        '500':
          content:
            application/json:
              example:
                message: 'Error writing to key store '
                status: error
              schema:
                $ref: '#/components/schemas/ApiStatusMessage'
          description: Internal server error.
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
          example: portal-developer@example.org
          type: string
        allowance:
          example: 1000
          format: double
          type: number
        apply_policies:
          example:
            - 641c15dd0fffb800010197bf
          items:
            type: string
          nullable: true
          type: array
        apply_policy_id:
          deprecated: true
          description: >-
            deprecated use apply_policies going forward instead to send a list
            of policies ids
          example: 641c15dd0fffb800010197bf
          type: string
        basic_auth_data:
          $ref: '#/components/schemas/BasicAuthData'
        certificate:
          type: string
        data_expires:
          example: 0
          format: int64
          type: integer
        date_created:
          example: '2024-03-13T03:56:46.568042549Z'
          format: date-time
          type: string
        enable_detail_recording:
          deprecated: true
          description: deprecated use enable_detailed_recording going forward instead
          example: false
          type: boolean
        enable_detailed_recording:
          example: true
          type: boolean
        enable_http_signature_validation:
          example: false
          type: boolean
        expires:
          example: 1712895619
          format: int64
          type: integer
        hmac_enabled:
          example: false
          type: boolean
        hmac_string:
          type: string
        id_extractor_deadline:
          format: int64
          type: integer
        is_inactive:
          example: false
          type: boolean
        jwt_data:
          $ref: '#/components/schemas/JWTData'
        last_check:
          example: 0
          format: int64
          type: integer
        last_updated:
          example: '1710302206'
          type: string
        max_query_depth:
          example: -1
          type: integer
        meta_data:
          additionalProperties: {}
          example:
            tyk_developer_id: 62b3fb9a1d5e4f00017226f5
          nullable: true
          type: object
        monitor:
          $ref: '#/components/schemas/Monitor'
        oauth_client_id:
          type: string
        oauth_keys:
          additionalProperties:
            type: string
          nullable: true
          type: object
        org_id:
          example: 5e9d9544a1dcd60001d0ed20
          type: string
        per:
          example: 5
          format: double
          type: number
        quota_max:
          example: 20000
          format: int64
          type: integer
        quota_remaining:
          example: 20000
          format: int64
          type: integer
        quota_renewal_rate:
          example: 31556952
          format: int64
          type: integer
        quota_renews:
          example: 1710302205
          format: int64
          type: integer
        rate:
          example: 1
          format: double
          type: number
        rsa_certificate_id:
          type: string
        session_lifetime:
          example: 0
          format: int64
          type: integer
        smoothing:
          $ref: '#/components/schemas/RateLimitSmoothing'
        tags:
          example:
            - edge
            - edge-eu
          items:
            type: string
          nullable: true
          type: array
        throttle_interval:
          example: 10
          format: double
          type: number
        throttle_retry_limit:
          example: 1000
          type: integer
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
    BasicAuthData:
      properties:
        hash_type:
          type: string
        password:
          type: string
      type: object
    JWTData:
      properties:
        secret:
          type: string
      type: object
    Monitor:
      properties:
        trigger_limits:
          example:
            - 80
            - 60
            - 50
          items:
            type: number
          nullable: true
          type: array
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