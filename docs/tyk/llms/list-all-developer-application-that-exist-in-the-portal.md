# Source: https://tyk.io/docs/api-reference/applications-and-credentials/list-all-developer-application-that-exist-in-the-portal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all developer application that exist in the portal

> List all developer applications



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /apps
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
  /apps:
    get:
      tags:
        - Applications and credentials
      summary: List all developer application that exist in the portal
      description: List all developer applications
      operationId: list-apps
      parameters: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Client-index'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    Client-index:
      items:
        $ref: '#/components/schemas/Client-index-elem'
      type: array
    Client-index-elem:
      allOf:
        - $ref: '#/components/schemas/Client-basic'
        - $ref: '#/components/schemas/Client-ID-attributes'
    Client-basic:
      properties:
        Name:
          type: string
          description: Name of this application
          example: Payment App
        Description:
          type: string
          description: Human-readable description of this application
          example: This is my payment application
        RedirectURLs:
          type: string
          description: Redirect URL for OAuth2.0 authorization_code and PKCE grant types
          example: https://app-host/auth
        UserID:
          type: integer
          description: UID of a user to whom this application will belong
          example: 1
        Visibility:
          type: string
          description: >-
            Controls who can access this application. Options are: `personal`
            (visible only to you), `team` (shared with your team), and
            `organisation` (accessible to all members of your organisation).
          enum:
            - personal
            - team
            - organisation
          example: personal
          default: organisation
      type: object
    Client-ID-attributes:
      properties:
        ID:
          type: integer
          description: UID of this app
          example: 1
        CreatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this application was created
          example: 2023-06-25 13:37
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).