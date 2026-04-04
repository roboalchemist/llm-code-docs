# Source: https://tyk.io/docs/api-reference/oauth20-providers/register-a-new-oauth20-identity-provider-in-the-portal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Register a new OAuth2.0 Identity Provider in the portal

> Create a new OAuth2.0 provider



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml post /oauth-providers
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
  /oauth-providers:
    post:
      tags:
        - OAuth2.0 providers
      summary: Register a new OAuth2.0 Identity Provider in the portal
      description: Create a new OAuth2.0 provider
      operationId: create-oauth-provider
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OAuthProviderCreate'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuthProviderElem'
          description: OK
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Bad request
      security:
        - AdminAPIToken: []
components:
  schemas:
    OAuthProviderCreate:
      allOf:
        - $ref: '#/components/schemas/OAuthProviderBasic'
        - type: object
          properties:
            RegistrationAccessToken:
              type: string
              description: >-
                This token is used solely for registering a specific instance of
                the application.
              examples:
                - >-
                  eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI5MGVmNWRmYy1hNTViLTQ0N2MtODg4ZS1lNjNkNjEwMDc1ZTMifQ.eyJleHAiOjE3OTYyMjQ4MTUsImlhdCI6MTcwOTgyNDgxNSwianRpIjoiMGNiZjMyYmYtZTdmYi00M2U2LTkwNzEtZmNjMGE3YWMzZGNiIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2F1dGgvcmVhbG1zL0RDUiIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MC9hdXRoL3JlYWxtcy9EQ1IiLCJ0eXAiOiJJbml0aWFsQWNjZXNzVG9rZW4ifQ.KHx7faY5-DTgUVOKj8aK9RSmM_xRcXf7LJfgHOmPGzc
    OAuthProviderElem:
      allOf:
        - $ref: '#/components/schemas/OAuthProviderBasic'
        - type: object
          properties:
            ID:
              type: integer
              description: UID of this Identity Provider
              examples:
                - 1
            CreatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              type: string
              description: Timestamp of when this Identity provider was created
              examples:
                - 2023-06-25 13:37
            UpdatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              type: string
              description: Timestamp of when this Identity provider was created
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
    OAuthProviderBasic:
      type: object
      required:
        - Name
        - Type
        - WellKnownURL
      properties:
        Name:
          type: string
          description: Name of this Identity Provider
          examples:
            - My Keycloak instance
        Type:
          type: string
          description: >-
            Type of the identity provider. At the moment we support `Keycloak`,
            `Gluu`, and `Okta`. If your provider is not in the list but it is
            compliant with the Dynamic Client Registration protocol, select
            `Other`.
          enum:
            - Keycloak
            - Gluu
            - Okta
            - Other
          examples:
            - Keycloak
            - Gluu
            - Okta
            - Other
        WellKnownURL:
          type: string
          description: >-
            The well-known endpoint provides metadata about the OpenID Connect
            Identity Provider, facilitating dynamic client registration by
            allowing clients to discover configuration details such as
            registration endpoints automatically. Check documentation of your
            Identity provider for more information.
          examples:
            - >-
              http://localhost:8080/auth/realms/DCR/clients-registrations/openid-connect
        SSLInsecureSkipVerify:
          type: boolean
          description: >-
            If enabled, the portal will ignore failed SSL checks when connecting
            to the Identity provider
          examples:
            - false
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).