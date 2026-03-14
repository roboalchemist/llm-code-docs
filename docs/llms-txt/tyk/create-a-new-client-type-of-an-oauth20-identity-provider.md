# Source: https://tyk.io/docs/api-reference/oauth20-providers/create-a-new-client-type-of-an-oauth20-identity-provider.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new client type of an OAuth2.0 Identity Provider

> Create a new client type of an OAuth2.0 Identity Provider



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml post /oauth-providers/{provider_id}/client-types
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
  /oauth-providers/{provider_id}/client-types:
    post:
      tags:
        - OAuth2.0 providers
      summary: Create a new client type of an OAuth2.0 Identity Provider
      description: Create a new client type of an OAuth2.0 Identity Provider
      operationId: create-oauth-provider-client-type
      parameters:
        - description: UID of this OAuth2.0 provider
          in: path
          name: provider_id
          required: true
          schema:
            type: integer
            example: 1
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OAuthClientTypeBasic'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuthClientTypeElem'
          description: OK
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Bad request
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Identity Provider Not found
      security:
        - AdminAPIToken: []
components:
  schemas:
    OAuthClientTypeBasic:
      type: object
      required:
        - Name
        - ResponseTypes
        - GrantType
      properties:
        Name:
          type: string
          description: Name of this Client type
          examples:
            - Server-side application
        Description:
          type: string
          description: Description of this Client type
          examples:
            - >-
              Use this client configuration to create server-side applications
              that don't act on behalf of end-users
        ResponseTypes:
          type: string
          description: >-
            The OAuth 2.0 response type(s) the client is permitted to use,
            determining how it receives authorization responses from the
            Identity Provider. Format as CSV and Specify at least one.
          enum:
            - code
            - token
            - it_token
            - none
          examples:
            - code,token
        GrantType:
          type: string
          description: >-
            The OAuth 2.0 grant types the client is permitted to use,
            determining how it obtains access tokens from the authorization
            server. Format as CSV and Specify at least one.
          enum:
            - authorization_code
            - pkce
            - client_credentials
            - device_code
            - refresh_token
            - password
            - implicit
          examples:
            - authorization_code,refresh_token,password
        TokenEndpointAuthMethod:
          type: string
          description: >-
            The authentication method a client can use at the token endpoint,
            ensuring secure communication with the authorization server during
            the OAuth 2.0 authentication.
          enum:
            - client_secret_basic
            - client_secret_post
          examples:
            - client_secret_basic
            - client_secret_post
        OktaAppType:
          type: string
          description: >-
            Dictates how an application will authenticate and interact with
            Okta's authorization servers, including whether it operates as a
            web, native, single-page, or service application. This setting is
            required to register Okta Identity Providers and not required for
            other Identity Provider. Please note that Okta overwrites values of
            the `TokenEndpointAuthMethod`, `GrantType`, and `ResponseTypes`
            properties and fills them based on the value of the `OktaAppType`
            property.
          enum:
            - web
            - native
            - browser
            - service
          examples:
            - web
            - native
            - browser
            - service
    OAuthClientTypeElem:
      allOf:
        - $ref: '#/components/schemas/OAuthClientTypeBasic'
        - type: object
          properties:
            ID:
              type: integer
              description: UID of this client type
              examples:
                - 1
            CreatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              type: string
              description: Timestamp of when this client type was created
              examples:
                - 2023-06-25 13:37
            UpdatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              type: string
              description: Timestamp of when this client type was created
              examples:
                - 2023-06-25 13:37
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