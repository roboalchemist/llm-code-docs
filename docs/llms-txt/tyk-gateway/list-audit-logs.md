# Source: https://tyk.io/docs/api-reference/auditlogs/list-audit-logs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List audit logs

> Retrieve audit logs from database

## OpenAPI

````yaml swagger/5.8/dashboard-swagger.yml get /api/audit-logs
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
  /api/audit-logs:
    get:
      tags:
        - AuditLogs
      summary: List audit logs
      description: Retrieve audit logs from database
      operationId: getAuditLogs
      parameters:
        - description: >-
            Use p query parameter to say which page you want returned. The size
            of the page is determined by the configuration option page_size of
            dashboard.
          example: 1
          in: query
          name: p
          required: false
          schema:
            type: integer
        - description: >-
            Filters audit logs to show only actions performed by the specified
            user. This parameter allows you to focus on the activity of a
            particular user across the system.
          example: jhon@mail.com
          in: query
          name: user
          required: false
          schema:
            type: string
        - description: >-
            Filters audit logs based on the specific action performed by users.
            This parameter allows you to focus on particular types of activities
            within the system.
          example: List APIs
          in: query
          name: action
          required: false
          schema:
            type: string
        - description: >-
            Filters audit logs based on the IP address from which the action
            originated. This parameter allows you to focus on activities from
            specific network locations or to investigate actions from particular
            IP addresses.
          example: 127.0.0.1
          in: query
          name: ip
          required: false
          schema:
            type: string
        - description: >-
            Filters audit logs based on the HTTP method used in the API request.
            This parameter allows you to focus on specific types of operations
            performed on the API.
          example: POST
          in: query
          name: method
          required: false
          schema:
            type: string
        - description: >-
            Filters audit logs based on the HTTP status code returned by the API
            in response to the request. This parameter allows you to focus on
            specific outcomes of API interactions.
          example: 200
          in: query
          name: status
          required: false
          schema:
            type: integer
        - description: >
            This parameter filters audit logs based on partially matching the
            accessed API endpoint's URL path. It allows searching for actions
            performed on related resources or sections of the API by matching
            any portion of the URL. The match is case-sensitive and ignores
            additional path segments or query parameters beyond the matched
            portion.  

            For example, if the database contains URLs like `/tib/create`,
            `/tib/get/1?schema=json`,  `/api/schema`, and `/schema1` searching
            with `url=schema` would return  `/api/schema` and `/schema1`.
          example: /api/apis
          in: query
          name: url
          required: false
          schema:
            type: string
        - description: >-
            Specifies the start date for the audit log search. If not provided,
            the search will include records from the earliest available date.
            Format DD-MM-YYYY.
          example: 25-11-1990
          in: query
          name: from_date
          required: false
          schema:
            type: string
        - description: >-
            Specifies the end date for the audit log search. If not provided,
            the search will include records up to the current date and time.
            Format DD-MM-YYYY.
          example: 18-12-2030
          in: query
          name: to_date
          required: false
          schema:
            type: string
        - description: >-
            Determines whether the response should be a downloadable file
            containing the records. If set to `true`, the API returns a file
            instead of a JSON list of records. When enabled, pagination is not
            applied, and the file will include all records that match the search
            criteria.
          example: true
          in: query
          name: download
          required: false
          schema:
            type: boolean
        - description: >-
            Specifies the format of the downloadable file. This parameter is
            only applied when `download` is set to `true`. If set to `csv`, the
            file content will be in CSV format; otherwise, JSON format will be
            used.
          in: query
          name: type
          required: false
          schema:
            type: string
            enum:
              - csv
              - json
          example: csv
      responses:
        '200':
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
                description: >-
                  A file containing the audit logs in either JSON or CSV format,
                  depending on the `type` query parameter.
            application/json:
              example:
                pages: 1
                audit_logs:
                  - _id: 672a83e2b0418b224440ce29
                    req_id: 0462e283-a55f-41ab-6482-60d2eeb1858c
                    org_id: 66cf7f8db0418b1fbe91852b
                    date: Tue, 05 Nov 2024 17:45:22 -03
                    timestamp: 1730839522
                    ip: 127.0.0.1
                    user: jhon@mail.com
                    action: ''
                    method: GET
                    url: /api/audit-logs
                    status: 200
                  - _id: 672a83e9b0418b224440ce2a
                    req_id: 1276517a-a57e-4b20-5cf5-a6d830fc399d
                    org_id: 66cf7f8db0418b1fbe91852b
                    date: Tue, 05 Nov 2024 17:45:29 -03
                    timestamp: 1730839529
                    ip: 127.0.0.1
                    user: jhon@mail.com
                    action: ''
                    method: GET
                    url: /api/audit-logs
                    status: 200
                  - _id: 672a83ecb0418b224440ce2b
                    req_id: 9c720384-2c93-4c38-7164-35b876fd56ef
                    org_id: 66cf7f8db0418b1fbe91852b
                    date: Tue, 05 Nov 2024 17:45:32 -03
                    timestamp: 1730839532
                    ip: 127.0.0.1
                    user: jhon@mail.com
                    action: ''
                    method: GET
                    url: /api/audit-logs
                    status: 200
              schema:
                $ref: '#/components/schemas/AuditLogs'
          description: Audit Logs retrieved successfully
        '400':
          content:
            application/json:
              example:
                Message: could not retrieve audit records
                Meta: null
                Status: Error
          description: Bad Request
        '401':
          content:
            application/json:
              example:
                Message: Not authorised
                Meta: null
                Status: Error
          description: Unauthorized
        '403':
          content:
            application/json:
              example:
                Message: >-
                  access denied: You do not have permission to access 
                  /api/audit-logs
                Meta: null
                Status: Error
          description: Forbidden
components:
  schemas:
    AuditLogs:
      properties:
        pages:
          type: integer
        audit_logs:
          items:
            $ref: '#/components/schemas/AuditLog'
          nullable: true
          type: array
      type: object
    AuditLog:
      properties:
        _id:
          example: 672a83e2b0418b224440ce29
          type: string
        req_id:
          example: 0462e283-a55f-41ab-6482-60d2eeb1858c
          type: string
        org_id:
          example: 5e9d9544a1dcd60001d0ed20
          type: string
        date:
          example: Tue, 05 Nov 2024 17:45:22 -03
          type: string
        timestamp:
          example: 1730839522
          type: integer
        ip:
          example: 127.0.0.1
          type: string
        user:
          example: jhon@mail.com
          type: string
        action:
          example: List APIS
          type: string
        method:
          example: GET
          type: string
        url:
          example: /api/apis
          type: string
        status:
          example: 200
          type: integer
      type: object
  securitySchemes:
    bearerAuth:
      description: The Tyk Dashboard API Access Credentials
      scheme: bearer
      type: http

````

Built with [Mintlify](https://mintlify.com).
