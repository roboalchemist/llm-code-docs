# Source: https://tyk.io/docs/api-reference/streams-apis/update-streams-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Streams API.

> Updating an API definition uses the same signature object as a `POST`. It will first ensure that the API ID being updated is the same as in the `PUT` object.<br/> Updating will completely replace the file descriptor and will not change an API definition that has already been loaded. The hot-reload endpoint will need to be called to push the new definition to live.



## OpenAPI

````yaml swagger/5.8/dashboard-swagger.yml put /api/apis/streams/{apiId}
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
  /api/apis/streams/{apiId}:
    put:
      tags:
        - Streams APIs
      summary: Update Streams API.
      description: >-
        Updating an API definition uses the same signature object as a `POST`.
        It will first ensure that the API ID being updated is the same as in the
        `PUT` object.<br/> Updating will completely replace the file descriptor
        and will not change an API definition that has already been loaded. The
        hot-reload endpoint will need to be called to push the new definition to
        live.
      operationId: updateStreamsApi
      parameters:
        - name: Content-Type
          in: header
          required: true
          description: >-
            Content type for streams endpoints should be
            `application/vnd.tyk.streams.oas`
          schema:
            type: string
            enum:
              - application/vnd.tyk.streams.oas
        - description: ID of the API you want to update.
          example: 4c1c0d8fc885401053ddac4e39ef676b
          in: path
          name: apiId
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/vnd.tyk.streams.oas:
            examples:
              StreamsAPIExample:
                $ref: '#/components/examples/streamsExample'
            schema:
              allOf:
                - $ref: '#/components/schemas/OpenAPI3Schema'
                - $ref: '#/components/schemas/TykVendorExtension'
                - $ref: '#/components/schemas/XTykStreaming'
      responses:
        '200':
          content:
            application/json:
              example:
                Message: API updated.
                Meta: null
                Status: OK
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Updated API.
        '400':
          content:
            application/json:
              example:
                Message: >-
                  The payload should contain x-tyk-api-gateway and/or
                  x-tyk-streaming.
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Malformed API data.
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
                Message: Found API with same url.
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Forbidden
        '404':
          content:
            application/json:
              example:
                Message: API definition does not exist
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: API not found.
        '500':
          content:
            application/json:
              example:
                Message: Error while creating API.
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Internal server error.
components:
  examples:
    streamsExample:
      value:
        components:
          securitySchemes:
            bearerAuth:
              description: The API Access Credentials
              scheme: bearer
              type: http
        info:
          description: This is a sample Streams API.
          title: Streams Sample
          version: 1.0.0
        openapi: 3.0.3
        paths:
          /api/sample/users:
            get:
              operationId: getUsersSample
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
              value: /user-test-six/
          upstream:
            url: https://localhost:8080
        x-tyk-streaming:
          streams:
            stream1:
              input:
                kafka:
                  addresses:
                    - localhost:9093
                  auto_replay_nacks: true
                  checkpoint_limit: 1024
                  consumer_group: group1
                  target_version: 3.3.0
                  topics:
                    - instrument.json.AMZN
                    - instrument.json.GOOG
              output:
                broker:
                  outputs:
                    - stdout:
                        codec: lines
                    - http_server:
                        allowed_verbs:
                          - GET
                        path: /one
                        stream_path: /sse
                        ws_path: /ws
                  pattern: fan_out
  schemas:
    OpenAPI3Schema:
      type: object
      additionalProperties: true
    TykVendorExtension:
      properties:
        x-tyk-api-gateway:
          $ref: '#/components/schemas/XTykAPIGateway'
      type: object
    XTykStreaming:
      properties:
        x-tyk-streaming:
          type: object
          properties:
            streams:
              type: object
              additionalProperties: true
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
      nullable: true
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
      nullable: true
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
      nullable: true
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
      nullable: true
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
      nullable: true
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
      nullable: true
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
      nullable: true
      properties:
        enabled:
          type: boolean
      type: object
    DetailedTracing:
      nullable: true
      properties:
        enabled:
          type: boolean
      type: object
    EventHandlers:
      items:
        $ref: '#/components/schemas/EventHandler'
      type: array
    GatewayTags:
      nullable: true
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
      nullable: true
      properties:
        domainToPublicKeysMapping:
          $ref: '#/components/schemas/PinnedPublicKeys'
        enabled:
          type: boolean
      type: object
    MutualTLS:
      nullable: true
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
      nullable: true
      properties:
        enabled:
          type: boolean
        per:
          $ref: '#/components/schemas/TimeReadableDuration'
        rate:
          type: integer
      type: object
    ServiceDiscovery:
      nullable: true
      properties:
        cache:
          $ref: '#/components/schemas/ServiceDiscoveryCache'
        cacheTimeout:
          format: int64
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
      nullable: true
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
      nullable: true
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
          format: int64
          type: integer
      type: object
    ContextVariables:
      nullable: true
      properties:
        enabled:
          type: boolean
      type: object
    CORS:
      nullable: true
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
      nullable: true
      properties:
        bundle:
          $ref: '#/components/schemas/PluginBundle'
        data:
          $ref: '#/components/schemas/PluginConfigData'
        driver:
          type: string
      type: object
    PostAuthenticationPlugin:
      nullable: true
      properties:
        plugins:
          $ref: '#/components/schemas/CustomPlugins'
      type: object
    CustomPlugins:
      items:
        $ref: '#/components/schemas/CustomPlugin'
      type: array
    PostPlugin:
      nullable: true
      properties:
        plugins:
          $ref: '#/components/schemas/CustomPlugins'
      type: object
    PrePlugin:
      nullable: true
      properties:
        plugins:
          $ref: '#/components/schemas/CustomPlugins'
      type: object
    ResponsePlugin:
      nullable: true
      properties:
        plugins:
          $ref: '#/components/schemas/CustomPlugins'
      type: object
    TrafficLogs:
      nullable: true
      properties:
        enabled:
          type: boolean
      type: object
    TransformHeaders:
      nullable: true
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
      nullable: true
      properties:
        AuthSources:
          $ref: '#/components/schemas/AuthSources'
        config:
          $ref: '#/components/schemas/AuthenticationPlugin'
        enabled:
          type: boolean
      type: object
    HMAC:
      nullable: true
      properties:
        AuthSources:
          $ref: '#/components/schemas/AuthSources'
        allowedAlgorithms:
          items:
            type: string
          type: array
        allowedClockSkew:
          format: double
          type: number
        enabled:
          type: boolean
      type: object
    OIDC:
      nullable: true
      properties:
        AuthSources:
          $ref: '#/components/schemas/AuthSources'
        enabled:
          type: boolean
        providers:
          items:
            $ref: '#/components/schemas/Provider'
          type: array
        scopes:
          $ref: '#/components/schemas/Scopes'
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
    TimeReadableDuration:
      format: duration
      type: string
      example: PT2H30M15S
    ServiceDiscoveryCache:
      nullable: true
      properties:
        enabled:
          type: boolean
        timeout:
          format: int64
          type: integer
      type: object
    PluginBundle:
      nullable: true
      properties:
        enabled:
          type: boolean
        path:
          type: string
      type: object
    PluginConfigData:
      nullable: true
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
      nullable: true
      properties:
        enabled:
          type: boolean
        ignoreCase:
          type: boolean
      type: object
    CachePlugin:
      nullable: true
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
          format: int64
          type: integer
      type: object
    CircuitBreaker:
      nullable: true
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
          format: double
          type: number
      type: object
    TrackEndpoint:
      nullable: true
      properties:
        enabled:
          type: boolean
      type: object
    EnforceTimeout:
      nullable: true
      properties:
        enabled:
          type: boolean
        value:
          type: integer
      type: object
    Internal:
      nullable: true
      properties:
        enabled:
          type: boolean
      type: object
    MockResponse:
      nullable: true
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
      nullable: true
      properties:
        enabled:
          type: boolean
        per:
          $ref: '#/components/schemas/TimeReadableDuration'
        rate:
          type: integer
      type: object
    RequestSizeLimit:
      nullable: true
      properties:
        enabled:
          type: boolean
        value:
          format: int64
          type: integer
      type: object
    TransformBody:
      nullable: true
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
      nullable: true
      properties:
        enabled:
          type: boolean
        toMethod:
          type: string
      type: object
    URLRewrite:
      nullable: true
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
      nullable: true
      properties:
        enabled:
          type: boolean
        errorResponseCode:
          type: integer
      type: object
    VirtualEndpoint:
      nullable: true
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
      nullable: true
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
    Provider:
      properties:
        clientToPolicyMapping:
          items:
            $ref: '#/components/schemas/ClientToPolicy'
          type: array
        issuer:
          type: string
      type: object
    Scopes:
      nullable: true
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
      nullable: true
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
      nullable: true
      properties:
        enabled:
          type: boolean
        name:
          type: string
      type: object
    IDExtractor:
      nullable: true
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
      nullable: true
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
    bearerAuth:
      description: The Tyk Dashboard API Access Credentials
      scheme: bearer
      type: http

````

Built with [Mintlify](https://mintlify.com).