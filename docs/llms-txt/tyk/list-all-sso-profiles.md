# Source: https://tyk.io/docs/api-reference/sso-profiles/list-all-sso-profiles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all SSO profiles

> List all SSO profiles



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /sso_profiles
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
  /sso_profiles:
    get:
      tags:
        - SSO Profiles
      summary: List all SSO profiles
      description: List all SSO profiles
      operationId: list-sso-profiles
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SSOProfile-index'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    SSOProfile-index:
      type: array
      items:
        $ref: '#/components/schemas/SSOProfile-index-elem'
    SSOProfile-index-elem:
      type: object
      properties:
        ID:
          type: string
          description: Unique identifier/key for the SSO profile
          example: ldap_dev
        Name:
          type: string
          description: Name of the SSO profile
          example: Developers@LocalAD
        ActionType:
          type: string
          description: Type of action to perform
          example: GenerateOrLoginDeveloperProfile
        LoginURL:
          type: string
          description: URL for SSO login
          example: http://localhost:3001/tib/auth/ldap_dev/ldap
        RedirectURL:
          type: string
          description: Callback URL for SSO authentication
          example: http://localhost:3001/tib/auth/ldap_dev/ldap/callback
        SelectedProviderType:
          type: string
          description: Type of the selected provider
          example: ldap
        UpdatedAt:
          type: string
          description: Timestamp of when this profile was last updated
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          example: 2024-11-14 12:36
        UpdatedBy:
          type: string
          description: Email of the user who last updated this profile
          example: auto_test@tyk.io
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).