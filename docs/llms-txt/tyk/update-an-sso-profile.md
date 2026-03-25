# Source: https://tyk.io/docs/api-reference/sso-profiles/update-an-sso-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an SSO profile

> Update an existing SSO profile



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml put /sso_profiles/{profile_id}
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
  /sso_profiles/{profile_id}:
    put:
      tags:
        - SSO Profiles
      summary: Update an SSO profile
      description: Update an existing SSO profile
      operationId: update-sso-profile
      parameters:
        - description: ID of the SSO profile
          in: path
          name: profile_id
          required: true
          schema:
            type: string
            example: ldap_dev
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SSOProfile-response'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SSOProfile-response'
          description: OK
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Profile not found
      security:
        - AdminAPIToken: []
components:
  schemas:
    SSOProfile-response:
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
        OrgID:
          type: string
          description: Organization ID
          example: '1'
        ActionType:
          type: string
          description: Type of action to perform
          example: GenerateOrLoginDeveloperProfile
        MatchedPolicyID:
          type: string
          description: ID of the matched policy
        Type:
          type: string
          description: Type of SSO profile
          example: redirect
        ProviderName:
          type: string
          description: Name of the provider
          example: ADProvider
        CustomEmailField:
          type: string
          description: Custom field for email mapping
        CustomUserIDField:
          type: string
          description: Custom field for user ID mapping
        ProviderConfig:
          type: object
          description: JSON configuration for the provider
          additionalProperties: true
        IdentityHandlerConfig:
          type: object
          description: JSON configuration for identity handling
          additionalProperties: true
        ProviderConstraintsDomain:
          type: string
          description: Domain constraints for the provider
        ProviderConstraintsGroup:
          type: string
          description: Group constraints for the provider
        ReturnURL:
          type: string
          description: URL to return to after SSO
          example: http://localhost:3001/sso
        DefaultUserGroupID:
          type: string
          description: Default group ID for new users
        CustomUserGroupField:
          type: string
          description: Custom field for user group mapping
          example: cn
        UserGroupMapping:
          type: object
          description: JSON mapping of user groups
          additionalProperties: true
          example:
            TeamA: '9'
            TeamB: '11'
        UserGroupSeparator:
          type: string
          description: Separator used in user group strings
        SSOOnlyForRegisteredUsers:
          type: boolean
          description: Whether SSO is restricted to registered users only
          default: false
    OnlyErrors:
      properties:
        errors:
          type: array
          description: Human-readable description of the errors
          items:
            type: string
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).