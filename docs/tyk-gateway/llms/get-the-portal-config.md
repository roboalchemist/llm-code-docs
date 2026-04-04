# Source: https://tyk.io/docs/api-reference/portal-configuration/get-the-portal-config.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the portal config

> View the current configuration of the portal

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /configs
openapi: 3.1.0
info:
  title: Tyk Developer Portal
  description: >-

    <img src="https://tyk.io/docs/img/developer_portal_swagger_image.png"
    width="963" height="250">

    ## <a name="introduction"></a> Introduction

    The Tyk Enterprise Developer Portal Management API offers programmatic
    access to all portal resources that your instance of the portal manages.
    This API repeats functionality of the user interface and enables APIs
    consumers integrating their portal instances with their other IT systems
    such as billings, CRMs, ITSM systems and other software.


    ## Authentication

    This API requires an admin authorisation token that is available for admin
    users of the portal in the profile page.
  version: 1.14.0
servers:
  - url: http://localhost:3001/portal-api
security: []
tags:
  - name: Providers
    description: API Providers connected to this portal instance
  - name: Users
    description: Portal admins and API consumers
  - name: Organisations
    description: Organisation of API consumers and the portal admins
  - name: Teams
    description: Teams of API consumers and the portal admins
  - name: Products
    description: >-
      Marketing description and visibility of the API Products surfaced in this
      portal instance
  - name: Tutorials for API Products
    description: Tutorials that are defined for the API products
  - name: API documentation for API Products
    description: OpenAPI specs for APIs included into the API Prodcuts
  - name: Plans
    description: >-
      Marketing description and visibility settings of usage plans defined in
      this portal instance
  - name: Catalogues
    description: Catalogues of API Products listed on this portal instance
  - name: Catalogue audiences
    description: Audience management
  - name: Access requests
    description: Access requests to API Products
  - name: Applications and credentials
    description: Developer applications and API credential for developers
  - name: Portal configuration
    description: Show the current portal configuration
  - name: Pages and content
    description: Pages and content on the pages
  - name: Themes
    description: Management of the portal's visual themes
  - name: Custom Attributes
    description: Extend already existing models (User) by adding custom attributes
  - name: OAuth2.0 providers
    description: OAuth2.0 providers registered in the portal
  - name: Webhooks
    description: Webhooks management
  - name: Posts
    description: Posts management
  - name: SSO Profiles
    description: SSO Profiles management
  - name: Tags
    description: >-
      Tags management: link API Products to blog posts and control their
      display.
paths:
  /configs:
    get:
      tags:
        - Portal configuration
      summary: Get the portal config
      description: View the current configuration of the portal
      operationId: get-configs
      parameters: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Settings-index'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    Settings-index:
      items:
        $ref: '#/components/schemas/Settings-index-elem'
      type: array
    Settings-index-elem:
      properties:
        Blog:
          $ref: '#/components/schemas/BlogSetting'
        Database:
          $ref: '#/components/schemas/DatabaseSetting'
        Forms:
          $ref: '#/components/schemas/FormsSetting'
        HostPort:
          type: integer
          description: Port on which the portal serves HTTP traffic
          example: 3001
        JwtSigningKey:
          type: string
        LicenseKey:
          type: string
          description: License key for the portal. Provided by the Tyk's account managers
          example: XXX
        LogFormat:
          type: string
          enum:
            - dev
            - prod
          example: prod
          description: >-
            Log output format. The `dev` format is more human-friendly but takes
            more space, `prod` is a json-like format that fits in production use
            cases but is difficult to read
        LogLevel:
          type: string
          enum:
            - debug
            - info
            - warn
            - error
            - dpanic
            - panic
            - fatal
          description: The portal's log level. The default value is `info`
          example: info
          default: info
        PortalAPISecret:
          type: string
          description: >-
            API secret that must be set by the admin team to use the SSO flow.
            [SSO
            instructions](https://tyk.io/docs/tyk-stack/tyk-developer-portal/enterprise-developer-portal/managing-access/enable-sso/)
          example: portal123
        ProductDocRenderer:
          type: string
          enum:
            - stoplight
            - redoc
          description: >-
            Identifies which OpenAPI specification render engine the portal uses
            on the API Product Page
          default: stoplight
          example: stoplight
        RefreshInterval:
          type: integer
          description: >-
            Defines how often the portal synchronizes data with the connected
            API Providers. Measured in seconds
          example: 10
          default: 10
        S3:
          $ref: '#/components/schemas/S3Setting'
        Site:
          $ref: '#/components/schemas/SiteSetting'
        Storage:
          type: string
          enum:
            - '`fs`'
            - '`db`'
            - '`s3`'
          description: >-
            Defines which type of storage the portal uses for its CMS assets.
            [More about storing the portal's assets in the
            documentation](https://tyk.io/docs/tyk-stack/tyk-developer-portal/enterprise-developer-portal/install-tyk-enterprise-portal/configuration/#storage-settings)
          example: '`db`'
        StoreSessionName:
          type: string
          description: Defines name of the cookie where the portal stores its session
          example: portal-store-session-name
          default: portal-store-session-name
        TLSConfig:
          $ref: '#/components/schemas/TLSSetting'
        Theming:
          $ref: '#/components/schemas/ThemeSetting'
      type: object
    BlogSetting:
      properties:
        AllowFormSubmission:
          type: boolean
        Enable:
          type: boolean
      type: object
    DatabaseSetting:
      properties:
        ConnectionString:
          type: string
          example: por....db
          description: >-
            Connection string to the portal's database. May hold secure secrets,
            therefore it's masked
        Dialect:
          type: string
          enum:
            - '`sqlite3`'
            - '`mysql`'
            - '`postgres`'
          description: Database dialect of the portal's database
        EnableLogs:
          type: boolean
          description: Defines if the portal should write connection logs to the database
        MaxRetries:
          type: integer
          description: Max retries when establishing connection to the database
          example: 3
          default: 3
        RetryDelay:
          type: integer
          description: >-
            Delay between connection retries when establishing connection to the
            database. Measured in milliseconds
          example: 5000
          default: 5000
      type: object
    FormsSetting:
      properties:
        Enable:
          type: boolean
          description: Identifies if the forms are enabled. By default their are disabled
          example: false
          default: false
      type: object
    S3Setting:
      properties:
        ACL:
          type: string
          description: ACL rules for the S3 bucket
        AccessKey:
          type: string
        Bucket:
          type: string
        Endpoint:
          type: string
        PresignURLs:
          type: boolean
        Region:
          type: string
        SecretKey:
          type: string
      type: object
    SiteSetting:
      properties:
        Enable:
          type: boolean
          description: Identifies if the live portal is enabled
          example: true
      type: object
    TLSSetting:
      properties:
        Certificates:
          items:
            $ref: '#/components/schemas/Certificate'
          type: array
        Enable:
          type: boolean
          description: Defines if SSL is enabled in the portal
        InsecureSkipVerify:
          type: boolean
          description: Defines if the portal accepts self-signed certificates
        MinVersion:
          type: integer
        MaxVersion:
          type: integer
        PreferServerCipherSuites:
          type: boolean
          description: >-
            If true, the server will prefer the server ciphers over the client
            ciphers
        CipherSuites:
          items:
            type: string
            description: Cipher suite name
            example: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
          type: array
      type: object
    ThemeSetting:
      properties:
        Path:
          type: string
          example: ./themes
        Theme:
          type: string
          example: default
      type: object
    Certificate:
      properties:
        CertFile:
          type: string
          example: portal.crt
        KeyFile:
          type: string
          example: portal.key
        Name:
          type: string
          example: localhost
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).
