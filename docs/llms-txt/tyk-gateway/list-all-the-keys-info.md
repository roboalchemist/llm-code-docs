# Source: https://tyk.io/docs/api-reference/keys/list-all-the-keys-info.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List All the Keys info

> List all the keys and all the keys details. If `q` query parameter is passed it will only return keys whose key ID contain the passed text.

## OpenAPI

````yaml swagger/5.8/dashboard-swagger.yml get /api/keys/detailed
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
  /api/keys/detailed:
    get:
      tags:
        - Keys
      summary: List All the Keys info.
      description: >-
        List all the keys and all the keys details. If `q` query parameter is
        passed it will only return keys whose key ID contain the passed text.
      operationId: getKeysDetailed
      parameters:
        - description: Filter and return all keys that contain this text in there key ID.
          example: itachi
          in: query
          name: q
          required: false
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/KeysDetailed'
          description: Keys fetched.
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
                  /api/keys/detailed
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Forbidden
        '404':
          content:
            application/json:
              example:
                Message: Could not retrieve keys.
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Unable to connect to the gateway.
        '500':
          content:
            application/json:
              example:
                Message: Failed to unmarshal keys data from Tyk API.
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Internal server error.
components:
  schemas:
    KeysDetailed:
      properties:
        keys:
          items:
            $ref: '#/components/schemas/KeyData'
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
    KeyData:
      properties:
        api_model:
          $ref: '#/components/schemas/ApiModel'
        data:
          $ref: '#/components/schemas/SessionState'
        key_hash:
          example: 41c5cb1e
          type: string
        key_id:
          example: 5e9d9544a1dcd60001d0ed20e7f75f9e03534825b7aef9df749582e5
          type: string
      type: object
    ApiModel:
      type: object
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
            - 615d2e528bf3980001c7c6c2
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
          properties:
            hash_type:
              example: bcrypt
              type: string
            password:
              example: testuse1
              type: string
            user:
              example: admin-user@example.org
              type: string
          type: object
        certificate:
          type: string
        data_expires:
          example: 0
          format: int64
          type: integer
        date_created:
          example: '2024-05-14T13:15:46.560506+03:00'
          format: date-time
          type: string
        enable_detailed_recording:
          example: true
          type: boolean
        expires:
          example: 1716895221
          format: int64
          type: integer
        hmac_enabled:
          example: false
          type: boolean
        hmac_string:
          type: string
        id_extractor_deadline:
          example: 0
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
          example: 0
          format: int64
          type: integer
        last_updated:
          example: '1715681746'
          type: string
        max_query_depth:
          example: 5
          type: integer
        meta_data:
          example:
            tyk_developer_id: 62b3fb9a1d5e4f00017226f5
        monitor:
          properties:
            trigger_limits:
              example:
                - 80
                - 60
                - 50
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
          example: 5e9d9544a1dcd60001d0ed20
          type: string
        per:
          example: 60
          format: double
          type: number
        quota_max:
          example: 1710302205
          format: int64
          type: integer
        quota_remaining:
          example: 20000
          format: int64
          type: integer
        quota_renewal_rate:
          example: -1
          format: int64
          type: integer
        quota_renews:
          example: 1715681745
          format: int64
          type: integer
        rate:
          example: 1000
          format: double
          type: number
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
          example: -1
          type: integer
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
          example: d1dfc6a927a046c54c0ed470f19757cc
          type: string
        api_name:
          example: Rate Limit Proxy API
          type: string
        disable_introspection:
          example: false
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
          example:
            - Default
            - v2
          items:
            type: string
          nullable: true
          type: array
      type: object
    RateLimitSmoothing:
      nullable: true
      properties:
        delay:
          description: >-
            Delay is a hold-off between smoothing events and controls how
            frequently the current allowance will step up or down (in seconds).
          format: int64
          minimum: 1
          type: integer
        enabled:
          description: ' Enabled indicates if rate limit smoothing is active.'
          type: boolean
        step:
          description: >-
            Step is the increment by which the current allowance will be
            increased or decreased each time a smoothing event is emitted.
          format: int64
          minimum: 1
          type: integer
        threshold:
          description: >-
            Threshold is the initial rate limit beyond which smoothing will be
            applied. It is a count of requests during the per interval and
            should be less than the maximum configured rate.
          format: int64
          minimum: 1
          type: integer
        trigger:
          description: >-
            Trigger is a fraction (typically in the range 0.1-1.0) of the step
            at which point a smoothing event will be emitted as the request rate
            approaches the current allowance.
          format: double
          minimum: 0
          multipleOf: 0.01
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
          example:
            - GET
            - PATCH
            - HEAD
            - PUT
            - DELETE
          items:
            type: string
          nullable: true
          type: array
        url:
          example: anything/rate-limit-1-per-5
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
    bearerAuth:
      description: The Tyk Dashboard API Access Credentials
      scheme: bearer
      type: http

````

Built with [Mintlify](https://mintlify.com).
