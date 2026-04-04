# Source: https://tyk.io/docs/api-reference/oauth20-providers/delete-a-client-type-for-an-oauth20-identity-provider.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a client type for an OAuth2.0 Identity Provider

> Delete a client type for an OAuth2.0 Identity Provider. If the client type is used in any API Products, the endpoint will return 400 error.

To force remove the client, specify `?force=true`. In in this case,the portal will remove the client type, de-associate it from any API Products where it is used and reject any access requests with such API Products.

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml delete /oauth-providers/{provider_id}/client-types/{client_type_id}
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
  /oauth-providers/{provider_id}/client-types/{client_type_id}:
    delete:
      tags:
        - OAuth2.0 providers
      summary: Delete a client type for an OAuth2.0 Identity Provider
      description: >
        Delete a client type for an OAuth2.0 Identity Provider. If the client
        type is used in any API Products, the endpoint will return 400 error.


        To force remove the client, specify `?force=true`. In in this case,the
        portal will remove the client type, de-associate it from any API
        Products where it is used and reject any access requests with such API
        Products.
      operationId: delete-oauth-provider-client-type
      parameters:
        - description: UID of this OAuth2.0 provider
          in: path
          name: provider_id
          required: true
          schema:
            type: integer
            example: 1
        - description: UID of this client type
          in: path
          name: client_type_id
          required: true
          schema:
            type: integer
            example: 1
        - description: >-
            Enforce removal of the client type if it is used in any API
            Products. If set to `true`, the portal will remove the client type,
            de-associate it from any API Products where it is used and reject
            any access requests with such API Products. Considered `false`, when
            not specified.
          in: query
          name: force
          required: false
          schema:
            type: boolean
            example: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Status'
          description: OK
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Client type is used in API Products
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Identity Provider or Client Type Not found
      security:
        - AdminAPIToken: []
components:
  schemas:
    Status:
      properties:
        status:
          type: string
          description: Status of the operation
          example: ok
      type: object
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
