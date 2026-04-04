# Source: https://tyk.io/docs/api-reference/applications-and-credentials/update-a-custom-credential.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Custom Credential

> Update an existing custom credential for a specific application.



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml put /apps/{app_id}/custom_credentials/{credential_id}
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
  /apps/{app_id}/custom_credentials/{credential_id}:
    put:
      tags:
        - Applications and credentials
      summary: Update a Custom Credential
      description: Update an existing custom credential for a specific application.
      parameters:
        - name: app_id
          in: path
          required: true
          description: The ID of the application.
          schema:
            type: string
        - name: credential_id
          in: path
          required: true
          description: The ID of the custom credential.
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CustomCredential-update'
      responses:
        '200':
          description: Custom credential updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomCredential-show'
        '422':
          description: Validator error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
      security:
        - AdminAPIToken: []
components:
  schemas:
    CustomCredential-update:
      type: object
      properties:
        Alias:
          type: string
          description: Alias for the custom credential
    CustomCredential-show:
      allOf:
        - $ref: '#/components/schemas/CustomCredential'
        - type: object
          properties:
            CreatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              type: string
              description: Timestamp of when this webhook was created
              example: 2023-06-25 13:37
            UpdatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              type: string
              description: Timestamp of when this webhook was updated the last time
              example: 2023-06-25 13:37
    OnlyErrors:
      properties:
        errors:
          type: array
          description: Human-readable description of the errors
          items:
            type: string
      type: object
    CustomCredential:
      type: object
      properties:
        ID:
          type: integer
          description: Unique identifier for the custom credential
        Alias:
          type: string
          description: Alias for the custom credential
        Type:
          type: string
          enum:
            - CREDENTIAL_TYPE_TYK_MANAGED
            - CREDENTIAL_TYPE_CUSTOM
          description: Type of the custom credential
        PlanID:
          type: string
          description: Plan ID associated with the custom credential
        AuthenticationMethod:
          type: string
          description: Authentication method used for the custom credential
        ProductIDs:
          type: array
          items:
            type: integer
          description: List of product IDs associated with the custom credential
        AuthTokenType:
          type: string
          enum:
            - AUTH_TOKEN_CUSTOM
            - AUTH_TOKEN_STANDARD
          description: Type of authentication token used
        KeyID:
          type: string
          description: Key ID for the custom credential
        ProviderID:
          type: integer
          description: ID for OAuth2.0 provider
        ClientTypeID:
          type: integer
          description: ID for OAuth2.0 client type
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).