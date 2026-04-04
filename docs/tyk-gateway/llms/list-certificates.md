# Source: https://tyk.io/docs/api-reference/certs/list-certificates.md

# Source: https://tyk.io/docs/api-reference/certificates/list-certificates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Certificates

> Return list of certificates. If you send the mode query parameter with the value `detailed` the certificates returned will have more information (Will contains all certs basic details). To retrieve a list with complete certificate details use [this endpoint](#operation/listDetailedCertificates). If the mode query parameter is omitted or is empty this endpoint will only return the certificates IDs. The list of certificates returned is paginated.

## OpenAPI

````yaml swagger/5.8/dashboard-swagger.yml get /api/certs
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
  /api/certs:
    get:
      tags:
        - Certificates
      summary: List Certificates.
      description: >-
        Return list of certificates. If you send the mode query parameter with
        the value `detailed` the certificates returned will have more
        information (Will contains all certs basic details). To retrieve a list
        with complete certificate details use [this
        endpoint](#operation/listDetailedCertificates). If the mode query
        parameter is omitted or is empty this endpoint will only return the
        certificates IDs. The list of certificates returned is paginated.
      operationId: listCertificates
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
        - description: >-
            Set to detailed to get certificates that are more with more details
            (Will contains certs basic details). To retrieve a list of
            certificates with all the certificate details use [this
            endpoint](#operation/listDetailedCertificates).
          example: detailed
          in: query
          name: mode
          required: false
          schema:
            enum:
              - detailed
            type: string
        - description: >-
            Defines the filtering strategy applied to certificate keys.

            This query parameter only works with detailed mode (mode=detailed).

            omit (default) – Returns all certificates regardless of private key
            association.

            with_pk – Returns only certificates that include a private key.

            without_pk – Returns only certificates that do not include a private
            key.
          name: filter
          example: omit
          required: false
          in: query
          schema:
            type: string
            default: omit
            enum:
              - omit
              - with_pk
              - without_pk
      responses:
        '200':
          content:
            application/json:
              examples:
                detailed_mode:
                  summary: Returned when you send mode=detailed in query parameter.
                  value:
                    cert_basics:
                      - dns_names:
                          - .*itachi.io
                        has_private: false
                        id: >-
                          5e9d9544a1dcd60001d0ed208edce514c2d0a866063550c64d6c90be99d01561ac5aa7e82b8610b7e273d37d
                        is_ca: false
                        issuer_cn: tyk-gateway-2.localhost
                        not_after: '2025-05-19T05:23:10Z'
                        not_before: '2024-05-19T05:23:10Z'
                        subject_cn: tyk-gateway-2.localhost
                      - dns_names:
                          - .*tyk.io
                        has_private: false
                        id: >-
                          5e9d9544a1dcd60001d0ed207c440d66ebb0a4629d21329808dce9091acf5f2fde328067a6e60e5347271d90
                        is_ca: false
                        issuer_cn: tyk.io
                        not_after: '2034-03-26T08:46:37Z'
                        not_before: '2024-03-25T08:46:37Z'
                        subject_cn: tyk.io
                    pages: 1
                empty_mode:
                  summary: Returned if `mode` in query parameter is empty.
                  value:
                    certs:
                      - >-
                        5e9d9544a1dcd60001d0ed208edce514c2d0a866063550c64d6c90be99d01561ac5aa7e82b8610b7e273d37d
                      - >-
                        5e9d9544a1dcd60001d0ed207c440d66ebb0a4629d21329808dce9091acf5f2fde328067a6e60e5347271d90
                    pages: 1
              schema:
                oneOf:
                  - $ref: '#/components/schemas/CertificateBasics'
                  - $ref: '#/components/schemas/CertificateList'
          description: OK
        '400':
          content:
            application/json:
              example:
                Message: Could not retrieve certs.
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Unable to retrieve certificates.
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
                  /api/certs
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Forbidden
        '500':
          content:
            application/json:
              example:
                Message: Failed to marshal data for certificates basics list.
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiResponse'
          description: Internal server error.
components:
  schemas:
    CertificateBasics:
      properties:
        cert_basics:
          items:
            $ref: '#/components/schemas/CertsCertificateBasics'
          nullable: true
          type: array
        pages:
          type: integer
      type: object
    CertificateList:
      properties:
        certs:
          items:
            type: string
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
    CertsCertificateBasics:
      properties:
        dns_names:
          items:
            type: string
          nullable: true
          type: array
        has_private:
          type: boolean
        id:
          type: string
        is_ca:
          type: boolean
        issuer_cn:
          type: string
        not_after:
          format: date-time
          type: string
        not_before:
          format: date-time
          type: string
        subject_cn:
          type: string
      type: object
      x-go-package: github.com/TykTechnologies/tyk/certs
  securitySchemes:
    bearerAuth:
      description: The Tyk Dashboard API Access Credentials
      scheme: bearer
      type: http

````

Built with [Mintlify](https://mintlify.com).
